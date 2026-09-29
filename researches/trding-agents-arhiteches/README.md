# Trading Agent Architectures

Research notes on how automated trading agents are actually built, with every architecture
visualised as a standalone interactive diagram (archify, showcase profile).

Open `index.html` for the diagram gallery. Diagram sources are in `specs/`, rendered pages in `diagrams/`.

---

## The design space

Recent surveys organise trading agents along four architectural axes rather than by
paper lineage ([Agentic Trading, arXiv:2605.19337](https://arxiv.org/abs/2605.19337)):

| Axis | Question it answers | Where it varies |
|---|---|---|
| **Perception** | What can the agent see? | Text only → time-series + fundamentals → multimodal (chart images) |
| **Memory** | What does it carry between decisions? | Context window → episodic store → layered decay + semantic knowledge |
| **Reasoning** | How long may it think? | Reactive (ms) → reflective chain-of-thought (s) → strategic search (hours) |
| **Action** | How does a decision become an order? | Assumed fill → typed order + cost model → microstructure and latency aware |

Almost every published system is a specific point in that space. The useful comparison is not
"which returned more in backtest" but which axis each one invested in.

---

## 1. TradingAgents — the firm as a role-split team

→ [`diagrams/01-tradingagents.html`](diagrams/01-tradingagents.html)

Seven-plus LLM agents arranged like a trading firm. Four analysts (fundamentals, news,
sentiment, technical) gather evidence **concurrently** and write typed reports into shared
state. A bull and a bear researcher then argue over that state for multiple rounds; a
research manager terminates the debate and commits an investment plan. A trader sizes the
position, a three-way risk debate (risky / neutral / safe) re-argues it, and a fund manager
approves the release.

Two design choices carry the weight:

- **Structured documents, not transcripts.** Agents exchange typed reports through a global
  state rather than chatting. The paper's stated motivation is avoiding the "telephone
  effect" where detail degrades across conversation hops. Free-form natural language is
  confined to the researcher and risk debates, where disagreement is the point.
- **Tiered models.** Quick models handle summarisation, retrieval and tool calls; deep
  models handle analysis and decisions. Cost tracks reasoning depth, not message count.

The by-product is auditability: every decision arrives with a natural-language rationale
chain, which is the main thing a deep-learning policy cannot give you.

Sources: [arXiv:2412.20138](https://arxiv.org/abs/2412.20138) ·
[TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents)

## 2. FinMem — depth from memory, not headcount

→ [`diagrams/02-finmem.html`](diagrams/02-finmem.html)

A single agent with three modules: profiling, layered memory, decision-making.

- **Profiling** makes risk character an explicit input: risk-seeking, risk-averse, or
  self-adaptive (switching on recent realised performance), plus a professional knowledge base.
- **Working memory** summarises raw news, filings and prices into short insights, observes
  price movement, and reflects — immediately per day and over longer windows.
- **Layered long-term memory** stores those insights in three buckets with different decay
  characteristics: shallow (daily news, ~14-day stability), intermediate (10-Q, ~90-day),
  deep (10-K and extended reflections, ~365-day). Retrieval scores each event on recency
  (layer-specific decay), relevancy (embedding similarity) and importance; an access counter
  promotes events that preceded profitable trades into deeper layers. A "cognitive span"
  caps how many memories reach the prompt.

The claim being tested is that a flat context window is the wrong shape for financial
information, because a 10-K and a headline do not stay useful for the same length of time.

Source: [arXiv:2311.13743](https://arxiv.org/abs/2311.13743)

## 3. FinAgent — trading as an information-fusion problem

→ [`diagrams/03-finagent.html`](diagrams/03-finagent.html)

A market intelligence module fuses numeric, textual **and visual** inputs — rendered K-line
charts are a first-class modality, not a re-encoding of the numbers. Two reflection layers
ask different questions: low-level reflection relates an observation to the price move that
followed; high-level reflection critiques the agent's own past trades. Retrieval is split
per task so trading queries do not pull reflection noise. The decision module folds in
expert guidance and classic indicator strategies (MACD, KDJ) as callable priors that
constrain rather than replace the model's reasoning.

Reported results: >36% average profit improvement over 12 baselines across 6 stock and
crypto datasets. Treat cross-paper backtest numbers with the caution described in
[§ What the evidence actually supports](#what-the-evidence-actually-supports).

Source: [arXiv:2402.18485](https://arxiv.org/abs/2402.18485) (KDD '24)

## 4. ContestTrade — competition as a noise filter

→ [`diagrams/04-contesttrade.html`](diagrams/04-contesttrade.html)

The most interesting idea here is that **prompt context is a scarce resource to be
allocated**, not a bucket to be filled.

A Data Team of parallel agents cuts a day of market information down to text factors of
≤4k tokens each. Then a contest runs a three-phase pipeline — quantify, predict, allocate:

- **Quantify** — a "zero-intelligence trader" scores each observation on its raw predictive
  power, isolated from any agent's strategy.
- **Predict** — factor scores show short-term momentum, so a LightGBM model maps recent
  scores to expected utility and volatility, giving a risk-adjusted `û = μ̂/σ̂`.
- **Allocate** — a 0/1 knapsack selects the factor set maximising predicted utility subject
  to an *effective* context length `L*` (~16k tokens), below the nominal limit, because
  decision capability decays sigmoidally with prompt length.

A Research Team of agents with distinct LLM-generated trading beliefs then works the
selected factors under Plan + ReAct with a financial tool belt. A second contest scores them
on trailing Sharpe plus an LLM judge panel assessing logical soundness and evidence quality,
and allocates capital proportionally to positive predicted Sharpe.

Source: [arXiv:2508.00554](https://arxiv.org/abs/2508.00554)

## 5. Agentic alpha discovery — the loop is the architecture

→ [`diagrams/05-alpha-discovery.html`](diagrams/05-alpha-discovery.html)

The Alpha-GPT / QuantAgent lineage automates the quant research workflow rather than the
trade itself: hypothesis generation → executable factor construction → backtest →
critique → repeat. The LLM proposes; deterministic code decides what survives.

What distinguishes the more recent systems is what they put *back* into generation:

- **Regularisation against crowding.** AlphaAgent penalises factors that duplicate what the
  book already trades, to slow alpha decay.
- **Search-process memory.** AlphaMemo and similar systems store the structure of the search
  — including failed branches — not just the winners.
- **Joint factor–model optimisation.** RD-Agent coordinates research and development agents
  over the full stack.

The hard part is not idea generation; it is the point-in-time guard and the cost model.

Sources: [QuantaAlpha](https://arxiv.org/abs/2602.07085) ·
[AlphaMemo](https://arxiv.org/abs/2606.20625) ·
[Chain-of-Alpha](https://arxiv.org/abs/2508.06312) ·
[QuantEvolve](https://arxiv.org/abs/2510.18569)

## 6. FinRL — the pre-LLM baseline worth keeping

→ [`diagrams/06-finrl.html`](diagrams/06-finrl.html)

Three layers, each exposing an API upward: environment (data processor, Gym-style market
simulator, observation and reward), agent (PPO / SAC / TD3 / DDPG over a replay buffer),
and application (train → validate → backtest → paper/live). The same agent code runs
against backtest, paper and live environments because only the environment changes.

Worth diagramming alongside the LLM systems because it makes the trade-off explicit: fast
and cheap at inference, an explicitly encoded objective, no deliberation step — and a policy
that cannot explain itself, needs a separate pipeline for unstructured text, and must be
retrained rather than re-prompted when the regime shifts.

Sources: [arXiv:2111.09395](https://arxiv.org/abs/2111.09395) ·
[FinRL-Meta, arXiv:2112.06753](https://arxiv.org/abs/2112.06753) ·
[AI4Finance-Foundation/FinRL](https://github.com/AI4Finance-Foundation/FinRL)

## 7. LLM agent market simulation — when the agents make the price

→ [`diagrams/07-market-simulation.html`](diagrams/07-market-simulation.html)

ASFM, StockSim and related platforms replace the replayed tape with a real order book:
heterogeneous LLM agents with different beliefs, information sets and endowments submit
limit and market orders that clear against each other under price-time priority, with
partial fills, dividends and equilibrium clearing.

This changes what you can study. In a backtest the agent is a price-taker and cannot be
wrong about liquidity. In a simulation the agents move the price they then observe, so
herding, path dependence and strategy crowding become measurable — and a strategy can be
stress-tested against adaptive counterparties rather than a fixed history.

Sources: [ASFM, arXiv:2406.19966](https://arxiv.org/abs/2406.19966) ·
[StockSim, arXiv:2507.09255](https://arxiv.org/abs/2507.09255) ·
[Can LLMs Trade?, arXiv:2504.10789](https://arxiv.org/abs/2504.10789)

## 8. Production reference stack — seven layers

→ [`diagrams/08-production-stack.html`](diagrams/08-production-stack.html)

None of the research architectures above is deployable as-is, because they stop at the
decision. A production agent is a distributed system in which the LLM happens to be the
planner:

1. **Ingestion & normalisation** — vendor integration, point-in-time correctness, survivorship audit.
2. **Deterministic signals** — indicators, regime classification, confidence scoring. *Cheap
   arithmetic before expensive inference*; the guide this layering comes from reports ~80%
   of candidates filtered before any model call.
3. **Context & state** — positions, regime assessment, decision history.
4. **Reasoning & orchestration** — the multi-agent layer (this is where §1–§4 live).
5. **Policy enforcement** — a rules engine evaluating position limits, exposure caps and the
   execution authority contract *after* the model proposes and *before* the order goes out.
   No model interprets policy.
6. **Execution gateway** — order routing, rate limiting, a tested kill switch, named human
   operators per time zone.
7. **Evidence ledger** — agent identity, contract version in force, observed market state,
   each agent's reasoning, guardrail evaluations, approval status and outcome, retrievable
   per order in minutes.

Two operational details that generalise: each agent gets **its own credential and revocation
path** (a shared API key makes it impossible to attribute or revoke one agent's authority),
and every order links to the **version** of the authority contract that authorised it.

Source: [AI Trading Agent Development: 2026 Architecture Guide](https://www.ampcome.com/post/ai-trading-agent-development)
(industry guide, not peer-reviewed — treat the layering as a useful checklist rather than a result)

## 9. Graded autonomy — authority as a versioned contract

→ [`diagrams/09-graded-autonomy.html`](diagrams/09-graded-autonomy.html)

Autonomy is per-instrument, per-notional, per-regime, not a boolean. Five levels run from
advisory (human writes every order) through approval workflow, conditional autonomy and
bounded autonomy to supervised autonomy. The practical advice in the source: **ship at
approval workflow and earn the next level on evidence.**

An *execution authority contract* is the machine-readable envelope: agent identity and
ownership, instrument universe, size and daily notional limits, a permission matrix,
quantified guardrails (drawdown %, concentration %, sector exposure %), escalation
thresholds, kill-switch triggers and authorised operators, and evidence retention rules.
It is authored by risk, reviewed by compliance, versioned alongside code, and evaluated
deterministically.

Escalation triggers include notional thresholds, confidence degradation, conflicting agent
verdicts, data staleness and unrecognised market regimes. An escalation pauses one order —
it should not demote the agent; only an unanswered review or a confirmed breach rolls the
contract back.

---

## Comparison

| System | Type | Perception | Memory | Coordination | Action model |
|---|---|---|---|---|---|
| TradingAgents | Multi-agent firm | Text + indicators, split by role | Reflection on past decisions + returns | Role debate, manager arbitration | Discrete decision + risk gate |
| FinMem | Single agent | Text + prices | Three-layer decay, scored retrieval | — | Buy / sell / hold |
| FinAgent | Single agent | Numeric + text + **images** | Vector store, task-split retrieval | — | Position with reasoning trace |
| ContestTrade | Multi-agent, competitive | Text factors from broad corpus | Trailing performance scores | Contest + capital allocation | Sharpe-weighted signal portfolio |
| Alpha discovery | Agent loop | Panel data + research corpus | Experiment / search-process memory | Researcher–developer split | Factor added to a live book |
| FinRL | RL policy | Numeric state vector | Replay buffer (no semantics) | — | Continuous or discrete action |
| Market simulation | Multi-agent, adversarial | Public tape + private portfolio | Per-agent, heterogeneous | None — only the order book | Limit / market orders, partial fills |

---

## What the evidence actually supports

This is the part most write-ups skip. The 2026 agentic-trading survey ran a protocol audit
over its primary studies and found reporting thin where it matters most
([arXiv:2605.19337](https://arxiv.org/abs/2605.19337)):

- **2 of 19** studies used time-consistent data splits.
- **1 of 19** stated an explicit transaction-cost model.
- **1 of 19** documented universe construction and survivorship handling.
- **11 of 19** specified execution timing and semantics.
- **15 of 19** were coded at the lowest reproducibility tier (no code or minimal artifacts);
  **none** reached full deterministic replay with versioned data snapshots.

So: the architectures are real and the mechanisms are worth borrowing; the *return numbers*
across papers are not comparable, and a headline Sharpe from a paper with no cost model and
no point-in-time guarantee should be read as an upper bound on a fantasy.

Practical consequences if you build on any of this:

1. Fix the evaluation protocol before the architecture. Point-in-time data, survivorship
   handling, an explicit cost and slippage model, and a stated execution timing convention.
2. Log decisions as immutable artifacts from day one — prompt version, tool calls, retrieved
   memories, search budget, rejected branches. You cannot reconstruct them later.
3. Put the deterministic layers around the model early. Layers 2 and 5 of the production
   stack are cheap to build and are what make layer 4 safe to iterate on.
4. Live behaviour diverges from backtest. LiveTradeBench exists precisely because streaming,
   portfolio-level decisions expose gaps that single-asset replay hides
   ([arXiv:2511.03628](https://arxiv.org/abs/2511.03628)).

---

## Regenerating the diagrams

```bash
ARCHIFY=~/.claude-faridagazizov/skills/archify/bin/archify.mjs
node $ARCHIFY validate architecture specs/01-tradingagents.architecture.json --quality showcase
node $ARCHIFY deliver  architecture specs/01-tradingagents.architecture.json diagrams/01-tradingagents.html --quality showcase
```

All nine specs pass the showcase profile with 9/9 artifact checks and 0 composition errors
or warnings. Browser-based visual review (`archify visual-check`) could not run in this
environment — the bundled Chromium is missing `libasound.so.2` / `libgbm.so.1`. Install
`libasound2` and `libgbm1` and rerun it for screenshot evidence.
