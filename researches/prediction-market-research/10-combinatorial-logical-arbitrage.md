# 10 - Combinatorial / logical arbitrage: dependent markets, same-game market types, strike and date ladders
_Band: established-emerging · Evidence grade: A-B (three papers, one live scan); no operator PnL · Last verified: 2026-09-24_

### Combinatorial / logical arbitrage
- **One-line summary**: Trade violations of logical constraints between separate markets. Examples: "A implies B" pairs; moneyline vs spread vs total in the same game; "above K" ladders that must fall as K rises; "by March" prices that cannot exceed "by June". Nothing in the protocol enforces these, because they are not wired together the way neg-risk events are.
- **Category**: Arbitrage [logical dependencies across markets; single-event identities are file 09]
- **Maturity**: Emerging, and retail-sized. The executable evidence is small. Across 173 NBA games (February-March 2026), 290 cross-market-type episodes had a median yield of 101 bps and a median life of 16 s. 76.9% were limited to an average executable size of 14.8 shares, and the capped aggregate profit was $559.59 (uncapped theoretical $2,032.75) [1]. Cross-event "combinatorial" arbitrage in the April 2024 to April 2025 on-chain study realised only ~$95k, all in US-election pairs [2][E4]. Live on 24 Sep 2026, a scan of 125 price ladders found three genuine executable crossings, each 0.1-0.5c [3].
- **Requires AI?**: optional, for finding dependencies. Dependency search is combinatorially large (naively O(2^(n+m)) states for two markets with n and m outcomes). The on-chain study cut it down with timeliness and topical-similarity filters, then used an LLM or expert to validate dependence [2]. Pricing and execution are arithmetic, and every AI-proposed dependency needs a rules check.
- **How it works (simple flow)**:
  1. Build a dependency graph with three edge types. (a) Same game: moneyline, spread and total lines, which imply bounds on each other. (b) Ladders: P(above K1) ≥ P(above K2) for K1 < K2; for "hits" ladders, the same monotonicity on each side; nested deadlines P(by T1) ≤ P(by T2); implied bucket masses ≥ 0 [4]. (c) Cross-event implications: "X wins the general election" implies "X's party wins", a state result bounds a national result, and so on.
  2. For each edge, check executable prices (bid vs ask, at depth) against the constraint.
  3. When violated, buy the underpriced leg and sell the overpriced one (selling YES = buying NO). The combined payoff is ≥ 0 in every state, and sometimes pays both legs (a "middle").
  4. Net per-leg taker fees: 0.05 x p x (1-p) in most sports, 0.07 crypto, 0.04 politics; zero in geopolitics and in NFL and college-football game markets [5].
  5. Hold to resolution, or unwind when the prices re-align. There is no converter, so capital stays locked until then.
- **What creates the edge**: Separate books quoted by different makers who update at different speeds, especially in the final minutes of live games (279 of 290 NBA episodes were in play [1]). Retail piles into single strikes or single dates without looking at neighbours. The protocol gives no way to convert between separate markets. On the other side are retail takers and single-market makers. The largest violations sit at the thin end (e.g. disease-count ladders that "placed probability mass on impossible outcomes, including decreasing values in cumulative forecasts" [6]), which is also where size is smallest.
- **Capital required**: <$1k. Executable size is tiny (~15 shares per NBA episode [1]), and ladder crossings sit at prices under 2c [3]. Lock-up runs to resolution: hours for games, weeks to months for ladders.
- **Technical requirements**: (1) Data in: WebSocket books for every market in a game or ladder; Gamma metadata (`groupItemTitle`, strike parsing, rules text, "hit" vs "close above" semantics, deadline times); `feeSchedule`. (2) Decision logic: strike and date parser with unit normalisation (the live scan's first pass mis-parsed "$5B" vs "$100M" and flagged six false violations [3]); constraint checks at depth; a same-game payoff matrix per league; a dependency validator. (3) Execution: two- or three-leg FOK/FAK, or maker-legged entry; the 1 s sports delay means legs cannot be cancelled while pending [5]. (4) Risk: rules-semantics checks, per-structure caps. (5) Test: recorded books; replicate [1] with current fees. Build: 1-3 weeks for ladders and calendars, 3-5 weeks for same-game in-play.
- **Opportunity size**: Small. NBA same-game: at most ~$560-$2,000 per month-long regular-season sample for everyone [1], measured when NBA carried no taker fee. A 101 bps median edge is now below a single leg's 1.25c fee at p = 0.50 (derived from [5]). NFL and CFB game markets are fee-free today [5], so NFL in-play cross-type episodes are not fee-gated, only delay-gated. Ladders on 24 Sep 2026: 884 adjacent rung pairs across 125 ladders in the top 1,100 events [3]. Three genuine executable crossings: gold "hit $4,800 in September" bid 0.017 against "hit $4,700" ask 0.012 (0.5c); "Republican Senate odds hit 60" vs "hit 55" (0.3c); BTC "dip to $15k before 2027" vs "$20k" (0.1c). All sit in the 0.001-tick zone below 2c. Cross-event: $95k over a full election year [2]. Direction: stable, small, fee-gated.
- **Pros**: A true payoff floor when the semantics match; tiny capital; scanning ladders is cheap; the dependency graph doubles as a consistency layer for any quoting engine; NFL and geopolitics legs are fee-free.
- **Cons / risks**: Size (~15 shares), fees on 2-3 taker legs, the 1 s sports delay on multi-leg execution, and semantic traps: "hits" vs "closes above", different resolution sources or times across a "ladder", placeholder strikes. Capital is locked to resolution. The theoretical "middle" payout was never realised in the NBA sample [1].
- **Expected results**: no public operator data, theoretical only, beyond the aggregate capped $559.59 across 173 NBA games [1] and ~$95k across a 2024-25 election-year sample [2]. Guess for a solo scanner: $10-100 a month from ladders and calendars; NFL in-play same-game adds an unknown but small amount; best run as a feature inside a quoting engine (file 02) rather than alone.
- **Competitive landscape**: Few specialists, because the dependency search is tedious and the size is tiny. Same-game in-play competes with fast sports makers, who resync their lines within ~16 s [1]. Ladders compete with the makers of each rung, who increasingly quote whole ladders together.
- **Regulatory/ethical flag**: none (E9: trading on own models and speed is Allowed).
- **How you'd validate it**: 1) Nightly scan of all numeric ladders and nested-date families: executable crossings of at least 1c after fees, with depth. 2) One NFL weekend of recorded books for all moneyline, spread and total markets per game: replicate [1] with the fee-free NFL schedule and the 1 s delay. 3) Pass: ≥ 10 executable episodes a week netting ≥ $5 each. Fail: fewer, or all below one leg's fee. Cost: ~15 engineering hours, $0.

### Speed and execution sensitivity
- **Speed class**: latency-sensitive for same-game in play (median episode 16 s, with a 1 s taker delay per leg [1][5]). Speed-insensitive for ladders and calendars: crossings persist but are sub-cent.

| Part of the strategy | What it depends on | If you are slower or execute worse | Realistic target for a solo team |
|---|---|---|---|
| Same-game detection | WebSocket books for all market types in a game | episodes last a median 16 s [1] | <500 ms detection |
| Multi-leg execution | taker delay (1 s sports), FOK/FAK | a second leg that moves during the first leg's delay leaves you with a naked position | maker-leg the thicker side, take the thinner |
| Ladder / calendar scan | parser quality | false positives from unit or semantics errors [3] | nightly or hourly |

- **How speed changes the result**: (1) In play, the 1 s delay applies to each taker leg, so two sequential legs cost ~2 s against a 16 s median episode (derived from [1][5]). (2) For ladders, speed is irrelevant; parser accuracy decides whether a "violation" is real.
- **Where to run it**: eu-west-1 for in-play; anywhere for ladders.

### Results by investment size
Assumptions: ladders and calendars plus opportunistic NFL same-game episodes; ~15-share clips; per-leg fees where charged. All figures are guesses.

| Capital | Workable? | How it is deployed | Gross / month | Running costs / month | Net / month | Net / capital / month | Binding constraint |
|---|---|---|---|---|---|---|---|
| $1k | yes | scanner-triggered clips of 10-50 shares | $5-$100 | $10-20 | -$15 to +$80 | -1.5% to +8% | depth (~15 shares) |
| $5k | same as $1k | extra capital is idle | $5-$120 | $10-70 | -$60 to +$100 | ~0-2% | depth |
| $10k | same as $1k | extra capital is idle | $5-$120 | $10-70 | -$60 to +$100 | ~0-1% | depth |

- **Minimum sensible capital**: ~$300-500.
- **Capacity ceiling**: ~$1k-$2k (guess). Capital beyond that sits idle.

### APIs, data and third-party services
| Service | What for | Needed? | Cost | Access / jurisdiction notes |
|---|---|---|---|---|
| CLOB REST + WebSockets | books for every rung and market type | required | free | not for US, UK or other restricted persons [E9] |
| Gamma API | ladder grouping, strikes, rules, `feeSchedule`, `secondsDelay` | required | free | semantics differ between "hit" and "close above" markets |
| LLM API | dependency proposals across unrelated markets | optional | pay per call | validate every edge by rules |
| Recorded books / Telonex | replaying [1] with current fees | optional | own recorder free; Telonex $99 / $199 per month (vendor) [E6] | none |
| Hosting | runtime | required | $10-20/month (ladders); ~$65-100 in eu-west-1 for in-play [7] | not UK or US |

- **Monthly running cost**: minimum ~$10; comfortable ~$70-100.

### Related files
- 09-rebalancing-arbitrage-yesno-negrisk.md: identities inside one event (sum to $1, converter).
- 04-sportsbook-anchored-sports-mm.md: same-game fair values off sportsbooks.
- 06-combos-rfq-market-making.md: same-game correlation, priced for parlays.
- 11-derivatives-implied-relative-value.md: pricing whole ladders off option surfaces rather than only checking monotonicity.
- 67-semantic-market-graph-relative-value.md: the soft (non-arbitrage) version of the dependency graph.
- 71-print-process-twins-numeric-brackets.md: bracket ladders settled by a publisher's rounding rules.

### Sources
[1] https://arxiv.org/html/2605.00864v1 - arXiv, Cheng, Yang, Zou - 2026-04-22, fetched 2026-09-24 - 173 NBA games, 75,088,497 snapshots (4 Feb-4 Mar 2026): 7 single-market episodes (median 3.6 s); 290 combinatorial episodes, 279 in live play, median 16 s, median 101 bps, 76.9% constrained to ~14.8 shares; $559.59 capped vs $2,032.75 theoretical; "middle" never realised; NBA fee-free in the sample (per the brief).
[2] https://arxiv.org/abs/2508.03474 - arXiv / AFT 2025, Saguillo et al. - 2025-08-05 (via E4 [1], F, and the brief) - combinatorial arbitrage ~$95k (largest pair $60,237), 4 of 11 dependent pairs, all US election; dependency-search heuristic with LLM or expert validation.
[3] https://gamma-api.polymarket.com/events?active=true&closed=false&order=volume24hr - Polymarket Gamma API - own query 2026-09-24 ~21:20 UTC - 125 ladders, 884 adjacent rung pairs; 9 flagged top-of-book crossings, of which 6 were unit-parsing artefacts (FDV ladders) and 3 genuine: what-price-will-xauusd-hit-in-september-2026 4,700↑ ask 0.012 vs 4,800↑ bid 0.017; republican-senate-odds-hit-by-october-31 55 ask 0.008 vs 60 bid 0.011; what-price-will-bitcoin-hit-before-2027 ↓15,000 bid 0.018 vs ↓20,000 ask 0.017; depth not checked.
[4] https://arxiv.org/abs/2606.30040 - arXiv - 2026-06-29 (brief) - turning adjacent threshold contracts into a probability mass function (CPI); the construction exposes negative masses.
[5] https://gamma-api.polymarket.com/events?tag_slug=nfl and https://docs.polymarket.com/changelog/predictions.md - Polymarket - own query and fetch 2026-09-24 - NFL and CFB game markets `zero_fees` with `secondsDelay` 1; other sports 0.05; sports fee 0.03 to 0.05 on 2026-07-10; pending orders cannot be cancelled (order-lifecycle page).
[6] https://arxiv.org/abs/2605.11220 - arXiv, Dudley and Magdaleno, "Prediction Markets Underperform Simple Baselines For Infectious Disease Forecasting" - 2026-05-11, fetched 2026-09-24 - Polymarket flu and measles ladders placed "probability mass on impossible outcomes (e.g., decreasing values in cumulative forecasts)"; optimal ensemble weight on markets was zero.
[7] https://instances.vantage.sh/aws/ec2/c7i.large - Vantage - fetched 2026-09-24 - $0.089/h list price.
[E4] Evidence pack E4 - $39.69M decomposition incl. combinatorial ~$95k.
[E6] Evidence pack E6 - Telonex list prices.
[E9] Evidence pack E9 - traffic-light table.
