# Self-Improving AI Trading Agents — Approaches and Architectures

Research note, 2026-09-22. Companion to `../trding-agents-arhiteches/` (TradingAgents, FinMem, FinAgent static architectures).
This note covers the *adaptation* layer: what a trading agent changes about itself, when, how, and who is allowed to approve the change.

---

## 0. The one distinction that organizes everything

Almost every paper labelled "self-improving trading agent" is doing one of two very different things:

| | **A. Self-improving research process** | **B. Self-improving trading policy** |
|---|---|---|
| What improves | The *search* for strategies/factors: hypotheses, code, model configs, search heuristics | The *live decision rule*: memory, beliefs, weights, risk posture |
| Clock | Offline, hours–weeks per iteration | Online, per-bar to per-week |
| Feedback | Backtest / held-out IC, Sharpe | Realized PnL, slippage, regime signal |
| Main enemy | Meta-overfitting, data leakage, multiple testing | Non-stationarity, forgetting, self-reinforcing bad beliefs |
| Failure is | Silent — you deploy a strategy that never had edge | Loud — you lose money as it drifts |
| Examples | RD-Agent(Q), AQuA, QuantEvolve, AlgoEvolve, AlphaAgent, EVOQUANT | FinMem, FinCon, FLAG-Trader, ReCAP, Reflexion-style loops |

**They need opposite safety engineering.** (A) needs sealed data, statistical discipline about how many things you tried, and a promotion gate. (B) needs memory governance, forgetting control, and a kill switch. Systems that blur them — an agent that rewrites its own live strategy from its own live PnL — are the most dangerous configuration and the least evidenced in the literature.

Everything below is tagged **[A]**, **[B]** or **[A+B]**.

---

## 1. Taxonomy: four axes

Adapted from the self-evolving agent surveys ([Survey of Self-Evolving Agents](https://arxiv.org/html/2507.21046v3), [Comprehensive Survey of Self-Evolving AI Agents](https://arxiv.org/pdf/2508.07407), [Self-Improvements in Modern Agentic Systems](https://arxiv.org/html/2607.13104v1)) and specialized to trading.

### Axis 1 — WHAT evolves

Formally the agent is `A_t = (θ_t, Σ_t)`: model weights `θ` plus scaffolding `Σ` (prompts, memory, tools, control logic). Ordered by cost and reversibility:

| Level | Object | Speed | Reversible? | Trading instances |
|---|---|---|---|---|
| **L0 Execution/context** | transient in-context reasoning | seconds | yes (discarded) | CoT, self-consistency, debate |
| **L1 Memory** | episodic + semantic stores | per decision | yes (versioned) | FinMem layered memory, FinAgent retrieval+reflection, AlphaMemo search-process memory |
| **L2 Beliefs / prompts** | investment principles, system prompts | daily–weekly | yes | FinCon conceptual verbal reinforcement, AlgoEvolve "prompt genome" |
| **L3 Artifacts** | factor expressions, strategy code, model configs | per experiment | yes (git) | AlphaAgent, QuantEvolve, EVOQUANT, RD-Agent(Q), AQuA |
| **L4 Tools/workflow** | operator set, agent topology, search routine | weekly–monthly | yes, harder | AlgoEvolve outer loop, ADAS/AFlow, DGM |
| **L5 Weights** | policy/LLM parameters | batch retrain | **no** | FLAG-Trader (PPO on LLM policy), ReCAP policy vectors |

Practical rule: **push improvement as low on this list as will do the job.** L1–L3 give most of the benefit, are auditable, and roll back cleanly. L5 is where irreversibility and catastrophic forgetting live.

### Axis 2 — WHEN it evolves

- **Intra-episode** (within one decision/trading day): reflection, retry, self-critique. Cheap, bounded blast radius.
- **Inter-episode** (across days/experiments): memory consolidation, belief update, factor promotion.
- **Meta / inter-run**: the search procedure itself is rewritten.

### Axis 3 — HOW the update is produced

1. **Verbal / reflective** — the LLM writes a lesson in natural language and stores it (Reflexion lineage; FinCon's conceptual verbal reinforcement). No gradients.
2. **Evolutionary / population** — mutate + select over a population of programs, LLM as the mutation operator (FunSearch → AlphaEvolve → QuantEvolve, AlgoEvolve, QuantaAlpha).
3. **Gradient RL** — reward (PnL, IC) backpropagated into weights (FLAG-Trader).
4. **Retrieval / experience reuse** — no parameter change at all; better indexing of what already happened (AlphaMemo, FinAgent).
5. **Config/hypothesis search** — structured proposals over a frozen space (RD-Agent(Q), AQuA Part II).

### Axis 4 — WHO verifies (the axis most papers skip)

This determines whether the loop compounds skill or compounds delusion:

- **Self-judged** (LLM grades its own output) → error amplification, reward hacking. Never sufficient in trading.
- **Execution-grounded** (the code runs, the backtest returns a number) → necessary, not sufficient — the number can be leaked.
- **Sealed-evaluator** (agent cannot touch the data loader, splits, or metric; optimization metric ≠ reported metric) → this is the state of the art.
- **Market-grounded** (paper/live PnL with costs) → the only real verifier, and the slowest.

---

## 2. The six architecture families

### F1 — Reflective memory loop (no weight change) **[B]**

*FinMem, FinAgent, FinCon, TradingAgents' reflection, Reflexion lineage.*

```
observe → retrieve similar past episodes → decide → observe outcome
        → write reflection (what I believed, what happened, why)
        → consolidate into layered memory (recency × relevance × importance)
```

Design points that actually matter:

- **Stratified memory with decay.** FinMem splits working memory from long-term layers ranked by novelty/relevance/importance, with time decay per layer — so a lesson from a 2020 liquidity shock does not outweigh last week.
- **Two-level reflection.** FinAgent separates low-level (what happened to *this* trade) from high-level (what does this say about my *strategy*). Without the split, the agent overfits to single trades.
- **Belief objects, not transcripts.** FinCon's contribution: distill reflections into a small set of *conceptual investment beliefs*, broadcast selectively. This cuts communication cost and, more importantly, makes the learned state inspectable and editable by a human.
- **Known weakness:** similarity-based retrieval surfaces *outdated* episodes. The survey calls this the **Oracle Fallacy** — a retrieved 2008 episode carries a post-hoc narrative that the agent could not have had at the time, which is a subtle form of look-ahead inside the memory itself.

Verdict: cheapest real self-improvement, works today, and is the right default for a discretionary-style LLM agent. Do not expect it to find alpha — it mostly improves *consistency* and risk discipline.

### F2 — Gradient RL with the LLM as policy **[B]**

*[FLAG-Trader](https://arxiv.org/abs/2502.11433) (ACL Findings 2025).*

A partially fine-tuned LLM *is* the policy network in an actor-critic setup; trading reward drives PPO updates through PEFT adapters, with most of the base model frozen to preserve pretrained knowledge. Reported to improve trading and to transfer to other financial tasks; base model in the paper is tiny (SmolLM2-135M).

Use when: you have a well-defined state/action space and enough episodes. Avoid when: your reward is a handful of noisy monthly PnL observations — the sample complexity is not there. This is the family with the worst irreversibility properties (L5) and the best asymptotics.

### F3 — Evolutionary program search over strategies and factors **[A]**

The FunSearch → AlphaEvolve pattern (LLM as semantic mutation operator + programmatic evaluator), transplanted into quant.

| System | Key mechanism | Reported result (self-reported, unreplicated) |
|---|---|---|
| [AlphaAgent](https://arxiv.org/abs/2502.16789) (KDD'25) | 3 regularizers: **originality** (AST similarity vs. existing alphas), **complexity control** (AST size limits), **hypothesis–factor alignment** | +81% effective-factor hit ratio, −30% tokens |
| [QuantEvolve](https://arxiv.org/html/2510.18569v1) | **MAP-Elites quality-diversity** over a feature map (category × frequency × MDD × Sharpe × Sortino × return) + islands with migration | Sharpe 1.52 vs 1.07 equal-weight, 256% cum. return (6 mega-caps, 2022–25 test) |
| [QuantaAlpha](https://arxiv.org/html/2602.07085v2) | Mutation/crossover over *whole mining trajectories*; AST-isomorphism redundancy filter; complexity caps (≤250 chars, ≤6 base features) | IC 0.1501 vs 0.0966 (AlphaAgent) on CSI300; zero-shot transfer to CSI500/S&P500 |
| [EVOQUANT](https://arxiv.org/html/2607.12455v1) | **Verifier-guided** evolution of a typed "strategy genome" (signal / risk / sizing / entry / exit layers); hard gates before scoring; escalation ladder repair→bridge→redesign→family-migration | Mean test Sharpe −0.298 → 0.538 across 4 A-share strategies; 115/120 non-degradation |
| [AlgoEvolve](https://arxiv.org/html/2606.26173) | **Bi-level**: inner loop evolves strategies, outer loop evolves the *evolver prompt* (mutation intensity, focus, constraints, reasoning genes) | Sharpe 5.60 peak vs 1.21 population mean (short 20–30 day windows — treat with heavy skepticism) |

The structural lessons, independent of the headline numbers:

1. **Diversity is a first-class objective, not a nicety.** MAP-Elites-style binning is what stops the population collapsing onto one over-fit family. QuantEvolve's ablation: coarse bins (1–4) converged prematurely by gen 50; 16 bins kept improving through gen 150.
2. **Novelty must be measured structurally**, not semantically — AST similarity against the existing alpha library. This is also the only honest defense against *crowding*: a factor that is structurally identical to what everyone else runs has no capacity.
3. **Complexity caps are anti-overfitting devices**, cheap and effective.
4. **Hard gates before soft scoring.** EVOQUANT rejects zero-trade, excessive-drawdown, excessive-drift candidates *before* they can be ranked. Gaming a hard gate is much harder than gaming a score.
5. **Simpler often wins late.** QuantEvolve observed later generations adding sophistication and *underperforming* simpler ancestors.

### F4 — Automated R&D pipeline (hypothesis → code → backtest → belief) **[A]**

*[RD-Agent(Q)](https://github.com/microsoft/RD-Agent) (Microsoft, open source, integrated with Qlib) and [AQuA](https://arxiv.org/html/2608.12841v1).*

Less "evolution", more "an automated research department". Agents split into Research (propose hypothesis) and Development (implement, backtest), with factor–model co-optimization. RD-Agent(Q) reports ~2× annualized return vs. classical factor libraries with 70% fewer factors.

AQuA is the most carefully engineered example I found, and its main contribution is a **safety architecture, not a performance number**:

- **Sealed sandbox.** The agent *cannot write arbitrary code*. It emits specifications in a constrained DSL: fixed operator trees (rank, z-score, rolling stats, correlations) over raw fields. Every time-series operator reads only backward windows, and causality is **closed under composition** — so temporal leakage is *inexpressible*, not merely *reviewed*.
- **Why that matters:** an earlier permissive version let agents write feature code with a second agent reviewing it. A "volume participation ratio" normalized intraday volume by *daily total* volume — end-of-day information at a mid-day timestamp. Author *and* reviewer approved it, because both reasoned about intent rather than bar-level causality. **Shared failure mode between generator and critic is the reason LLM review is not a leakage control.**
- **Selection leakage control.** Optimization metric ≠ reported metric. Agents see only an inner validation slice; the test window is scored once, after freeze, and never returned to the agent.
- **Two decoupled subsystems** (factor discovery, model development) with no shared state — limiting how far a bad belief can propagate.
- Results: US equities 30-min, per-stock IC 0.0843 vs 0.0613 GRU baseline; long/short Sharpe 2.15 (2.50 with vol targeting, 2.00 walk-forward), positive every year 2021–2025, 22bp two-leg cost assumed. Backtest only — explicitly not live-validated.

### F5 — Meta-level / scaffolding self-modification **[A]**

The agent edits *itself*: its prompts, its tools, its search operators, its workflow graph.

- **AlgoEvolve's outer loop** — evolving the evolver prompt. Notable because the inner loop alone got stuck in "zero-trade stagnation" (over-regularized into never trading) and the meta-loop diagnosed and fixed that failure mode. That is a genuine qualitative capability, not parameter tuning.
- **[Darwin Gödel Machine](https://arxiv.org/abs/2505.22954)** (ICLR 2026) — self-modifying coding agent validated empirically on benchmarks rather than by proof; SWE-bench 20.0%→50.0%, Polyglot 14.2%→30.7%. Maintains an *archive* of all agent variants (open-ended search) rather than a single lineage. The trading-relevant lesson is the archive: keep every variant, because a currently-worse ancestor is often the parent of the next breakthrough.
- **Workflow evolution** (ADAS, AFlow): the multi-agent topology itself is the search space.

In trading this is where the expected value is highest *and* the governance burden is greatest. The DGM authors sandbox and human-supervise all runs; do the same.

### F6 — Continual / regime-adaptive RL **[B]**

*[ReCAP](https://arxiv.org/html/2606.00143) (regime-adaptive continual learning for portfolio management), meta-RL, streaming continual learning.*

The cleanest answer to non-stationarity that does not require an LLM at all:

```
θ_t = θ_0 + D · α̃_t
```
Frozen base policy `θ_0` + a **library of regime-specific policy vectors** `D` + a **regime gate** producing attention weights `α̃_t`. Regimes are detected online by CUSUM over VIX / turbulence / Bollinger / RSI. Only the gate and the current regime's vector are trained; the base and the library stay frozen, so nothing is forgotten. New vectors merge into the library by cosine-similarity threshold; near-zero-norm vectors are discarded.

Reported: NAS100 cumulative 164.9% vs 125.4% best baseline, Sharpe 1.14 vs ~0.91, MDD 23.9% vs ~25.3%; consistent across 5 datasets vs 13 portfolio baselines and 5 continual-learning strategies.

**Architectural idea worth stealing regardless of whether you use RL:** *modular, additive, frozen-base adaptation with a gate*. It gives continual learning without catastrophic forgetting, and every module is independently attributable and removable. The same pattern works with strategies instead of policy vectors: a frozen library of validated strategies + a regime-conditioned allocator.

### F7 — Population / market co-evolution **[A+B]**

Agents evolve against *each other* in a simulated market rather than against a static backtest ([Alpha Singularity](https://arxiv.org/pdf/2606.29194), agent-based market simulators, TwinMarket-style sandboxes).

Motivation is correct and important: a backtest is a *stationary opponent*; real markets are adversarial and your own trading changes them. Co-evolution is the only setup that can, in principle, model crowding, alpha decay from adoption, and market impact endogenously. Current evidence is thin and results are simulator-dependent — treat as a research direction and as a **stress-testing tool** (evolve adversaries against your champion strategy) rather than as an alpha source.

---

## 3. The control plane: what separates a compounding loop from a delusion loop

This section is the actual deliverable. The families above are interchangeable; the control plane is not.

### 3.1 Make invalid states unrepresentable (the AQuA principle)

Rank of leakage controls, weakest to strongest:

1. Prompt instruction ("do not use future data") — worthless.
2. LLM reviewer agent — **fails on shared blind spots**, demonstrated.
3. Static analysis / unit tests on generated code — catches some.
4. **Constrained DSL whose operators are causal by construction, closed under composition** — leakage cannot be written.
5. Sealed data loader, splits, and evaluator that the agent can never modify.

Aim for 4+5. Accept 3 only for exploratory work you will not fund.

### 3.2 Separate the optimization metric from the reported metric

Non-negotiable. The agent optimizes against an inner validation slice. A held-out window is scored **once**, after freeze, and never re-enters the loop. Every time you let the agent see the test number, your test set becomes a training set at a rate proportional to the number of iterations.

Corollary: **track the trial count.** A self-improving loop runs thousands of backtests. Report deflated Sharpe / multiple-testing-adjusted statistics (Bailey & López de Prado's deflated Sharpe, CSCV probability of backtest overfitting), or your Sharpe 2.5 is a Sharpe 0.

### 3.3 Meta-overfitting is the distinctive risk

Classic overfitting: a strategy is tuned on history. **Meta-overfitting: the whole research *process* is tuned on the same history.** A self-improving research agent that learns "momentum + volatility confluence works" from 2018–2021 has embedded that regime into its *priors*, and the embedding survives every subsequent train/test split because it lives in the memory, not the model.

Mitigations, in order of effectiveness:
- Hold out *entire periods* from the research agent's existence, not just from a model fit — run the whole loop on 2010–2018, then evaluate the *process* on 2019–2025 untouched.
- Cap memory/belief lifetime; force periodic belief expiry (see 3.5).
- Run the loop independently on disjoint historical segments and keep only what both discover.
- Walk-forward the *meta-loop*, not just the strategy.

### 3.4 Hard gates, then soft scores, then a promotion engine

EVOQUANT's ablation is the most useful empirical number in this whole literature: removing the **promotion engine** cost 87% of the improvement; removing memory cost 20%; removing diagnosis 29%. **The gate matters more than the intelligence.**

A workable gate stack:

```
G1 executable + type-checks + no sealed-component modification
G2 minimum trade count in validation AND out-of-sample (kills sparse-signal artifacts)
G3 max drawdown ceiling on OOS
G4 semantic-drift bound vs. parent (edit stays in its declared layer)
G5 novelty: AST/structural distance from the existing library
G6 cost stress: 2x fees, +1 bar execution delay, slippage perturbation — must survive
G7 validation→test decay penalty in the score (not a post-hoc filter)
-- only now: rank by risk-adjusted score
-- then: shadow → small capital → full capital, with automatic demotion
```

G6 deserves emphasis: EVOQUANT retained 0.700 mean Sharpe uplift at 2× costs (from 0.982), but only 0.368 under alternative data splits. **Split sensitivity was a bigger threat than cost sensitivity.**

### 3.5 Memory governance (the SSGM four)

Evolving memory has its own failure modes ([SSGM framework](https://arxiv.org/pdf/2603.11768)): **poisoning** (adversarial or just bad data injected into memory), **drift** (memory diverges from original mandate), **error accumulation**, and **self-reinforcement** (the agent treats its own earlier wrong conclusion as ground truth). In trading, self-reinforcement is the one that kills you: a lucky trade becomes a "principle" becomes a concentration.

Four controls, all cheap to implement:
- **Validation** — nothing enters long-term memory without an outcome-grounded check.
- **Decay** — confidence declines with age; beliefs must be re-earned.
- **Provenance** — every belief carries the trades and dates that produced it, so a human can audit and delete.
- **Rollback** — memory is versioned; you can restore the state from before a degradation.

Add a trading-specific fifth: **attribution before consolidation** — a lesson may only be written if the outcome is statistically distinguishable from noise for that sample size. Otherwise the agent learns from coin flips.

### 3.6 Deployment spine: champion–challenger + shadow + capital ramp

Standard MLOps, and it is exactly the right shape here:

- One **champion** trades. Challengers run in **shadow** on identical live data, orders logged but never sent.
- Promotion requires a pre-declared window of shadow outperformance *plus* passing the gate stack — not a backtest.
- **Capital ramp**, not a switch: 5% → 25% → 100% of the sleeve, with automatic demotion on drawdown or on live-vs-shadow divergence.
- The **meta-allocator** across strategies is itself a learning problem (regime-conditioned allocation, or bandit-style if you accept the exploration cost), but it should be a *simple, slow, auditable* model. Do not stack a self-evolving allocator on top of self-evolving strategies.
- **Immutable audit log**: every proposal, its diff, its rationale, its gate results, its promotion decision. This is also your regulatory artifact.

### 3.7 Rate limiting

Give each loop a different clock and a hard budget:

| Loop | Period | Budget | Blast radius |
|---|---|---|---|
| Execution | ms–s | — | one order (hard risk limits, no LLM in path) |
| Reflection / memory write | per decision | N writes/day | one belief, rollback-able |
| Policy / parameter adaptation | weekly | bounded step size | one strategy sleeve |
| Discovery (evolution) | continuous offline | compute cap | nothing live until promoted |
| Meta / scaffolding | monthly | human-approved | the search itself |

The single most common architectural mistake is letting the discovery loop and the live loop share state.

---

## 4. Failure-mode → mitigation table

| Failure mode | Where it bites | Mitigation |
|---|---|---|
| Generation leakage (future data inside a feature) | [A] | Causal operator DSL, sealed loader (AQuA) |
| Selection leakage (test set consumed by iteration) | [A] | Optimization metric ≠ reported metric; score test once |
| Meta-overfitting (process tuned to history) | [A] | Hold out whole eras from the loop; walk-forward the meta-loop |
| Multiple testing / backtest overfitting | [A] | Trial counting, deflated Sharpe, CSCV |
| Verifier gaming / Goodharting | [A] | Hard gates + external execution grounding; never self-judged alone |
| Strategy homogenization → crowding, alpha decay | [A] | AST-novelty regularization, MAP-Elites diversity, capacity modelling |
| Zero-trade / degenerate optima | [A] | Minimum trade-count gates; consistency term in fitness |
| Memory poisoning / self-reinforcement | [B] | SSGM: validation, decay, provenance, rollback + noise-threshold on lessons |
| Oracle fallacy in retrieval | [B] | Timestamp-aware retrieval; store only info available at decision time |
| Catastrophic forgetting | [B] | Frozen base + additive modular adaptation + gate (ReCAP) |
| Regime shift | [B] | Online regime detection; regime-conditioned policy library |
| Error compounding across iterations | [A+B] | Blacklist failed mechanisms with reasons; bounded edit hierarchy |
| Cost/impact blindness | [A+B] | Cost stress tests in gates; capacity limits; live slippage feedback |
| Irreversible weight damage | [B] | Prefer L1–L3 edits; PEFT adapters you can detach; versioned checkpoints |
| Runaway compute spend | [A] | Per-loop budgets; fitness must include research cost |

---

## 5. How much to believe the literature

Be blunt about this, because the field's headline numbers are mostly not evidence.

The most rigorous thing published on this is the reproducibility audit inside [*Agentic Trading: When LLM Agents Meet Financial Markets*](https://arxiv.org/html/2605.19337v1): of 77 studies, only **19** actually emit tradable actions in closed-loop evaluation. Of those 19:

- **2/19** disclose extractable train/test splits
- **1/19** specifies a transaction-cost model
- **1/19** documents universe/survivorship handling
- **11/19** report execution timing or semantics
- **15/19** have no reproducible artifacts; **0/19** reach full reproducibility

Their conclusion: the primary subset "is not yet protocol-comparable."

And when someone does build a contamination-free forward-window benchmark — [StockBench](https://arxiv.org/html/2510.02209v2), 20 DJIA names, Mar–Jun 2025, after model cutoffs — **most frontier LLM agents fail to beat buy-and-hold** (baseline +0.4% / −15.2% MDD; best agent ~+1.9% / −11.8%). [LiveTradeBench](https://arxiv.org/html/2511.03628v1) and Agent Market Arena are pushing the same live, contamination-resistant direction.

So: treat every Sharpe in section 2 as a *hypothesis about a mechanism*, not a result. What transfers from these papers is **architecture and control**, which is why this note is weighted that way.

---

## 6. Reference architecture (synthesis)

A blueprint combining the pieces that are actually load-bearing. Five loops, one spine.

```
                         ┌──────────────── GOVERNANCE SPINE ─────────────────┐
                         │ immutable audit log · versioned memory · budgets  │
                         │ promotion engine · kill switch · human approval   │
                         └───────────────────────────────────────────────────┘
                                       ▲          ▲          ▲
 ┌─────────────────────────────────────┴──┐  ┌────┴─────┐  ┌─┴──────────────────────────┐
 │  L4 META LOOP (monthly, human-gated)   │  │ CAPITAL  │  │  L3 DISCOVERY LOOP (cont.) │
 │  evolve operators, prompts, workflow   │  │ ALLOCATOR│  │  hypothesis → DSL spec →   │
 │  archive of all variants (DGM-style)   │  │ regime-  │  │  sealed backtest → gates   │
 └────────────────────────────────────────┘  │ condit.  │  │  MAP-Elites diversity grid │
                                             │ frozen   │  │  AST-novelty vs library    │
 ┌────────────────────────────────────────┐  │ library  │  └────────────┬───────────────┘
 │  L2 ADAPTATION LOOP (weekly)           │  └────┬─────┘               │ promoted artifacts
 │  regime gate → policy/param vectors    │       │                     ▼
 │  frozen base + additive modules        │       │        ┌────────────────────────────┐
 └───────────────────┬────────────────────┘       │        │  STRATEGY LIBRARY (frozen, │
                     │                            └───────▶│  versioned, attributed)    │
 ┌───────────────────▼────────────────────┐               └────────────┬───────────────┘
 │  L1 REFLECTION LOOP (per decision)     │                            │
 │  layered memory: working / episodic /  │◀───────────────────────────┘
 │  semantic · decay · provenance         │
 │  two-level reflection (trade/strategy) │
 └───────────────────┬────────────────────┘
                     ▼
 ┌────────────────────────────────────────┐        ┌───────────────────────────────────┐
 │  L0 EXECUTION (no learning in path)    │───────▶│ SHADOW LANE: challengers on live  │
 │  hard pre-trade risk limits, sizing,   │        │ data, orders logged not sent      │
 │  cost model, order routing             │        └───────────────────────────────────┘
 └────────────────────────────────────────┘
```

Non-obvious properties of this design:

1. **The discovery loop never touches live state.** Its only output is a promoted, frozen artifact.
2. **Everything live is frozen + additive.** Adaptation happens through a gate over a library, never by mutating a running policy.
3. **Memory is versioned infrastructure**, sitting under reflection, with the same rollback guarantees as code.
4. **The capital allocator is deliberately dumb** relative to the rest — it is the one component whose failure is unhedged.
5. **Two human gates only**: meta-loop changes and first capital allocation to a new strategy. Everything else is automatic but logged.
6. **Diversity is enforced at the library level**, not per-strategy — the library is the thing that must stay uncorrelated.

---

## 7. Build order (what I'd actually do, in order)

1. **Sealed evaluation harness first.** Causal operator registry / DSL, immutable splits, cost model, single-shot test scoring, trial counter with deflated-Sharpe reporting. Nothing else matters until this exists — and it is the part no paper will give you.
2. **Strategy library + promotion engine + shadow lane.** Still no AI. This is the 87%-of-the-value component per EVOQUANT's ablation.
3. **L1 reflection + governed memory** on your existing agent (validation, decay, provenance, rollback, timestamp-aware retrieval). Cheapest real improvement.
4. **L3 discovery loop**: LLM-as-mutation-operator over the DSL, MAP-Elites feature map for diversity, AST-novelty vs. your library, hard gates. Start with factor expressions (small, verifiable) before whole strategies.
5. **L2 regime-conditioned allocation** over the now-populated library (ReCAP pattern; can be non-neural — a regime classifier plus weights is fine).
6. **L4 meta loop** last, human-gated, with an archive. Only after 1–5 have been stable for months.
7. **L5 weight-level RL** only if you have a genuine high-frequency reward signal. For most desks this is never.

Explicitly deprioritized: agent-vs-agent market co-evolution (use it as an adversarial stress test, not an alpha source); multi-agent debate scaffolds for their own sake (cost scales, evidence is weak); anything that lets an LLM edit live trading code without the gate stack.

---

## 8. Open problems

- **No accepted protocol** for reporting self-improving trading results (trial counts, meta-loop walk-forward, cost assumptions). The audit above is the closest thing to a checklist.
- **Capacity and crowding are unmodelled** in every discovery system reviewed. Novelty is measured structurally, not economically — an AST-novel factor can still be economically identical to a crowded one.
- **Credit assignment over long horizons**: which memory/belief caused which PnL, at sample sizes where nothing is significant.
- **Stopping rules**: nobody has a principled answer to when a self-improving loop should stop, other than compute budget.
- **Co-evolution with other AI agents**: as more capital is run by similar LLM-driven agents trained on similar corpora, homogenization risk is systemic, not just per-fund.
- **Cryptographic rather than procedural test-set isolation** — AQuA notes its own isolation relies on governance discipline.

---

## Sources

Self-evolution, general:
- [A Survey of Self-Evolving Agents: On Path to Artificial Super Intelligence](https://arxiv.org/html/2507.21046v3)
- [A Comprehensive Survey of Self-Evolving AI Agents](https://arxiv.org/pdf/2508.07407)
- [Self-Improvements in Modern Agentic Systems: A Survey](https://arxiv.org/html/2607.13104v1)
- [Darwin Gödel Machine: Open-Ended Evolution of Self-Improving Agents](https://arxiv.org/abs/2505.22954) · [code](https://github.com/jennyzzt/dgm) · [Sakana writeup](https://sakana.ai/dgm/)
- [Governing Evolving Memory in LLM Agents (SSGM)](https://arxiv.org/pdf/2603.11768)
- [Awesome-Self-Evolving-Agents](https://github.com/XMUDeepLIT/Awesome-Self-Evolving-Agents)

Trading-specific architectures:
- [Agentic Trading: When LLM Agents Meet Financial Markets](https://arxiv.org/html/2605.19337v1) — the survey + reproducibility audit
- [AQuA: Recursively Self-Improving Quantitative Trading Research Agents](https://arxiv.org/html/2608.12841v1)
- [EVOQUANT: Self-Evolving Verifier-Guided Strategy Optimization](https://arxiv.org/html/2607.12455v1)
- [QuantEvolve: Multi-Agent Evolutionary Framework](https://arxiv.org/html/2510.18569v1)
- [AlgoEvolve: LLM-driven Meta-evolution of Algorithmic Trading Programs](https://arxiv.org/html/2606.26173)
- [QuantaAlpha: Evolutionary Framework for LLM-Driven Alpha Mining](https://arxiv.org/html/2602.07085v2)
- [AlphaAgent: Regularized Exploration to Counteract Alpha Decay](https://arxiv.org/abs/2502.16789) (KDD'25)
- [AlphaMemo: Structured Search-Process Memory](https://arxiv.org/pdf/2606.20625)
- [RD-Agent](https://github.com/microsoft/RD-Agent) / [RD-Agent-Quant](https://www.microsoft.com/en-us/research/publication/rd-agent-quant-a-multi-agent-framework-for-data-centric-factors-and-model-joint-optimization/) · [Qlib](https://github.com/microsoft/qlib)
- [FLAG-Trader: Fusion LLM-Agent with Gradient-based RL](https://arxiv.org/abs/2502.11433) (ACL Findings 2025)
- [FinCon: Conceptual Verbal Reinforcement](https://arxiv.org/html/2407.06567v2) (NeurIPS 2024)
- [FinMem: Layered Memory Trading Agent](https://ojs.aaai.org/index.php/AAAI-SS/article/download/31290/33450)
- [TradingAgents](https://arxiv.org/html/2412.20138v5)
- [ReCAP: Regime-Adaptive Continual Learning for Portfolio Management](https://arxiv.org/html/2606.00143)
- [AI Trading's Alpha Singularity: Agent-to-Agent Self-Evolution](https://arxiv.org/pdf/2606.29194)
- [Awesome-LLM-Quantitative-Trading-Papers](https://github.com/Tom-roujiang/Awesome-LLM-Quantitative-Trading-Papers)

Evaluation:
- [StockBench](https://arxiv.org/html/2510.02209v2) · [LiveTradeBench](https://arxiv.org/html/2511.03628v1) · [FinWorld](https://github.com/TradeMaster-NTU/FinWorld)
