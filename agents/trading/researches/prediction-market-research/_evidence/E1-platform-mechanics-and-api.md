# Polymarket mechanics, microstructure, fees and API surface
_As of 2026-09-20. Evidence pack E1 for the Polymarket strategy survey._

Conventions: `[n]` = row in the source ledger. **(derived)** = my arithmetic on cited inputs. "Vendor" = VPS/affiliate marketing, a lead, not proof. Everything here was fetched or searched on 2026-09-20; nothing is asserted from memory. "International" = polymarket.com (Polygon); "US" = the CFTC-regulated Polymarket US exchange.

## Key facts

1. **CLOB V2 cut over on 2026-04-28 (~11:00 UTC, ~1 h downtime): new exchange contracts, rewritten backend, pUSD collateral, no V1 compatibility, every resting order wiped.** Order struct lost `nonce`, `feeRateBps`, `taker`; gained `timestamp` (ms), `metadata`, `builder`. Fees are set at match time. EIP-712 Exchange domain version "2" (ClobAuth stays "1") [1][29].
2. **Current taker fee (international): `fee = C x feeRate x p x (1-p)`**, feeRate: Crypto 0.07, Sports 0.05, Economics/Culture/Weather/Other 0.05, Finance/Politics/Mentions/Tech 0.04, Geopolitics 0. Makers pay 0. Peak = $1.75 / $1.25 / $1.00 per 100 shares at p=0.50. Rounded to 5 dp, minimum 0.00001 [2]. Since V2, fees are charged in USDC (pUSD), not in shares [29].
3. **Fee as a share of cash outlay is `feeRate x (1-p)` (derived from [2])**: crypto taker at p=0.50 pays 3.5% of premium, at p=0.10 6.3%, at p=0.97 0.21%. A taker round trip at 0.50 in crypto costs 3.5c/share.
4. **Maker rebates are a per-market, per-day pro-rata pool**: 20% of taker fees (Crypto), 15% (Sports, cut from 25% on 2026-07-10 when the sports rate rose 0.03 -> 0.05), 25% elsewhere; paid daily in pUSD, $1 minimum [11][1].
5. **Taker Rebate Program (from 2026-05-28)**: seven tiers by 30-day weighted volume, 3% rebate at $2k up to 50% at $10M+; `wV = size x (1 - entry price) x category weight x bonuses` (weights 1.0 sports ... 2.3 crypto); omnibus-wallet integrations excluded [12].
6. **Deliberate taker delay changed three times in 2026**: a 500 ms crypto speed bump vanished unannounced ~Feb 2026 [47]; a 250 ms taker delay on crypto + finance markets started 2026-06-05, during which the order is `pending`, non-cancellable, balance reserved, duplicates rejected [48][7]; crypto cut to 50 ms on 2026-08-17 11:00 UTC [1][49].
7. **Crypto up/down markets settle on Chainlink Data Streams TWAP since 2026-08-07** (was a single snapshot). 5-minute markets: 30 s window, moved to 60 s on 2026-08-14; 15-min and 4-hour: 60 s. Both price-to-beat and settlement use the TWAP [1].
8. **Primary servers are officially AWS `eu-west-2` (London); closest non-restricted region `eu-west-1` (Dublin).** A KYC/KYB form gives co-location access in eu-west-2, explicitly not for Builder Program participants or third-party apps trading for end users [21].
9. **Rate limits are two-layered**: Cloudflare per-IP (POST /order 5,000/10 s burst, 120,000/10 min) [4] plus per-signer token buckets tiered by 30-day maker-wallet volume: Standard 40 orders/s (burst 60), 80 cancels/s; Elite ($10M+) 600/s and 1,200/s; tiers refresh every 3 h; over-limit = HTTP 429 + `Retry-After` [5].
10. **Post-only exists (since 2026-01-06)**, GTC/GTD only; a heartbeat dead-man switch cancels all open orders if no heartbeat within 10 s (send every 5 s) [1][6][28][34].
11. **Trading API 90-day uptime is 99.13%** (about 19 h down, derived) with at least nine trading incidents between 2026-07-28 and 2026-09-19, including a 4 h 24 min halt on 2026-08-31 and cancel-only recovery modes [40][41]. Polymarket says it will replace the CLOB with a Rust rewrite in mid/late Q4 2026 (target 200k orders/s, 10-20x better p99) [42].
12. **New wallets are Deposit Wallets (signature type 3, POLY_1271/ERC-7739) for every account deployed on/after 2026-05-04**; EOAs trade directly only if allowlisted and pay POL gas [20][39].
13. **Public WebSocket trade direction is unreliable**: it matched on-chain ground truth only ~59% of the time (volume-weighted, top-100 markets) [43].
14. **Market count is dominated by ephemeral markets**: 305,003 new markets in the latest month on The Block's series [59]; 385,198 distinct markets seen on the WS feed in 52 days [43]; only ~7,200-8,000 "active" on the site at once [60].
15. **No official order-book history.** CLOB `/prices-history` has minute fidelity [27]; Data API v2 (2026-09-04) adds `bucket_seconds` price history [1]. Historical L2 exists only at third parties (1-minute snapshots from Aug 2025 at the most explicit one) [61].
16. **Polymarket US fee (effective 2026-09-17)**: `Theta x C x p x (1-p)`, taker Theta 0.0695 (max $1.74/100), maker Theta -0.0125 (rebate credited at fill), monthly taker-volume rebates 10%/25%/50% at $250k/$1M/$10M, banker's rounding to $0.01 [30].

## Trading architecture today

- **Hybrid CLOB**: operator validates signature, balance, allowance, tick size, matches off-chain, then submits to the exchange contract on Polygon; settlement is atomic. Trade status path: `MATCHED_NOT_BROADCASTED` -> `MATCHED` -> `MINED` -> `CONFIRMED`, or `RETRYING` -> `FAILED` (terminal) [7][19]. A matched trade can therefore still fail on-chain.
- **Contracts (Polygon 137)**: CTF Exchange `0xE111180000d2663C0091e4f400237545B87B996B`; Neg Risk CTF Exchange `0xe2222d279d744050d28e00520010520000310F59`; Conditional Tokens `0x4D97DCd97eC945f40cF65F87097ACe5EA0476045`; pUSD proxy `0xC011a7E12a19f7B1f670d46F03B03f3342E82DFB`; CollateralOnramp `0x9307...B8ee`; CollateralOfframp `0x2957...5854`; UMA Adapter `0x6A9D...4F74`; audits by Quantstamp and Cantina, March 2026 [16]. The V2 exchange is operator-gated, has a global pause and a per-user pause, a protocol max fee rate, and "preapproved orders" [37].
- **Match types**: COMPLEMENTARY (BUY vs SELL, direct transfer), MINT (two BUYs on complementary outcomes whose prices sum to $1 -> collateral split into YES+NO), MERGE (two SELLs -> tokens merged back to collateral) [37][9]. Price improvement always goes to the taker [7].
- **Split / merge / redeem**: $1 collateral <-> 1 YES + 1 NO; redeem burns the whole balance for the condition, no amount parameter [33c]. 50/50 resolutions pay $0.50 per token [24].
- **Neg risk**: 1 NO in any outcome converts to 1 YES in every other outcome via the adapter [10]; general form: converting `amount` of NO on `m` questions returns `amount x (m-1)` collateral plus `amount` YES on each complementary question; the adapter has a `feeRate` parameter on conversion (current value unverified) [38]. The V1 adapter `0xd91E...5296` was retired 2026-07-17; V2 uses `0xadA2005600Dec949baf300f4C6120000bDB6eAab` [1] (the contracts page still lists only the old address as "deprecated" [16]). Augmented neg risk adds placeholder outcomes and an explicit "Other" whose definition narrows as placeholders are named; docs say trade named outcomes only [10].
- **pUSD**: ERC-20, 6 decimals, 1:1 wrapper enforced on-chain, transferable, "no current plans" for external listing [3]. Sources disagree on backing: help centre says native USDC [29]; the pUSD page names USDC.e for wrapping [3]; the contract repo says it wraps "USDC/USDCe" with permissionless on/off-ramp plus a witness-signed PermissionedRamp [37]; the deposit page says incoming USDC or USDC.e is wrapped [22]. API traders wrap themselves via the Onramp [3]. pUSD is UUPS-upgradeable [37].
- **Wallets and gas**: signature types 0 EOA, 1 Proxy, 2 Safe, 3 Deposit Wallet [6]. Deposit Wallets are ERC-1967 proxies (beacon proxies for deployments after 2026-06-29, i.e. centrally upgradable), support batched calls and scoped, time-limited session keys, and are relayed gaslessly [20]. Gasless relayer covers deployment, approvals, split/merge/redeem, transfers and needs Builder credentials [33d]; relayer `/submit` is limited to 25 req/min and since 2026-04-21 returns only `transactionID` (poll for the hash) [4][1].
- **Deposits / withdrawals**: Bridge API accepts EVM chains, Solana, Bitcoin, Tron; above $50k the docs recommend third-party bridges [22]. Withdrawals are "instant and free": pUSD -> Offramp -> Uniswap v3 pool -> native USDC, UI enforces <10 bp output difference; if the pool is exhausted you withdraw pUSD itself [23]. Bridge API is 50 req/10 s [4].

## Order types and microstructure

- **Types**: GTC, GTD, FOK, FAK (FAK added 2025-05-28) [6][1]. All orders are limit orders; "market" orders are marketable limits; market BUY is sized in pUSD, SELL in shares; `maxSpend` caps spend including platform and builder fees [6][39]. No in-place modify: cancel and replace [39].
- **GTD**: expires one minute before the stated time; expirations under ~3 minutes are rejected, so GTD cannot give sub-minute auto-expiry [6][39].
- **Tick and size**: tick sizes 0.1 / 0.01 / 0.001 / 0.0001 [34]; tick tightens to 0.001 when price > 0.96 or < 0.04, signalled by `tick_size_change`; orders on the old grid are rejected [35]. World Cup markets were set to 0.0025 on 2026-07-02, a value outside the usual list [1]. Minimum size is per-market `min_order_size` (typically 5 shares); marketable orders under $1 notional are rejected [6][39]. Docs state no maximum size [9].
- **Displayed price**: midpoint, or last trade when the spread exceeds $0.10 [9].
- **Priority and self-trade**: the docs fetched do not state price-time priority or any self-trade prevention [7]. Empirically self-counterparty fills exist: median 0.97% of volume per market, p99 10.6%, max 22.2% [43]. Wash trading has been explicitly prohibited since the March 2026 integrity rules [69].
- **Batching**: `POST /orders` up to 15 orders (5 at launch 2025-06-03, 15 since 2025-08-21); a batch is admitted only if the signer bucket covers every entry [1][5]. `DELETE /orders` max 1,000 IDs since 2026-06-15 [1] (one docs page still says 3,000 [28]).
- **Responses**: `live`, `matched`, `delayed`, `unmatched` [6]. Since 2026-07-24 FAK/FOK responses carry `tradeIDs`, not transaction hashes; poll until hash or `FAILED` [1].
- **Delays**: see Key fact 6. Sports: docs say "configured delay windows around live game conditions" [7]; the official agent-skills file says outstanding limit orders are auto-cancelled at game start and marketable orders get a 3-second placement delay [34] (that repo still references USDC.e, so it may be stale). The order-lifecycle page still says 250 ms for crypto/finance, contradicting the 50 ms changelog entry for crypto; finance presumably remains 250 ms [7][1].
- **Restarts**: order endpoints return HTTP 425 during a matching-engine restart; after every restart the engine is post-only for 2 minutes; notice (~2 days when possible) goes out on Telegram/Discord [8].
- **Incident log (status page, last 90 days)**: 07-28 rollback 54 min; 07-28/29 price-history lag (hours); 07-30 35 min; 08-30 53 min; 08-31 three incidents (32 min, 4 h 24 min, ~1.9 h, "delayed open order read responses"); 09-11 40 min; 09-19 ~2 h with cancel-only, then 42 min attributed to degraded Polygon PoS block production [40][41]. WebSockets, market data and settlement stayed up during the 08-31 halt [41].

## Fee history -> current schedule

| Date | Change | Source |
|---|---|---|
| 2025 | no trading fees (Sacra: $0 revenue in 2025) | [32] |
| 2026-01-05 | taker fees + maker rebates on 15-minute crypto; curve peaks at 1.56% at p=0.50 | [1] |
| 2026-02-12 | 5-minute crypto markets launch with the same curve | [1] |
| 2026-02-18 | NCAAB and Serie A taker fees; rebates computed per market | [1] |
| 2026-03-06 | all crypto horizons (1H, 4H, daily, weekly), new markets only | [1] |
| 2026-03-30 | Fee Structure V2: ten fee categories; geopolitics/world events stay free; 03-31: compute from the market's `feeSchedule` object | [1] |
| 2026-04-28 | V2: fee decided at match time, charged in USDC | [1][29] |
| 2026-05-28 | Taker Rebate Program | [12] |
| 2026-07-10 | sports 0.03 -> 0.05, sports maker rebate 25% -> 15% | [1] |

- Pine Analytics reports the March formula as `C x p x feeRate x (p(1-p))^exponent` with per-category peaks (crypto 1.80%, sports 0.75%, economics 1.50%) [46]; Sacra and the current docs give crypto 0.07 with exponent 1 [32][2][39]. Treat the current docs as authoritative; the pre-V2 parameters were not re-verified here.
- Pine also reports a referral programme paying 30% of taker fees (direct) and 10% (indirect), a blended effective fee of 0.76% of taker volume, ~$160M/day taker volume and ~$1.2M/day gross fees [46]. Daily fees first exceeded $1M on 2026-04-01 per DefiLlama [68]. Sacra estimates $1B annualised revenue in June 2026 [32].
- **Builder fees stack on top**: up to 100 bps taker and 50 bps maker, additive to the platform fee [15].
- **Gas**: none for CLOB trades (operator settles) or relayed Deposit Wallet operations; allowlisted EOAs pay POL for approvals, splits, merges, redeems [20]. No Polymarket deposit/withdrawal fee [2][23].
- **Liquidity rewards** (separate from rebates): quadratic score `((v-s)/v)^2 x b`, per-market max spread and min size, single-sided orders scored at 1/3 when mid is within [0.10, 0.90] and two-sided required outside it, sampled every minute, paid daily, $1 minimum [13]. March Madness programme: $2M+, orders must rest 3.5 s to count, up to $60k/day on a live full-game moneyline [1]. August 2026: $1M across crypto TWAP markets ($550k 5-min, $350k 15-min, $100k 4-hour), ended [13].
- **Polymarket US history**: CFTC filings in March 2026 moved the taker fee 10 -> 30 bps and maker rebate 10 -> 20 bps of contract premium [67]; Sacra reports a 0.05 coefficient with -0.0125 maker rebate from 2026-04-03 [32]; current 0.0695 / -0.0125 from 2026-09-17 [30].

## API / on-chain surface

- **Hosts**: CLOB `https://clob.polymarket.com`; Gamma `https://gamma-api.polymarket.com`; Data API `https://data-api.polymarket.com` (v2 under `/v2`, v1 frozen); relayer `https://relayer-v2.polymarket.com`; WS market `wss://ws-subscriptions-clob.polymarket.com/ws/market`, user `.../ws/user`, sports `wss://sports-api.polymarket.com/ws`, RTDS `wss://ws-live-data.polymarket.com` [33b][33d][18][19][1].
- **Market WS**: `book`, `price_change` (format changed 2025-09-15), `last_trade_price`, `tick_size_change`; with `custom_feature_enabled`: `best_bid_ask`, `new_market`, `market_resolved`. The 100-token subscription cap was removed 2025-05-28; dynamic subscribe/unsubscribe; PING every ~10 s [18][35][1]. User WS is keyed by condition ID and streams order PLACEMENT/UPDATE/CANCELLATION plus trade status [19]. Sports WS pushes all live game state with no subscription and carries a "may be delayed" disclaimer [18]. RTDS topics: `crypto_prices` (Binance), `crypto_prices_chainlink`, `equity_prices` (Pyth), comments [18].
- **Gamma**: events/markets/tags/series/sports metadata; offset endpoints deprecated in favour of `/markets/keyset` and `/events/keyset` (max limit 100 since 2026-05-14); `closed` defaults to false since 2026-04-09 [1][25]. Limits: 4,000 req/10 s general, `/markets` 300, `/events` 500 [4].
- **Data API**: positions, closed positions, trades, activity, top holders, open interest, live volume, trader leaderboard, biggest wins, builder leaderboard/volume, accounting snapshot ZIP [25]. v2 adds `/v2/user-pnl`, `/v2/user-stats`, `/v2/user-volume`, `/v2/holders?include_pnl=true`, `/v2/resolutions`, cursor pagination, 429 + `Retry-After` [1]. `REDEEM` activity is per outcome and positions expose `entryFeesUsdc` since 2026-08-10 [1]. v1 `/trades` and `/activity` cap `limit` 500 / `offset` 1,000 [1].
- **CLOB read limits**: `/book`, `/price`, `/midpoint` 1,500 req/10 s; batch variants 500; `/prices-history` 1,000 [4]. Exceeding Cloudflare limits throttles (queues) rather than rejects [4]. Rewards and rebates have their own endpoints (order scoring status, earnings by date, rebated fees per maker) [25].
- **History**: CLOB `/prices-history` takes `interval` (1h...max) and `fidelity` in minutes (default 1); what price `p` represents is not documented [27]. On-chain: Goldsky subgraphs (positions, pnl, activity, oi, orderbook) [33b][66], Goldsky/CryptoHouse, Dune, Allium [17]. Third-party L2 history: PolymarketData (1-minute full ladder from Aug 2025, "sub-minute data doesn't exist historically") [61]; Telonex, PMData, Pendulum Flow, pmxt archive (claims not verified) [62]. One academic collector logged 30.3B book events / 623.8 GB in 52 days; raw data not redistributed, collector config public [43].
- **SDKs**: `@polymarket/clob-client-v2`, `py-clob-client-v2`, Rust client, `real-time-data-client`, builder relayer/signing SDKs [1][33]. Open issues show the Python V2 client binding API keys to the EOA instead of the deposit wallet and EOA flows rejected with "maker address not allowed, please use the deposit wallet flow" [65].
- **Builder Program**: builder code serialised in the signed order, gasless relayer, leaderboard with 24 h lag, optional `X-Builder-Code` on Bridge API (2026-06-25) [14][1]. New account creation requires a Builder API key [20].
- **Agent tooling**: official `Polymarket/agent-skills` repo (8 skill files, 188 stars, one commit, V1-era content) [33]; a Rust CLI is mentioned only in a search snippet [63]. No official MCP server found; the many third-party MCP servers are untrusted code.
- **Combos / RFQ**: multi-leg positions priced by RFQ: makers have 400 ms to quote, the user 10 s to accept, optional 1 s last look; quoter gateway over WebSocket [26][25]. Launched on Polymarket US 2026-08-21; $31.4M in 24 h (21.6% of US volume) two days later [64].
- **Polymarket US API**: retail REST (23 endpoints) + 2 WS, Ed25519 auth, launched Feb 2026 [63b]; institutional REST/gRPC-streaming with 3-minute bearer tokens, drop copy, combos/RFQ, per-firm limits; FIX by request [31][63b]. Exchange entity per Sacra: QCX LLC [32].
- **Perps**: separate international product launched 2026-09-03, up to 20x, own status group and OpenAPI spec [64b][40]. Out of scope here.

## Market catalogue

- **Volume**: international $7.89B (July) -> $4.59B (August 2026); US $5.0B -> $3.82B; the drop follows the World Cup [56][57]. Sacra: peak $10.5B March 2026, $8.9B May [32]. One tracker has Kalshi at 86% of combined current-month volume [58]; Kalshi August volume reported at $38.67B [56]. An analysis cited by Shift Markets estimates ~30% of international volume came from US-linked accounts (12 months to April 2026) [57].
- **Category mix**: May 2026 sports 39-40%, politics 32%, crypto 20% [32]. Category trackers disagree strongly (one shows 64% "Other") [58]; treat any mix as taxonomy-dependent.
- **Short-duration crypto** (Dune, via a news summary; the Dune post 404'd on fetch): 5-minute markets did $2.3B in ~7 weeks vs $795M for 15-minute; fast markets $532M in the week of 2026-03-23, 77% BTC, 13% ETH, ~5-6% each SOL/XRP; bots 55-62% of fast-market volume vs 31% in daily/weekly; 6,189 bot addresses made 56M trades at $6-7 average; crypto fees $23.7M in 83 days [45].
- **Spreads and depth**:
  - First-trade median quoted spread by category (160k contracts, Oct 2025-Mar 2026): sports 3c, politics 8c, geopolitics 10c, monetary policy/elections 13c, other 14c, crypto 19c, economy 21c; by hour 24: sports 3c, politics/geopolitics 2c, crypto 3c, elections 3.6c, economy 4c, monetary policy 5c; most compression happens in the first hour; sports are 46,131 of ~54k markets in that table [44].
  - Cross-section (600 markets, Feb-Apr 2026): median quoted half-spread ~400 bps for mids 0.40-0.60, 1,300-1,800 bps below 0.10; depth is spread across levels (median L1/L10 = 0.137); ~32 effective makers per market; depth decays into resolution; on the top-100 markets the median effective half-spread is ~0 when measured with on-chain direction [43].
  - In-play NBA (173 games, 75M snapshots): 7 executable single-market arbitrage episodes, median life 3.6 s; 290 combinatorial episodes, median 101 bps, 76.9% limited to ~14.8 shares [55].
- **Live count**: 7,207 active markets on the site at fetch [60]; a Columbia study cited by a tracker put ~25% of historical volume as wash trading [58] [pre-2026 study, possibly stale].

## Latency geography

- Official: primary `eu-west-2`, nearest unrestricted `eu-west-1`, KYC/KYB co-location excluding builders [21]. Glassnode's monitor says origin is AWS London behind Cloudflare [51]. The UK is close-only on frontend and API, so London IPs cannot open positions; Ireland and the Netherlands are close-only on the frontend only, API unrestricted [21].
- Vendor claims (unverified): Dublin -> CLOB 0.8-2 ms network [53][54]; 70-85 ms internal CLOB processing and 80-180 ms tick-to-order for a Dublin bot [52]. Polymarket shipped an "async commit pipeline" latency cut on 2026-07-24 [1], so older processing-time numbers are likely stale.
- Practitioner report (March 2026): for earnings-news markets a ~500 ms newswire was too slow (book swept first); the official SDKs add slow pre-trade network checks; match timestamps have only second granularity [50].

## What a builder who already runs LP / cross-venue arb / resolution-sniping / copy-trading bots is likely to UNDERESTIMATE

1. **Regime half-life is weeks.** In 2026: three taker-delay regimes, two TWAP windows in one week, a sports fee/rebate flip, a full order wipe, a wallet-type change, and a Rust CLOB replacement due Q4 [1][42][47][48]. A changelog/status watcher is infrastructure, not a nicety.
2. **Fees scale with `(1-p)` of outlay and with your size tier.** Longshot takers pay up to 7% of premium in crypto; whales get 50% of it back, and rate-limit tiers (40/s vs 600/s) follow maker volume [2][12][5] (derived). A small team is structurally slower and more expensive than incumbents on the same strategy.
3. **Resolution sniping is fee-light but not free**: crypto at 0.99 costs 0.0007/share against 1c gross (7% of edge, derived from [2]); geopolitics is free [2].
4. **Matched is not settled.** `RETRYING`/`FAILED`, Polygon stalls (2026-09-19), no tx hash in FAK/FOK responses: a cross-venue hedge can be left naked [7][40][1].
5. **Availability risk is quote risk.** Cancel-only modes, HTTP 425, 2-minute post-only after restarts, 99.13% uptime [8][40]. The heartbeat is the only dead-man switch; GTD cannot expire in under ~2 minutes [6][28].
6. **The public feed mislabels aggressor side ~41% of the time** [43]; flow and copy signals need on-chain `OrderFilled` or Data API.
7. **Co-location vs Builder is a choice**: builders and apps trading for users are excluded from eu-west-2 co-location [21], yet gasless relayer and new-account deployment need Builder credentials [20][33d].
8. **Maker rebates are zero-sum within a market** and sports dropped to 15% [11][1]; liquidity rewards need 3.5 s resting and minute sampling [1][13].
9. **300k markets a month** means discovery (keyset pagination at 100, `new_market` events) and tick-regime handling (0.0025, 0.001 switches) are first-order engineering [59][1][35].
10. **Depth sits behind the top of book** (L1/L10 0.137) and longshot spreads are 13-18% [43]; sizing off best bid/ask misstates both.
11. **Combos RFQ is a new maker surface** with a 400 ms quote window and last look [26][64].
12. **Pending taker orders lock balance and cannot be cancelled** [48].

## Could not verify / open questions

- Matching priority (price-time?) and any self-trade prevention on the international CLOB: not documented in fetched pages [7].
- Whether heartbeats are opt-in, and the exact sports delay length in 2026 (3 s comes from a possibly stale repo) [34].
- How a user cancels on-chain now that `nonce` is gone [1].
- Current neg-risk conversion `feeRate` [38]; pre-V2 fee parameters; whether the March 30 schedule applied only to new markets.
- pUSD backing (native USDC vs USDC.e) [3][29][37]; who earns reserve yield.
- Finance-market taker delay today (docs say 250 ms) [7]; any delay on politics/other categories.
- Resolution page says anyone can propose [24] while UMA's managed oracle (Aug 2025) restricted proposals to a whitelist [70]; not reconciled here.
- A "June 2026 four-provider benchmark" (13-15 ms feed, 21-23 ms order RTT from Dublin) surfaced only in a search summary; source page not isolated. 70-85 ms internal processing is a single marketing blog [52].
- Category volume mix after the World Cup; no primary dashboard was fetched. `archive.pmxt.dev` refused connection; `dune.com/blog/polymarket-fast-markets` returned 404; cryptodaily returned 403.
- Rust CLI existence and scope (snippet only) [63].

## Source ledger

| n | URL | Publisher | Date | Supports | F/S |
|---|---|---|---|---|---|
| 1 | https://docs.polymarket.com/changelog (and /changelog/predictions) | Polymarket docs | entries to 2026-09-04 | V2, fees history, delays, TWAP, rate limits, Data API v2 | F |
| 2 | https://docs.polymarket.com/trading/fees | Polymarket docs | undated | fee formula, rates, rounding | F |
| 3 | https://docs.polymarket.com/concepts/pusd | Polymarket docs | undated | pUSD spec, onramp | F |
| 4 | https://docs.polymarket.com/api-reference/rate-limits | Polymarket docs | undated | per-IP limits | F |
| 5 | https://docs.polymarket.com/api-reference/trading-rate-limits | Polymarket docs | undated | per-signer tiers | F |
| 6 | https://docs.polymarket.com/trading/place-orders.md | Polymarket docs | undated | order types, GTD, post-only, sig types, batch | F |
| 7 | https://docs.polymarket.com/concepts/order-lifecycle.md | Polymarket docs | undated | matching, delays, trade statuses | F |
| 8 | https://docs.polymarket.com/trading/matching-engine.md | Polymarket docs | undated | HTTP 425, post-only after restart | F |
| 9 | https://docs.polymarket.com/concepts/prices-orderbook.md | Polymarket docs | undated | displayed price, YES/NO crossing | F |
| 10 | https://docs.polymarket.com/concepts/negative-risk.md | Polymarket docs | undated | convert, augmented neg risk | F |
| 11 | https://docs.polymarket.com/programs/maker-rebates.md | Polymarket docs | undated | rebate shares and formula | F |
| 12 | https://docs.polymarket.com/programs/taker-rebates.md | Polymarket docs | launch 2026-05-28 | taker tiers | F |
| 13 | https://docs.polymarket.com/programs/liquidity-rewards.md | Polymarket docs | undated | scoring, August pool | F |
| 14 | https://docs.polymarket.com/programs/builders/overview.md | Polymarket docs | undated | builder programme | F |
| 15 | https://docs.polymarket.com/programs/builders/fees.md | Polymarket docs | undated | builder fee caps | F |
| 16 | https://docs.polymarket.com/resources/contracts.md | Polymarket docs | undated | addresses, audits | F |
| 17 | https://docs.polymarket.com/resources/blockchain-data.md | Polymarket docs | undated | Goldsky, Dune, Allium | F |
| 18 | https://docs.polymarket.com/market-data/realtime-data.md (and /market-data/websocket/market-channel) | Polymarket docs | undated | WS endpoints, events, RTDS | F |
| 19 | https://docs.polymarket.com/trading/realtime-order-updates.md | Polymarket docs | undated | user channel | F |
| 20 | https://docs.polymarket.com/trading/deposit-wallets | Polymarket docs | undated | deposit wallets, EOA allowlist | F |
| 21 | https://docs.polymarket.com/api-reference/geoblock | Polymarket docs | undated | eu-west-2, co-location, restrictions | F |
| 22 | https://docs.polymarket.com/trading/bridge/deposit.md | Polymarket docs | undated | deposits | F |
| 23 | https://docs.polymarket.com/trading/bridge/withdraw.md | Polymarket docs | undated | withdrawals | F |
| 24 | https://docs.polymarket.com/concepts/resolution.md | Polymarket docs | undated | UMA flow, 50/50 | F |
| 25 | https://docs.polymarket.com/_llms/en/api-reference/predictions.md | Polymarket docs | undated | endpoint inventory | F |
| 26 | https://docs.polymarket.com/market-makers/rfq/api-reference | Polymarket docs | undated | combos RFQ timings | F |
| 27 | https://docs.polymarket.com/api-reference/markets/get-prices-history.md | Polymarket docs | undated | price history params | F |
| 28 | https://docs.polymarket.com/trading/orders/overview | Polymarket docs | undated | heartbeat, cancel batch | F |
| 29 | https://help.polymarket.com/en/articles/14762452-polymarket-exchange-upgrade-april-28-2026 | Polymarket Help | 2026-04 | V2 summary, fees in USDC | F |
| 30 | https://docs.polymarket.us/fees | Polymarket US docs | eff. 2026-09-17 | US fee schedule | F |
| 31 | https://docs.polymarket.us/institutional/introduction | Polymarket US docs | undated | institutional API | F |
| 32 | https://sacra.com/c/polymarket/ | Sacra | 2026 | revenue, mix, US fee history | F |
| 33 | https://github.com/Polymarket/agent-skills | Polymarket (GitHub) | undated | official agent skills, SDK names | F |
| 33b | https://github.com/Polymarket/agent-skills/blob/main/market-data.md | Polymarket (GitHub) | undated | hosts, subgraph URL | F |
| 33c | https://github.com/Polymarket/agent-skills/blob/main/ctf-operations.md | Polymarket (GitHub) | undated | split/merge/redeem | F |
| 33d | https://github.com/Polymarket/agent-skills/blob/main/gasless.md | Polymarket (GitHub) | undated | relayer | F |
| 34 | https://github.com/Polymarket/agent-skills/blob/main/order-patterns.md | Polymarket (GitHub) | undated | tick sizes, sports rules, heartbeat | F |
| 35 | https://github.com/Polymarket/agent-skills/blob/main/websocket.md | Polymarket (GitHub) | undated | tick change threshold, WS usage | F |
| 37 | https://github.com/Polymarket/ctf-exchange-v2/blob/main/CLAUDE.md | Polymarket (GitHub) | 2026 | match types, pause, pUSD design | F |
| 38 | https://github.com/Polymarket/neg-risk-ctf-adapter/blob/main/docs/NegRiskAdapter.md | Polymarket (GitHub) | undated (V1-era) | convert maths, fee param | F |
| 39 | https://nautilustrader.io/docs/nightly/integrations/polymarket/ | NautilusTrader | 2026 nightly | order quirks, fee model, $1 min | F |
| 40 | https://status.polymarket.com/ and /history | Polymarket status | 2026-09-20 | uptime, incidents | F |
| 41 | https://www.cryptotimes.io/2026/08/31/polymarket-halts-trading-for-four-hours-after-same-failure-recurs-twice-in-a-day/ | The Crypto Times | 2026-08-31 | outage detail | F |
| 42 | https://coingape.com/block-of-fame/pulse/polymarket-is-rebuilding-its-clob-after-multiple-outages-vp-engineering-josh-stevens-says/ | CoinGape | 2026-09-01 | Rust rebuild | F |
| 43 | https://arxiv.org/html/2604.24366v1 | arXiv (P. Dubach) | 2026 | microstructure numbers | F |
| 44 | https://dspace.networks.imdea.org/bitstream/handle/20.500.12761/2065/Polymarket_Initial_Liquidity-3.pdf?sequence=1 | IMDEA / Lund (Jornell, Perez, Saguillo) | 2026 | opening spreads by category | F |
| 45 | https://blockchain.news/news/polymarket-fast-markets-volume-bots-fees-analysis | Blockchain.News (summarising Dune) | 2026-04-14 | fast-market stats | F |
| 46 | https://pineanalytics.substack.com/p/polymarket-fee-rollout | Pine Analytics | 2026 (c. April) | fee rollout, referral, revenue | F |
| 47 | https://cryptonews.net/news/market/32461495/ | CryptoNews.net | 2026-02-20 | 500 ms bump removed | F |
| 48 | https://www.bitget.com/news/detail/12560605442364 | Bitget News | 2026-06 | 250 ms rules | F |
| 49 | https://x.com/PolymarketDevs/status/2089295325660172578 | Polymarket Devs (X) | 2026-08 | 50 ms announcement | S |
| 50 | https://eventwaves.substack.com/p/trying-to-build-a-low-latency-polymarket | EventWaves | 2026-03-17 | practitioner latency report | F |
| 51 | https://latency.glassnode.com/prediction-markets/about | Glassnode | undated | origin London, Cloudflare | F |
| 52 | https://www.turbinefi.com/blog/prediction-market-arbitrage-latency-speed-2026 | Turbine (marketing) | 2026-05-26 | processing-time claim | F |
| 53 | https://www.quantvps.com/blog/polymarket-servers-location | QuantVPS (vendor) | 2026-07-04, upd. 09-18 | Dublin pings | F |
| 54 | https://newyorkcityservers.com/blog/polymarket-server-location-latency-guide | NYCServers (vendor) | 2026-04-07 | location claims | F |
| 55 | https://arxiv.org/abs/2605.00864 | arXiv (Cheng, Yang, Zou) | 2026-04-22 | NBA in-play arbitrage | F |
| 56 | https://crypto-economy.com/polymarket-activity-slides-35-with-monthly-volume-down-to-4-59-billion/ | Crypto Economy | 2026-09-08 | monthly volumes | F |
| 57 | https://www.shiftmarkets.com/prediction-markets-brief/august-2026 | Shift Markets | 2026-08 | July volumes, US-linked share | F |
| 58 | https://defirate.com/prediction-markets/volume/polymarket/ | DeFi Rate | 2026-09-20 | tracker mix, Kalshi share, wash note | F |
| 59 | https://www.theblock.co/data/decentralized-finance/prediction-markets/polymarket-new-markets-monthly | The Block | mod. 2026-09-01 | new markets per month | F |
| 60 | https://polymarket.com/predictions/all | Polymarket | 2026-09-20 | active market count | F |
| 61 | https://www.polymarketdata.co/polymarket-order-book-data | PolymarketData (vendor) | undated | third-party L2 history | F |
| 62 | https://telonex.io/ ; https://pmdata.dev/ ; https://archive.pendulumflow.com/ ; https://archive.pmxt.dev/Polymarket/v2 | vendors | undated | other L2 archives | S |
| 63 | https://blockchain.news/ainews/clis-as-agent-native-interfaces-2026-analysis-on-polymarket-cli-github-cli-and-mcp-for-ai-automation | Blockchain.News | 2026 | Rust CLI mention | S |
| 63b | https://www.quantvps.com/blog/polymarket-us-api-available ; https://defirate.com/news/polymarket-launches-public-api-unlocks-permissionless-liquidity/ | QuantVPS / DeFi Rate | 2026 | US retail API facts | S |
| 64 | https://finance.yahoo.com/markets/crypto/articles/polymarket-set-launch-combos-sports-094405317.html ; https://www.bitget.com/news/detail/12560605500754 | Yahoo Finance / Bitget | 2026-08 | combos launch and volume | S |
| 64b | https://www.cnbc.com/2026/04/21/polymarket-launches-trading-of-heavily-leveraged-perps-contracts.html ; https://www.bloomberg.com/news/articles/2026-09-03/polymarket-launches-perpetual-oil-futures-in-24-7-trading-push | CNBC / Bloomberg | 2026-04-21 / 2026-09-03 | perps | S |
| 65 | https://github.com/Polymarket/py-clob-client-v2/issues/53 ; /issues/70 | GitHub issues | 2026 | deposit-wallet SDK problems | S |
| 66 | https://github.com/Polymarket/polymarket-subgraph ; https://thegraph.com/docs/en/subgraphs/guides/polymarket/ | Polymarket / The Graph | undated | subgraph list | S |
| 67 | https://www.cftc.gov/filings/orgrules/rules03022640118.pdf | CFTC filing | 2026-03-02 | US fee amendment | S |
| 68 | https://finance.yahoo.com/markets/crypto/articles/polymarket-fee-overhaul-pushes-daily-054836739.html | Yahoo Finance | 2026-04 | $1M daily fees | S |
| 69 | https://www.businesswire.com/news/home/20260320997513/en/Polymarket-Publishes-Enhanced-Market-Integrity-Rules-Across-Its-DeFi-Platform-and-CFTC-Regulated-U.S.-Exchange | Business Wire | 2026-03-20 | integrity rules | S |
| 70 | https://www.theblock.co/post/366507/polymarket-uma-oracle-update | The Block | 2025-08 | managed oracle whitelist | S |
