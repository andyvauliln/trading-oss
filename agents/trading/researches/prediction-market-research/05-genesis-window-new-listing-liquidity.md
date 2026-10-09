# 05 - New-listing (genesis-window) liquidity provision and initial price discovery
_Band: established-emerging · Evidence grade: A for the opening-spread measurements (one paper, ~160,000 contracts, fee-free sample); B-C for the maker's net result (no operator has published PnL) · Last verified: 2026-09-24_

### New-listing (genesis-window) liquidity provision
- **One-line summary**: Be the first sensible quote in newly listed non-sports markets. First-minute takers pay a median 12-16c half-spread, against ~1c a few hours later. The business is to collect the part of that cost that is not adverse selection, and to earn the first-quoter share of any reward pool attached at listing.
- **Category**: Market-making [lifecycle-specific; steady-state quoting is file 02]
- **Maturity**: Emerging. The rent is measured; the business is not. A study of ~160,000 contracts created October 2025 to March 2026 finds first-minute median effective half-spreads of 12-16c in every non-sports category versus 1.5c in sports, falling ~10x within the first hour [1]. It also finds that in politics, geopolitics, elections and "other" only 25-35% of what early takers pay stays with the maker; the rest is the price moving after the trade [1]. The sample ends on 29 March 2026, one day before Fee Structure V2 put taker fees and maker rebates on almost every category. The authors predict that rebates "should compress opening spreads" [1]. No operator has published genesis-window PnL. The only practitioner number, "80-200% annualised in new markets", is a 2025-era self-report [E4].
- **Requires AI?**: optional but useful. A fair-value seed is needed before any trade exists. Deterministic seeds (a cross-listed Kalshi price, an option-implied probability, a base rate for the market family) come first. An LLM prior helps for one-off questions with no anchor, and to parse rules and flag the "Other" and placeholder legs in new neg-risk events. The LLM sets a prior and a width, never the size.
- **How it works (simple flow)**:
  1. Discovery: subscribe to the market WebSocket's `new_market` event (with `custom_feature_enabled`) and poll Gamma's keyset endpoints for new events [E1]. About 305,000 markets were created in the latest month on The Block's series [E1], overwhelmingly sports and crypto templates. The 1,100 newest markets on 24 Sep 2026 were all created in ten minutes and were all sports or crypto up/down [2].
  2. Filter: keep non-sports, non-template markets (politics, geopolitics, elections, economy, culture, tech, "other"), where opening spreads are wide. Sports opens at the tick floor because its price discovery happened at bookmakers [1].
  3. Seed fair value: a cross-listed price (file 08), options (file 11), a family base rate, or an LLM prior with an explicit uncertainty band.
  4. Quote small and wide first. Post-only two-sided quotes inside the prevailing opening spread (median opening quoted spread 8-21c by category [1]), sized so that one informed first taker costs little. Tighten as trades reveal where the market sits.
  5. Manage the informed-first-taker problem by category. Economy and scheduled-release markets keep most of the spread (realised/effective, R/E, 0.86). Politics (0.35), elections (0.29), geopolitics (0.25) and "other" (0.33) mostly do not [1].
  6. Reward timing: many new markets carry a reward config from day one. On 24 Sep 2026, 53 of 72 sampled non-sports markets under six hours old already had one, worth $6,365/day between them [3]. Being in band before competitors arrive earns the highest share (file 01).
  7. Hand over after one to three hours: by then half-spreads have converged to ~1c [1]. Leave, or pass the market to the steady-state engine (file 02).
- **What creates the edge**: A structural gap in the first minutes. Polymarket creates every market with "no inherited orders, no assigned market maker, and no opening auction" [1]. The first quotes sit far from where the market soon trades, and the first taker pays the visible book almost one-for-one (execution ratio 1.00) [1]. On the other side are early takers: some are uninformed enthusiasts (economy), many are people who know where the price should be (politics, geopolitics). Uninformed early takers keep paying because they want to be first. In the categories with low R/E, the maker is the one paying, and the edge exists only with a good seed or strict size limits.
- **Capital required**: <$1k-$10k. Per-market exposure is small (5-share minimum [E1]; $20-200 a side is enough in a new market), and capital recycles when you hand markets over after 1-3 hours. Fills you choose to carry lock capital to resolution.
- **Technical requirements**: (1) Data in: WebSocket `new_market` events, Gamma keyset pagination (limit 100 [E1]), market rules and neg-risk flags, reward configs (`/rewards/markets/{condition_id}`), and seeds (Kalshi public API, Deribit or CME option chains, family base rates, optional LLM). (2) Decision logic: category classifier; seed plus uncertainty width; size ladder by category R/E; toxicity triggers (size of the first takers, one-sided sweeps); handover rule by age and spread. (3) Execution: post-only, fast cancel-replace, heartbeat; tick-size handling (0.01, becoming 0.001 near the extremes) [E1]. (4) Risk: per-market cap, per-category daily loss cap, hard stops for augmented neg-risk "Other" legs. (5) Test: replay on the open genesis-window order-book dataset (Dome snapshots, Oct 2025-Apr 2026) [1][E1] plus a fresh post-fee recording. Build: 2-4 weeks for a solo developer with an existing quoting engine; the seed and classifier are the work.
- **Opportunity size**: Measured rent per share, fee-free era, first six minutes, one-hour horizon [1]:

| Category | Median effective half-spread | Realised (maker keeps) | Price impact | R/E | N markets |
|---|---|---|---|---|---|
| Economy | 3.50c | 3.00c | 2.00c | 0.86 | 221 |
| Politics | 10.00c | 3.50c | 4.00c | 0.35 | 1,021 |
| Geopolitics | 12.00c | 3.00c | 5.00c | 0.25 | 1,864 |
| Elections | 5.00c | 1.45c | 3.50c | 0.29 | 981 |
| Crypto (non-recurring) | 6.50c | 3.50c | 1.50c | 0.54 | 677 |
| Other | 7.50c | 2.50c | 3.50c | 0.33 | 2,045 |
| Sports | 1.00c | 1.00c | 0.00c | 1.00 | 48,908 |

  Components are category medians, so they need not sum. A maker filled early keeps a median 1.5-3.5c/share outside sports, with wide dispersion (P25-P75 roughly -1.5c to +12.5c in politics). The rent sits in the first hour: first-minute half-spreads of 12-16c become 3-6.5c at 1-6 minutes and ~1c at 1-3 hours [1]. Live on 24 Sep 2026: among the newest ~1,000 non-sports markets, mid-priced markets showed a median quoted full spread of 5c under six hours old and 13c at 6-24 hours [3]. That is a snapshot of quotes, not trades. Direction: likely shrinking as rebates and reward configs pull quotes toward the mid, as the authors predict; not yet re-measured.
- **Pros**: A measured, category-specific rent; tiny per-market capital and fast recycling; stacks with first-quoter reward share; no speed arms race in scheduled categories (economy); the output (a seeded fair value) feeds files 02 and 08.
- **Cons / risks**: Adverse selection is two thirds of the cost in politics and geopolitics [1]. Informed first takers are exactly who shows up early in those markets (1,950 suspected insider accounts [E4]). The evidence predates fees, so rebate-driven competition may already have compressed opening spreads. Rules are least tested in new markets: clarifications arrive before the first proposal in 83% of cases [E3], and augmented neg-risk "Other" legs change meaning as placeholders are named [E1]. Discovery at 300k markets a month is an engineering load, and 99% of listings are templates you will skip [2].
- **Expected results**: no public data for a genesis-window maker's PnL, theoretical only. Reasoned range (guess): fills of 30-150 shares in 20-60 non-sports new markets a day, keeping a median 2-3c realised on half of them and losing on informed first takers, gives $10-60/day gross before rewards. Rewards add first-quoter share on configs of $10-1,000/day (file 01). Net could be negative in politics and geopolitics if seeds are poor. The one self-reported number ("80-200% annualised in new markets", 2025) predates fees and the 2026 competition [E4].
- **Competitive landscape**: Thin but not empty. Reward farmers and generic makers join within the first hour, which is why spreads converge by 1-3 hours [1]. Nobody is known to specialise in the first minutes; poly-maker and similar bots discover markets by polling rather than on the `new_market` event [E6]. Being competitive takes event-driven discovery (seconds), a good seed and category-aware sizing.
- **Regulatory/ethical flag**: none for quoting (E9: two-sided LP from one identity is Allowed). Trading on non-public knowledge of the event behind a new market (for example employees of the organisation being forecast) is prohibited under the insider prongs of ToS §4.2 [E9].
- **How you'd validate it**: 1) Re-measure after the fee change: for 14 days, record the first 3 hours of every new non-sports market (WebSocket book plus `OrderFilled`). Compute effective and realised half-spreads by bucket and category, exactly as in [1]. 2) Paper-quote your seed ± width with the category size ladder. 3) Pass: realised half-spread ≥ 1.5c and R/E ≥ 0.5 in at least two categories over 300+ early fills, and simulated net positive after worst-decile first-taker losses. Fail: post-fee opening spreads already below 3c in the first minute, which means rebates competed the rent away. Cost: ~25 engineering hours, no capital; the pre-fee baseline is free on Hugging Face [1].

### Speed and execution sensitivity
- **Speed class**: latency-sensitive. First-minute half-spreads (12-16c) halve within 1-6 minutes [1], so the rent belongs to whoever is quoting in the first seconds to minutes. It is not a millisecond race: no known competitor specialises in the opening, and polling bots arrive later.

| Part of the strategy | What it depends on | If you are slower or execute worse | Realistic target for a solo team |
|---|---|---|---|
| Discovery | WebSocket `new_market` vs Gamma polling | the first-minute rent (12-16c) is gone by minute six (3-6.5c) [1] | seconds from creation to first quote |
| Seed fair value | cross-listed prices, options, base rates, LLM prior | a wrong seed sells the informed first taker a free option; that is the 65-75% of cost that is price impact in politics [1] | seed ready within 30 s; LLM prior within 10-30 s |
| Tightening | reading early trades | stay wide too long and you miss the fills; tighten too fast and you are picked off | re-quote each fill |
| Handover | age and spread rules | quoting a converged market at genesis size is plain market making (file 02) | exit at 1-3 hours |

- **How speed changes the result**: (1) Minute zero to minute one is worth ~3x minutes one to six in half-spread terms [1]. (2) An LLM seed that takes 30-60 s arrives after the richest minute; deterministic seeds should quote first, and the LLM should adjust the width later. (3) Rewards sample once a minute, so being in band from the first minute of a config earns share before competitors arrive [E2].
- **Where to run it**: eu-west-1 is helpful but not decisive; a VPS anywhere unrestricted with a persistent WebSocket works. Do not host in the UK or US [E9].

### Results by investment size
Assumptions: post-fee rents at half the fee-free medians; 20-60 non-sports new markets quoted a day; fills of 30-150 shares per market; 10-20% of markets producing an informed-first-taker loss of 5-10c per filled share; first-quoter reward share ignored (upside). All figures are guesses.

| Capital | Workable? | How it is deployed | Gross / month | Running costs / month | Net / month | Net / capital / month | Binding constraint |
|---|---|---|---|---|---|---|---|
| $1k | yes | 10-20 new markets a day, $20-50 a side, exit after 1-3 h | $60-250 | $10-30 (small VPS; free APIs; LLM calls optional) | $0-$200 | 0-20% | size per market is too small to matter in economy markets |
| $5k | yes | 30-50 markets a day, $50-150 a side, carry only seeded winners | $300-1,000 | $30-100 | $100-$800 | 2-16% | informed first takers in politics and geopolitics |
| $10k | yes | 50-80 markets a day plus reward-pool farming on the same listings | $500-1,800 | $70-150 | $200-$1,500 | 2-15% | number of genuinely new non-template listings per day |

- **Minimum sensible capital**: ~$1k. Per-market exposure is tiny and positions recycle within hours.
- **Capacity ceiling**: ~$20k-$50k (guess). The rent is per new market and per share of early flow, not per dollar deployed, and early takers trade small.

### APIs, data and third-party services
| Service | What for | Needed? | Cost | Access / jurisdiction notes |
|---|---|---|---|---|
| CLOB market WebSocket (`new_market`, book, trades) | discovery in seconds, early fills | required | free | `custom_feature_enabled` for `new_market` [E1] |
| Gamma API (keyset events and markets, rules, neg-risk flags) | metadata, category, rules | required | free | limit 100 per page [E1] |
| CLOB rewards endpoints | reward configs attached at listing | recommended | free | configs appear within hours of listing [3] |
| Kalshi public API | seed from cross-listed markets | optional | free market data; trading needs KYC [E5] | ~6% of events are cross-listed across venues [E5] |
| Deribit public API / CME data | seeds for price-threshold listings | optional | Deribit market data free without auth (own query [4]); CME data paid (unverified) | Deribit trading not open to US persons (unverified) |
| LLM API | prior and rule parsing for one-off questions | optional | pay per call | only after deterministic seeds |
| Genesis-window book snapshots (Hugging Face, Dome data, Oct 2025-Apr 2026) | pre-fee baseline replay | recommended | free [1] | Dome itself was acquired by Polymarket and discontinued 28 Apr 2026 [1][E6] |
| Hosting | runtime | required | $10-20/month small VPS; ~$65/month c7i.large list [5] | not UK or US |

- **Monthly running cost**: minimum ~$10-20; comfortable ~$100-150 (Dublin VPS plus LLM calls on the few dozen markets a day you actually quote).

### Related files
- 01-maker-reward-pool-farming.md: first-quoter share of reward configs attached at listing.
- 02-event-market-making-spread-carry.md: steady-state quoting after the handover.
- 08-cross-venue-leadlag-signals.md and 11-derivatives-implied-relative-value.md: seeds from other venues and option surfaces.
- 15-rules-dispute-trading.md and 64-rules-ambiguity-hazard-layer.md: rule risk, which is highest in new markets.
- 21-llm-forecasting-agents.md: the LLM prior as a seed.
- 58-market-anchored-selective-deference.md: day-zero quoting of LLM residuals.

### Sources
[1] https://dspace.networks.imdea.org/bitstream/handle/20.500.12761/2065/Polymarket_Initial_Liquidity-3.pdf?sequence=1 - Jornell, Perez (Lund) and Saguillo (IMDEA Networks), "Opening Wide, Moving Fast: Polymarket Spread Dynamics" - 2026, PDF fetched and text-extracted 2026-09-24 - ~160,000 contracts, Oct 2025-29 Mar 2026; Table 2 opening quoted spreads (sports 3c, politics 8c, geopolitics 10c, elections and monetary policy 13c, other 14c, crypto 19c, economy 21c); Table 9 median effective half-spread by bucket (<1 min: monetary policy 14.5, economy 12.0, geopolitics 16.0, politics 13.5, elections 13.5, sports 1.5, crypto 12.5, other 14.0c; ~1c by 1-3 h); Table 6 R/E decomposition; execution ratio 1.00; sample ends "one day before Fee Structure V2"; conclusion: rebates "should compress opening spreads and push the R/E ratio upward"; open dataset at huggingface.co/datasets/vpcapitano/polymarket-genesis-liquidity; Dome coverage 14 Oct 2025-28 Apr 2026.
[2] https://gamma-api.polymarket.com/markets?order=createdAt&ascending=false - Polymarket Gamma API - own query 2026-09-24 21:27 UTC - the 1,100 newest markets were created between 21:17:33 and 21:27:37 UTC; 1,060 sports, 40 crypto up/down.
[3] https://gamma-api.polymarket.com/events?tag_slug={politics,geopolitics,tech,culture,economy,mentions,weather,finance,world,elections}&order=createdAt&ascending=false and https://clob.polymarket.com/rewards/markets/current - Polymarket APIs - own query 2026-09-24 ~21:30 UTC (100 newest events per tag) - markets under 6 h old: 72, of which 53 had reward configs worth $6,365/day; median quoted full spread for mids 0.10-0.90 among non-empty books: 5.0c (<6 h, n=43), 13.0c (6-24 h, n=455), 10.1c (24-72 h), 5.0c (>7 days).
[4] https://www.deribit.com/api/v2/public/get_book_summary_by_currency?currency=BTC&kind=option - Deribit public API - own query 2026-09-24 - option marks and IVs returned without authentication.
[5] https://instances.vantage.sh/aws/ec2/c7i.large - Vantage - fetched 2026-09-24 - $0.089/h list price.
[E1] Evidence pack E1 - `new_market` WebSocket event, keyset pagination, ~305k new markets per month (The Block), tick sizes, 5-share minimum, neg-risk augmented "Other".
[E2] Evidence pack E2 - reward sampling per minute, first-quoter dynamics (Telonex sponsored-pool case).
[E3] Evidence pack E3 - 83.34% of clarifications arrive after request creation but before the first proposal.
[E4] Evidence pack E4 - "80-200% annualised in new markets" (PANews, @defiance_cr, self-reported, 2025-era); 1,950 suspected insider accounts.
[E5] Evidence pack E5 - ~6% of events cross-listed; Kalshi international access.
[E6] Evidence pack E6 - Dome acquisition (2026-02-19); discovery in open-source bots.
[E9] Evidence pack E9 - traffic-light table, insider prongs, restricted jurisdictions.
