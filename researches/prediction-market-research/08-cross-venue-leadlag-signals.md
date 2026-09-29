# 08 - Cross-venue lead-lag: follower quoting and price-discovery signals
_Band: established-emerging · Evidence grade: B-C (one election-era paper, a dataset paper with a null trading result, practitioner self-reports; A for live cross-venue quotes and endpoints) · Last verified: 2026-09-24_

### Cross-venue lead-lag: follower quoting and price-discovery signals
- **One-line summary**: Use the deeper or faster venue (Kalshi, the Polymarket US book, sharp sportsbooks, Binance, option markets) as a real-time fair-value input for trading or quoting on Polymarket international only. You need no capital on the second venue and never hold a locked two-leg position.
- **Category**: Arbitrage [statistical, single-venue execution; locked structures are file 07]
- **Maturity**: Emerging. The mechanism is documented but the profit is not. In the 2024 election, Polymarket led Kalshi in price discovery and large-trade imbalance predicted returns [1] (abstract only). A practitioner reports Kalshi sports depth of 30-50k contracts against 5-10k on Polymarket, with the follower repricing "within 2-3 seconds" [2] (self-reported). In crypto, Polymarket quotes respond to large Binance moves after a median 347 ms, yet a walk-forward model built on exactly that lag lost -0.116 payoff units per attempted trade out of sample [3]. Live on 24 Sep 2026, pre-game NFL moneylines matched within one tick on all three venues [4][5][6]: the slow pre-game signal is gone in liquid sports.
- **Requires AI?**: optional. Pair matching and a news-relevance filter (is the leader's move semantically about this market?) can use embeddings and an LLM. The lead-lag model itself is statistical: cross-correlations, a Hasbrouck information share, and a Kalman-filtered fair value.
- **How it works (simple flow)**:
  1. Pick pairs where another venue is plausibly faster or deeper: Kalshi or the US book for US sports and macro; sharp books for pre-game sports; Binance and Deribit for crypto thresholds; CME FedWatch or fed funds futures for FOMC markets (a model output, not tradable) [E5].
  2. Measure who leads, per category and per regime: lagged cross-correlation of mid changes at 250 ms to 60 s horizons, information share, and the decay of the gap (half-life).
  3. Fair value for Polymarket = a weighted blend of the leader's mid (adjusted for tick size, fees and rules) and Polymarket's own microprice.
  4. Express it as a maker (preferred): skew and centre your Polymarket quotes on the blended fair value, pull on leader jumps, and earn the rebate instead of paying the taker fee.
  5. Or as a taker (selectively): hit stale Polymarket quotes when the leader has moved by more than fee + half-spread + delay risk. Sports taker orders wait 1 s and crypto 150 ms, and cannot be cancelled while pending [7].
  6. Exit on convergence or a time stop. There is no second-venue leg to unwind.
- **What creates the edge**: Segmented crowds and uneven depth. Kalshi carried 71.5% of July 2026 volume and 80% of it is sports [E5], so it has more participants re-pricing US sports and macro. The US book is a separate, KYC'd crowd trading in half-cent ticks [5]. Option markets are professionally arbitraged [E5]. On the other side are Polymarket makers and takers who price only Polymarket's book. Stale resting quotes are the counterparty for the taker version; uninformed takers who cross your better-centred quotes are the counterparty for the maker version.
- **Capital required**: <$1k-$10k on Polymarket only. Positions are short-horizon (seconds to hours) for the taker variant; maker inventory follows file 02 rules. There is no capital on the leader venue, only data access.
- **Technical requirements**: (1) Data in: Polymarket CLOB WebSocket; Kalshi market data (public, no auth for reads [6]); the Polymarket US public gateway BBO (no auth [5]); odds feeds; Binance and Deribit public feeds; on-chain `OrderFilled` for signed large-trade flow. (2) Decision logic: pair map and rules adjustments; timestamp alignment (venue clocks can differ; OpenMarket found a 16 ms median source-clock lag with ±99 ms offset ambiguity [3]); rolling lead-lag estimates; a blended fair value; trade and quote rules net of fees and delays. (3) Execution: the maker engine of file 02, or FOK/FAK taker orders with delay-aware sizing. (4) Risk: stop when the leader diverges beyond a rules-explained threshold, since a big gap can mean the leader is distorted [8]. (5) Test: recorded multi-venue books. Build: 2-4 weeks for a solo developer with existing Polymarket and Kalshi clients.
- **Opportunity size**: Hard to size. The documented lag magnitudes: 2-3 s in US sports (self-reported) [2], 347 ms median in BTC 15-minute markets [3], an option-implied gap with a ~4 h half-life for BTC thresholds in 2023 [E5]. Practitioners report occasional 5-8c gaps on identical outcomes [9] (self-reported). Where the signal meets the most retail flow (live sports, macro prints, crypto), fast makers already quote at one tick and three venues agree pre-game [4][5][6]. Direction: shrinking in liquid markets as makers link the books; persistent in thin Polymarket markets whose Kalshi or options equivalent is deep.
- **Pros**: Single-venue capital; the leader's data is free; it improves any quoting engine even without a standalone taker strategy; no rule-mismatch settlement risk because you never hold the other leg.
- **Cons / risks**: Lead-lag can flip (Polymarket led in 2024 [1]; Kalshi is now much larger [E5]). Taker delays mean the Polymarket makers you try to hit can cancel inside your 1 s or 150 ms delay while you cannot [7], so you get filled when they did not cancel, which is adverse selection. Rules differences create divergences that are not lead-lag: deadline snapshot times, index methodology [E5]. The leader may be distorted: the 2024 "French whale" pushed Polymarket 10-15 points above competitors [8]. Data terms: Polymarket US app market data is "personal, non-commercial" [E9], so commercial use of the US gateway feed is grey.
- **Expected results**: no public data on realised lead-lag PnL, theoretical only. The one systematic attempt with published results (Binance to BTC 15-minute) lost out of sample [3]. Guess: as a maker overlay, the benefit shows up as fewer adverse fills, perhaps 10-30% lower markout losses in linked markets. As a standalone taker strategy, near zero after fees in liquid pairs; small positive (tens to low hundreds of dollars a month) in thin Polymarket markets with deep Kalshi equivalents.
- **Competitive landscape**: Institutional makers link the books (Wintermute moves capital between venues [10]); crypto makers react in a few hundred milliseconds [3]; sports makers quote off sharp lines (file 04). The follower edge is left mainly in thin Polymarket markets and in the minutes after unusual news, where pair matching and rules knowledge matter more than speed.
- **Regulatory/ethical flag**: none for using public data from other venues to trade Polymarket international as a non-restricted person (E9: trading on own research, models and speed is Allowed). Grey: commercial use of Polymarket US market data (US app ToS) and, for incorporated traders, the international ToS clause on "Capital Market Clients" using Polymarket Data [E9]. The international-vs-US book gap is a signal only: one person may not hold both books [E9].
- **How you'd validate it**: 1) Record Polymarket, Kalshi and US-book top of book for 30-50 matched markets for 2 weeks, with synchronised clocks. 2) Estimate lead-lag by category (sports pre-game, in-play, macro, politics) at 0.25-60 s; compute the Polymarket-only follower PnL under three executions (taker with delay, maker skew, no-trade baseline) net of fees. 3) Pass: positive net follower PnL in at least one category over 500+ signals with a t-stat > 2, or ≥ 15% reduction in maker markout losses in paper quoting. Fail: all gains vanish once delay and fee are applied. Cost: ~25 engineering hours; free data.

### Speed and execution sensitivity
- **Speed class**: latency-sensitive. The measured lags are seconds (sports, self-reported) to a few hundred milliseconds (crypto) [2][3]. The venue's taker delay decides whether the taker version is even possible.

| Part of the strategy | What it depends on | If you are slower or execute worse | Realistic target for a solo team |
|---|---|---|---|
| Leader feed | Kalshi WS / REST, US gateway, Binance, odds push feeds | the lag you measure is someone else's profit | <100 ms feed latency from Dublin (crypto); <500 ms (sports) |
| Clock alignment | NTP/PTP, venue timestamps | false lead-lag signals; ±99 ms offset ambiguity in one dataset [3] | log local receive and venue timestamps |
| Taker execution on Polymarket | taker delay: 1 s sports, 150 ms crypto, 250 ms some finance [7] | makers cancel inside your delay; you fill mostly when wrong | prefer maker expression |
| Maker quote centring | cancel-replace on leader moves | stale quotes filled by other followers | <300 ms re-centre after a leader jump |

- **How speed changes the result**: (1) Sports pre-game: no measurable lag left on main lines [4][5][6]; speed buys nothing. (2) In play and crypto: sub-second, and you race co-located makers [3][E1]. (3) The Polymarket delay favours the maker side: a follower who quotes rather than takes gets the free cancel window instead of paying for it [7].
- **Where to run it**: AWS eu-west-1 for Polymarket execution. Leader feeds arrive over the internet; place a second listener near the leader only if measurement shows it pays.

### Results by investment size
Assumptions: Polymarket-only capital; maker overlay on 20-60 linked markets plus selective taking in thin markets; gains measured as avoided markout losses plus a small taker PnL. All figures are guesses.

| Capital | Workable? | How it is deployed | Gross / month | Running costs / month | Net / month | Net / capital / month | Binding constraint |
|---|---|---|---|---|---|---|---|
| $1k | yes | taker clips of $20-100 in thin Polymarket markets with deep Kalshi twins | $0-$100 | $10-70 | -$50 to +$60 | -5% to +6% | fees and 1 s sports delay on small clips |
| $5k | yes | maker overlay on 20-30 markets plus selective taking | $50-$400 | $70-150 | -$100 to +$300 | -2% to +6% | lead-lag instability by category |
| $10k | yes | maker overlay on 40-60 markets, larger clips on thin twins | $100-$700 | $70-250 | -$150 to +$500 | -1.5% to +5% | liquidity in the thin markets where the lag persists |

- **Minimum sensible capital**: ~$1k. The signal is free and clips are small.
- **Capacity ceiling**: ~$25k-$50k (guess). The lag persists only where Polymarket depth is thin.

### APIs, data and third-party services
| Service | What for | Needed? | Cost | Access / jurisdiction notes |
|---|---|---|---|---|
| Kalshi market data (REST / WebSocket) | leader prices and depth | required for US sports / macro | free; reads need no auth (own query [6]); trading not needed | rate tiers Basic 200/100 tokens/s [11] |
| Polymarket US public gateway (`/v1/markets/{slug}/bbo`) | second crowd's BBO in half-cent ticks | optional | free, no auth [5] | app data terms say "personal, non-commercial" [E9]: grey for commercial use |
| Polymarket CLOB + Gamma (international) | execution, rules | required | free | not for US, UK or other restricted persons [E9] |
| Sportsbook odds feed | pre-game sports leader | optional | The Odds API $30-249/month [12] | licensed feed |
| Binance spot WebSocket / PolyBolt | crypto leader, settlement reference | optional | free; PolyBolt needs CLOB credentials [7] | Binance's global API refuses US IPs (not re-checked) |
| Deribit public API | option-implied leader for crypto thresholds | optional | free, no auth (own query [13]) | see file 11 |
| Kalshi historical candlesticks (1-minute, public) | backtest lead-lag | recommended | free [E5] | bid/ask OHLC |
| Polymarket + Kalshi trades dataset (Jon Becker, ~36 GiB Parquet, MIT) | historical study | optional | free [E5] | trades, not books |
| Hosting | runtime | required | ~$65-100/month eu-west-1 [14] | not UK or US |

- **Monthly running cost**: minimum ~$10-70 (VPS, free feeds); comfortable ~$150-300 (Dublin VPS, odds feed, storage for recorded books).

### What you are probably underestimating
1. **The famous lead-lag result is from one election.** Polymarket led Kalshi in 2024 [1]. By July 2026 Kalshi had 71.5% of volume and 80% sports [E5], so leadership has plausibly flipped by category. Measure it; do not inherit it.
2. **The free signals are free for everyone.** Kalshi market data and the Polymarket US BBO need no auth [5][6], and scanners and open-source bots already consume them [E5]. On 24 Sep four NFL games matched across three venues within a tick [4][5][6].
3. **Tick sizes manufacture fake gaps.** The US book quotes in 0.005 steps (0.265/0.270) while the international book uses 0.01 (0.27/0.28) on the same game [4][5]. A half-cent "lead" is often just the finer grid. Compare mids adjusted to tick, not last trades.
4. **The taker delay makes stale-quote picking adverse by construction.** Your marketable order waits 1 s in sports and 150 ms in crypto and cannot be cancelled, while the makers you are hitting can cancel [7]. You fill mostly when they did not bother, which is when you are wrong. Put the signal into your quotes, not your taker orders.
5. **A measured lag is not a profit.** The OpenMarket author measured a 347 ms Binance-to-Polymarket response and built the data to trade it. The model underperformed the market's implied probability out of sample [3].
6. **Flow signals need corrected turnover.** Naive volume overstated turnover by 2.45x in one study (median 3.08x): $9.1M of corrected flow moved the October Trump contract 5 points against a naive $15.6M estimate [15]. The public feed also mislabels trade direction ~41% of the time [E1]. Build flow signals from `OrderFilled` and dedupe.
7. **The leader can be the distorted venue.** The 2024 French whale kept Polymarket 10-15 points above other venues for weeks [8]. A follower who copied it into thinner books lost when it converged. Cap how far you follow a leader that is off consensus.
8. **Rule differences look like lead-lag near deadlines.** Kalshi's morning-ET snapshots against Polymarket's 11:59 p.m. ET [E5], and Binance-candle vs CF-RTI crypto settlement [E5][16], create predictable divergences at the end. Exclude the last hours before a deadline from any lead-lag estimate.
9. **Data licences bite when you incorporate.** Once you trade through a company, the international ToS restricts use of Polymarket Data by "proprietary trading firms", including on-chain data, without a written agreement. The US app ToS makes market data personal and non-commercial [E9]. A solo individual is fine; a fund is not automatically.

### Related files
- 07-cross-venue-locked-arbitrage.md: locked two-leg structures across the same venues.
- 02-event-market-making-spread-carry.md: the quoting engine this signal feeds.
- 04-sportsbook-anchored-sports-mm.md: sportsbooks as the pre-game sports leader.
- 11-derivatives-implied-relative-value.md: option markets as the leader for price thresholds.
- 12-short-crypto-latency-taker.md and 18-sports-inplay-feed-latency-taking.md: the pure-latency taker versions.
- 27-whale-informed-flow-tracking.md: large-trade flow as a within-venue leader.
- 78-two-book-crowd-differential.md: the US vs international crowd as a sentiment index (speculative).
- 81-flow-fading-and-leadlag-statarb.md: experimental stat-arb on lead-lag between related contracts.

### Sources
[1] https://doi.org/10.2139/ssrn.5331995 - SSRN, Ng, Peng, Tao, Zhou - 2025-07-01 (abstract via the brief and E5 [43]; SSRN blocks automated fetches) - Polymarket led Kalshi in price discovery before the 2024 election, especially when liquidity and activity were high; net large-trade imbalance predicts subsequent returns.
[2] https://hn.algolia.com/api/v1/items/47500591 - Hacker News comment (sharp_runner_84) - 2026-03-24, fetched 2026-09-24 - "30-50k of depth on Kalshi vs 5-10k on Poly for the same contract"; "the other follows within 2-3 seconds". Self-reported.
[3] https://arxiv.org/abs/2607.26245 - arXiv, G. Young, OpenMarket - 2026-07-28, fetched 2026-09-24 - median 347 ms quote response to large Binance moves; 16 ms median source-clock lag, ±99 ms offset ambiguity; walk-forward model -0.116 payoff units per attempted trade; null out-of-sample result.
[4] https://gamma-api.polymarket.com/events?tag_slug=nfl - Polymarket Gamma API - own query 2026-09-24 ~21:30 UTC - NYJ-DET 0.27/0.28, SEA-WAS 0.75/0.76, CIN-PIT 0.62/0.63, KC-MIA 0.84/0.85.
[5] https://gateway.polymarket.us/v1/markets/aec-nfl-nyj-det-2026-09-27/bbo - Polymarket US public gateway - own query 2026-09-24 - 0.2650 / 0.2700 (half-cent ticks); SEA-WAS 0.750/0.755; CIN-PIT 0.625/0.630; KC-MIA 0.850/0.855; no authentication.
[6] https://api.elections.kalshi.com/trade-api/v2/markets?series_ticker=KXNFLGAME&status=open - Kalshi public API - own query 2026-09-24, no authentication - NYJ 0.27/0.28, SEA 0.75/0.76, CIN 0.62/0.63, KC 0.85/0.86.
[7] https://docs.polymarket.com/changelog/predictions.md and https://docs.polymarket.com/concepts/order-lifecycle.md - Polymarket docs - fetched 2026-09-24 - crypto taker delay 150 ms since 2026-09-04; sports delay windows (`secondsDelay` 1 on NFL and most sports markets per Gamma); pending orders cannot be cancelled; PolyBolt price WebSocket.
[8] https://doi.org/10.2139/ssrn.6670638 - SSRN, Abid - 2026 (via the brief; not fetched) - the 2024 French-whale episode: Polymarket 10-15 points above competitors.
[9] https://hn.algolia.com/api/v1/items/47500689 - Hacker News comment - 2026-03-24 (brief) - builder of a Kalshi-Polymarket discrepancy detector reports 5-8c spreads on identical outcomes. Self-reported.
[10] https://finance.yahoo.com/markets/crypto/articles/wintermute-providing-liquidity-kalshi-polymarket-162008202.html - Yahoo Finance - 2026-05-29 (brief) - institutional capital flows dynamically between both venues.
[11] https://docs.kalshi.com/getting_started/rate_limits - Kalshi docs - fetched 2026-09-24 - tiers and token costs.
[12] https://the-odds-api.com/ - The Odds API (vendor) - fetched 2026-09-24 - plans $0-249/month.
[13] https://www.deribit.com/api/v2/public/get_book_summary_by_currency?currency=BTC&kind=option - Deribit public API - own query 2026-09-24 - option marks returned without authentication.
[14] https://instances.vantage.sh/aws/ec2/c7i.large - Vantage - fetched 2026-09-24 - $0.089/h list price.
[15] https://arxiv.org/html/2603.03136v3 - arXiv - 2026-03-03 (via the brief) - ~$9.1M corrected flow moved the October Trump contract 5 points (naive $15.6M); $1M moved 4-15 points in January vs ~0.5 in October; naive volume overstates turnover 2.45x (median 3.08x).
[16] https://gamma-api.polymarket.com/events?slug=bitcoin-above-on-september-27-2026 - Polymarket Gamma API - own query 2026-09-24 - resolves on the Binance BTC/USDT 1-minute candle close at 12:00 ET.
[E1] Evidence pack E1 - public-feed direction ~59% accurate; co-location; delays.
[E5] Evidence pack E5 - venue shares (Kalshi 71.5% of July 2026), Kalshi 80% sports, deadline conventions, crypto settlement indices, historical data sources, scanners, FedWatch gap (snippet), option-implied BTC gap half-life.
[E9] Evidence pack E9 - traffic-light table, data-licence clauses (international ToS Capital Market Clients; US app "personal, non-commercial"), one person may not hold both books.
