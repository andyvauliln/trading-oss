# AI / LLM forecasting state of the art and LLM trading on prediction markets
_As of 2026-09-20. Evidence pack E7 for the Polymarket strategy survey._

Conventions: **[n]** = source-ledger row. **H** = hard (paper, official leaderboard, docs), **V** = vendor / self-reported, **M** = media or content blog. "Brier" = lower is better unless stated. BSS = Brier skill score vs the market price (positive = beats market). Research method note: the session's WebSearch quota was exhausted; searches were run through Brave Search / arXiv listing / GitHub search fetched as pages, and every cited URL was either fetched (F) or appeared in those result pages (S).

## Key facts

1. **"Parity with superforecasters" is real on benchmarks, but it is not parity with a liquid market price.** FRI (2026-07-16): Cassi AI ranks first on the ForecastBench tournament leaderboard, statistically indistinguishable from superforecasters (one-sided bootstrap p = 0.41); xAI and Google DeepMind also at parity; 17 submissions rank above superforecasters on dataset questions; the superforecaster baseline was last elicited in 2024 [1][5] (H).
2. **ForecastBench tournament entries are shown the market price.** GPT-4.5's forecasts correlated 0.994 with the supplied market forecasts and it submitted the exact market value on 26 of 122 questions [3]; Cassi's "crowd adjustment" toward the market price was worth ~0.01 Brier [2] (H). A high tournament rank therefore says little about edge *against* the price.
3. **On liquid markets the price still wins head to head.** Bridgewater AIA Forecaster, 1,610 liquid-market questions (Apr-May 2025): market Brier 0.1106 vs AIA 0.1258; the blend (0.67 market / 0.33 AIA) scores 0.1060 [37]. RL-tuned 14B model on 1,265 Polymarket questions: market 0.151 vs model 0.190 vs o1 0.202 [35]. 15 LLMs on 254 questions: "substantially less accurate" than the market even when the market is evaluated at each model's training cutoff [28]. Four frontier agents on 104 World Cup 2026 matches: none beat the market Brier, and a flat stake on the favourite out-earned all four [30] (H).
4. **Live leaderboard, today:** Prophet Arena (Kalshi events, updated 2026-09-20): Kalshi baseline 1-Brier 0.7998; best entry (agentic GPT-5.6 Sol) 0.8022, skill +0.24 +/- 0.44; only four entries sit above the market and every interval straddles zero [22] (H).
5. **Where LLMs do beat the price: early and on toss-ups, never late.** TimeSeek (150 Kalshi markets x 10 models x 5 checkpoints): four models beat the market at Open+1 (Claude +0.167 BSS), all are below -0.7 BSS at Close-1; on toss-up markets Claude +0.301, on strong-consensus markets every model is -0.69 to -1.68 [26]. Halawi 2024 found the same shape: system beat the crowd only when the crowd sat at 0.3-0.7 (0.238 vs 0.240) [32] [pre-2025, possibly stale] (H).
6. **Real money, frontier models, no special scaffolding: losses.** Prediction Arena, $10,000 per model, 2026-01-12 to 03-09: Kalshi -16.0% to -30.8%; Polymarket (02-09 to 03-09) 0.00% (one model never traded) to -2.68%, average -1.1% [23] (H).
7. **Real money, with a disciplined sizing rule: one small positive result.** Gemini 3 with "proper betting" on Kalshi, $200, 26 days (Apr/May 2026): 1,605 forecasts -> 396 signals -> 236 fills, +80.33% ROI, Sharpe 3.35, win rate 50.9%, fees $26.31; a Kalshi Research employee is co-author [24] (H, tiny n).
8. **Bet sizing dominates model choice.** Same forecasts, 200-event subset: proper betting +22.1% (Claude Opus 4.6) / +8.1% (Gemini 3); Kelly criterion -99.9% / -42.7% [24]. Brier-derived rule: position s = 2(p - q), linear in the disagreement [24] (H).
9. **Statistical power:** detecting a 0.02 edge at 80% power needs ~350 resolved binary predictions; 0.01 needs ~4x that [40] (H, simulation-based).
10. **Backtests are contaminated by default.** Frontier-vs-small-model gap collapses from 35.8% to 8.9% on questions resolving after all training cutoffs [28]; date-filtered search leaks the future [39]; 1.65% of AIA's search results carried foreknowledge [37]; at least 3.8% of Halawi's questions resolved "early", which itself leaks the answer [39] (H).
11. **Pros vs bots on Metaculus closed from -20.03 (Q2 2025, p = 0.00001) to -1.25 (Spring 2026, 95% CI -4.87..2.37, p = 0.247)** on 99 shared questions; 9 of the top 10 individuals would still be Pros [9][10] (H). A bot ("laertes") won the Summer 2026 Metaculus Cup (resolved 2026-09-05), Mantic second, best human third [15][16][18] (M, consistent across outlets).
12. **Design levers with measured effect:** search on/off 0.1002 vs 0.3609 Brier [37]; Platt scaling / extremizing with coefficient sqrt(3): 0.1140 -> 0.1076 [37], +0.016 Brier on Metaculus bots [12]; 10-run ensemble + agentic supervisor 0.1125 vs 0.1199 for a single run [37]; scaffolding is worth ~9 months of base-model progress [11]; winners use ~28 LLM calls and ~$1.40 per question vs 7 calls / $0.50 [11] (H).
13. **LLM traders are a monoculture.** DPO-tuned agents: error correlation 0.70, ten agents = ~1.4 independent forecasters, ten-agent market 67.6% vs single agent 70.2% [29]; four frontier agents made the identical top pick in 92% of World Cup matches [30] (H).
14. **Vendor books, self-reported:** FutureSearch Kalshi real account +5.9% (2026-06-09 to 08-11, 26 W / 12 L), Kalshi paper +49.8%, Polymarket paper -19.6% (04-24 to 08-11, 24 W / 21 L) [45]; Olas says 33% of Polystrat agents were profitable "this month" vs ~16% of Polymarket users [51] - i.e. two thirds of the agents lost (V).
15. **Rule reading:** web-enabled LLMs agree with UMA's final vote 89.58% of the time once a dispute exists, and cannot predict which markets will be disputed [41] (H).
16. **Polymarket's own reference agent repo is archived** (Polymarket/agents, 3,796 stars, archived) [57]; the live replacement is Polymarket/agent-skills (created 2026-02-19) [58] (H).

## 1. Benchmarks and tournaments: where systems stand

**ForecastBench (FRI).** Difficulty-adjusted Brier; two question families: "dataset" (ACLED, FRED, Yahoo, etc.) and "market" (Polymarket, Manifold, Metaculus...). Timeline: Oct 2025 superforecasters 0.081 vs best LLM (GPT-4.5) 0.101, public median fell to rank 22, trend 0.016 Brier/yr, projected parity late 2026 (95% CI Dec 2025-Jan 2028) [3]. Jan 2026: superforecasters still #1 by 0.017; Grok 4.20 Preview (0.102) and Cassi `ensemble_2_crowdadj` tied #2; parity projected Nov 2026 overall, Jun 2026 dataset, Aug 2026 market [2][7]. Jun 2026: Torchcast (three-person Singapore start-up) took ranks 1-2-2 on the *preliminary* board with Brier Index 67.4 / 67.3 / 67.3 [8][18]. Jul 2026: parity declared, with the caveat "the 95% CIs ... overlap substantially; the results are more consistent with superforecaster parity than with outperformance" [1]. Karger et al.'s original paper reported a 0.054 gap between superforecasters and GPT-4o [34] (S).
**Sources disagree on meaning.** Good Judgment: baseline is "a frozen July 2024 snapshot of individual Superforecasters working largely alone"; many submissions every two weeks = multiple comparisons; some market questions are "dataset questions in market clothing"; on market questions superforecasters were ~0.04 vs ~0.059 for the best AI (Feb-Apr 2026); the FT found the AI "relied heavily on market-based trackers" [4][5][6].

**Metaculus AI Benchmark / FutureEval.** Head-to-head peer score, bot team minus Pro team: Q3 2024 -11.3, Q4 2024 -8.9, Q1 2025 -17.7, Q2 2025 -20.03, Spring 2026 -1.25 [9][10][11]. Spring 2026: 173 bots, 297 questions, $50k; bots beat Pros on numeric questions (+3.47) and lose on binary (-2.51) and multiple choice (-5.02); best plain-prompt baseline (GPT-5.1) placed 18th of 173; Community Prediction averages a 14.8 peer score vs 11.32 for the best in-house bot [9]. Whether bots can see the community prediction could not be confirmed (Metaculus pages returned 403). $175k/yr in prizes, $1k MiniBench every two weeks [13]; Metaculus' own trend projects plain baseline bots passing Pros around June 2027 [11]. ACX (2026-07-02): scaffolded AIs ~31 vs top Pros ~36 on Metaculus' scale; "statistical dead heat" in cups [19]; ACX (2026-08-03) estimates remaining headroom would move a 50% market call by only 4-12 points [20] (M).
**Metaculus Cup.** Mantic 8th of 549 in Summer 2025, with TIME's caveats: 60 questions, mostly amateurs, scoring rewards constant updating and coverage [14]. Summer 2026: bots 1st, 2nd, 5th; five bots in the top 10 [15][17][18]. "The bot can be systematically worse at the hard questions and still win, provided it is adequate on the easy ones and relentless about both" [17] (M).

**Prophet Arena (UChicago/USC, Kalshi events).** Paper (2025-10): 1,367 events / 72,136 markets; GPT-5 Brier 0.184 vs market 0.187, ECE 0.042 vs 0.069, average return 0.943 vs 0.899 - all below break-even; LLMs are more conservative than markets and "markets incorporate breaking information ... more rapidly than LLMs" as resolution nears; market data alone is almost as good as market data + news [21]. Live board in Key fact 4 [22].
**FutureX (ByteDance-led, ~500 new events/week).** 25 models in the 2025 paper; flags susceptibility to misleading web pages [55]; vendors now advertise #1 weeks (H2O [69], "Agentic Time Machine" [70]) - leaderboard itself not retrievable (S).
**Others.** KalshiBench: 300 questions, all five frontier models overconfident, ECE 0.120 (Claude Opus 4.5) to 0.395 (GPT-5.2-XHigh), only one model with positive BSS [31]. PolyBench: 38,666 Polymarket markets snapshotted 2026-02-06..12, seven cheap models, only two profitable (MiMo-V2-Flash +17.6%, Gemini-3-Flash +6.2% confidence-weighted return); alpha survives $10 lots and dies above ~$500 against real CLOB depth; one week of data [25]. FutureSearch BTF-3 (2,386 questions, Jun-Aug 2026): FutureSearch 0.116, Claude Opus 5 0.120 [44] (V). Schoenegger et al.: 12-LLM ensemble matched 925 humans on 31 questions; showing the human median improved accuracy 17-28% [33] [pre-2025, possibly stale].

## 2. System design choices that matter

| Lever | Evidence |
|---|---|
| Base model | "Model choice was the largest differentiator" [13]; higher-reasoning variants better (p = 0.004) [9]; automated prompt optimisation failed to replicate live ("o3 null on n = 278") [11] |
| Retrieval | No-search Brier 3.6x worse [37]; agentic > one-shot search [37]; no provider reliably best, breadth of providers correlates r = 0.42 with score [9][11]; search *hurts* in 12% of model-checkpoint pairs and Claude's optimum is 4-7 queries (1-3: -0.811 BSS; 13+: -0.115) [26]; retrieval backfires when the corpus holds only speculation (Entertainment -31 markets) [27] |
| Ensembling | 86% of Fall 2025 winners aggregate [11]; sweet spot 4-10 members, larger declines [9]; Mantic's optimum: Gemini 3 Pro + GPT-5 + Grok 4 + fine-tuned gpt-oss-120b [11]; a logistic-regression aggregator over 15 LLMs beats every member and classical pooling, the useful signal being model disagreement [28]; cross-family diversity cuts error correlation 0.68 -> 0.40 [29] |
| Calibration / extremizing | LLMs "hedge toward 0.5" (RLHF); Platt scaling and extremizing are mathematically equivalent; coefficient sqrt(3) [37]; +0.016 Brier on binary, +0.005 multiple choice [12]; but raw frontier models on Kalshi questions are *over*confident [31][25] - fit the direction per system, do not assume |
| Outcome RL / fine-tuning | 14B model, 10k Polymarket + 100k synthetic questions, ReMax without per-question std scaling: 0.190 Brier, ECE 0.062, beats o1, loses to market; simulated +$52 on 1,265 questions (~10%), ~20% ROI in the 40-60% price band, rule "bet only when edge > ECE" [35]. Foresight Learning: Qwen3-32B +27% Brier, ECE halved, beats Qwen3-235B [36]. Halawi: generated 73,632 reasoning traces, kept the 13,253 that beat the crowd, fine-tuned on the ~6,000 most recent [32] |
| Market as prior | Market-conditioned prompting + mixing beats the market on earnings-call mention markets [42]; AIA blend 0.33 weight [37]; Halawi blend 0.149 -> 0.146 [32] |
| Bet sizing | Proper betting s = grad G(p) - grad G(q); profit = score gap + Bregman divergence - liquidity loss; "essentially the only" robustly profitable rule; log-score version loses less when the forecaster is worse than the market [24] |

## 3. LLM agents trading real money

- **Prediction Arena** (Arcada Labs / Harvard) [23]: weather was 71-97% of Kalshi settlements and models were bad at it (grok-4-1-fast 15.4% weather accuracy); early exits had negative average PnL, holding to settlement was better; token spend uncorrelated with PnL; spreads of 2-5c and rejected orders mattered; same models lost 21.5 points less on Polymarket, where they chose their own markets - selection vs pricing not separable. Cohort 2 (3 days, paper): Gemini 3.1 Pro +6.02%, Claude Opus 4.6 -10.06%. Press framing: "AI traders ... losing money" [66] (S).
- **When do prophets profit** [24]: decomposition attributes the live gain to accuracy (+0.7205) rather than divergence (+0.0828); markets were pre-filtered for resolution clarity.
- **Lo et al. (MIT, ICML 2026)** [43] (secondary summary; primary not retrievable): 822 resolved Polymarket questions, 32-member LLM ensemble, ROI +4.0% vs -0.5% for the market baseline, +9.1% when ensemble agreement is 70-90%, p = 0.004; the edge is "losing less" by fading optimism and favourite-longshot bias, not higher accuracy; single-shot backtest, no market impact.
- **Vendors**: FutureSearch book [45] and its own warning "even a high quality forecast is not enough for me to trade" [46]; Olas Polystrat 4,200+ trades in month one, single trades up to +376%, "37% of agents positive" [50], later 33% [51]; CEO: "simply prompting off-the-shelf models ... no better than a coin-flip" [50]. Preseen "$35 into $1.94m over seven months, the sixth-best return in Kalshi's history" (Economist syndication) [67][19] - unverified, ACX is sceptical.
- **Individuals**: a Kalshi mention-market bot netted $5,516 on $342,506 of cost over ~2 months from a structural NO-side maker strategy - "LLM approach for probability estimation underperformed" [53]; five viral "my AI bot made money" posts checked against primary data, none survived [64]; Reddit paper-trading league reports MiniMax-M3 +14.9% over 60 days (paper) [65] (S).
- **Open source**: Polymarket/agents archived [57]; alsk1992/CloddsBot 2,808 stars (Claude-based, multi-venue) [74]; PolySwarm (50 personas, quarter-Kelly) was evaluated on Jan-Mar 2024 markets, i.e. inside current models' training data [59]. No repository found with audited live PnL.

## 4. Methodological traps

1. **Leakage**: search date filters, post-dated articles, knowledge cutoffs later than advertised, and question sets whose existence reveals the answer [39]; Hindcast replays 216 Polymarket markets against a frozen Reddit archive - no open-weight model beats the price at t0 [27].
2. **Contamination flatters big models** (35.8% -> 8.9%) [28].
3. **Price in the prompt**: tournament-style scores partly measure copying [3][5].
4. **Question mix**: ForecastBench dataset questions reward data access; Polymarket over-represents crypto and sports [39][4].
5. **Brier is not PnL**: equal Brier, better calibration, still return < 1 [21]; a (non-LLM) 15-minute-crypto bot logged a 92% win rate over 176 trades for ~$2 net because the average loss was $12.00 against an average win of $0.15 [76]; Kelly on miscalibrated p is ruinous [24]; Brier over-rewards the 40-60% band relative to rare events [39].
6. **Costs**: Polymarket taker fee = C x feeRate x p(1-p), politics 0.04, sports 0.05, crypto 0.07, geopolitics 0, makers 0 [56] - 2% of premium at p = 0.50 in politics; Kalshi fees were 13% of starting capital in 26 days in [24]; PolyBench alpha vanishes above ~$500 clips [25]; paper fills at mid or Gamma bid are fiction.
7. **Small n**: see Key fact 9; most reported live runs have 40-250 bets.
8. **Poisoned retrieval**: Polymarket's own AI "Market Context" cited non-existent AP articles in almost a third of 152 audited markets; a Pravda-network domain was cited 1,000+ times [54].

## 5. Where an LLM plausibly has edge

- **Early-life, toss-up, thinly followed markets** [26][32]; blend rather than replace the price [37][42].
- **Bias harvesting** (longshot / optimism) with an agreement filter [43] - overlaps with classic favourite-longshot strategies (see E4).
- **Breadth**: coverage wins cups [17]; $0.15-$2 per forecast retail [47], ~$1.40 for winning bots [11].
- **Numeric / data-rich questions**: bots beat Pros [9]; LLM macro nowcasts are "broadly comparable" to Bloomberg consensus and Fed nowcasts across 16 indicators [62].
- **Rule reading at the dispute stage** [41]; multi-agent oracle 83.43% [75] (S).
- **Speed**: weak evidence. On 109 Polymarket events X and news were tied (-0.02 min; X first in 38%) [60]; markets out-update LLMs near resolution [21][26]. Moving a prominent market 5 points costs ~$0.7-1.0M [61], so headline markets are not where a text-reading bot is early.
- **Multilingual sources**: no study found (unverified).
- **Human + LLM**: only a minority of users who reason *with* the model match the market; deferrers underperform [63].

## 6. Commercial players

Mantic (London; $25M seed 2026-09-18, Radical Ventures, M12, Thinking Machines, Balderton; "hedge funds and trading firms" cited as keenest) [15][16][49]; FutureSearch (API, public trading book) [44][45][47]; Lightning Rod Labs (Foresight models; claims "1st place on ProphetArena (Mar-Jul 2026)"; customers include Numinous, Shore Capital) [48]; Cassi AI (London) [7]; Torchcast [8]; Preseen [19]; Bridgewater AIA Labs [37]; Olas / Valory (Polystrat, OLAS-subsidised) [50]; Arcada Labs [23]; Kalshi Research [24][42]; xAI-Kalshi (2025-07) and X-Polymarket (2025-06) partnerships [71] (S). Prop side: Jump Trading, Clear Street and Marex building access layers, AQR and Susquehanna hiring specialist prediction-market roles; on-chain prop firm Propr routes only ~5% of signals to live venues [52]; "what if everyone uses the same AI tool?" [72] (S).

## What a builder who already runs LP / cross-venue arb / resolution-sniping / copy-trading bots is likely to UNDERESTIMATE

1. **The LLM's edge lives at the opposite end of the market lifecycle from resolution sniping**: positive BSS at Open+1 and on toss-ups, below -0.7 at Close-1 [26]. Never let an LLM probability override the book late; use it at listing time and for 30-70% prices.
2. **Its best use is as a 0.2-0.35-weight fair-value input to the LP bot's quote skew**, not as a taker signal: the blend beats both parts [37][42][32], makers pay no fee [56], and taker fee + half-spread will exceed a 2-4 point edge in most long-tail books (E1).
3. **Sizing rule > model**: linear-in-disagreement sizing made money where Kelly lost 43-100% on the same forecasts [24]. Gate on edge > own ECE [35].
4. **You need ~350 resolved bets to see a 2-point edge** [40]; correlated positions shrink that further (one session cost a model 8.99% [23]). Plan for months of tiny-size forward testing.
5. **Any historical backtest of an LLM forecaster is suspect** [28][39][27]; only forward, timestamped, executable-price paper trading counts.
6. **Monoculture**: every competitor's frontier model reaches the same view [30][29]; LLM-visible mispricings are the first to be competed away once prop firms deploy [52]. Diversity across model families and private data is the only measured remedy.
7. **Base-model upgrades beat prompt work; scaffolding is worth ~9 months** [11]; budget $0.5-1.5 per question-update [11], so triage thousands of markets with a cheap model first.
8. **Retrieval is an attack surface** on a venue where fabricated citations sit inside the product itself [54][55].
9. **LLMs cannot pre-screen dispute risk**, only adjudicate after the fact [41].
10. **Vendor success rates imply most autonomous agents lose** even with token subsidies [51].

## Could not verify / open questions

- Exact July-September 2026 ForecastBench scores (site renders client-side); an AI-synthesised report quotes superforecasters ~70.2 vs DeepMind "green-tree" ~67.8 Brier Index and itself flags a "March 15 parity" claim as uncorroborated [68].
- Primary text of Lo et al. [43]; Preseen's Kalshi return [67]; identity and method of "laertes"; Lightning Rod's Prophet Arena claim (not visible in the top 10 on 2026-09-20 [22]).
- Meaning of Prophet Arena's live "Return" column (126-165%) versus the paper's "< 1 = below break-even" [21][22].
- "30%+ of Polymarket wallets use AI agents" (LayerHub via CoinDesk [50]) - no primary data; E4 reached the same verdict.
- Why identical models lost 20+ points more on Kalshi than Polymarket [23].
- No on-chain study isolates LLM-driven wallets' PnL on Polymarket; no evidence on multilingual edge; FutureX live standings [55].
- Fast Company, CNBC, Cybernews, Hindustan Times and OpenReview pages returned 403 / verification walls; used as snippets only.

## Source ledger

| n | URL | Publisher | Date | Supports | F/S |
|---|---|---|---|---|---|
| 1 | https://forecastingresearch.substack.com/p/ai-models-have-likely-reached-parity | Forecasting Research Institute | 2026-07-16 | parity claim, p = 0.41, 17 submissions | F |
| 2 | https://forecastingresearch.substack.com/p/llms-are-closing-the-gap-on-human | FRI | 2026-01-29 | standings, crowd adjustment, projections | F |
| 3 | https://forecastingresearch.substack.com/p/ai-llm-forecasting-model-forecastbench-benchmark | FRI | 2025-10-08 | 0.081 vs 0.101, 0.994 correlation | F |
| 4 | https://goodjudgment.substack.com/p/what-superforecasters-actually-said | Good Judgment | 2026-02-25 | market-question gap, critique | F |
| 5 | https://goodjudgment.substack.com/p/not-so-fast | Good Judgment | 2026-07-24 | stale baseline, FT quote | F |
| 6 | https://goodjudgment.com/what-forecastbench-doesnt-measure/ | Good Judgment | 2026-04-14 | 0.039 vs 0.059 | S |
| 7 | https://blog.cassi-ai.com/p/humanitys-last-exam-for-forecasting | Cassi AI | 2026-02-23 | 0.102 vs 0.086, question counts | F |
| 8 | https://torchcast.ai/blog/forecastbench-sweep | Torchcast | 2026-06-25 | Brier Index 67.4 | F |
| 9 | https://www.lesswrong.com/posts/wZBbDqzfBjYG58CxK/futureeval-spring-results-pros-beat-bots-but-the-gap-is | Metaculus on LessWrong | 2026 (tournament Jan 7-Apr 15) | Spring 2026 results, design findings | F |
| 10 | https://forum.effectivealtruism.org/posts/F2stjK9wHSy3HPEC9/q2-ai-benchmark-results-pros-maintain-clear-lead | Metaculus on EA Forum | 2025-12-18 | Q2 2025 -20.03 | F |
| 11 | https://www.lesswrong.com/posts/a82q6yd8zKpYk56cF/ai-forecasting-in-2026-what-11-analyses-say (mirror https://forum.nunosempere.com/posts/Spyz3wESZu2eeqhDj/ai-forecasting-in-2026-what-11-analyses-say) | B. Wilson / Metaculus | 2026-07-08 | calls, cost, scaffolding, ensembles | F |
| 12 | https://www.metaculus.com/notebooks/43356/calibration-adjustment-analysis/ | Metaculus | 2026-05-01 | Platt scaling +0.016 | F |
| 13 | https://metaculus.substack.com/p/metaculus-futureeval-ai-forecasting-benchmark | Metaculus | 2026-06-30 | prizes, success factors | F |
| 14 | https://time.com/7318577/ai-model-forecasting-predict-future-metaculus/ | TIME | 2025-09-18 | Mantic 8th of 549, caveats | F |
| 15 | https://techstartups.com/2026/09/18/british-ai-startup-mantic-raises-25m-to-build-superhuman-ai-forecasting-after-metaculus-win/ | TechStartups | 2026-09-18 | raise, Cup result | F |
| 16 | https://www.globalbankingandfinance.com/ai-startup-mantic-raises-25-million-superhuman-forecasting/ | Reuters via GBAF | 2026-09-18 | raise, hedge-fund interest | F |
| 17 | https://www.explainx.ai/blog/ai-beats-forecasters-metaculus-cup-coverage-2026 | explainx.ai (content blog) | 2026-09 | Cup 1st/2nd/5th, coverage argument | F |
| 18 | https://aventineresearchinstitute.substack.com/p/ai-is-getting-astonishingly-good | Aventine | 2026-09-17 | laertes, players list | F |
| 19 | https://www.astralcodexten.com/p/the-ai-superforecasters-are-here | Astral Codex Ten | 2026-07-02 | scores 31 vs 36, Preseen claim | F |
| 20 | https://www.astralcodexten.com/p/does-forecasting-have-room-at-the | Astral Codex Ten | 2026-08-03 | headroom 4-12 points | F |
| 21 | https://arxiv.org/html/2510.17638v1 | arXiv (Prophet Arena) | 2025-10-20 | LLM vs Kalshi price | F |
| 22 | https://www.prophetarena.co/leaderboard/forecast | Prophet Arena | 2026-09-20 | live board | F |
| 23 | https://arxiv.org/html/2604.07355v1 | arXiv (Prediction Arena) | 2026-03-28 | live real-money results | F |
| 24 | https://arxiv.org/html/2607.06166v1 | arXiv (Gu, Kagan, Sun, Wu, Xu) | 2026-07-07 | proper betting, live Kalshi run | F |
| 25 | https://arxiv.org/html/2604.14199v1 | arXiv (PolyBench) | 2026-04-03 | slippage vs size | F |
| 26 | https://arxiv.org/html/2604.04220 | arXiv (TimeSeek) | 2026-04-05 | lifecycle BSS | F |
| 27 | https://arxiv.org/html/2607.14051 | arXiv (Hindcast) | 2026-07-15 | leak-free replay | F |
| 28 | https://arxiv.org/abs/2607.18269 | arXiv (Douven) | 2026-07-22 | contamination, aggregation | F |
| 29 | https://arxiv.org/abs/2606.26583 | arXiv (Begin et al.) | 2026-06-25 | monoculture | F |
| 30 | https://arxiv.org/abs/2607.17765 | arXiv (WC2026-Agents) | 2026-07-20 | agents vs bookmaker | F |
| 31 | https://arxiv.org/abs/2512.16030 | arXiv (KalshiBench) | 2025-12-17 | overconfidence | F |
| 32 | https://arxiv.org/html/2402.18563 | arXiv (Halawi et al.) | 2024-02-28 [pre-2025] | 0.179 vs 0.149 | F |
| 33 | https://arxiv.org/abs/2402.19379 | arXiv (Schoenegger et al.) | 2024-02-29 [pre-2025] | silicon crowd | F |
| 34 | https://faculty.wharton.upenn.edu/wp-content/uploads/2026/02/ForecastBench_A_Dynamic_.pdf | Karger et al. (Wharton copy) | 2026-02 upload | 0.054 gap | S |
| 35 | https://arxiv.org/html/2505.17989 | arXiv (Turtel et al.) | 2025-05-23, rev. 2025-12-01 | outcome RL, market 0.151 | F |
| 36 | https://arxiv.org/abs/2601.06336 | arXiv (Future-as-Label) | 2026-01-09 | Foresight Learning | F |
| 37 | https://arxiv.org/html/2511.07678 | arXiv (AIA Forecaster) | 2025-11-10 | market blend, search, Platt | F |
| 38 | https://saulius.io/blog/using-ai-agents-to-forecast-prediction-markets | saulius.io | 2025-12-27 | cross-check of [37] | F |
| 39 | https://arxiv.org/html/2506.00723 | arXiv (Paleka et al.) | 2025-05-31 | evaluation pitfalls | F |
| 40 | https://arxiv.org/abs/2605.00420 | arXiv (Foresight Arena) | 2026-05-01 | sample-size requirement | F |
| 41 | https://arxiv.org/abs/2604.15674 | arXiv (Wen et al.) | 2026-04-17 | UMA agreement 89.58% | F |
| 42 | https://arxiv.org/abs/2602.21229 | arXiv (Kim et al.) | 2026-02-04 | market-conditioned prompting | F |
| 43 | https://lacuna.tiptreesystems.com/work/beyond-accuracy-can-llm-forecasters-profit-on-prediction-markets/wrk_58f2322089a110fc5d773e7231e0dd88 (paper: https://openreview.net/forum?id=TSA5kRUKZv, not retrievable) | Lacuna summary of Henry, Ross, Marzoev, So, Lo | ICML 2026 | +4.0% / +9.1% ROI | F (secondary) |
| 44 | https://evals.futuresearch.ai/ | FutureSearch | 2026 | BTF-3, standings | F |
| 45 | https://markets.futuresearch.ai | FutureSearch | to 2026-08-11 | real and paper books | F |
| 46 | https://futuresearch.ai/blog/polymarket-forecasting-tutorial/ | FutureSearch | 2026-04-01 | caveat quote | F |
| 47 | https://futuresearch.ai/ | FutureSearch | undated | $0.15-$2 per question | F |
| 48 | https://www.lightningrod.ai/ | Lightning Rod Labs | undated | claims, customers | F |
| 49 | https://www.mantic.com/ | Mantic | undated | product, Cup ranks | F |
| 50 | https://www.coindesk.com/tech/2026/03/15/ai-agents-are-quietly-rewriting-prediction-market-trading | CoinDesk | 2026-03-15 | Polystrat, LayerHub claim | F |
| 51 | https://x.com/autonolas/status/2097314645858283622 | Olas on X | ~2026-09 | 33% vs 16% profitable | S |
| 52 | https://cryptoslate.com/easy-money-on-polymarket-and-kalshi-is-disappearing-as-prop-firms-deploy-ai-agents | CryptoSlate | 2026-07-22 | prop firms, Propr 5% | F |
| 53 | https://mcinerney.ai/writings/how-i-botted-6k-prediction-markets-as-i-slept/ | D. McInerney | 2026-05 | Kalshi mention bot | F |
| 54 | https://www.cjr.org/tow_center/polymarkets-ai-is-feeding-users-fabricated-information.php | Columbia Journalism Review | 2026-08-27 | fabricated Market Context | F |
| 55 | https://arxiv.org/abs/2508.11987 | arXiv (FutureX) | 2025-08-16 | benchmark, web-poisoning risk | F |
| 56 | https://docs.polymarket.com/trading/fees | Polymarket docs | undated | fee formula and rates | F |
| 57 | https://github.com/Polymarket/agents | GitHub | archived; seen 2026-09-20 | archived, 3,796 stars | S |
| 58 | https://github.com/Polymarket/agent-skills | GitHub | created 2026-02-19 | successor repo | S |
| 59 | https://arxiv.org/abs/2604.03888 (eval window per https://pith.science/paper/2604.03888) | arXiv / Pith | 2026-04-04 | PolySwarm, 2024 test set | F / S |
| 60 | https://arxiv.org/abs/2605.21521 | arXiv (Bazyari et al.) | 2026-05-18 | X vs news latency | F |
| 61 | https://arxiv.org/abs/2609.06005 | arXiv (Ibrahim, Zaki) | 2026-09-05 | cost to move a market | F |
| 62 | https://arxiv.org/abs/2608.30110 | arXiv (LiveMacroEval) | 2026-08-31 | macro nowcasts | F |
| 63 | https://arxiv.org/abs/2607.02467 | arXiv (V. Ming) | 2026-07-02 | human + AI on Polymarket | F |
| 64 | https://dev.to/wataru_suda_d295dab9cca4f/i-fact-checked-5-viral-my-ai-bot-made-money-posts-against-primary-data-none-survived-5c3d | DEV Community | 2026-09 | viral claims debunked | F |
| 65 | https://www.reddit.com/r/algotrading/comments/1uy5328/update_on_the_ai_vs_polymarket_project/ | Reddit | 2026-07-16 | paper league | S |
| 66 | https://fastcompany.com/91531389/ai-traders-are-already-testing-prediction-markets-and-losing-money | Fast Company | 2026-04-24 | press on [23] | S |
| 67 | https://hindustantimes.com/world-news/artificial-intelligence-now-beats-some-of-the-best-human-forecasters-101789639904836.html | Hindustan Times (syndicated) | 2026-09-17 | Preseen $35 -> $1.94m | S |
| 68 | https://parallect.ai/reports/ai-superforecasters-parity-may-2026-fb32ac | Parallect (AI-synthesised) | 2026-05-31 | unverified index values | F |
| 69 | https://h2o.ai/blog/2026/h2oai-super-agent-tops-futurex-leaderboard/ | H2O.ai | 2026 | FutureX vendor claim | S |
| 70 | https://arxiv.org/abs/2606.21013 | arXiv listing | 2026-06 | FutureX weekly #1 claim | S |
| 71 | https://www.coindesk.com/markets/2025/07/24/elon-musk-s-xai-partners-with-kalshi-to-bring-grok-to-prediction-markets | CoinDesk | 2025-07-24 | xAI partnerships | S |
| 72 | https://www.bloomberg.com/news/newsletters/2026-07-01/ai-models-could-make-hedge-fund-trading-riskier-wall-street-researchers-warn | Bloomberg | 2026-07-01 | same-model risk | S |
| 73 | https://cybernews.com/ai-news/viral-ai-trading-debunk-model-lost-money-polymarket-kalshi/ | Cybernews | 2026-04-22 | "researchers lost $3,000" (not used for numbers) | S |
| 74 | https://github.com/alsk1992/CloddsBot | GitHub | seen 2026-09-20 | open-source agent, 2,808 stars | S |
| 75 | https://arxiv.org/abs/2605.30802 | arXiv listing | 2026-05 | multi-agent oracle 83.43% | S |
| 76 | https://dev.to/manja316/176-trades-on-polymarket-what-my-bot-actually-made-its-not-what-you-think-3iib | DEV Community (individual) | 2026-03-14 | win rate vs PnL | F |
