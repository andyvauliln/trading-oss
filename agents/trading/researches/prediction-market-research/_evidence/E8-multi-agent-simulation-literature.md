# Adjacent literature for simulation-based and multi-agent forecasting
_As of 2026-09-20. Evidence pack E8 for the Polymarket strategy survey._

Tags: **[H]** paper / preprint / official data with a stated dataset · **[C]** named-outlet report · **[S]** self-reported, unchecked · **[M]** marketing. "(derived)" = my arithmetic. arXiv items are preprints unless a venue is named. **[pre-2025]** = published before 2025, possibly stale.

Method: the session's WebSearch quota was exhausted, so discovery used WebFetch on the arXiv API, OpenAlex, Crossref and Bing HTML, then primary pages. Ledger column F = page fetched, S = seen only as a listing abstract ("snippet" below). Numbers come from abstracts / HTML via the fetch summariser and were not re-checked against PDFs.

## Key facts

1. **Ten LLM agents can equal ~1.4 independent forecasters.** DPO-tuned agents in an LLM prediction market: pairwise error correlation rho = 0.70; N_eff flat from N=5 to N=40; ten-agent market 67.6% accurate vs 70.2% for one agent alone. DPO adds +0.24 to +0.46 correlation vs identical SFT baselines (8B, 70B); mixing model families cuts 0.68 -> 0.40 [42][H]. Check (derived): N_eff = N / (1 + (N-1)rho) = 10 / 7.3 = 1.37; limit 1/rho = 1.43.
2. **Multi-agent debate is a martingale; majority vote carries the gain.** NeurIPS 2025 spotlight, 7 benchmarks: "Majority Voting alone accounts for most of the performance gains typically attributed to MAD"; debate "induces a martingale over agents' belief trajectories" [25][H]. Replications: 5 MAD methods x 9 benchmarks x 4 models "often fail to outperform" CoT / self-consistency at higher compute [24][H]; homogeneous debate uses 2.1-3.4x the tokens of isolated self-correction for equal or lower accuracy, with "sycophantic conformity" up to 85.5% [27, snippet].
3. **The one forecasting-specific debate test: ~4%, only with model diversity.** 202 resolved Metaculus Q2-2025 questions; GPT-5, Claude Sonnet 4.5, Gemini 2.5 Pro: deliberation cut log loss 0.020 (~4%, p = 0.017) for diverse models; homogeneous groups and extra context: no gain [30][H].
4. **Interview-grounded agents, the best-validated individual simulators, reach 83-86% of human test-retest consistency.** 1,052 Americans, 2-hour interviews: v1 abstract 85% normalised GSS accuracy; current version 83% (interview), 82% (survey), 86% (both), 74% (demographics-only persona) [2][H]. The cheap persona prompt sits 9-12 points lower.
5. **Digital twins trained on 500+ answers per person correlate r = 0.20 with their human** (19 pre-registered studies, 164 outcomes); "only modestly more accurate than a homogeneous base LLM"; distortions: insufficient individuation, stereotyping, representation bias, ideological bias, hyper-rationality [8][H].
6. **Aggregate treatment effects are much easier: r = 0.85.** GPT-4 vs 70 pre-registered US survey experiments (469 conditions, 119,330 participants); r = 0.90 on studies unpublished at training time; on par with human forecasters; overestimates effect sizes [19][H, snippet].
7. **Synthetic polling: one strong prospective hit, one public miss.** PoSSUM (1,054 X users read by a multimodal LLM + MrP, fielded 17-26 Oct 2024) called 50 of 51 states, Republican win probability 0.65, lower state-level bias than most pollsters [14][H]. Aaru (~5,000 census-seeded agents per poll) called the June 2024 NY-16 primary within 371 votes but on 2024-09-20 projected Harris +4.2 in the popular vote [15][C]; actual Trump +1.5 [18] -> 5.7-point margin error (derived; Aaru's final call unverified).
8. **Silicon samples are under-dispersed and structurally wrong even when means match.** ChatGPT vs ANES: 48% of regression coefficients differ significantly and the sign flips in 32% of those; identical prompts drifted between April and July 2023 [10][H][pre-2025]. 2026: instruction-tuned models returned the identical answer on 50% of items while describing the true distribution correctly [13a, snippet].
9. **LLM simulations are fragile to cosmetic changes.** Persona-format and instruction-framing perturbations moved cooperation rates by up to 76 percentage points in one frontier model and 1 point in another [7][H]; a systematic review finds validation "poorly addressed", often mere "believability" [6][H].
10. **Leakage manufactures LLM forecasting skill.** 254 prediction-market questions, 15 LLMs: the frontier-vs-small gap fell from 35.8% to 8.9% on questions resolved after every training cutoff [41][H]. Paleka et al. document temporal leakage through search and a benchmark-to-live gap in earlier "human-level" claims [38][H].
11. **LLM forecasters add value early and on uncertain markets, not near resolution.** 10 models x 150 Kalshi markets x 5 checkpoints (15,000 forecasts): "most competitive early in a market's life and on high-uncertainty markets, much less competitive near resolution and on strong-consensus markets"; web search hurt in 12% of model-checkpoint pairs; two-model ensembles did not beat the market [77][H]. Prophet Arena: "slower information aggregation compared to markets when resolution nears" [76][H].
12. **The best engineered forecaster loses to liquid-market consensus, but forecaster + market beats the market.** AIA Forecaster (agentic search, supervisor reconciliation, statistical calibration) equals superforecasters on ForecastBench, underperforms consensus on the liquid-market benchmark, yet "an ensemble combining AIA Forecaster with market consensus outperforms consensus alone" [39][H].
13. **Stated confidence is worthless; wagered confidence is not.** PolyBench (38,666 Polymarket markets, 4,997 events, 6-12 Feb 2026, order-book execution simulated): 2 of 7 LLMs profitable (+17.6%, +6.2% confidence-weighted return); five lost "despite uniformly high stated confidence" [78][H]. In play-money betting, wagers >= 40,000 coins were ~99% correct vs ~74% below 1,000 [43][H; single author, maths/logic tasks].
14. **RL on resolved market questions works at 14B.** RLVR on Polymarket questions + headlines matches or beats o1 with much better calibration; simulated Polymarket betting > 10% ROI over the test set [72][H, simulated fills]. Also: outcome-ranked self-play + DPO +7-10% accuracy (Phi-4 14B, DeepSeek-R1 14B ~ GPT-4o) [73]; Qwen3-32B +27% Brier, halved calibration error [74, snippet]; online memory evolution +20.8% Brier, +12.9% market return over 10 weeks on Prophet Arena [75].
15. **GJP's algorithmic layer is the automatable part.** 2,400+ forecasters, 261 events: team polls + temporal decay + differential weighting + recalibration beat continuous-double-auction markets (12% Brier per the proceedings abstract), most "at the beginning of long-duration questions" [86, snippet]. Under an hour of debiasing training: 6-11% Brier [83]; noise reduction is the consistent driver across training, teaming and tracking [85].
16. **Zero-intelligence baselines set the bar for market simulators.** Budget-constrained random traders reach ~100% allocative efficiency [52]; a one-parameter ZI order-flow model explains 96% of spread variance and 76% of price-diffusion variance [53] [both pre-2025, snippets].
17. **LLMs agree with UMA's final resolution 89.58% of the time** [71, snippet] - the only institutional-twin number found that maps onto a Polymarket mechanism.

## 1. LLM agent-society simulation

- **Generative Agents** (25 agents, Apr 2023): believability and ablation only, no real-world validation [1][pre-2025]. **Concordia** (DeepMind, Dec 2023): library with a Game-Master agent adjudicating natural-language actions; no validity claim [5][pre-2025].
- **OASIS** (Nov 2024, v5 Mar 2025): up to 1M agents on X/Reddit clones, Llama3-8B-instruct. Validated on 198 real propagation instances (Twitter15/16, 9 topics, 100-700 users): normalised RMSE ~30%; scale and max breadth track reality, depth too shallow. Agents follow down-votes more than humans did; polarisation emerges, more with uncensored models [3][H].
- **AgentSociety** (Feb 2025, v2 Apr 2026): > 10k agents, ~5M interactions; claims "alignment" with real experiments on polarisation, inflammatory messages, UBI, hurricane mobility; agreement metrics not retrievable [4].
- **Field status**: [6][7]; the LLM black box "exacerbates" ABM calibration problems [6]. Positive micro-results are stylised-fact matches (980 agents vs real participation patterns; friendship paradox) [95, snippets], not forecasts.
- **Election simulators**: ElectionSim (million-scale voter pool, PPE benchmark) [20b]; Yu et al. (theory-driven personas) [20a]; FlockVote "replicates" 2024 in seven swing states but was published Nov 2025 with no leakage control in the abstract [20c]. None is a scored prospective forecast; PoSSUM is [14].
- **MiroFish** (OASIS-based "prediction engine", 74.1k GitHub stars): demo videos, no accuracy metrics, backtests or market comparison [91][M].
- **FOR**: aggregate effects r = 0.85 [19]; grounded agents 83-86% [2]; diffusion scale within ~30% [3]. **AGAINST**: individual fidelity r = 0.20 [8]; prompt fragility [7]; no prospective scored society-level forecast found. **Failure modes**: believability mistaken for validity; shallow cascades; over-herding on negative signals; alignment tuning suppresses extremes; "replicating" events inside the training window.

## 2. Silicon sampling / synthetic respondents

- Origin: Argyle et al. (2022) - GPT-3 conditioned on thousands of real backstories shows "algorithmic fidelity" to subgroup distributions [9][pre-2025].
- Critiques: variance collapse, sign flips, prompt sensitivity, drift [10]; misportrayal and flattening of 16 identities (4 LLMs, 3,200 humans; mitigations "reduce, but do not remove") [11]; German 2017 vote: GPT-3.5 biased to Greens / Left, adequate only for strong partisans [12]; "severe homogenization" on ANES abortion / immigration items [13d]; marginals match, joints fail [13c]; all five frontier models failed dynamic belief-updating tests [13b]; weak demographic nuance and post-cutoff events (Harvard researchers via Semafor) [15].
- What does better: supervised transfer on real survey data (up to 93%, "especially on sensitive measures") [13e]; zero-shot LLMs 52% on unseen Taiwan election-survey items, 6 points behind a random forest, partisan items 67%, sovereignty 23% [13f]; screening questions by R^2 > 0.7 lifts twin-human correlation 15% and cuts badly answered questions 25.9% -> 4.3% [92] (all snippets).
- Commercial: Aaru - founded Mar 2024; Series A Dec 2025 (Redpoint) at a $1B headline valuation, ARR < $10M; clients EY, Accenture, IPG, campaigns [17][C]. Vendor-sourced accuracy: NY-16 within 371 votes [15]; NYC mayoral primary "within 2,000 votes" from ~2M simulated voters; EY wealth survey: humans said 82% would keep the parents' adviser, real retention 20-30%, Aaru ~40% [16][S]. Aaru concedes it cannot predict high-variance individuals "like President Trump or Jerome Powell" [16]. Named competitors (CulturePulse, Simile, Listen Labs, Keplar, Outset) [17]: no independent election scorecard found.
- **FOR**: [14][19]. **AGAINST**: [8][10][11][12][13a-d]; Harris +4.2 [15]. **Failure modes**: under-dispersion (uncertainty too tight, Kelly over-bets); stereotyped subgroups; liberal / socially-desirable skew; silent model updates; nothing after cutoff unless agents browse, and then they inherit media skew.

## 3. Multi-agent debate and judge methods

- Du et al. (May 2023): multi-round debate, gains in maths, strategy, factuality [21][pre-2025]. Controlled follow-ups: [24][25][27]; MAD does not reliably beat self-consistency and is hyper-parameter sensitive [26]; "majority pressure suppresses independent correction" [29]; vanilla MAD "underperforms simple majority vote" unless diversity and calibrated confidence are injected [28]; voting protocols +13.2% on reasoning, consensus +2.8% on knowledge tasks [97] (snippets).
- Debate under information asymmetry: judges reading two stronger debaters reach 76% (LLM judge) and 88% (human) vs 48% / 60% naive baselines; optimising debaters for persuasiveness helps truth [22][2024]. DeepMind: debate beats consultancy everywhere, beats direct QA only on extractive tasks with information asymmetry, mixed on maths / code / logic, gains "more modest" [23][2024]. Debate pays when one agent holds evidence the judge lacks, not when all share one context.
- LLM-as-judge: GPT-4 > 80% agreement with humans, with position, verbosity and self-enhancement bias [31][pre-2025]; "worse than random" against deceptive models 5-20x the judge's size, while peer-prediction scoring holds at > 100x gaps [32][H]; judges and reward models are least calibrated where human preferences diverge, and model families give "strikingly similar outputs" [33][H].
- Red-teaming: arbitrage-style consistency violations (negation, conjunction, conditional) correlate with eventual Brier score - an instant label-free quality signal [34, snippet]. No study of a red-team agent improving forecast Brier found.
- **FOR**: [22][30]. **AGAINST**: [24][25][26][27]. **Failure modes**: conformity cascades; shared context makes agents exchangeable; persuasive-but-wrong debaters beat weak judges; 2-3x token cost.

## 4. Internal prediction markets and aggregation

- **LMSR** (Hanson): C(q) = b ln sum_i exp(q_i / b); p_i = exp(q_i / b) / sum_j exp(q_j / b); worst-case subsidy b ln n [47][pre-2025].
- **Artificial markets over ML models**: Barbu & Lay (2011) - classifiers trade with budgets, price = ensemble output; detection 79.6% -> 81.2% at 3 false positives [44]. Storkey: markets implement product- and mixture-of-experts [45] [both pre-2025]. Hybrid human-AI replication markets "match or outperform" artificial-only ones [46] (snippets).
- **LLM-agent markets**: monoculture [42]; a betting frame makes confidence legible and sped learning (+12.0 points over four rounds vs +2.9, p = .011), but the accuracy edge was weak (81.5% vs 79.1%, p = .089) [43].
- **LLM ensembles**: 12-LLM median statistically indistinguishable from 925 humans on 31 questions; acquiescence bias (mean forecast > 50% with balanced outcomes); showing GPT-4 / Claude 2 the human median improved accuracy 17-28% [35][2024]. Logistic-regression stacking of 15 LLMs beat every single model and every classical pooling rule; an MLP added nothing - the gain is linear re-weighting of diverse outputs [41].
- **Peer prediction / BTS**: "surprisingly popular" rule - choose the answer whose actual frequency exceeds its predicted frequency (Prelec, Seung, McCoy, Nature 2017) [48]; error-reduction figures not retrievable. With LLMs: resists deception [32]; peer-predictive self-training +2.2-4.3 points [49, snippet]. No forecasting test of BTS over LLM agents found.
- **Delphi with LLMs**: only a qualitative scenario study surfaced [50]; [30] is in effect a one-round Delphi worth 4%.
- **FOR**: [41][44][35]. **AGAINST**: [42]. **Failure modes**: correlated errors from shared pre-training and preference tuning; wealth weighting amplifies a lucky agent; pool-wide acquiescence bias; contamination read as skill.

## 5. Agent-based economics and market simulation

- **Santa Fe Artificial Stock Market** (Arthur, Holland, LeBaron, Palmer, Tayler, 1996/97): slow exploration converges to rational expectations; faster exploration yields bubbles, crashes, technical trading, GARCH-like volatility [51][pre-2025, snippet]. A regime explanation, not a forecast.
- **Zero-intelligence**: [52][53]. For CLOBs like Polymarket's, spread and short-horizon volatility are largely mechanical functions of order-arrival and cancellation rates.
- **ABIDES** (2019): discrete-event simulator modelled on NASDAQ ITCH/OUCH, per-agent latency, tens of thousands of agents; demonstrated with a market-impact experiment, not prediction [54][pre-2025]. Closest prediction-market analogue: PredictionMarketBench, Kalshi replay with maker/taker semantics and fees [78b, snippet].
- **LLM traders**: agents hold assigned roles (value, momentum, market maker); the market shows price discovery, bubbles, underreaction, strategic liquidity provision; "prompts can generate correlated behaviors affecting market stability" [55][H]. 2026 snippets: outcomes range from convergence on fundamental value to human-like bubbles; advanced models "fail to consistently stabilise the market" [56]; disposition effect and recency-weighted extrapolation [57]; strategy rankings depend on the competitor ecology, "patterns invisible to static backtests" [61].
- **What ABMs have predicted**: euro-area ABM "outperforms DSGE and VAR models in out-of-sample forecasting" (Hommes & Poledna 2023; Poledna et al., European Economic Review 2023) [58]; a Bayesian-calibrated variant beats it and AR(1) across 38 OECD countries [59] (snippets); the Oxford input-output model's May 2020 UK lockdown forecast "predicted aggregate dynamics very well" per its authors [60][S].
- **FOR**: macro out-of-sample wins [58][59]; microstructure variance explained [53]. **AGAINST**: nothing found showing an ABM or LLM-trader simulation forecasting contract prices out of sample. **Failure modes**: calibration degrees of freedom; stylised facts as the only validation; LLM agents too rational or too uniform; ecology dependence.

## 6. Wargaming and institutional digital twins

- Escalation: all five off-the-shelf LLMs escalated, with arms races and rare nuclear use [62][2024]; 2026 frontier models (GPT-5.2, Claude Sonnet 4, Gemini 3 Flash) show theory-of-mind reasoning and still cross the nuclear threshold [66] (snippets).
- Human comparison: 214 national-security experts vs LLMs in a US-China crisis - LLMs more aggressive and scenario-sensitive; simulated team discussions show "farcical harmony" and ignore personalities [63][H][2024]. Free-form recommendations are semantically inconsistent across reruns [64, snippet]. 2026 position paper: decision laundering, adjudication opacity, role collapse, escalation-through-adjudication, failure of strategic imagination; no LM wargame should inform policy without an auditable safety case [65].
- Committees: MiniFed simulates FOMC members [68, snippet]; FedSight reports 93.75% accuracy, 93.33% stability on 2023-24 meetings vs MiniFed and an ordinal random forest; the abstract names neither the LLM nor a leakage control, and gives no comparison with futures-implied probabilities [67][H]. LLM-reader disagreement on ECB press conferences correlates ~0.5 with realised OIS volatility over 293 events [69, snippet].
- Courts and oracles: GPT-based SCOTUS agents "better than random" on 96 cases [70][pre-2025, snippet]; LLM vs UMA 89.58% [71].
- **FOR**: [69][71]. **AGAINST**: [62][63][64][65]; leakage-exposed backtests [67]. **Failure modes**: escalation / action bias; rerun inconsistency; harmony instead of dissent; no named-individual fidelity [16]; evaluation inside the training window; no market baseline.

## 7. Self-improving forecasters

- **Hedge (expert advice)**: w_i(t+1) = w_i(t) exp(-eta m_i(t)); cumulative loss <= best expert + ln N / eta + eta T [80]; with eta = sqrt(ln N / T), regret <= 2 sqrt(T ln N) (derived). Extra agents cost only ln N, but the bound is relative to the best expert: make the market price one of the experts (cf. [39]).
- **Outcome-supervised training**: [72][73][74]; [72] relies on synthetic question augmentation, stability guardrails and median-of-samples inference (a noise-reduction step, cf. [85]).
- **Online memory evolution**: Live-Evo keeps an experience bank and a meta-guideline bank, re-weighted by realised usefulness [75]; other 2026 agentic forecasters benchmark on Prophet Arena / FutureX [75b].
- **Population / evolutionary search**: PBT - exploit-and-explore over a population, discovers hyper-parameter schedules [79][pre-2025]. LLM-driven strategy evolution in equities: QuantaAlpha IC 0.0472, ARR 4.68%, MDD 11.8% on CSI 300 (author-reported); MadEvolve estimates p-hacking probability [81, snippets]. No prediction-market application found.
- **Human calibration feedback**: [83]; frequent small updates mark skill (400,000 forecasts) [87].
- **FOR**: [72][74][75]. **AGAINST**: evaluation leakage [38][41]; simulated fills [72]. **Failure modes**: slow labels (weeks to months); few independent events per regime; shifting question mix; search-time answer leakage; selection bias from many variants on few resolved markets.

## 8. Superforecaster methodology and what is automatable

- Findings beyond key fact 15 (snippets): training, teaming and tracking (top 2% into elite teams) each improved accuracy over two years [82]; superforecaster teams did not regress to the mean over hundreds of questions [84]; coarsening probabilities into verbal bins loses accuracy (888,328 forecasts) [89]; log-odds pooling / extremising from [88] (parameters not retrievable).
- Human vs machine: GPT-4 below the human median in 2023 [93][pre-2025]; expert forecasters beat the best LLM at p < 0.001 on ForecastBench's 200-question human subset (paper v5, Feb 2025) [37]; frontier models beat the Metaculus crowd but "significantly underperform" experts on 464 questions [40]; AIA claims superforecaster parity, Nov 2025 [39]. LLM assistants raised the accuracy of 991 humans 24-28%; even a deliberately biased assistant gave +29% in exploratory analysis [36][2024]. Mellers et al. 2023: algorithms as aggregators and hybrid partners [90].
- Automatable now: base-rate lookup, decomposition, update scheduling, recency-weighted pooling, skill weighting, extremising, recalibration, consistency checks [34], multi-sample medians. Not shown automatable: picking the top 2% (needs years of scored history per agent), genuine information diversity (agents share a corpus), recognising an ambiguous question.

## What a builder who already runs LP / cross-venue arb / resolution-sniping / copy-trading bots is likely to UNDERESTIMATE

1. **Agent count is not diversity.** Ten personas on one model family ~ 1.4 forecasters [42]; debate adds nothing in expectation [25]. Buy diversity with different model families, information sets and non-LLM models (order flow, base rates); measure pairwise error correlation on resolved markets before trusting a "swarm".
2. **LLM edge sits at the opposite end of market life from sniping.** Competitive early and on high-uncertainty markets, weak near resolution [77][76]; GJP polls beat markets mostly at the start of long questions [86]. A forecasting agent complements a sniper and belongs in new, thin, long-dated markets - where LP inventory is also most exposed.
3. **The model is a second opinion on the price, not a replacement.** Forecaster + market beats market alone although the forecaster alone loses [39]; the human median improved LLMs 17-28% [35]. Practical form: a linear stacker over market price, several models and microstructure features [41].
4. **LLM backtests are contaminated by default.** 35.8% -> 8.9% [41]; [38]; FedSight and FlockVote are scored inside plausible training windows [67][20c]. Only markets opened and resolved after every model cutoff, with date-restricted retrieval, count.
5. **Sizing from stated probabilities over-bets.** Five of seven LLMs lost with high stated confidence [78]; silicon samples are under-dispersed [10][13a]. Shrink toward the market, calibrate on resolved history, elicit a wager rather than a probability [43].
6. **Noise reduction is the cheapest edge.** [85] + median sampling [72]: many samples of one good pipeline pooled in log-odds may beat adding agents.
7. **Simulation popularity is not validation.** MiroFish-class tools have no scored record [91]; best diffusion fit ~30% NRMSE [3]; cosmetic prompt changes move outcomes 76 points [7]. Treat society simulators as scenario generators until they have a Brier history.
8. **Synthetic polls are a usable but fat-tailed input.** 50/51 states [14] and a 5.7-point miss [15][18] coexist; the hit used a small social-media-grounded sample with MrP, the miss a large census-seeded population. Vendors admit named individuals (Trump, Powell) are not predictable [16] - exactly the "will X say / do Y" contracts.
9. **Price institutional twins by the 10% they miss.** 89.58% agreement with UMA [71] puts the money in the disagreements; wargame LLMs are escalation-biased [62][63], so a geopolitical simulation will likely over-price conflict (inference, untested).
10. **Homogeneous LLM traders are becoming market structure.** Shared prompts produce correlated behaviour [55]; models converge across vendors [33]. As more participants run the same frontier models, their common error becomes a fadeable factor (inference, untested).
11. **Resolved Polymarket markets are a training asset.** [72][74][75] all improve from resolutions; the constraint is leak-free, timestamped question + news + price snapshots, which an operator already logging order books is well placed to build.

## Could not verify / open questions

- WebSearch unavailable (quota exhausted): coverage of news, vendor blogs and non-arXiv journals is thin; Bing often returned irrelevant pages.
- AgentSociety's quantitative agreement with real data; ElectionSim / Yu et al. / FlockVote state-level errors and leakage controls.
- Aaru's final 2024 general-election forecast; its NYC-primary and EY figures are vendor claims via Fortune; no independent scorecard for other synthetic-polling vendors.
- Current ForecastBench leaderboard (JS-rendered), any projected LLM-superforecaster parity date, Metaculus AI Benchmark bots-vs-pros results.
- Halawi et al. (2024) Brier numbers; the BIN bias / information / noise split; Satopaa extremising parameters; Prelec 2017 error reductions; Poledna 2023 abstract; the numeric UK-GDP forecast-vs-actual in Pichler et al.
- FedSight's LLM and cutoff; no FOMC simulation is compared with futures-implied probabilities.
- Fill, fee and depth assumptions behind the > 10% simulated ROI in [72]; PolyBench covers one week.
- Nothing found that (a) scores an agent-society simulation prospectively against prediction-market prices, (b) tests Bayesian truth serum or Delphi over LLM agents for forecast accuracy, (c) shows a red-team agent improving Brier, or (d) applies population-based / evolutionary strategy search to prediction markets.

## Source ledger

| n | URL | publisher | published / updated | what it supports | F/S |
|---|---|---|---|---|---|
| 1 | https://arxiv.org/abs/2304.03442 | arXiv, Park et al. | 2023-04-07, rev. 2023-08-06 | Generative Agents, believability only | F |
| 2 | https://arxiv.org/abs/2411.10109 (and /abs/2411.10109v1) | arXiv, Park et al. | v1 2024-11-15; later version retitled, date not captured | 1,052-person agents: 85% (v1); 83/82/86/74% | F |
| 3 | https://arxiv.org/abs/2411.11581 ; https://arxiv.org/html/2411.11581v5 | arXiv, Yang et al. | 2024-11-18, v5 2025-03-23 | OASIS scale, ~30% NRMSE, herd effect | F |
| 4 | https://arxiv.org/abs/2502.08691 | arXiv, Piao et al. | 2025-02-12, v2 2026-04-10 | AgentSociety scale and claims | F |
| 5 | https://arxiv.org/abs/2312.03664 | arXiv, Vezhnevets et al. (DeepMind) | 2023-12-06 | Concordia, Game Master, no validation | F |
| 6 | https://arxiv.org/abs/2504.03274 | arXiv, Larooij & Toernberg | 2025-04-04 | critical review of generative ABMs | F |
| 7 | https://arxiv.org/abs/2605.18890 | arXiv, Ye, Cao, Chen, Ferrara | 2026-05-17 | 76-pt perturbation sensitivity, TRAILS | F |
| 8 | https://arxiv.org/abs/2509.19088 | arXiv, Peng et al. | 2025-09-23, rev. 2026-04-19 | digital twins r = 0.20, five distortions | F |
| 9 | https://arxiv.org/abs/2209.06899 | arXiv, Argyle et al. | 2022-09-14 | silicon sampling, algorithmic fidelity | F |
| 10 | https://www.cambridge.org/core/journals/political-analysis/article/synthetic-replacements-for-human-survey-data-the-perils-of-large-language-models/B92267DC26195C7F36E63EA04A47D2FE | Political Analysis, Bisbee et al. | online 2024-05-17 | 48% / 32% coefficients, drift | F |
| 11 | https://arxiv.org/abs/2402.01908 | arXiv / Nature Machine Intelligence, Wang et al. | 2024-02-02, v3 2025-02-03 | misportrayal, flattening | F |
| 12 | https://arxiv.org/abs/2407.08563 | arXiv / Social Science Computer Review, von der Heyde et al. | 2024-07-11 | German vote, Green/Left bias | F |
| 13 | http://export.arxiv.org/api/query?search_query=all:%22silicon+sampling%22&max_results=15&sortBy=submittedDate | arXiv API listing | fetched 2026-09-20 | discovery of 13a-13d | F |
| 13a | https://arxiv.org/abs/2607.25292 | arXiv, Jang, Lee, Kim | 2026-07-28 | identical answer on 50% of items | S |
| 13b | https://arxiv.org/abs/2609.15849 | arXiv, Wali & Tayyab | 2026-09-14 | belief-updating failures | S |
| 13c | https://arxiv.org/abs/2606.12433 | arXiv, J. Bae | 2026-05-15 | marginal vs joint fidelity | S |
| 13d | https://arxiv.org/abs/2507.02919 | arXiv, Li, Li, Qiu | 2025-06-25 | homogenisation on ANES items | S |
| 13e | https://arxiv.org/abs/2501.06577 | arXiv, A. Amini | 2025-01-11 | survey transfer learning beats LLMs | S |
| 13f | https://arxiv.org/abs/2607.03091 | arXiv, Ku et al. | 2026-07-03 | 52% zero-shot, Taiwan | S |
| 14 | https://arxiv.org/abs/2503.05529 | arXiv, R. Cerina | 2025-03-07 | PoSSUM 50/51 states, prospective | F |
| 15 | https://www.semafor.com/article/09/20/2024/ai-startup-aaru-uses-chatbots-instead-of-humans-for-political-polls | Semafor | 2024-09-20 | Aaru method, 371 votes, Harris +4.2 | F |
| 16 | https://fortune.com/2026/06/17/aaru-cofounder-ned-koh-ai-startup-sales-pitch-do-not-trust-us/ | Fortune | 2026-06-17 | Aaru claims, admitted limits | F |
| 17 | https://techcrunch.com/2025/12/05/ai-synthetic-research-startup-aaru-raised-a-series-a-at-a-1b-headline-valuation/ | TechCrunch | 2025-12-05 | Aaru funding, clients, competitors | F |
| 18 | https://en.wikipedia.org/wiki/2024_United_States_presidential_election | Wikipedia | fetched 2026-09-20 | popular vote 49.8 / 48.3 | F |
| 19 | https://doi.org/10.24433/co.6384242.v1 | Code Ocean capsule, Hewitt et al. (via OpenAlex) | 2026-01-01 | r = 0.85 / 0.90, 70 experiments | S |
| 20a | https://arxiv.org/abs/2412.15291 | arXiv, Yu et al. | 2024-12-19, rev. 2025-04-10 | LLM election simulation framework | F |
| 20b | https://arxiv.org/abs/2410.20746 | arXiv, Zhang et al. | 2024-10-28 | ElectionSim, PPE benchmark | F |
| 20c | https://arxiv.org/abs/2512.05982 | arXiv, Zhou et al. (ICAIS 2025) | 2025-11-27 | FlockVote, retrospective swing states | F |
| 21 | https://arxiv.org/abs/2305.14325 | arXiv, Du et al. | 2023-05-23 | multi-agent debate | F |
| 22 | https://arxiv.org/abs/2402.06782 | arXiv, Khan et al. | 2024-02-09 | 76% / 88% vs 48% / 60% | F |
| 23 | https://arxiv.org/abs/2407.04622 | arXiv, Kenton et al. (DeepMind) | 2024-07-05 | debate vs consultancy vs QA | F |
| 24 | https://arxiv.org/abs/2502.08788 | arXiv, Zhang et al. | 2025-02-12 | MAD fails vs CoT / SC | F |
| 25 | https://arxiv.org/abs/2508.17536 | arXiv / NeurIPS 2025 spotlight, Choi, Zhu, Li | 2025-08-24, rev. 2025-10-23 | martingale, majority vote | F |
| 26 | https://arxiv.org/abs/2311.17371 | arXiv, Smit et al. | 2023-11-29 | MAD vs self-consistency | S |
| 27 | https://arxiv.org/abs/2605.00914 | arXiv, Bertalanic & Fortuna | 2026-04-29 | 2.1-3.4x tokens, 85.5% conformity | S |
| 28 | https://arxiv.org/abs/2601.19921 | arXiv, Zhu et al. | 2026-01-09 | vanilla MAD < majority vote | S |
| 29 | https://arxiv.org/abs/2511.07784 | arXiv, Wu, Li, Li | 2025-11-11 | majority pressure | S |
| 30 | https://arxiv.org/abs/2512.22625 | arXiv, Schneider & Schramm | 2025-12-27 | deliberation -4% log loss | F |
| 31 | https://arxiv.org/abs/2306.05685 | arXiv / NeurIPS 2023, Zheng et al. | 2023-06, v4 2023-12-24 | LLM-as-judge > 80%, biases | F |
| 32 | https://arxiv.org/abs/2601.20299 | arXiv (ICLR 2026 per page), Qiu, Carroll, Allen | 2026-01-28 | peer prediction vs judge | F |
| 33 | https://arxiv.org/abs/2510.22954 | arXiv / NeurIPS 2025 oral, Jiang et al. | 2025-10-27 | inter-model homogeneity | F |
| 34 | https://arxiv.org/abs/2412.18544 | arXiv, Paleka et al. | 2024-12-24 | consistency checks ~ Brier | S |
| 35 | https://arxiv.org/abs/2402.19379 | arXiv, Schoenegger et al. | 2024-02-29, final 2024-07-22 | 12-LLM crowd vs 925 humans | F |
| 36 | https://arxiv.org/abs/2402.07862 | arXiv, Schoenegger et al. | 2024-02-12, rev. 2024-08-22 | LLM assistant +24-28% | F |
| 37 | https://arxiv.org/abs/2409.19839 | arXiv, Karger et al. | 2024-09-30, v5 2025-02-28 | ForecastBench design, p < 0.001 | F |
| 38 | https://arxiv.org/abs/2506.00723 | arXiv, Paleka, Goel, Geiping, Tramer | 2025-05-31 | evaluation pitfalls, leakage | F |
| 39 | https://arxiv.org/abs/2511.07678 | arXiv, Alur et al. | 2025-11-10 | AIA Forecaster, market ensemble | F |
| 40 | https://arxiv.org/abs/2507.04562 | arXiv, J. Lu | 2025-07-06, final 2025-08-04 | 464 Metaculus questions | F |
| 41 | https://arxiv.org/abs/2607.18269 | arXiv, I. Douven | 2026-05-26, rev. 2026-07-22 | stacking, 35.8% -> 8.9% | F |
| 42 | https://arxiv.org/abs/2606.26583 | arXiv, Begin et al. | 2026-06-25 | N_eff 1.4, rho 0.70 | F |
| 43 | https://arxiv.org/abs/2512.05998 | arXiv, M. Todasco | 2025-12-01 | bet size as confidence | F |
| 44 | https://arxiv.org/abs/1102.1465 | arXiv / JMLR, Barbu & Lay | 2011-02-07 | artificial prediction markets | S |
| 45 | https://arxiv.org/abs/1106.4509 | arXiv, A. Storkey | 2011-06-22 | machine learning markets | S |
| 46 | https://arxiv.org/abs/2605.27394 | arXiv, Chakravorti et al. | 2026-04-19 | hybrid human-AI markets | S |
| 47 | https://mason.gmu.edu/~rhanson/mktscore.pdf | R. Hanson (GMU) | undated PDF | LMSR, b log n bound | F |
| 48 | https://en.wikipedia.org/wiki/Surprisingly_popular | Wikipedia | last edited 2025-05-26 | SP algorithm, Nature 541:532-535 | F |
| 49 | https://arxiv.org/abs/2604.13356 | arXiv, Feng et al. | 2026-04-14 | peer-predictive self-training | S |
| 50 | https://arxiv.org/abs/2502.21092 | arXiv, Bertolotti & Mari | 2025-02-28 | LLM Delphi (qualitative) | S |
| 51 | https://doi.org/10.2139/ssrn.2252 ; https://econpapers.repec.org/RePEc:wop:safiwp:96-12-093 | SSRN / SFI WP, Arthur et al. (via OpenAlex) | 1996-12 / 1997 | Santa Fe ASM regimes | S |
| 52 | https://doi.org/10.1086/261868 | Journal of Political Economy, Gode & Sunder (via OpenAlex) | 1993-02 | ZI traders ~100% efficiency | S |
| 53 | https://arxiv.org/abs/cond-mat/0309233 | arXiv, Farmer, Patelli, Zovko | 2003-09-09 | 96% / 76% variance explained | S |
| 54 | https://arxiv.org/abs/1904.12066 | arXiv, Byrd, Hybinette, Balch | 2019-04-26 | ABIDES | F |
| 55 | https://arxiv.org/abs/2504.10789 | arXiv, A. Lopez-Lira | 2025-04-15 | LLM traders, correlated prompts | F |
| 56 | https://arxiv.org/abs/2604.18602 | arXiv, Saxena & Pangallo | 2026-04-09 | LLM bubbles vs fundamentals | S |
| 57 | https://arxiv.org/abs/2604.18373 | arXiv, Ouyang & Sui | 2026-04-20 | disposition effect, extrapolation | S |
| 58 | https://doi.org/10.2139/ssrn.4381261 ; https://doi.org/10.1016/j.euroecorev.2022.104306 | SSRN, Hommes & Poledna; European Economic Review, Poledna et al. (via Crossref) | 2023 | ABM beats DSGE / VAR out of sample | S |
| 59 | https://arxiv.org/abs/2409.18760 | arXiv, S. Wiese et al. | 2024-09-27 | calibrated ABM, 38 OECD countries | S |
| 60 | https://arxiv.org/abs/2102.09608 | arXiv, Pichler et al. | 2021-02-18 | UK lockdown forecast (authors' claim) | F |
| 61 | https://arxiv.org/abs/2602.00948 | arXiv, Zou et al. | 2026-02-01 | FinEvo ecology dependence | S |
| 62 | https://arxiv.org/abs/2401.03408 | arXiv, Rivera et al. | 2024-01-07 | escalation in 5 LLMs | S |
| 63 | https://arxiv.org/abs/2403.03407 | arXiv, Lamparth et al. | 2024-03-06, rev. 2024-10-03 | 214 experts vs LLMs | F |
| 64 | https://arxiv.org/abs/2410.13204 | arXiv, Shrivastava, Hullman, Lamparth | 2024-10-17 | rerun inconsistency | S |
| 65 | https://arxiv.org/abs/2609.16189 | arXiv, Riedl & Matlin | 2026-07-31 | five failure modes | F |
| 66 | https://arxiv.org/abs/2602.14740 | arXiv, K. Payne | 2026-02-16 | frontier models in nuclear crises | S |
| 67 | https://arxiv.org/abs/2512.15728 | arXiv / NeurIPS 2025 workshop, Hou et al. | 2025-12-05 | FedSight 93.75% | F |
| 68 | https://arxiv.org/abs/2410.18012 | arXiv, Seok et al. | 2024-10-23 | MiniFed | S |
| 69 | https://arxiv.org/abs/2508.13635 | arXiv, U. Collodel | 2025-08-19 | ECB disagreement ~ OIS vol 0.5 | S |
| 70 | https://arxiv.org/abs/2301.05327 | arXiv, S. Hamilton | 2023-01-12 | SCOTUS agents, 96 cases | S |
| 71 | https://arxiv.org/abs/2604.15674 | arXiv, Wen, Zhou, Huang | 2026-04-17 | LLM vs UMA 89.58% | S |
| 72 | https://arxiv.org/abs/2505.17989 | arXiv, Turtel et al. | 2025-05-23, v4 2025-12-01 | RLVR 14B, > 10% simulated ROI | F |
| 73 | https://arxiv.org/abs/2502.05253 | arXiv, Turtel, Franklin, Schoenegger | 2025-02-07 | self-play + DPO 7-10% | F |
| 74 | https://arxiv.org/abs/2601.06336 | arXiv, Turtel et al. | 2026-01 (listing shows 01-09 and 01-14) | Future-as-Label +27% Brier | S |
| 75 | https://arxiv.org/abs/2602.02369 | arXiv, Zhang et al. | 2026-02-02 | Live-Evo +20.8% / +12.9% | F |
| 75b | https://arxiv.org/abs/2608.20920 ; https://arxiv.org/abs/2605.30858 | arXiv, Zhong et al.; Chang et al. | 2026-08-21; 2026-05-29 | memory-based agentic forecasters | S |
| 76 | https://arxiv.org/abs/2510.17638 | arXiv, Yang et al. | 2025-10-20, rev. 2025-12-21 | Prophet Arena bottlenecks | F |
| 77 | https://arxiv.org/abs/2604.04220 | arXiv, Mostafa, Shastri, Lee | 2026-04-05 | TimeSeek, early vs late | F |
| 78 | https://arxiv.org/abs/2604.14199 | arXiv, Cheng, Liu, Long | 2026-04-03 | PolyBench 2 of 7 profitable | F |
| 78b | https://arxiv.org/abs/2602.00133 | arXiv, Arora & Malpani | 2026-01-28 | PredictionMarketBench | S |
| 79 | https://arxiv.org/abs/1711.09846 | arXiv, Jaderberg et al. (DeepMind) | 2017-11-27 | population based training | F |
| 80 | https://en.wikipedia.org/wiki/Multiplicative_weight_update_method | Wikipedia | last modified 2026-08-29 | Hedge update and bound | F |
| 81 | https://arxiv.org/abs/2602.07085 ; https://arxiv.org/abs/2605.23007 | arXiv, Han et al.; Kvasiuk et al. | 2026-02-06; 2026-05-21 | LLM evolutionary alpha search | S |
| 82 | https://doi.org/10.1177/0956797614524255 | Psychological Science, Mellers et al. (via OpenAlex) | 2014-03-21 | training, teaming, tracking | S |
| 83 | https://doi.org/10.1017/s1930297500004599 | Judgment and Decision Making, Chang et al. | 2016-09-01 | training 6-11% Brier | S |
| 84 | https://doi.org/10.1177/1745691615577794 | Perspectives on Psychological Science, Mellers et al. | 2015-05-01 | superforecasters persist | S |
| 85 | https://doi.org/10.1287/mnsc.2020.3882 | Management Science, Satopaa et al. | 2021-02-10 | BIN model, noise | S |
| 86 | https://doi.org/10.1287/mnsc.2015.2374 ; https://doi.org/10.5465/ambpp.2015.15192abstract | Management Science / AOM Proceedings, Atanasov et al. | 2016-04-22; 2015 | polls + algorithms vs markets, 12% | S |
| 87 | https://doi.org/10.1016/j.obhdp.2020.02.001 | OBHDP, Atanasov et al. | 2020-03-30 | frequent small updates | S |
| 88 | https://doi.org/10.1016/j.ijforecast.2013.09.009 | International Journal of Forecasting, Satopaa et al. | 2014-02-03 | logit pooling / extremising | S |
| 89 | https://doi.org/10.1093/isq/sqx078 | International Studies Quarterly, Friedman et al. | 2018-03-19 | precision matters, 888,328 forecasts | S |
| 90 | https://doi.org/10.1177/17456916231185339 | Perspectives on Psychological Science, Mellers et al. | 2023-08-29 | human + algorithm hybrids | S |
| 91 | https://github.com/666ghj/MiroFish | GitHub | fetched 2026-09-20 | OASIS-based engine, no validation | F |
| 92 | https://arxiv.org/abs/2609.13995 | arXiv, Netzer & Sambandam | 2026-09-12 | when to trust synthetic data | S |
| 93 | https://arxiv.org/abs/2310.13014 | arXiv, Schoenegger & Park | 2023-10-17 | GPT-4 below human median | S |
| 95 | https://arxiv.org/abs/2601.15114 ; https://arxiv.org/abs/2502.05919 | arXiv, La Gatta et al.; Orlando et al. | 2026-01-21; 2025-02-09 | GABM micro-validation | S |
| 97 | https://arxiv.org/abs/2502.19130 | arXiv, Kaesberg et al. | 2025-02-26 | voting vs consensus protocols | S |

(Numbers 94 and 96 intentionally unused.)
