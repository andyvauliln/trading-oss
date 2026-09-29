# 06 - Combos (parlay) RFQ market making
_Band: established-emerging · Evidence grade: A for mechanics (official docs, public catalog API); B for the parlay premium (one Kalshi paper); D for any outside maker's results on Polymarket · Last verified: 2026-09-24_

### Combos (parlay) RFQ market making
- **One-line summary**: Answer requests for quote on multi-leg sports parlays ("Combos") within 400 ms (200 ms on Polymarket US). Earn the premium that parlay buyers pay over the product of the leg prices, hedge the legs on the CLOB, and graduate to Last Look once you qualify.
- **Category**: Market-making [RFQ underwriting of correlated multi-leg payoffs]
- **Maturity**: Experimental for an outside maker. The product is live: international Combos launched ~10 June 2026 [3][4]; the US venue's beta did $7.4M from 5 August [5], and full launch reportedly did $31.4M in 24 hours, 21.6% of US volume [E1] (snippet). No non-Polymarket maker has been named anywhere, and Polymarket is reported to be building an in-house desk to trade RFQ parlays against customers [E4]. On Kalshi, parlay underwriting is an established desk business: $4.77B of parlay volume in May, $13.78B in July, and $25M of taker fees in the first 16 days of August [5].
- **Requires AI?**: no for pricing. Leg fair values come from the CLOB mids or sportsbook prices, and the joint probability from a correlation model. Optional: an LLM or simulation to estimate dependence between unusual leg pairs, which is speculative (file 66).
- **How it works (simple flow)**:
  1. A user builds a Combo from 2-50 mutually compatible legs (sports moneyline, spread and total today) and sends an unsigned request [1][2][E1].
  2. The RFQ system forwards it to connected makers. You have 400 ms to return a signed quote in pUSD per YES share [1][2].
  3. The best quote is shown and the user has 10 s to accept. If you have Last Look, you get up to 1 s to confirm or decline [1]. Makers rejecting more than 15% of selected quotes in an hour "may be paused from quoting for a few minutes" [2].
  4. Filling: from collateral (you effectively take the NO side at 1 minus the price; the SDK handles the token purchases) or from inventory [2].
  5. Pricing: the product of leg probabilities, adjusted for correlation. Same-game legs (team wins and team covers, or over and a star's points) are positively correlated, so the independent product understates the joint probability. Then add a markup that depends on leg count.
  6. Hedge: buy or sell legs on the CLOB, where a hedge exists and pays for its taker fee (0.05 in most sports; NFL and CFB game legs are fee-free [7]).
  7. Capital recycling: legs resolve one by one and positions compress. "Collateral Return" releases pUSD from offsetting Combo positions before resolution [E1].
- **What creates the edge**: Lottery demand. On Kalshi, 12,639 parlay trades from March to May 2026 were systematically priced above the product of their contemporaneous leg prices. The overpricing was ~0 for 2-4 legs, ~3.7% at 7 legs, ~22.3% at 10 legs and ~30.5% at 11 legs, while single legs were calibrated [6]. The brief's reading of the paper gives ~3% inflation per leg. On the other side is the recreational parlay buyer, who pays for a high multiplier and cannot easily compute the product of legs. They keep paying because parlays are entertainment, which is why sportsbooks push them. Few quoting engines exist on Polymarket, and Last Look is a free option against stale-leg picking.
- **Capital required**: $10k+. Selling a parlay locks capital against its maximum payout. Filling a $10 stake at price 0.01 locks ~$990 for a ~$2 expected premium at 20% overpricing (derived). Capital sits until the last leg resolves (hours to days for same-day sports), partly released by Collateral Return. Last Look needs ~$2,500 of Combo notional traded first [2].
- **Technical requirements**: (1) Data in: the RFQ WebSocket stream (AsyncAPI spec in the docs), CLOB mids for every leg, a sportsbook odds feed, and the public combo-legs catalog (`combos-rfq-api.polymarket.com/v1/rfq/combo-markets`, no auth) [8]. (2) Decision logic: leg fair values; a correlation model for same-game legs from historical joint outcomes; a leg-count markup schedule; exposure per game, team and player (one touchdown can complete hundreds of parlays); and a stale-leg guard that refuses to quote when a leg's mid moved in the last few seconds. (3) Execution: sign and return quotes in under 400 ms (under 200 ms on the US venue [9]), handle Last Look decisions, hedge legs post-fill with taker orders, and track Collateral Return. (4) Risk: max payout per game, correlated-cluster limits, a daily loss stop, pausing on feed divergence. (5) Test: listen-only logging of the request flow before quoting. Build: 4-8 weeks for a solo developer; the correlation model and exposure engine dominate.
- **Opportunity size**: Unknown in dollars internationally: no public combo volume figure was found. Leg universe on 24 Sep 2026: the public catalog listed at least 20,000 combo-able markets, essentially all sports, plus 131 politics and geopolitics markets flagged `pending` (a likely expansion beyond sports) [8]. On Polymarket US, full launch reportedly did $31.4M on day two, 21.6% of that venue's volume [E1] (search snippet); the beta did $7.4M volume, $928,093 of taker stakes and 16,173 trades in two weeks [5]. On Kalshi, combos are 36% of contracts traded [10] (partly paywalled) and parlay volume grew ~3x from May to July [5]. Direction: growing fast, with the maker side contested by Polymarket's own desk and sportsbook operators [5][E4].
- **Pros**: A documented, growing premium that increases with leg count; recreational counterparties; a hard deadline filters out slow competitors; Last Look gives optionality; it reuses sports fair values from file 04; the same engine runs on Kalshi.
- **Cons / risks**: Correlated same-game legs priced as independent are the classic parlay blow-up. Sharp requesters pick off stale leg prices inside 400 ms. Tail risk: one 10-leg hit pays ~1,000x the premium. Capital lock-up against maximum payout. Combo fees are not published in the fetched docs. Access is gated in practice: Last Look needs a relationship with Polymarket, and US-venue RFQ is institutional. You compete with a reported in-house Polymarket desk [E4].
- **Expected results**: no public data for any outside Combos maker on Polymarket, theoretical only. Anchor: at the Kalshi overpricing levels, a maker who quotes at the prevailing market level on 7-11-leg parlays earns ~4-30% of premium in expectation [6], before correlation errors and adverse selection. Guess: a solo maker with $10k-$25k of payout capacity and good correlation handling could net 1-3% of capacity a month, with drawdown months of -10% from correlated hits. Short parlays (2-4 legs) show ~0 premium [6] and should be quoted only as hedgeable flow.
- **Competitive landscape**: Early. Polymarket's in-house desk [E4]; sportsbook operators named as likely makers on the US venue [5]; on Kalshi, established desks (SIG, Jump, Kalshi Trading) [E5]. Being competitive takes precomputed leg fair values, sub-100 ms quote assembly, a same-game correlation model and a Last Look relationship.
- **Regulatory/ethical flag**: none for quoting from one identity on the international venue (E9: Allowed). Using Last Look to reject only losing fills systematically would likely breach the programme's expectations: makers "are expected to accept most selected quotes", with pauses above 15% rejections [2]. Polymarket US: institutional onboarding on a CFTC DCM, own-name funding, kill switches mandatory [E9].
- **How you'd validate it**: 1) Connect to the RFQ stream listen-only for 2 weeks. Log each request (legs, size) and, from fills, the winning price against the product of CLOB leg mids at request time, split by leg count and same-game vs cross-game. 2) Estimate the realised premium by leg count; replay your correlation model on the same requests. 3) Pass: realised premium over the correlation-adjusted fair value ≥ 5% on 5+ leg parlays across 500+ observed fills, and enough request flow ($5k+/day of stakes in your target segment) to diversify tails. Fail: winning quotes sit at the independent product (someone better is already quoting), or flow is too thin. Cost: ~30 engineering hours; no capital.

### Speed and execution sensitivity
- **Speed class**: latency-sensitive with a hard deadline. A quote that arrives after 400 ms (200 ms on the US venue) does not exist [1][9]. Within the window, what matters is precomputation and a stale-leg guard, not microseconds. Last Look (1 s) protects against legs that moved after you quoted [1].

| Part of the strategy | What it depends on | If you are slower or execute worse | Realistic target for a solo team |
|---|---|---|---|
| Quote assembly | precomputed leg fair values and correlation tables | missing the 400 ms window means zero fills | <100 ms from request to signed quote |
| Stale-leg guard | CLOB WebSocket for every leg | sharp requesters pick legs that just moved | refuse to quote if any leg moved in the last 2-5 s |
| Last Look decision | fresh leg prices at confirmation | declining too often (>15%/hour) gets you paused [2] | confirm or decline in <300 ms |
| Leg hedging | CLOB taker orders after the fill | unhedged exposure to correlated outcomes | hedge within seconds where a hedge is worth its fee |

- **How speed changes the result**: (1) The deadline is binary: slow quoters get nothing, and fast but careless quoters get picked off. (2) The US venue's 200 ms window and 3 s last look [9] favour co-located institutional makers.
- **Where to run it**: AWS eu-west-1 for the international venue. For the US venue, follow the institutional connectivity docs (gRPC); location unverified.

### Results by investment size
Assumptions: 5+ leg sports parlays only; payout capacity equals capital; realised premium 5-15% of stakes after correlation errors; stakes sold per month of 3-10% of capacity; heavy-tailed outcomes. All figures are guesses; no outside maker has published results.

| Capital | Workable? | How it is deployed | Gross / month | Running costs / month | Net / month | Net / capital / month | Binding constraint |
|---|---|---|---|---|---|---|---|
| $1k | no | one maximum-payout parlay would take the whole balance | n/a | n/a | n/a | n/a | payout capacity; Last Look needs ~$2.5k notional first [2] |
| $5k | marginal | quote only small stakes on 5-8 leg parlays; cap $250 payout per game | $0-$150 expected | $70-130 | -$1,000 to +$100 (tail-driven) | -20% to +2% | tails dominate; too few tickets to diversify |
| $10k | pilot | caps of $500 payout per game and $2k per slate; listen-only first | $50-$500 expected | $100-200 | -$1,500 to +$400 | -15% to +4% | correlated hits on one slate; competition from the in-house desk |
| Scale reference | where it becomes a business (guess) | $100k+ of payout capacity across all sports, Last Look | not public | n/a | n/a | n/a | Kalshi desks do this at billions of volume [5] |

- **Minimum sensible capital**: ~$25k of payout capacity (guess), to diversify across enough tickets that one slate cannot erase a month.
- **Capacity ceiling**: set by request flow in your segment and by same-slate correlation, not by capital, once above ~$250k (guess).

### APIs, data and third-party services
| Service | What for | Needed? | Cost | Access / jurisdiction notes |
|---|---|---|---|---|
| Combos RFQ API (`combos-rfq-api.polymarket.com`): public `/v1/rfq/combo-markets`, authenticated `/v1/maker/quotes`, `/v1/maker/confirmations` | leg catalog, quoting, Last Look | required | free | maker endpoints need CLOB credentials; Last Look via request form [2][8] |
| RFQ WebSocket (AsyncAPI spec) | incoming requests, trade broadcasts | required | free | 400 ms window [1] |
| CLOB REST + WebSockets | leg mids, hedging | required | free | not for US, UK or other restricted persons [E9] |
| Sportsbook odds feed | independent leg fair values; props | recommended | The Odds API $30-249/month [11]; push feeds from ~$99/month (vendor) | licensed feeds, not scraping |
| Historical joint outcomes (league stats) | same-game correlation model | required | free box scores / play-by-play for major leagues (source varies) | build once per sport |
| Kalshi public trade data | parlay-premium calibration | optional | free | the evidence base for the premium [6] |
| Polymarket US institutional RFQ (gRPC) | US Combos | optional | free API; institutional onboarding | KYC'd entity, CFTC DCM rules [E9] |
| Hosting | runtime | required | ~$65-100/month eu-west-1 [12] | not UK or US |

- **Monthly running cost**: minimum ~$100 (Dublin VPS + basic odds tier); comfortable ~$300 (faster odds feed, larger instance).

### Related files
- 04-sportsbook-anchored-sports-mm.md: leg fair values and sports rule mismatches (void, DNP).
- 10-combinatorial-logical-arbitrage.md: moneyline, spread and total consistency within one game; the single-market side of correlation.
- 66-dependence-pricing-combos-joint.md: LLM and simulation-derived dependence for unusual leg pairs (speculative).
- 32-builder-code-routing-business.md: builders requesting Combos for their users via the Builder Gateway.
- 28-taker-rebates-fee-tier-overlay.md: taker costs of hedging legs.

### Sources
[1] https://docs.polymarket.com/trading/combos/overview.md - Polymarket docs - undated, fetched 2026-09-24 - RFQ sequence: 400 ms quote window, 10 s acceptance, optional 1 s Last Look confirmation; Combo position IDs complementary to CLOB token IDs.
[2] https://docs.polymarket.com/trading/combos/market-makers.md - Polymarket docs - undated, fetched 2026-09-24 - Last Look for makers with "approximately $2,500 in Combo notional volume" and "an established line of communication with Polymarket"; >15% rejections over one hour "may be paused from quoting for a few minutes"; collateral or inventory sourcing; wallet must hold funds for fulfilling requests.
[3] https://cryptobriefing.com/polymarket-combo-trading-feature/ - Crypto Briefing - 2026-07-11, fetched 2026-09-24 - launch "around June 10-11", sports moneyline / spread / totals, competing market makers unnamed, no volume disclosed.
[4] https://finance.yahoo.com/markets/crypto/articles/polymarket-set-launch-combos-sports-094405317.html - Yahoo Finance - 2026-06 (via E1 [64], S) - Combos launch announcement.
[5] https://news.bitcoin.com/igaming/polymarket-us-tests-parlays-as-kalshi-banks-25m-in-fees/ - Bitcoin.com News - 2026-08-19, fetched 2026-09-24 - US parlay beta from 2026-08-05: $7.4M volume, $928,093 taker stakes, 16,173 trades, 2-10 legs; offshore launch 2026-06-10; Kalshi parlay volume $4.77B (May) and $13.78B (July), $25M taker fees in the first 16 days of August; sportsbook operators as possible makers.
[6] https://arxiv.org/abs/2607.14430 - arXiv, N. Moshrefi, "Prices, Probabilities, and Parlays" - 2026-07-15, fetched 2026-09-24 - Kalshi, 12,639 parlay trades: overpricing ~3.7% at 7 legs, ~22.3% at 10, ~30.5% at 11; singles calibrated; the ~0 for 2-4 legs and ~3% per leg (beta 0.029, R2 0.94) are from the brief's reading of the HTML.
[7] https://gamma-api.polymarket.com/events?tag_slug=nfl - Polymarket Gamma API - own query 2026-09-24 - NFL and CFB game markets `zero_fees`; other sports 0.05 / rebate 0.15.
[8] https://combos-rfq-api.polymarket.com/v1/rfq/combo-markets (spec: https://docs.polymarket.com/api-spec/combos-rfq-openapi.yaml) - Polymarket Combos RFQ API - own query 2026-09-24 - public, no CLOB auth; the catalog returned 20,000 markets at the pagination cap (19,869 tagged sports) plus 131 politics / geopolitics markets flagged `pending`; maker endpoints authenticated.
[9] https://docs.polymarket.us/trader-guide/combos.md - Polymarket US docs - undated, fetched 2026-09-24 - quote submission 200 ms, maker last look 3 s, paired order delay 1 s; Drop Copy as source of truth for fills.
[10] https://news.bloomberglaw.com/securities-law/parlay-bets-are-burning-gamblers-as-market-takes-off-on-kalshi - Bloomberg Law - 2026-07-29 (brief; partly paywalled) - combos 36% of Kalshi contracts traded; retail buys longshot combinations.
[11] https://the-odds-api.com/ - The Odds API (vendor) - fetched 2026-09-24 - plans free / $30 / $59 / $119 / $249 per month.
[12] https://instances.vantage.sh/aws/ec2/c7i.large - Vantage - fetched 2026-09-24 - $0.089/h list price.
[E1] Evidence pack E1 - Combos RFQ timings and Collateral Return; US launch 2026-08-21 and "$31.4M in 24 h (21.6% of US volume)" (Yahoo / Bitget, search snippet).
[E4] Evidence pack E4 - Polymarket hiring an in-house team to trade RFQ parlays (CoinDesk, 2025-12-05).
[E5] Evidence pack E5 - Kalshi makers (SIG, Jump, Kalshi Trading).
[E9] Evidence pack E9 - traffic-light table; Polymarket US institutional and conduct rules.
