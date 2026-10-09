# 07 - Cross-venue locked arbitrage (Polymarket vs Kalshi / exchanges / sportsbooks)
_Band: established-emerging · Evidence grade: B (papers and a passive-logger thesis for gap size and realised payoff; A for fees and live quotes; D for any arbitrageur's realised PnL) · Last verified: 2026-09-24_

### Cross-venue locked arbitrage
- **One-line summary**: Buy the same outcome's YES on one venue and its NO on another when the two cost less than $1 after fees. More generally, solve for the cheapest portfolio across equivalent and subset-related contracts whose payoff floor exceeds its cost, and hold it to settlement.
- **Category**: Arbitrage [two-venue locked structures; lead-lag and signals are file 08]
- **Maturity**: Established as an activity, not as proven profit. It is crowded and tooled: 301 GitHub repositories match "polymarket kalshi arbitrage", pmxt (a unified prediction-market API) has 2,158 stars, and paid scanners cost $149-299/month [E5]. What is measured is the opportunity, not anyone's PnL. Across 100,000+ events on ten venues, ~6% were cross-listed and semantically equivalent markets deviated 2-4% on average [1]. A nine-day passive logger across Kalshi, Polymarket, Predict and Limitless found 796 structures with a modelled payoff floor of $6,148 at a capital-weighted 0.52% return; 306 of the 308 that resolved paid at or above the floor [2]. No documented cross-venue arbitrageur PnL exists [E5]. On liquid pre-game NFL lines the gap is now inside one tick across three venues [3][4][5].
- **Requires AI?**: optional. Matching events across venues ("is this the same contract?") is where money is lost. Embeddings plus an LLM verifier can shortlist pairs and diff resolution clauses, but a human or a deterministic rules table must approve each pair. The trade itself is arithmetic.
- **How it works (simple flow)**:
  1. Match: build equivalence classes (same event, same resolution source and timing) and subset relations (one contract's YES implies the other's) across Polymarket international, Kalshi, Polymarket US and others you can lawfully access.
  2. Diff the rules clause by clause: deadline timezone (Kalshi often snapshots in the morning ET, Polymarket at 11:59 p.m. ET), source hierarchy, death / "credible reporting" / void clauses, overtime and DNP handling, index methodology [E5][6].
  3. Price with executable depth and both venues' fees. Polymarket international: `feeRate x p x (1-p)` (0.04-0.07; geopolitics and NFL/CFB game markets 0). Kalshi: `ceil(0.07 x p x (1-p) x 100)/100` per contract. Polymarket US: 0.0695 taker, 0.0125 maker rebate [E5][3].
  4. Trade only if (gap - fees) / cost x 365 / days to resolution beats your hurdle rate, which should be at least the yield you give up [E5].
  5. Execute the thinner or slower leg first (usually Polymarket); hedge the other immediately; keep an unwind rule for partial fills.
  6. Hold to settlement, then recycle capital across venues.
- **What creates the edge**: Segmentation. Capital, KYC, collateral types (pUSD, USD, other stablecoins) and legal eligibility split the participants, and "semantic non-fungibility" means contracts that look identical are not [1]. On the other side are single-venue traders who price only their own book. They pay because they cannot or will not hold accounts on both venues. The edge survives where arbitrage capital cannot reach: long-dated markets (the lock-up destroys annualised returns), wording mismatches (not true arbitrage), and thin books.
- **Capital required**: $10k+, split across venues and each leg fully collateralised. Lock-up runs to the later settlement: hours for sports; months for politics. Kalshi pays within hours, Polymarket after at least the 2-hour UMA window, and 4-6 days if disputed [E5].
- **Technical requirements**: (1) Data in: both venues' books by WebSocket (Polymarket CLOB; Kalshi REST/WS/FIX, all on one token bucket [7]), metadata and rules text, fee schedules pulled at start-up (never hard-coded). (2) Decision logic: pair matcher plus a clause-level rules diff; an LP (linear programme) over outcome states for subset structures; depth-aware sizing; an APY hurdle. (3) Execution: leg ordering; FOK/FAK on the thin leg; immediate hedge; partial-fill unwind; handling of Polymarket's matched-but-failed trades (`RETRYING`/`FAILED`) and of FAK/FOK responses returning `tradeIDs`, not hashes [E1]. (4) Risk: per-pair notional caps, a divergent-settlement reserve, a venue-outage kill switch. (5) Funding operations: cross-venue rebalancing through crypto rails. Build: 3-6 weeks for a solo developer with an existing arb stack; the rules diff is the long pole.
- **Opportunity size**: Measured gaps: 2-4% average deviations on equivalent markets [1]. Passive logger: $6,148 of modelled floor in nine days across four venues, ~$680/day for the whole observable set before competition (derived from [2]). Fee-adjusted crossings in a 20-second collector: a 1c crossing on La Liga contracts lost ~$957 after fees on ~119,000 contracts, and a 3c BTC gap shrank to 2c after walking depth against 2.07c of fees [E5]. Pre-game NFL on 24 Sep 2026: international, Polymarket US and Kalshi quoted the same four games within one tick [3][4][5]. Direction: saturated in liquid same-rule pairs; persistent only where lock-up, rules or depth deter capital.
- **Pros**: A true payoff floor when the rules match (306 of 308 resolved structures paid at or above floor [2]); no model risk on the outcome; public venue APIs; reuses existing arb infrastructure.
- **Cons / risks**: Rule mismatch is the whole risk. Kalshi settled Cardi B at the last traded price ($0.26/$0.74) while Polymarket paid YES $1.00, and Kalshi applied a death carve-out to Khamenei while Polymarket's contract went to UMA [E5]. Leg risk and partial fills. Capital lock-up and fragmentation: Polymarket US cash returns only to the original funding method after 1-4 business days; Kalshi international funding is by card, wire (minimum $1,000) or crypto [E5]. Fee changes (three schedule changes in six months [E5]). Legal: a US person may not touch the international venue, and the international-vs-US pair needs two properly domiciled entities [E9]. Tax: from 2026 only 90% of gambling losses are deductible, so a flat hedged book can produce taxable income [E9].
- **Expected results**: no public data on realised cross-venue arbitrage PnL [E5]. Best proxy: 0.52% capital-weighted per structure in a nine-day logger, with realised payoff $533 against a $522 floor on the resolved set [2]. The simulated "1,218.66% over 800 days" in [1] rests on 15 trades and is not a design number. Guess: a solo operator with $10k-$25k across two venues earns 3-10% a year on deployed capital from same-rule pairs, more only by accepting rule risk (which is then a bet, not an arbitrage).
- **Competitive landscape**: Very crowded at the scanner level (301 repos, pmxt, Oddpool, ArbBets [E5]). Professional capital "flows dynamically between both platforms" (Wintermute) [8]. What still pays is careful rules work and a willingness to hold small, long-dated or odd-structure positions that bots skip.
- **Regulatory/ethical flag**: none for a non-US person holding Kalshi plus Polymarket international, or a US person holding Kalshi plus Polymarket US (plus other DCMs) [E9]. Prohibited: a US person or VPN user on the international venue; one person holding both Polymarket books [E9]. Grey: sportsbook legs (books ban arbitrageurs; accounts get limited) [E5].
- **How you'd validate it**: 1) Passive logger for 14 days, as in [2]: record every structure whose floor exceeds cost net of both venues' fees at executable depth, plus days to resolution. 2) Score each pair's rules diff and flag any clause difference. 3) Pass: ≥ 8% annualised on deployed capital across 50+ resolved structures, no floor breach on "equivalent" pairs, and at least 30% of structures resolving within 30 days. Fail: returns concentrated in pairs with clause differences. Cost: ~30 engineering hours, $0 capital.

### Speed and execution sensitivity
- **Speed class**: execution-sensitive. Liquid same-rule pairs are contested at sub-minute speed and are mostly inside the fee band [E5]. The persistent gaps are balance-sheet trades where leg risk, depth and rules decide PnL, not milliseconds.

| Part of the strategy | What it depends on | If you are slower or execute worse | Realistic target for a solo team |
|---|---|---|---|
| Gap detection | WebSocket on both venues vs polling scanners | paid scanners refresh every 30 s to real time [E5]; slower means you only see what is left | event-driven, <1 s |
| First (thin) leg | FOK/FAK on Polymarket; taker delay on crypto (150 ms) and sports (1 s) [9] | a pending order cannot be cancelled while the other venue moves [9] | size to visible depth only |
| Hedge leg | Kalshi token bucket (Basic 200 read / 100 write per s) [7]; Polymarket US 20 req/s [E5] | a naked leg on a moving price | hedge within 1-2 s |
| Settlement and recycling | Kalshi hours; Polymarket ≥2 h, 4-6 days if disputed [E5]; fiat holds 1-4 days on the US venue [E5] | capital idles, so annualised returns halve | crypto rails between Polymarket international and Kalshi |

- **How speed changes the result**: (1) In liquid pairs, speed only determines whether you see a crossing that fees already eat [E5]. (2) Matched is not settled on Polymarket: a trade can move from `MATCHED` to `FAILED` [E1], so hedge on confirmation or budget for the reversal. (3) Capital velocity (days to recycle) matters more than latency for annualised return.
- **Where to run it**: close to both engines. Polymarket's is in AWS eu-west-2, reached from eu-west-1 [E1]; Kalshi's hosting location was not verified here. For balance-sheet structures, any unrestricted VPS works.

### Results by investment size
Assumptions: same-rule pairs only, 0.5-1.0% net per structure after both fees, average lock of 5-20 days, capital split 50/50 across venues, 30-60% utilisation. All figures are guesses.

| Capital | Workable? | How it is deployed | Gross / month | Running costs / month | Net / month | Net / capital / month | Binding constraint |
|---|---|---|---|---|---|---|---|
| $1k | no | $500 per venue; Kalshi international wire minimum is $1,000 [E5] | $5-25 | $10-20 | -$15 to +$15 | ~0% | fixed costs, minimum funding, depth per leg |
| $5k | marginal | $2.5k per venue, sports and short-dated pairs | $25-150 | $10-70 | $0-$120 | 0-2.4% | capital sits locked on the wrong venue; rebalancing cost |
| $10k | yes, small | $5k per venue, 10-30 open structures | $50-350 | $10-100 | $0-$300 | 0-3% | lock-up; few same-rule pairs above the fee band |
| Scale reference | the logger's full set | ~$1.2M capital-weighted across all 796 structures [2] (derived) | ~$20k modelled floor a month across four venues (derived) | n/a | n/a | ~0.5% per structure | competition takes most of it |

- **Minimum sensible capital**: ~$10k, because each venue needs its own float and fixed funding frictions.
- **Capacity ceiling**: depth, not capital. Executable size at a quoted gap ranged from 171 to 119,000 contracts in one sample [E5]. A solo book stops scaling around $50k-$100k of same-rule pairs (guess).

### APIs, data and third-party services
| Service | What for | Needed? | Cost | Access / jurisdiction notes |
|---|---|---|---|---|
| Polymarket CLOB + Gamma (international) | book, rules, execution | required (non-US) | free | not for US, UK or other restricted persons [E9] |
| Kalshi API (REST, WebSocket, FIX) | second venue | required | free market data (own query [5]); trading needs a KYC'd account, 140+ countries [E5] | tiers Basic 200/100 tokens/s to Prestige 12,000/9,600 [7] |
| Polymarket US API / public gateway | second venue for US persons | alternative | free; public BBO needs no auth [4] | US persons and entities only; 20 req/s [E5] |
| pmxt (MIT) | unified multi-venue API | optional | free (open source) [E5] | third-party code; review before use |
| Paid scanners (ArbBets, Oddpool) | discovery | optional | $149-299/month (vendor) [E5] | marketing claims; everyone else sees the same gaps |
| Embeddings / LLM API | pair shortlisting and rules diff | optional | pay per call | a human approves every pair |
| Crypto on-/off-ramps | moving capital between venues | required | Polymarket withdrawals free (<10 bp swap slippage); Kalshi crypto deposits via a third-party processor (fees vary) [E5] | fiat on Polymarket US returns only to the original method [E5] |
| Hosting | runtime | required | $10-100/month [10] | not UK or US for the international leg |

- **Monthly running cost**: minimum ~$10-20 (small VPS, free APIs); comfortable ~$250-400 (paid scanner, Dublin VPS, LLM rules diffing).

### What you are probably underestimating
1. **The main lines are already one price.** At ~21:30 UTC on 24 Sep 2026, Jets-Lions was 0.27/0.28 internationally, 0.265/0.270 on Polymarket US and 0.27/0.28 on Kalshi; Seahawks-Commanders, Bengals-Steelers and Chiefs-Dolphins matched within a tick too [3][4][5]. The desks have closed liquid sports. Look where they will not go.
2. **The fee band depends on the category, and it changes.** International NFL and CFB game markets are fee-free while other sports pay 0.05 [3], so an NFL pair at 50c costs only Kalshi's 1.75c where an MLB pair costs ~3.0c [E5]. Pull `feeSchedule` per market on every scan.
3. **"Same event" crypto pairs settle on different prices.** Polymarket's daily "Bitcoin above X" resolves on the Binance BTC/USDT 1-minute candle close at 12:00 ET [11]. Its 5m/15m up/down markets resolve on a 60 s Chainlink TWAP. Kalshi uses the average of 60 one-second CF Benchmarks RTI prints [E5]. Every crypto "arb" carries index basis, worst near the strike at expiry.
4. **One clause can turn the hedge into a coin flip.** For Khamenei, long Kalshi YES plus long Polymarket NO would have lost the Polymarket leg while Kalshi refunded near cost [E5]. The thesis logger's only shortfall came from a settlement-rule difference [2]. Keep a divergent-settlement reserve and price it.
5. **Settlement timing is a funding cost.** Kalshi pays within hours; Polymarket needs at least 2 hours, and 4-6 days if disputed [E5]. Disputes are rising: over 1,150 disputed markets in 2026 by mid-May [E3]. The losing leg is debited while the winning leg waits.
6. **Idle capital earns on one venue and not the other.** Kalshi pays ~3.25-4.05% APY on cash and positions for US users [E5] (snippet). Polymarket pays 3.25% holding rewards only in flagged markets [E2]. A 0.5% structure locked for 90 days loses to the yield it forgoes.
7. **Taxes can make a flat book cost money.** With 90% of gambling losses deductible from 2026 and no IRS guidance, $100k won on one leg and lost on the other can leave $10k taxable, and the legs may fall under different regimes [E9]. Get advice before scaling.
8. **You probably cannot legally hold every leg.** Non-US: Kalshi plus Polymarket international. US: Kalshi plus Polymarket US. Never both Polymarket books as one person [E9]. API access from a country is not permission: the Netherlands and Ireland are Restricted Persons in the ToS even though the API accepts their orders [E9].
9. **The published numbers measure opportunity, not profit.** Gebele and Matthes measure deviations [1], the thesis measures a modelled floor at posted depth [2], and scanners sell percentages without dollars [E5]. Budget for fills at worse than the top of book, and assume other bots take the best 70% of structures.

### Related files
- 08-cross-venue-leadlag-signals.md: using the other venue as a signal instead of a hedge.
- 04-sportsbook-anchored-sports-mm.md: sportsbook legs, devigging, DNP and void rules.
- 09-rebalancing-arbitrage-yesno-negrisk.md and 10-combinatorial-logical-arbitrage.md: the single-venue versions of the same LP.
- 11-derivatives-implied-relative-value.md: options and futures as the "other venue".
- 14-near-certain-bond-carry.md: settlement-discount carry, the long-dated cousin.
- 15-rules-dispute-trading.md and 64-rules-ambiguity-hazard-layer.md: pricing the rule-divergence risk explicitly.
- 78-two-book-crowd-differential.md: the international vs US book as a sentiment signal (speculative).

### Sources
[1] https://arxiv.org/abs/2601.01706 - arXiv, Gebele and Matthes, "Semantic Non-Fungibility and Violations of the Law of One Price in Prediction Markets" - 2026-01-05, fetched 2026-09-24 - 100,000+ events on ten venues (2018-2025); ~6% cross-listed; 2-4% average deviations; frictions, not disagreement; the 1,218.66% / 15-trade simulation and ~8% vs 2% cross-listing shares are from the brief's reading of the HTML.
[2] https://repozitorij.uni-lj.si/IzpisGradiva.php?id=187046&lang=eng - University of Ljubljana, D. Krasovec, "Combinatorial Arbitrage Between Prediction Markets" (undergraduate thesis) - 2026-09-08, fetched 2026-09-24 - 9 days, Kalshi / Polymarket / Predict / Limitless; 796 structures; modelled floor $6,148; capital-weighted 0.52%; 306 of 308 resolved at or above floor ($533 vs $522); ~$0.38 loss from settlement-rule differences; LP over outcome space.
[3] https://gamma-api.polymarket.com/events?tag_slug=nfl - Polymarket Gamma API - own query 2026-09-24 ~21:30 UTC - nfl-nyj-det-2026-09-27 0.27 / 0.28, SEA-WAS 0.75/0.76, CIN-PIT 0.62/0.63, KC-MIA 0.84/0.85; `zero_fees`; other sports 0.05.
[4] https://gateway.polymarket.us/v1/markets/aec-nfl-nyj-det-2026-09-27/bbo - Polymarket US public gateway - own query 2026-09-24 - 0.2650 / 0.2700; SEA-WAS 0.750/0.755; CIN-PIT 0.625/0.630; KC-MIA 0.850/0.855.
[5] https://api.elections.kalshi.com/trade-api/v2/markets?series_ticker=KXNFLGAME&status=open - Kalshi public API - own query 2026-09-24 - NYJ 0.27/0.28, SEA 0.75/0.76, CIN 0.62/0.63, KC 0.85/0.86.
[6] https://about.darkhorseodds.com/guides/kalshi-polymarket-market-rules - Dark Horse Odds - updated 2026-09-22, fetched 2026-09-24 - DNP props graded No on Polymarket, last pre-game price on Kalshi, void at books.
[7] https://docs.kalshi.com/getting_started/rate_limits - Kalshi docs - fetched 2026-09-24 - seven tiers, 10 tokens per default request, batch items billed separately; REST and FIX share buckets.
[8] https://finance.yahoo.com/markets/crypto/articles/wintermute-providing-liquidity-kalshi-polymarket-162008202.html - Yahoo Finance - 2026-05-29 (brief) - institutional capital moves between both venues.
[9] https://docs.polymarket.com/changelog/predictions.md and https://docs.polymarket.com/concepts/order-lifecycle.md - Polymarket docs - fetched 2026-09-24 - crypto taker delay 150 ms since 2026-09-04; sports delay windows; pending orders cannot be cancelled.
[10] https://instances.vantage.sh/aws/ec2/c7i.large - Vantage - fetched 2026-09-24 - $0.089/h list price.
[11] https://gamma-api.polymarket.com/events?slug=bitcoin-above-on-september-27-2026 - Polymarket Gamma API - own query 2026-09-24 - rules: resolves on "the Binance 1 minute candle for BTC/USDT 12:00 in the ET timezone (noon)" close.
[E1] Evidence pack E1 - trade status path, `tradeIDs` in FAK/FOK responses, eu-west-2 / eu-west-1.
[E2] Evidence pack E2 - holding rewards 3.25% in flagged markets.
[E3] Evidence pack E3 - dispute counts and timing.
[E5] Evidence pack E5 - venue fees, funding, settlement timing, rule-mismatch cases, microstructure collector, scanners and repo counts, Kalshi APY, limits.
[E9] Evidence pack E9 - eligibility per venue, restricted persons, tax (90% cap).
