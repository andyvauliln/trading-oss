# Counterparty venues for cross-platform arbitrage and comparable data
_As of 2026-09-20. Evidence pack E5 for the Polymarket strategy survey._

Method: web research on 2026-09-20. `F` = page fetched this session, `S` = search snippet only (page blocked or not opened). Tags: **[DOC]** official docs / filings, **[PAPER]**, **[DATA]**, **[PRESS]**, **[VENDOR]** affiliate / SEO / tool-seller content (lead, not proof). _own arithmetic_ = derived here from cited fee formulas. This agent completed 42 web searches before the session-wide search quota (200) was exhausted; later work used direct page fetches only, so several venues (Deribit, Betfair, Smarkets, Limitless, Myriad) rest on snippets; see "Could not verify".

## Key facts

1. **Polymarket is now the smaller venue.** July 2026 volume: Kalshi $38.65B (71.5%), Polymarket international $7.89B (~14.6%), Polymarket US $4.86B (~9%), every other venue <1% each; total $54.09B (Dune dashboard via Bitcoin.com) [16]. Any "Polymarket leads price discovery" result predates this (it is from the 2024 election [43]).
2. **Polymarket US and Polymarket international are separate books, balances, fees, APIs and legal entities** (QCX LLC, a CFTC DCM, vs the Polygon venue) [15][13]. Polymarket's own geoblock list puts the US, UK, France, Germany and Australia among 35 close-only jurisdictions on frontend and API [6].
3. **Fee band at 50c is ~3c per $1 pair, taker/taker.** Polymarket intl taker = `r*p*(1-p)`, r = 0.07 crypto, 0.05 sports/economics/culture/weather/other, 0.04 politics/finance/tech/mentions, 0 geopolitics; makers pay 0 [1]. Kalshi taker = `ceil(0.07*p*(1-p)*100)/100`, maker about a quarter of that where charged [17]. Polymarket US taker coefficient 0.0695, maker rebate 0.0125 (effective 2026-09-17) [7]. At p=0.5: 1.25c + 1.75c = 3.0c for a sports pair (_own arithmetic_).
4. **Polymarket sports taker coefficient went 0.03 -> 0.05 and sports maker rebate 25% -> 15% on 2026-07-10**; fees were extended to 10 categories on 2026-03-30 [2]. Most blog numbers are stale.
5. **Collateral is pUSD, not USDC.e, since CLOB V2 (2026-04-28)** [2][3]. Withdrawals unwrap pUSD and swap via Uniswap v3 with a <10 bp tolerance; docs advise splitting withdrawals above $50,000 [4].
6. **An independent 20-second collector (Sept 2026) found nearly all Kalshi-Polymarket mid-price divergence disappears after fees and depth**: a 1c executable crossing on ~119,000 La Liga contracts loses ~$957 after fees; a 3c BTC-threshold gap shrinks to 2c after walking depth against 2.07c of fees [46] **[DATA, tiny sample: 2 pairs, ~48k rows]**.
7. **Academic evidence says gaps are large and persistent, but mostly where contracts are not truly identical**: across 100,000+ events on 10 venues (2018-2025) ~6% of events overlap; median deviation 2-4% from execution-adjusted parity; pre-election spreads averaged ~$0.03, up to $0.07 for sustained intervals; the authors name the cause "semantic non-fungibility" [44] **[PAPER]**.
8. **Same event, opposite payouts, twice in Q1 2026.** Cardi B Super Bowl: Kalshi invoked Rule 6.3(c) and settled at last trade ($0.26 YES / $0.74 NO); Polymarket resolved YES at $1.00; $47.3M and $10M+ volume [53]. Khamenei: Kalshi applied a death carve-out and paid last-traded price [54][55]; Polymarket's YES ($1.00) proposal was disputed twice and went to UMA final review [55][56]; the final vote was not confirmed this session.
9. **Kalshi's deadline convention is a morning-ET snapshot; Polymarket's is typically 11:59 p.m. ET**, a ~13-hour window in the January 2026 funding-deadline pair [52].
10. **Crypto short-dated markets settle on different indices**: Polymarket on a Chainlink TWAP (60 s window for 5-min since 2026-08-14, 60 s for 15-min and 4-hour) [2][58]; Kalshi on the average of 60 one-second CF Benchmarks RTI prints [22].
11. **Kalshi is reachable from 140+ countries since October 2025 with mandatory KYC**; international users fund by debit card, wire (min $1,000) or crypto and withdraw by debit card or crypto only [21]. UK, Canada, France and Australia are reported excluded [29] **[VENDOR, S]**.
12. **Position caps**: Polymarket US has no position limit, a $25,000-notional accountability level and 100% margin [14][8][10]; Kalshi moved most markets to accountability levels in Nov 2024, with e.g. $7,000,000 per strike on congressional-control contracts [24]; PredictIt $3,500 per contract [69].
13. **PredictIt charges 10% of profit plus 5% of every withdrawal (principal included)** [69]; as an arb leg it is effectively one-way capital.
14. **US tax year 2026 caps gambling-loss deductions at 90%**; the IRS has issued no prediction-market guidance, so the two legs of one arb can fall under different regimes [74].
15. **Crowding**: GitHub repository search for "polymarket kalshi arbitrage" returned 301 repositories on 2026-09-20; pmxt ("CCXT for prediction markets", created 2026-01) has 2,158 stars [51]. Paid scanners refresh every 30 s to real time [49][50].

## Venue by venue

### Kalshi (KalshiEX, CFTC DCM + DCO)
- **Fees** [DOC/VENDOR]: taker `ceil(0.07*P*(1-P)*100)/100` per contract; maker ~`0.0175*P*(1-P)` on markets that carry maker fees [17]. Kalshi's help centre says some markets have special fee structures and refers to the PDF schedule [19]; the PDF ("Fee Schedule for July 2026 - 7.7.26 Update") returned HTTP 429 on three attempts, and its snippet shows basis-point volume tiers that appear to belong to perps [18] (unverified).
- **Funding** [S]: ACH deposits 1-3 business days, ACH withdrawals 3-5; debit, PayPal, Venmo and crypto withdrawals "usually within 30 minutes"; card deposits up to 2%; crypto via a third-party processor that may charge [25].
- **Yield on locked capital** [S]: variable APY on cash and position value, recently quoted 3.25%-4.05%, US users only, $250 minimum, paid monthly [26].
- **Margin** [PRESS, S]: affiliate Kinetic Markets registered as an FCM on 2026-03-24; partially collateralised trading still needs separate CFTC approval and was not live when reported [27]. Kalshi perps (BTC live 2026-06-03, ~5.7x max leverage) use separate API rate buckets [28][20].
- **API** [DOC]: REST + WebSocket + FIX sharing one token bucket; 7 tiers from Basic (200 read / 100 write tokens per second, 10 tokens per default request) to Prestige (10,000 / 8,000); Expert and above are earned by share of exchange volume; batch creates cost 10 tokens per order; 429s carry no penalty [20].
- **Settlement** [VENDOR, F]: named source agencies per series; payout "within a few hours"; Outcome Review Committee; Rule 6.3(c) allows last-traded-price settlement; no independent appeal [53].
- **Who is on the other side** [PRESS citing SSRN + Roosevelt Institute]: takers lost 1.12% per trade on average and makers gained the same; retail lost $584M from July 2021 to May 2026; makers include Kalshi Trading, Susquehanna, Jump and Flutter [73].

### Polymarket US (QCX LLC) vs Polymarket international
- Separate order books, liquidity and customer balances [15]. Dates disagree: QCEX purchase reported as July 2025 for $112M [15] and as October 2025 [35]; launch 2 or 3 December 2025 [15].
- **Fees** [DOC]: taker `0.0695*C*p*(1-p)` (max $1.74 per 100 at 50c), maker rebate coefficient 0.0125 ($0.31 per 100), taker volume rebates 10% / 25% / 50% above $250K / $1M / $10M monthly, banker's rounding; effective 2026-09-17 [7]. Older snippets quoting 0.05 or "0.30% flat" are stale.
- **Limits and margin** [DOC]: no order-size limit [8]; no position limit, $25,000 notional accountability, margin 100% of at-risk amount [14]; sellers post $1.00 per contract; portfolio-level relief for mutually exclusive structures [10].
- **Cash** [DOC]: withdrawals must return to the original payment method, FIFO; holds of 3-4 business days (debit, ACH) or 1 business day (wire) [9]. No crypto rail found.
- **API** [DOC]: REST + WebSocket, 20 requests/s per key, FIX for institutions, market-maker, liquidity and volume incentive programs [11][13].
- **Resolution** [DOC]: the Exchange decides from sources named in the contract; "all resolutions are final" [12]. No UMA. A US-book vs international-book pair is therefore also a centralised-vs-UMA pair.
- **International** [DOC]: UMA Optimistic Oracle, ~$750 pUSD bond, 2-hour challenge window, 4-6 days if disputed [5]; withdrawals "instant and free" to EVM chains, Solana, Bitcoin and Tron [4].

### Robinhood / Rothera, Crypto.com (CDNA), IBKR ForecastEx, DraftKings, FanDuel, others
- **US map** [PRESS, F]: Kalshi distributes through Robinhood, Coinbase, Webull, PrizePicks and Sleeper; CDNA (DCM + DCO + FCM) powers Fanatics, Truth Predict, DraftKings and Underdog; CME serves FanDuel Predicts and DraftKings; DraftKings owns Railbird, Underdog owns Aristotle, Robinhood/SIG own MIAXdx (Rothera), Gemini runs Titan, IBKR runs ForecastEx [35]. A Robinhood quote may be the Kalshi book or the Rothera book; routing per contract is not documented (unverified).
- **Robinhood** [PRESS]: began routing to Rothera in 2026; commission based on price and size, capped at 1c per contract [32]; a snippet gives `10% * p * (1-p)` (5% with Gold), rounded up, from 2026-06-01 [33]. No public trading API was found (unverified).
- **ForecastEx** [DOC]: $0.01 per contract per side; **positions cannot be sold**, closing means buying the opposite contract; incentive coupon on daily closing value, paid monthly [30], quoted ~3.8% APY in April 2026 [31] **[S]**. <1% of volume [16].
- **Crypto.com** [VENDOR, F]: $0.02 to open and $0.02 to close a $1 contract, no settlement fee on $1 contracts; possible $45 USD fiat withdrawal fee [34].
- **DraftKings / FanDuel** [PRESS, S]: both are FCMs routing to CME, CDNA and (DraftKings) its own exchange [36]; FanDuel Predicts launched in five states [89].

### Betfair, Smarkets, Matchbook
- **Betfair** [VENDOR; official page 403]: commission on net market winnings reported raised from 5% to 6% in June 2026 (2% top tier unchanged); "Expert Fee" replaced the Premium Charge: 20% of winnings between GBP 25,000 and 100,000 per rolling 52 weeks, 40% above [37][38]. The fetched source is dated 2026-05-15 yet describes a June change; treat as unconfirmed.
- **Smarkets** 2% standard, 1% pro [39] **[S]**; **Matchbook** 2% UK/IE, 4% elsewhere [37].
- **Documented gaps**: a bettor forum reports Polymarket at 2% against a Betfair lay at 25.0 and gaps lasting "weeks and months" [41] **[forum, S]**; an asset manager's note cites GBP 170M matched on Betfair's 2024 election market and a 5-10% effective charge that forces wider bids [40] **[pre-2025, possibly stale]**.
- **Jurisdiction trap**: UK residents, Betfair's home base, are close-only on Polymarket [6].

### Sportsbooks
- Overround ~100-100.5% on prediction markets vs ~102% Pinnacle vs 105-108% retail books [72] **[VENDOR, S]**.
- Limits: stakes cut to $2-$14, then market, bonus and account restrictions; accounts last "days to many months"; detection keys on exact-cent stakes, bets seconds after line moves, and deposit/withdrawal cycling [71]. Racing Post survey: 31.9% restricted in the prior 12 months vs an industry "<1%" claim [85] **[S; exact page among the search results not confirmed]**.

### PredictIt, Manifold
- **PredictIt** [VENDOR, F + S]: DCM/DCO approval September 2025, cap $3,500 per contract, 5,000-trader cap removed, 10% profit fee + 5% withdrawal fee [69]. One August 2026 review title still says "$850 cap" [87] **[S]**; trader-cap removal per [88] **[S]**; sources disagree on whether the higher cap is live everywhere.
- **Manifold**: real-money Sweepcash ended 2025-03-28; play-money only [70]. Signal source, not a counterparty.

### On-chain venues
- **Opinion (BNB Chain)** [PRESS]: ~$10B cumulative volume but only ~$31M open interest and ~$29M TVL; points fell ~86% in OTC value after the airdrop ratio was announced; AI-assisted resolution [65]. That volume/OI ratio is consistent with incentive farming (_inference_). Takers pay a probability-scaled fee with a $0.50 minimum, makers 0 [86] **[S]**. Covered by Oddpool and ArbBets [49][50].
- **Limitless (Base)**: >$4B cumulative volume, ~0.5% of July 2026 volume, AMM fee 0.40% [66] **[S]**.
- **Myriad (Abstract, Linea, BNB)**: ~$1.25M 30-day volume, moving from AMM to CLOB with USD1 collateral [67][90] **[S]**. **predict.fun**: ~$534M 30-day volume [68] **[S]**.
- **Hyperliquid HIP-4** [VENDOR, F]: live 2026-05-02; fully collateralised binaries in USDH; zero fee to open, fees on close or settlement; phase 1 is crypto-price binaries on Hyperliquid's own mark price; US geoblocked on UI and API [64].
- Chainlink TWAP streams also settle predict.fun, Limitless, Myriad and Jupiter markets [58], so crypto pairs among those venues share an index while Kalshi does not.

### Deribit / CME as probability sources
- BTC threshold contracts: Polymarket YES averaged 5.6 pp above Binance-option-implied probability (214 hourly observations), 6.3 pp pooled over three contracts, 11 pp against Deribit; gap half-life ~4 hours; wedge largest at low probabilities and long maturities; delta-hedged net alpha 0.067, t = 2.10, p = 0.053 [60] **[PAPER; three contracts]**.
- 113,338 BTC/ETH contracts on Kalshi and Polymarket (Sep 2025-Feb 2026): implied variance exceeds realised in every series; risk-neutral skew near zero [61] **[PAPER, S]**.
- MSc dataset: 33,107 observations on 6,566 contracts, March 2024-June 2026, benchmarked to Deribit DVOL [62]; findings not in the README.
- Settlement manipulation: Polymarket 5-minute BTC contracts showed settlement-time spot-flow spikes and reversals, largely absent at 15 minutes [59] **[PAPER]**; press cites ~821 accounts and ~$8.2M, retail absorbing 93% of losses, as the reason for the TWAP change [58].
- Fed: an NBER paper reportedly finds Kalshi's modal FOMC forecast beat fed funds futures since 2022 [78] **[S]**; Polymarket vs CME FedWatch differed 6-10 pp in one 2026 episode (79.5% vs ~86%) [63] **[S]**. FedWatch is a futures-derived model output, not a tradable binary.

## Documented cross-venue arbitrage: size, duration, returns, crowding

| Source | Class | Gap size | Duration | Caveat |
|---|---|---|---|---|
| Gebele & Matthes [44] | PAPER | median 2-4% after execution costs; $0.03 avg, $0.07 peaks pre-election | most of the overlap period for many pairs | a "substantial mass" above 200% APY; naive strategy +1,218.66% over 800 days on only 15 trades; pairs often not semantically identical |
| Ng, Peng, Tao, Zhou [43] | PAPER, S | "economically meaningful" | n/a | 2024 election; Polymarket led Kalshi |
| "Price as Focal Point" [45] | PAPER, S | weekly Polymarket-Kalshi spreads all above ~2% break-even | weeks | 2024 election |
| Clinton & Huang [42] | PAPER via PRESS | identical contracts diverged; Harris + Trump did not sum to $1 on 62 of 65 days | peaked in final two weeks | 2,500+ markets, >$2B |
| Microstructure repo [46] | DATA | 1-3c quoted, ~0 after fees | not measurable at 20 s | 2 pairs |
| NBA intra-Polymarket [47] | PAPER | 101 bp median on combinatorial episodes | 3.6 s median for single-market | 76.9% of opportunities averaged 14.8 shares |
| ArbBets [50] | VENDOR | 1-8% ROI after Kalshi fees, 100+ per day, 990+ matched markets | 2-6 hours, minutes in volatility | tool marketing, $149-$299/month |
| Oddpool [49] | VENDOR | demo 1.8-3.2c net, 2.7-5.8% ROI, ~32 live | 30 s refresh | tool marketing |

**Reconciliation**: liquid same-rule pairs sit inside the ~3c fee band and are contested at sub-minute speed; persistent multi-cent gaps cluster in (a) long-dated markets where lock-up destroys the annualised return, (b) pairs with different resolution wording, (c) thin books sized in tens to hundreds of dollars.

**Annualised return** (_own arithmetic from [1][17]_): `APY ~= (gap - fees) / (1 - gap + fees) * 365 / days_locked`.
- Politics, p~0.5, 4c gap, taker both legs: fees 1.00 + 1.75 = 2.75c; net 1.25c on ~98.75c = 1.27%. Locked 45 days: ~10% a year. Locked 120 days: ~3.9%, roughly Kalshi's own APY on idle cash [26].
- Same gap at p = 0.90/0.10: fees ~0.36c + 0.63c ~= 1.0c (Kalshi leg 1c if rounding is per contract); net ~3c.
- Making the Polymarket leg (fee 0) cuts the pair to 1.75c but converts the trade into leg risk.
- Polymarket geopolitics (0 fee) paired with Kalshi: 1.75c at 50c, and exactly the category where the death carve-out and "credible reporting" clauses bite.

## Rule-mismatch losses
1. **Khamenei, 28 Feb-1 Mar 2026.** Kalshi's terms: "If Ali Khamenei dies, the market will resolve based on the last traded price prior to confirmed reporting of death" [55]. Last trades $0.09 (March) and $0.42 (April); DeFi Rate reports final resolution at $0.02 and $0.29 and $21.7M volume [55]; AlienWP reports $0.09 and $54M and that Kalshi reimbursed "all fees and net losses" [54]; a headline cites "$2.2 million" [57] **[S]**. Polymarket: YES proposed twice, disputed twice, then final review [55]; Crane reports $1.00 [56]. An arb long Kalshi YES + long Polymarket NO loses the whole Polymarket leg (~90% of the pair's cost) while Kalshi merely refunds near cost; the mirror-image arb gets a windfall, so the outcome is a coin-flip on direction, not a hedge (_own arithmetic, illustrative prices_).
2. **Cardi B, February 2026**: see key fact 8 [53].
3. **Shutdown end-date ladder, November 2025**: Polymarket's "November 12" contract peaked at 97c and collapsed to ~1c at midnight because the rule keyed on the OPM announcement date, not the signing date; ~$13.1M volume [52].
4. **Funding deadline, January 2026**: Kalshi snapshot at 10:00 a.m. ET in the fetched article (a search snippet says 11:00) vs Polymarket 11:59 p.m. ET; Kalshi binds to a named source, Polymarket adds "a consensus of credible reporting" [52].
5. **2024 presidency**: Polymarket resolved on network calls, Kalshi on inauguration, a strict-subset relation rather than identity [44].
6. **Kalshi operational errors**: NFL win totals reversed after press coverage (Jan 2026); a 2025 Oscars market paid the wrong side with no reversal; a wrong source agency listed in August 2025 [53].

## What a builder who already runs LP / cross-venue arb / resolution-sniping / copy-trading bots is likely to UNDERESTIMATE
- **The rulebook is the tail risk.** Two divergent settlements in one quarter on $10M+ markets [53][55]. Kalshi's last-traded-price settlement turns a hedge into an unhedged position on the other venue at the worst moment. A pair matcher needs a clause-level diff of deadline timezone, source hierarchy, death/"credible reporting"/void clauses and index methodology.
- **Fee schedules move faster than code.** Three schedule changes in six months across the two Polymarket venues [2][7]; pull coefficients from the API or docs at start-up, never hard-code. Kalshi rounds fees up to the next cent [17] (per contract in that source's formula; the PDF that would confirm whether rounding is per order could not be opened), which penalises small child orders.
- **Capital fragmentation.** Polymarket US cash leaves only to its original funding method after 1-4 business-day holds [9]; PredictIt taxes every withdrawal 5% [69]; Kalshi international has no ACH [21]. The fast recycling loop is crypto: Polymarket instant withdrawal [4] into a Kalshi crypto deposit [25]; processor fees and pUSD -> USDC swap slippage (<10 bp, split above $50K [4]) are the basis cost.
- **Yield differential.** Kalshi and ForecastEx pay ~3-4% on position value [26][31]; a fully collateralised Polymarket leg earns nothing by default, so long-dated pairs are partly a carry trade (_inference_).
- **Leg risk is structural.** Polymarket matching is off-chain with on-chain settlement, Kalshi is a central book with token-bucket limits [20], Polymarket US allows 20 req/s [11].
- **Settlement timing mismatch.** Kalshi pays within hours [53]; Polymarket needs at least 2 hours and 4-6 days if disputed [5]. The winning leg can be stuck while the losing leg is already debited.
- **Depth.** Executable size at the quoted gap ranges from 171 to 119,000 contracts in one sample [46]; 76.9% of NBA opportunities averaged 14.8 shares [47]. Vendor ROI percentages say nothing about dollars.
- **Counterparties.** Kalshi makers (SIG, Jump, Flutter) earn the 1.12% per trade that takers lose [73]; a taker/taker arb pays that spread on both venues.
- **Sportsbook legs are consumable.** Stakes fall to $2-$14 within days to months [71]; exchange legs carry the Betfair Expert Fee of 20-40% above GBP 25K a year [37].
- **Tax asymmetry.** With a 90% gambling-loss cap from tax year 2026 and no IRS position on event contracts [74], $100,000 won on one leg and lost on the other can create $10,000 of taxable income; if the legs fall under different regimes the losses may not offset at all (_inference, not advice_). Kalshi and Polymarket reportedly issue no 1099s [91] **[S]**.
- **Legal exposure.** Polymarket international rejects new orders from the US, UK, France, Germany, Australia and others by IP on the API [6]; Kalshi binds every account to a verified residence [21]. The legitimate two-venue pairs are: non-US resident on Kalshi + Polymarket international; US person on Kalshi + Polymarket US + other DCMs. The US-book vs international-book trade needs two properly domiciled entities.
- **FX and stablecoin basis.** Betfair, Smarkets and Matchbook are GBP/EUR venues; Opinion, Myriad and HIP-4 settle in chain-specific stablecoins (USD1, USDH) [67][64].

## Comparable historical data for backtesting
- **Polymarket + Kalshi trades and metadata**: Jon Becker's `prediction-market-analysis`, ~36 GiB compressed Parquet, MIT [75]; Hugging Face mirror (49,486 files, ~50 GiB) [79] **[S]**; used for a 353M-trade, 429,000-contract calibration study [76].
- **Polymarket only**: 1.1B trading records, cleaned [80] **[S]**.
- **Order books**: pmxt archive, free hourly snapshots for Polymarket, Kalshi, Limitless and Opinion (connection refused today) [81] **[S]**; Predexon, covering Polymarket, Kalshi and Opinion [82] **[S]**.
- **Kalshi official**: public, unauthenticated `/historical/` candlesticks at 1-minute, 1-hour and 1-day intervals with bid/ask OHLC, volume and open interest [23]. **Polymarket US**: time-and-sales and daily reports [13].
- **Cross-venue matched sets**: Gebele & Matthes (10 venues, 2018-2025) [44]; Clinton & Huang (2,500+ markets) [42].
- **Sportsbook lines**: The Odds API snapshots back to 2020 [77] **[S]**; third-party Pinnacle closing-line archives from ~2018 [84] **[S]**.
- **Forecast baselines**: Metaculus and Manifold via API [70][83] **[S]**; Deribit DVOL as used in [62].
- **Polling archives**: not researched this session.

## Could not verify / open questions
- Kalshi's fee PDF (HTTP 429): per-series coefficients, which series carry maker fees, whether sports differ.
- Whether the fast Kalshi crypto rail is open to every international user, and the processor's fee.
- Betfair commission and Expert Fee from Betfair's own pages (403); Betfair and Smarkets country lists, API fees, politics liquidity in 2026.
- Deribit and CME fees, margin and KYC; any live study of Deribit-vs-Polymarket arbitrage after the 2026 fee changes ([60] uses three contracts).
- Whether Robinhood, Coinbase and Webull show the Kalshi book or internalise; Robinhood API access.
- Whether Kalshi now leads Polymarket in price discovery, especially in sports; no 2026 lead-lag study found.
- No documented cross-venue arbitrageur P&L found; every profit figure is vendor marketing or intra-Polymarket (~$40M, April 2024-April 2025, "Unravelling the Probabilistic Forest" via [48]).
- Opinion, Limitless, Myriad, predict.fun: fee formulas, KYC and geoblocks rest on snippets.
- PredictIt API status and whether the $3,500 cap applies to all markets.
- Khamenei figures disagree ($21.7M vs $54M; $0.09 vs $0.02); the "$2.2 million" figure could not be opened.
- Full texts of SSRN 5331995 and 6748186 were blocked (403); their numbers here come from search snippets and from papers quoting them.

## Source ledger
| n | URL | Publisher | Date | Supports | F/S |
|---|---|---|---|---|---|
| 1 | https://docs.polymarket.com/polymarket-learn/trading/fees | Polymarket docs | undated | fee formula, category rates | F |
| 2 | https://docs.polymarket.com/changelog | Polymarket docs | to 2026-08-14 | pUSD, CLOB V2, fee changes, TWAP | F |
| 3 | https://docs.polymarket.com/concepts/pusd.md | Polymarket docs | undated | pUSD wrap/unwrap | F |
| 4 | https://docs.polymarket.com/trading/bridge/withdraw.md | Polymarket docs | undated | withdrawals, $50K note | F |
| 5 | https://docs.polymarket.com/concepts/resolution.md | Polymarket docs | undated | UMA bond, 2 h, 4-6 days | F |
| 6 | https://docs.polymarket.com/api-reference/geoblock | Polymarket docs | undated | blocked / close-only list | F |
| 7 | https://docs.polymarket.us/fees | Polymarket US | eff. 2026-09-17 | taker 0.0695, rebates | F |
| 8 | https://docs.polymarket.us/learn/trading/access-and-limits/trading-limits.md | Polymarket US | undated | no size limits | F |
| 9 | https://docs.polymarket.us/learn/deposits/withdraw-funds/rules.md | Polymarket US | undated | holds, same-source rule | F |
| 10 | https://docs.polymarket.us/market-structure/collateral-and-margin.md | Polymarket US | undated | full collateral | F |
| 11 | https://docs.polymarket.us/api-reference/rate-limits.md | Polymarket US | undated | 20 req/s | F |
| 12 | https://docs.polymarket.us/learn/markets/market-resolution.md | Polymarket US | undated | exchange-determined resolution | F |
| 13 | https://docs.polymarket.us/llms.txt | Polymarket US | undated | FIX, incentives, reports | F |
| 14 | https://www.cftc.gov/filings/ptc/ptc0520263802.pdf | CFTC (QCX filing) | 2026 | no position limit, $25K accountability | S |
| 15 | https://www.cryptonexa.com/polymarket-us-exchange-runs-two-separate-venues-under-one-brand | CryptoNexa | 2026-08-18 | separate books, volumes | F |
| 16 | https://news.bitcoin.com/featured/prediction-markets-explode-in-july-as-world-cup-fueled-54b-in-trades/ | Bitcoin.com News | 2026-08-03 | July 2026 shares | F |
| 17 | https://marketmath.io/platforms/kalshi | Market Math | 2026-09-20 | Kalshi fee formula | F |
| 18 | https://kalshi.com/docs/kalshi-fee-schedule.pdf | Kalshi | 2026-07-07 | schedule title, tiers | S |
| 19 | https://help.kalshi.com/en/articles/13823805-fees | Kalshi Help | undated | special-fee markets | F |
| 20 | https://docs.kalshi.com/getting_started/rate_limits | Kalshi docs | undated | tiers, token costs | F |
| 21 | https://help.kalshi.com/en/articles/14026044-international-access-eligibility | Kalshi Help | undated | international funding, KYC | F |
| 22 | https://help.kalshi.com/en/articles/13823838-crypto-markets | Kalshi Help | undated | RTI 60 s average | F |
| 23 | https://docs.kalshi.com/api-reference/historical/get-historical-market-candlesticks | Kalshi docs | undated | historical endpoints | F |
| 24 | https://www.oddsshopper.com/articles/prediction-markets/kalshi-position-limits | OddsShopper | 2026 | accountability levels, $7M | S |
| 25 | https://help.kalshi.com/en/articles/13823791-transfers-faq | Kalshi Help | undated | transfer times and fees | S |
| 26 | https://help.kalshi.com/en/articles/13823847-apy-on-kalshi | Kalshi Help | undated | APY terms | S |
| 27 | https://www.financemagnates.com/institutional-forex/kalshi-pushes-prediction-markets-into-derivatives-territory-with-margin-plans/ | Finance Magnates | 2026 | FCM, margin status | S |
| 28 | https://www.coinperps.com/learn/kalshi-perpetuals-review | CoinPerps | 2026 | perps dates, leverage | S |
| 29 | https://www.coinperps.com/learn/kalshi-restricted-countries | CoinPerps | 2026 | excluded countries | S |
| 30 | https://forecastex.com/about/how-forecast-contracts-work | ForecastEx | undated | fee, no selling, coupon | F |
| 31 | https://pm.wiki/learn/forecastex-prediction-market | pm.wiki | 2026 | coupon ~3.8% | S |
| 32 | https://finance.yahoo.com/markets/options/articles/robinhoods-prediction-market-push-why-130400265.html | Yahoo Finance | 2026-06-10 | Rothera, 1c cap | F |
| 33 | https://marketmath.io/platforms/robinhood | Market Math | 2026 | Robinhood formula | S |
| 34 | https://next.io/prediction-markets/crypto-com/fees/ | next.io | 2026-09-15 | Crypto.com fees | F |
| 35 | https://defirate.com/news/prediction-market-land-grab-dcms-fcms-and-the-race-to-control-the-stack/ | DeFi Rate | 2026-08-13 | US DCM/FCM map | F |
| 36 | https://www.ingame.com/cme-sports-contracts-stop-volume/ | InGame | 2026 | DraftKings / FanDuel routing | S |
| 37 | https://betherosports.com/blog/best-betting-exchanges | Bet Hero | 2026-05-15 | exchange commissions | F |
| 38 | https://www.betfair.com/aboutUs/Betfair.Charges/ | Betfair | undated | official charges (403) | S |
| 39 | https://help.smarkets.com/hc/en-gb/articles/212106009-Commission-breakdown | Smarkets | undated | 2% / 1% | S |
| 40 | https://www.acadian-asset.com/investment-insights/owenomics/presidential-prediction-markets | Acadian | undated [pre-2025, possibly stale] | Betfair volume, vig | S |
| 41 | https://arbusers.com/polymarket-vs-betfair-arbitrage-t11041/ | Arbusers forum | undated | Betfair gap anecdote | S |
| 42 | https://goodauthority.org/news/the-perils-of-election-prediction-markets/ | Good Authority | 2025-12-18 | 2,500-market study | F |
| 43 | https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5331995 | SSRN | 2025 | Polymarket led Kalshi | S |
| 44 | https://arxiv.org/html/2601.01706v1 | arXiv | 2026-01-05 | semantic non-fungibility | F |
| 45 | https://arxiv.org/html/2604.24147v1 | arXiv | 2026-04 | weekly spreads > 2% | S |
| 46 | https://github.com/MobinHariri/kalshi-polymarket-microstructure | GitHub | 2026-09 | fee-adjusted crossings | F |
| 47 | https://arxiv.org/abs/2605.00864 | arXiv | 2026-04-22 | NBA arbitrage | F |
| 48 | https://www.financemagnates.com/trending/prediction-markets-are-turning-into-a-bot-playground/ | Finance Magnates | 2026-03-16 | $40M, bots | F |
| 49 | https://www.oddpool.com/arb-dashboard | Oddpool | live | scanner claims | F |
| 50 | https://getarbitragebets.com/blog/best-prediction-market-arbitrage-tools | ArbBets | 2026-08-04 | tools, windows | F |
| 51 | https://github.com/pmxt-dev/pmxt | GitHub (repository search API, query "polymarket kalshi arbitrage") | 2026-09-20 | 301 repos, star counts | F (API) |
| 52 | https://www.oddsshopper.com/articles/prediction-markets/kalshi-vs-polymarket-settlement-rules | OddsShopper | 2026-08-15 | shutdown cases | F |
| 53 | https://defirate.com/prediction-markets/how-contracts-settle/ | DeFi Rate | 2026-08-17 | Cardi B, settlement process | F |
| 54 | https://alienwp.com/how-kalshi-and-polymarket-settled-the-khamenei-market-differently/ | AlienWP | 2026-03-04 | Khamenei, reimbursement | F |
| 55 | https://defirate.com/news/kalshi-halts-khamenei-market-polymarkets-contract-enters-second-dispute/ | DeFi Rate | 2026-03-01 | carve-out text, prices | F |
| 56 | https://harrycrane.substack.com/p/prediction-markets-and-the-death | Harry Crane | 2026-03-01 | Khamenei analysis | F |
| 57 | https://www.aol.com/news/kalshis-response-2-2-million-091701235.html | AOL | 2026 | "$2.2 million" (404) | S |
| 58 | https://genfinity.io/2026/08/12/chainlink-twap-data-streams-polymarket-crypto-markets/ | Genfinity | 2026-08-12 | TWAP, $8.2M | F |
| 59 | https://arxiv.org/abs/2606.31675 | arXiv | 2026-06-30 | settlement manipulation | F |
| 60 | https://arxiv.org/abs/2606.19517 | arXiv | 2026-06-17 | options vs Polymarket | F |
| 61 | https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6748186 | SSRN | 2026 | variance premium | S |
| 62 | https://github.com/giannandreadestefano/btc-prediction-market-efficiency | GitHub | 2026 | DVOL benchmark dataset | F |
| 63 | https://financefeeds.com/fed-rate-hike-odds-polymarket-79-5-vs-cme-fedwatch-86/ | FinanceFeeds | 2026 | FedWatch gap | S |
| 64 | https://chainstack.com/hyperliquid-hip4-vs-polymarket-2026/ | Chainstack | 2026-05-04 | HIP-4 mechanics | F |
| 65 | https://panews.io/articles/019cc26c-2732-74ac-8e99-438e2d953649 | PANews | 2026-03 | Opinion volume, OI | F |
| 66 | https://coinmarketcap.com/cmc-ai/limitless-lmts/latest-updates/ | CoinMarketCap | 2026 | Limitless | S |
| 67 | https://defillama.com/protocol/myriad-markets | DefiLlama | live | Myriad | S |
| 68 | https://practicalcrypto.net/en/prediction-markets/predict-fun.html | PracticalCrypto | 2026 | predict.fun | S |
| 69 | https://marketmath.io/platforms/predictit | Market Math | 2026-09-20 | PredictIt cap, fees | F |
| 70 | https://cryptoslate.com/prediction-markets/manifold-predictions-review/ | CryptoSlate | 2026 | Manifold status | S |
| 71 | https://www.oddsshopper.com/articles/betting-101/arbitrage-betting-limits-getting-banned | OddsShopper | 2026-06-23 | limiting behaviour | F |
| 72 | https://www.sports-ai.dev/blog/prediction-markets-vs-bookmakers-ai-betting-2026 | sports-ai.dev | 2026 | overround | S |
| 73 | https://prospect.org/2026/08/26/house-always-wins-kalshi-prediction-markets/ | The American Prospect | 2026-08-26 | taker losses, makers | F |
| 74 | https://tax.thomsonreuters.com/news/irs-silence-on-prediction-market-winnings-to-cause-confusion-as-world-cup-begins/ | Thomson Reuters | 2026-06-16 | tax treatments, 90% cap | F |
| 75 | https://github.com/jon-becker/prediction-market-analysis | GitHub | undated | dataset | F |
| 76 | https://arxiv.org/abs/2602.19520 | arXiv | 2026-02-23 | calibration study | F |
| 77 | https://the-odds-api.com/historical-odds-data/ | The Odds API | undated | odds history | S |
| 78 | https://www.fortune.com/2026/01/28/kalshi-prediction-market-federal-reserve-betting-forecast-nber-working-paper | Fortune | 2026-01-28 | NBER paper on Kalshi Fed forecasts | S |
| 79 | https://huggingface.co/datasets/rhinot/prediction-market-analysis | Hugging Face | undated | dataset mirror size | S |
| 80 | https://github.com/SII-WANGZJ/Polymarket_data | GitHub | undated | 1.1B Polymarket records | S |
| 81 | https://archive.pmxt.dev/ | pmxt | undated | hourly order-book snapshots | S |
| 82 | https://predexon.com/ | Predexon | undated | multi-venue history | S |
| 83 | https://www.metaculus.com/faq/ | Metaculus | undated | forecast data access | S |
| 84 | https://sportsapis.dev/historical-odds | sportsapis.dev | 2026 | Pinnacle closing-line archives | S |
| 85 | https://betherosports.com/blog/why-sportsbooks-limit-bettors | Bet Hero | 2026 | restriction statistics | S |
| 86 | https://messari.io/report/opinion-an-emerging-player-in-prediction-markets | Messari | 2025-2026 | Opinion fee shape (403) | S |
| 87 | https://tech-insider.org/prediction-markets/platforms/predictit-review/ | Tech Insider | 2026-08 | "$850 cap" title (403) | S |
| 88 | https://nexteventhorizon.substack.com/p/news-predictit-wins-approval-from-cftc | Next Event Horizon | 2025 | PredictIt approval, caps | S |
| 89 | https://defirate.com/news/fanduel-predicts-launches-in-five-states-in-partnership-with-cme-group/ | DeFi Rate | 2025-12 | FanDuel Predicts launch | S |
| 90 | https://finance.yahoo.com/news/myriad-usd1-bnb-chain-exclusive-173456444.html | Yahoo Finance | 2026 | Myriad USD1, CLOB move | S |
| 91 | https://www.monacocpa.cpa/prediction-market-tax | Monaco CPA | 2026 | no 1099s from Kalshi / Polymarket | S |
