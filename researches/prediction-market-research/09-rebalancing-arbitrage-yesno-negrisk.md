# 09 - Same-platform rebalancing arbitrage: YES+NO sets and NegRisk converter / baskets
_Band: established-emerging · Evidence grade: A (two on-chain papers, one reproducible study, official docs, live scan) · Last verified: 2026-09-24_

### Same-platform rebalancing arbitrage
- **One-line summary**: Enforce the no-arbitrage identities inside Polymarket. In one binary, YES + NO = $1 through split and merge. In a multi-outcome neg-risk event, 1 NO converts into 1 YES of every other outcome, and the YES prices must sum to $1. Buy or sell whichever side is mispriced after fees. Large in 2024, now small, fast, concentrated and fee-gated.
- **Category**: Arbitrage [protocol identities; cross-market logic is file 10]
- **Maturity**: Established but effectively closed to newcomers. The ~$40M headline (April 2024 to April 2025: $10.58M single-condition, $29.02M neg-risk, $95k combinatorial) measures wallets that assembled complete sets within ~1 hour, not atomic arbitrage [1][E4]. An execution-aware, mechanism-linked reconstruction to December 2025 finds $1.12M in total, of which $1.086M went through the neg-risk converter. The top 10 addresses took 75%, and median profit per conversion fell from ~$1 (2024) to $0.20 and then $0.08 by early 2026 [2]. Re-running the $40M method on the overlapping window gives $291,424 [2]. Since 30 March 2026 every leg pays a taker fee except in geopolitics [E1].
- **Requires AI?**: no. Detection and execution are arithmetic. The only judgement call is reading augmented neg-risk rules ("Other" and placeholder outcomes), which a rules parser can flag.
- **How it works (simple flow)**:
  1. Single binary, long: if best ask YES + best ask NO < $1 minus fees, buy both and merge the pair into $1 pUSD (gasless via the relayer) [E1].
  2. Single binary, short: if best bid YES + best bid NO > $1 plus fees, split $1 into YES + NO and sell both.
  3. Neg-risk, NO side (executable before settlement): in an event with n outcomes, converting 1 NO of each of k outcomes returns (k - 1) collateral plus YES on the remaining outcomes [E1]. If buying NOs and converting beats their price, profit is released immediately. This direction has the converter, which is why violations close faster: 36 NO-side episodes vs 2,098 YES-side, median 7.99 s vs 16.15 s, April-May 2026 [2].
  4. Neg-risk, YES side (no converter): if all YES asks sum to less than $1, buying the basket pays $1 at settlement. This is capital lock-up carry, not arbitrage: baskets earned just $32,283 in the whole reconstruction [2].
  5. Recycle: most realised converter profit (81.1%) came from partial conversions and managing the returned YES inventory, not clean full-set conversions (18.9%) [2]. ~80% of conversions used maker-assisted fills [2].
- **What creates the edge**: Transient incoherence. Retail piles into one candidate and the other legs reprice slowly; many-leg books drift. The protocol primitives (split, merge, convert) let one actor enforce coherence that other traders ignore. On the other side are takers who move one leg and makers who quote legs independently. Today the edge is mostly "being the fastest of ten bots" [2], and the fee turns most small violations negative.
- **Capital required**: <$1k-$10k for the executable variants (positions last seconds to minutes; merges and conversions release capital immediately). YES-basket carry locks capital to resolution, often months.
- **Technical requirements**: (1) Data in: CLOB WebSocket books for every leg of every neg-risk event, Gamma event metadata (`negRisk`, `negRiskAugmented`, active legs), per-market `feeSchedule`. (2) Decision logic: depth-aware sum checks (not top of book) net of per-leg fees; a converter-path optimiser (which NOs to buy, how many to convert); exclusion of placeholder and "Other" legs; YES-basket annualised-return hurdle. (3) Execution: multi-leg FOK/FAK or maker-legged entry, relayer split/merge/convert (the V2 adapter `0xadA2…6eAab`; V1 retired 17 Jul 2026 [E1]), orphan-leg handling. (4) Risk: leg-completion limits, event-rule checks. (5) Test: replay on recorded books. Build: 1-3 weeks for a solo developer with an existing CLOB client; weeks more to compete on speed.
- **Opportunity size**: Small. Executable profit through December 2025 was $1.12M across all actors for all time [2], and a reproducible September 2026 study finds that apparent multi-outcome violations are mostly liquidity and microstructure artefacts: genuine sub-$1 arbitrage is rare, at most 2.7% gross, and limited to small, dense fields [3]. The live scan on 24 Sep 2026 fits this. Among 236 active neg-risk events in the top 1,100 by 24-hour volume, the median sum of YES asks was 1.054 and of YES bids 0.967. Only 22 events showed a top-of-book sum outside that band, nearly all augmented events (named legs only) or events whose missing legs explain the gap [4]. Direction: shrinking per trade; concentrated in ten addresses. Two worked examples from the same scan [4]. *Fed decision, December 2026* (5 outcomes, feeRate 0.05): YES bids summed to 1.007. Buying the five NOs at 1 - bid (0.996, 0.987, 0.74, 0.29, 0.98) costs 3.993 against a conversion value of 4.000, +0.7c gross per set. Taker fees on the five legs total ~2.2c (derived), so a taker nets ≈ -1.5c per set; it is positive only as a patient maker on every leg. *Maduro prison time* (5 outcomes, fee-free, geopolitics tag): YES asks summed to 0.899, an 11.2% gross discount paid by 31 Dec 2027 at the latest, ~9% annualised (derived). The thinnest leg showed 29.3 shares, so the basket held ~$26 at those prices. The rules resolve on "the first sentence rendered" by that date, so whether "No prison time" covers "no sentence by the deadline" is rule risk. This is YES-side carry, the pattern [2] describes.
- **Pros**: Risk-free when both legs fill and the rules are read correctly; tiny capital; seconds-long exposure; zero outcome-model risk; fee-free geopolitics events still allow frictionless conversion.
- **Cons / risks**: Taker fees on every leg since March 2026 (at feeRate 0.05, 0.5-1.25c per leg near the middle of the price range [E1]). Leg risk: one pair bot completed 60 of 69 pairs and the 9 orphans erased its profit [5]. Speed: NBA single-market violations lasted a median 3.6 s, and 81.1% of detected anomalies occurred post-game when they could not be executed [6]. Augmented neg-risk "Other" redefinitions change what a "complete" set is [E1]. The adapter has a conversion `feeRate` parameter whose current value is unverified [E1]. Neg-risk markets add a fixed +1 h between `reportPayouts` and resolution and allow no 50/50 outcome [E3].
- **Expected results**: The historical winners: the top address made $2.01M over 4,049 transactions (~$496 each) in April 2024 to April 2025 [1][E4]; the top three wallets made $4.2M at typical margins of 1-5% [E4]. Today: median $0.08 per conversion [2]. Guess for a new solo entrant: near zero from taker-executed arbitrage; a few dollars to tens of dollars a month from maker-legged entries and fee-free geopolitics events; YES-basket carry at 5-10% annualised on small sizes. Not a standalone business.
- **Competitive landscape**: Ten addresses hold 75% of converter profit [2]; NO-side violations close in seconds [2]. The survivors are fast, maker-legged and inventory-recycling bots that treat conversion as part of a market-making book (file 02), not a standalone scanner.
- **Regulatory/ethical flag**: none. Using the protocol's split, merge and convert primitives is intended behaviour (E9: trading on own research, models and speed is Allowed). Avoid self-fills across your own wallets when legging [E9].
- **How you'd validate it**: 1) A 7-day read-only scan of all active binaries and neg-risk events: depth-aware (not top-of-book) set costs net of per-leg `feeSchedule`, episode duration, and depth at the violating price. 2) Split by taker-executable vs maker-legged vs fee-free geopolitics. 3) Pass: ≥ 20 executable episodes a week with net ≥ 50 bps and lifetime longer than your measured round trip. Fail: everything positive is either augmented (incomplete sets) or shorter than your latency. Cost: ~15 engineering hours, $0.

### Speed and execution sensitivity
- **Speed class**: latency-critical for the executable variants (violations last seconds; NO-side median 7.99 s [2], NBA single-market median 3.6 s [6]). Speed-insensitive for YES-basket carry, which is a balance-sheet trade.

| Part of the strategy | What it depends on | If you are slower or execute worse | Realistic target for a solo team |
|---|---|---|---|
| Detection | WebSocket books on every leg; depth-aware sums | you see violations that ten faster bots already closed [2] | <100 ms from book update to decision |
| Multi-leg execution | FOK/FAK per leg or maker-legged entry | orphan legs: 9 of 69 pairs in one bot erased all profit [5] | size to the thinnest leg's depth; fail closed |
| Conversion / merge | relayer throughput (25 req/min on `/submit`) and adapter calls [E1] | capital stuck in legs; no instant release | batch conversions; confirm on-chain |
| YES-basket carry | rules reading, annualised hurdle | none from speed; errors are rule errors | daily scan |

- **How speed changes the result**: (1) The NO side (with a converter) closes about twice as fast as the YES side [2], so the executable half of the opportunity is exactly the half that needs speed. (2) The crypto 150 ms and sports 1 s taker delays [7] make multi-leg taker arbitrage in those categories nearly impossible: legs cannot be cancelled while pending. (3) Maker-legged entry trades speed for leg risk.
- **Where to run it**: AWS eu-west-1 for the executable variants; anywhere for carry.

### Results by investment size
Assumptions: taker arbitrage ~0 after fees; maker-legged and fee-free episodes of $1-20 each, a few per week; YES-basket carry at 5-10% annualised with top-of-book depth caps (the Maduro basket in Opportunity size capped at ~$26). All figures are guesses.

| Capital | Workable? | How it is deployed | Gross / month | Running costs / month | Net / month | Net / capital / month | Binding constraint |
|---|---|---|---|---|---|---|---|
| $1k | yes, trivially | scanner plus a few maker-legged sets; small carry baskets | $0-$30 | $10-20 | -$20 to +$15 | -2% to +1.5% | depth at the violating price, not capital |
| $5k | yes, trivially | same, with more carry baskets | $10-$80 | $10-70 | -$30 to +$60 | -0.6% to +1.2% | ten faster bots; few genuine episodes |
| $10k | yes, trivially | same | $20-$120 | $10-70 | -$30 to +$100 | -0.3% to +1% | same; capital beyond ~$2k is idle |

- **Minimum sensible capital**: ~$500. Depth, not capital, binds.
- **Capacity ceiling**: ~$2k-$5k for the executable variants (guess); carry scales further but is not arbitrage.

### APIs, data and third-party services
| Service | What for | Needed? | Cost | Access / jurisdiction notes |
|---|---|---|---|---|
| CLOB REST + WebSockets | books on every leg, execution | required | free | not for US, UK or other restricted persons [E9] |
| Gamma API | `negRisk`, `negRiskAugmented`, active legs, `feeSchedule` | required | free | exclude placeholder and "Other" legs [E1] |
| Builder relayer + V2 Neg Risk Adapter | gasless split / merge / convert / redeem | required | free; Builder credentials | V1 adapter retired 2026-07-17 [E1] |
| Polygon RPC | verify conversions and fills | recommended | free public RPC; Alchemy free tier then $0.525 per 1M CU [8] | none |
| Reproducible coherence study (`polymarket-coherence`, MIT) | baseline method and public data | optional | free [3] | reproducible without API keys [3] |
| Hosting | runtime | required | ~$65-100/month eu-west-1 [9] | not UK or US |

- **Monthly running cost**: minimum ~$10-20; comfortable ~$70-100. Do not spend more than the opportunity.

### Related files
- 10-combinatorial-logical-arbitrage.md: logical constraints across separate markets (ladders, implication pairs, same-game lines).
- 02-event-market-making-spread-carry.md: where converter recycling now lives, inside a maker book.
- 03-short-crypto-maker-side.md: split-sell and merge as a maker business in up/down markets.
- 14-near-certain-bond-carry.md: YES-basket carry is a settlement-discount trade.
- 31-market-manipulation-and-exploits.md: ghost fills and reverted counterparties that historically targeted legging bots.
- 72-unnamed-outcome-unpacking.md: pricing the augmented "Other" leg.

### Sources
[1] https://arxiv.org/abs/2508.03474 - arXiv / AFT 2025, Saguillo et al. - 2025-08-05 (via E4 [1], F) - Apr 2024-Apr 2025: single-condition long $5.90M and short $4.68M; neg-risk $29.02M (buy NO $17.31M, buy YES $11.09M, sell YES $0.61M); combinatorial ~$95k; top address $2.01M over 4,049 transactions; bundles within ~950 blocks.
[2] https://arxiv.org/html/2608.00666v1 - arXiv, Gebele, Mutzel, Matthes - 2026-08-01, fetched 2026-09-24 - $1.12M total; converter $1.086M (full-set $205,531 = 18.9%, partial / recycling 81.1%); settlement baskets $32,283; top 10 = 75% of converter profit; median per conversion ~$1, then $0.20, then $0.08 by early 2026; ~80% maker-assisted; CLOB sample Apr-May 2026: 2,098 YES-side vs 36 NO-side violations, median 16.15 s vs 7.99 s; overlapping-window re-run of the prior method: $291,424.
[3] https://zenodo.org/doi/10.5281/zenodo.22739555 - Zenodo, A. Breguez, "polymarket-coherence" v1.0.6 (MIT) - 2026-09-14, fetched 2026-09-24 - apparent multi-outcome coherence violations are microstructure artefacts; genuine sub-$1 arbitrage is rare, ≤2.7% gross, in small dense fields; reproducible from public data.
[4] https://gamma-api.polymarket.com/events?active=true&closed=false&order=volume24hr and https://clob.polymarket.com/book?token_id=… - Polymarket APIs - own query 2026-09-24 ~21:15 UTC - 522 neg-risk events in the top 1,100 by 24 h volume, 236 with full bid/ask on all active legs; median sum of YES asks 1.0535, bids 0.967; 17 with ask-sum < 1 (mostly augmented), 5 with bid-sum > 1; Fed December YES bids 0.004 / 0.013 / 0.26 / 0.71 / 0.02; Maduro prison time asks 0.65 / 0.072 / 0.008 / 0.009 / 0.16, top sizes 238.62 / 120.94 / 335.06 / 152 / 29.3, end 2028-01-01, no fee schedule.
[5] https://api.pullpush.io/reddit/search/submission/?q=polymarket%20arbitrage&size=60&sort=desc&sort_type=score&after=1740000000 - Reddit via PullPush - March-July 2026 (brief) - a 0.48/0.48 up/down pair bot completed 60 of 69 pairs; orphans erased the profit; "fees kill arb" sentiment. Self-reported.
[6] https://arxiv.org/html/2605.00864v1 - arXiv, Cheng, Yang, Zou - 2026-04-22, fetched 2026-09-24 - 173 NBA games, 75,088,497 book snapshots: 7 executable single-market episodes, median 3.6 s; 81.1% of anomalies post-game and non-executable.
[7] https://docs.polymarket.com/changelog/predictions.md - Polymarket docs - fetched 2026-09-24 - crypto taker delay 150 ms since 2026-09-04; V1 neg-risk adapter deprecation (2026-07-14).
[8] https://www.alchemy.com/pricing - Alchemy (vendor) - fetched 2026-09-24.
[9] https://instances.vantage.sh/aws/ec2/c7i.large - Vantage - fetched 2026-09-24 - $0.089/h list price.
[E1] Evidence pack E1 - split / merge / convert maths, V2 adapter address, augmented neg-risk, adapter `feeRate` (value unverified), fee formula and Fee Structure V2 date, relayer limits.
[E3] Evidence pack E3 - neg-risk +1 h resolution delay, no 50/50 payouts.
[E4] Evidence pack E4 - $39.69M decomposition, top-10 share, DL News top-3 wallets and 1-5% margins.
[E9] Evidence pack E9 - traffic-light table.
