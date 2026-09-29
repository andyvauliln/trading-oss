# Tooling ecosystem, open-source bots and service / data businesses
_As of 2026-09-20. Evidence pack E6 for the Polymarket strategy survey._

Evidence tags: **[H]** hard data (official docs, first-party API, on-chain-derived, paper, GitHub/npm metadata) · **[C]** credible named report · **[S]** self-reported · **[M]** marketing / affiliate / SEO. "(derived)" = my arithmetic on cited numbers. "Own query" = read-only call to a public Polymarket, GitHub or npm endpoint on 2026-09-20.

**Method limit.** The session's shared WebSearch budget was exhausted after 4 of my searches. The rest of this pack comes from fetched pages, the GitHub API (metadata and README text only) and documented public Polymarket endpoints. I did not substitute another search channel. Topics that needed open search (paid-signal revenues, security incidents, LaaS deals) are therefore thin and listed under open questions. No third-party code was installed or run.

## Key facts

1. **Builder-routed volume is public per app, per month** (`/v1/builders/volume`). It went $32.1M (Oct 2025, 11 builders) -> $612.0M (Mar 2026, 253) -> peak $1,493M (Jun 2026, 299) -> $648.8M (Aug 2026, 303) -> $453.1M for 1-20 Sep (286). Lifetime: $7.39B across 548 builder codes [2][H].
2. **Distribution is extremely concentrated.** Aug 2026: top-1 (betmoar) 21.1%, top-5 58.9%, top-16 81.3%; 48 builders >= $1M, 191 of 303 < $100k, 118 < $10k, median ~$30k (derived) [2]. At the documented 100 bps cap the median builder could gross at most ~$300/month (derived) [4].
3. **Builder fee caps are 100 bps taker / 50 bps maker, flat on notional, stacked on the platform fee**; one rate change per 7 days with 3 days' notice; rates public; codes can be disabled and fees revoked for "automated, self-referred, or other non-bona fide" flow [4][H].
4. **Every competitor's fee rate and fills are readable without auth**: `GET clob.polymarket.com/builder/trades?builder_code=...` (spec `security: []`) returns `builderFee`, `feeUsdc` (total, builder fee included), maker address, `owner` id and tx hash per fill [3][H]. The `builder` bytes32 is part of the signed V2 order and is emitted in every `OrderFilled` event [4].
5. **Observed builder fee rates (600 most recent fills each, 2026-09-20, own query [3])**: PolyCop 50 bps both sides; Polygun 100 taker / 50 maker; polymtrade 50 / 25; Bagel 100 / 50; Bitget Wallet, POTS, Stan, Based 100; Polycool 75 / 50; traderline 10 / 5; SpreadCore 5 / 0; **betmoar, Kreo, standtrade, PolyBot, NautilusTrader, Gate, Jupiter, MagicMarkets, Tailgate, PolyHelper: 0**. **MetaMask and RedotPay charge 400 bps on buys (0 on sells); Axiom 300 bps on both sides — above the documented cap**; the explanation (partner terms?) is unverified.
6. **Who earns (derived: monthly volume [2] x sampled rate [3]; assumes today's rate applied earlier)**: MetaMask ~$0.48M in Aug 2026 and ~$1.0M for 1-20 Sep; polymtrade ~$284k (Jul) -> ~$122k (Aug); PolyCop ~$385k at its Apr 2026 peak -> ~$97k (Aug) -> ~$38k (1-20 Sep); Polygun ~$350k (Mar) -> ~$26k (Aug); RedotPay ~$230k (1-20 Sep); Bagel ~$63k. Based: $9.7M in Dec 2025 x 1% = ~$1.16M annualised, matching Chainstory's "$1 million in annualized recurring revenue" [11][C]; Based routed $0.2M in Aug 2026 -> ~$2k/month.
7. **Copy / Telegram-bot flow collapsed after April 2026.** PolyCop + Polygun + Kreo + Polycule + PolyBot: $125.2M (Apr) -> $28.5M (Aug), -77%, while all builder volume fell 18%; share of builder volume 15.7% -> 4.4% (derived) [2]. Monthly active users: PolyCop 3,604 (Mar) -> 1,577 (Aug); Polygun 3,954 -> 887; Kreo 3,803 (Apr) -> 918; Polycule 1,312 (Dec 2025) -> 26 [2][H]. CLOB V2 and the fee regime arrived 28 Apr 2026 (E1); causality unverified.
8. **Growth moved to distribution and pro terminals**: Gate $0 -> $280.1M (Jun) with 19 active users in Sep ($2.9M per user); traderline $0 -> $225.5M (Jul); MetaMask 2,360-9,344 monthly users; RedotPay 3,687; betmoar $2.23B lifetime, 83% maker notional in the sample, ~$138k per active user per month, 0 bps fee [1][2][3][H].
9. **Measured all-in entry cost of a copy fill** (sampled taker fills, category mix as traded): PolyCop ~110 bps platform + 50 bps builder; Polygun ~103 + 100; median ticket $3.85 and $1.58; Kreo $1.07 [3][H]. This is before spread and post-leader price drift.
10. **The only public measured copy experiment found**: 2 leaders that passed a t-stat / concentration screen out of top-30 + 30 control wallets; paper $10k; 3 Jul - 12 Aug 2026: 191 trades -$1,937 (38.7% win), then 81 trades +$2,108 (46.9%) after an in-play filter; net +$171; copy delay 26-130 min initially, median 5.6 min (p90 9.6) after tuning; author attributes the turnaround to "the leader's regime"; copied-vs-skipped difference $15/trade, not significant [15][H, single small sample, 0 stars].
11. **Polymarket's own newsletter (with Stand.Trade) says sharp traders run secondary / tertiary accounts, iceberg entries, and exit through merges that do not show as sells; followers become exit liquidity**; 6 of the 10 most-copied wallets are crypto bots; Stand tracked "over 1,500 Polymarket wallets and 5,000 strategies in two months" [14][C].
12. **Official SDK surface was replaced in 2026**: legacy `py-clob-client` (1,231 stars), `clob-client`, `rs-clob-client`, `ctf-exchange` and `Polymarket/agents` (3,796 stars, last push 2024-11-05) are archived; live repos are `py-sdk` (128 stars, created 2026-05-04), `ts-sdk` (39), `py-clob-client-v2` (166), `rs-clob-client-v2` (142), `clob-client-v2` (74), `polymarket-cli` (2,878, "early, experimental software") [16][28][H].
13. **Supply-chain hazard**: `dev-polymarket/clob-client-v2` (512 stars, 291 forks, created 2026-05-04) tells users to install `@polymarkets/clob-client-v2` (extra "s"). npm: single maintainer `polymarkets`, created 2026-05-07, adds an `inquirer` dependency the official client lacks, 115 downloads last month vs 254,876 for the official `@polymarket/clob-client-v2` (74 stars) [17][H]. Suspected typosquat; package contents not inspected, malice unverified. Stars are inverse to real usage.
14. **NautilusTrader's Polymarket adapter is V2-only, Rust-native, supports all four signature types, and hard-codes a Nautilus builder code on every order (fee fixed at zero, "not configurable")** [18][H]. That code routed $33.6M lifetime, 153 active users in Sep 2026 [1][2]; every Nautilus user's fills are enumerable through [3]. Hummingbot has no Polymarket connector (no `polymarket` directory in `hummingbot/connector/exchange`; GitHub search finds three 0-star forks) [46][16][H].
15. **Data vendors and prices**: Telonex $99 / $199 per month (Polymarket trades, books, quotes, on-chain fills "since Nov 2022", Parquet; no Kalshi) [35][S]; Probalytics $39 / $129 / $249 (Polymarket books only from Nov 2025, Kalshi books from May 2026) [36][S]. **Polymarket acquired Dome (YC F25) on 2026-02-19** [37]; Probalytics says the acquisition "shut down" Dome [36].
16. **Referral**: 10% of net fees on direct and 5% on indirect referrals, ending at the earlier of 30 days or the referee reaching Platinum; referrer needs $10k lifetime volume; omnibus integrations and fee-free markets excluded; paid daily in pUSD [7][H]. Perps referral: 20% of referred fees, no per-user cap, weekly, invites gated 10 -> 500 by volume [8][H].
17. **Ecosystem size vs traction**: >= 200 projects claim to build on Polymarket, 114 verifiable; Q1 2026: 80% of builders < $1M for the quarter, a third < $10k, 16 platforms = 90% of volume; ~$20M disclosed venture funding into native builders [11][C]. Directories list 170+ tools (defiprime, Jan 2026) [12][M], 115 bots in 14 categories incl. 29 copy-trading and 19 Telegram (polbots) [32][M].
18. **"Fund / hedge / delegation" products checked are empty shells**: uma.rocks shows "0 UMA ($0) from 0 delegators" although directories still quote 14% APR [41][13]; Gondor (borrow against positions) is "Coming soon" [42]; PolyHedg is a demo dashboard for "John Doe" [42]; PolyFund discloses no TVL or fees [42].

## 1. Open-source landscape (GitHub API, 2026-09-20 [16][H]; stars | licence | last push)

13,667 repositories match "polymarket". Official org: 71 repos.

**Official.** See key fact 12. Also `real-time-data-client` 228 | MIT | 2026-03-05; `polymarket-subgraph` 217 | LGPL-3.0 | 2026-02-13; `agent-skills` 188 | none | 2026-02-19; `builder-relayer-client` 56 and `py-builder-relayer-client` 42 (no licence); `polymarket-us-python` 29 | MIT | 2026-09-17; `uma-ctf-adapter` 120; `neg-risk-ctf-adapter` 90. `Polymarket/poly-market-maker` 323 | MIT | last push 2024-07-05 [pre-2025, possibly stale]. `polymarket-cli` supports `-o json` for agents; README does not mention V2 [28].

**Market making.** `warproxxx/poly-maker` 1,503 | MIT | 2026-07-09: rewritten for CLOB V2, TOML + SQLite, Gamma discovery, `--paper`; README: "competitive and can lose money. This is a reference implementation and a research harness" [20]. `lihanyu81/polymarket_lp_tool` 526 | no licence | 2026-05-06.

**Arbitrage scanners.** `ImMike/polymarket-arbitrage` 282 (Polymarket + Kalshi, "10,000+ markets"); `CarlosIbCu/polymarket-kalshi-btc-arbitrage-bot` 250 (BTC 1-hour); `realfishsam/prediction-market-arbitrage-bot` 178 (built on pmxt); `rohanthomas1202/truthlayer` 65 (FAISS + LLM matching, fee-adjusted spreads, settlement-verified scoreboard). None publishes realised PnL.

**Copy trading.** `HarrierOnChain/Prediction-Markets-Trading-Bot-Toolkits` 453 | MIT | Rust, 122 commits, dry-run default, Telegram contact; its managed service was "never operational with real funds" [31]. `Drakkar-Software/OctoBot-Prediction-Market` 114; `Abomination81/copybot` 104 stars / 56 forks eight days after creation (2026-09-12); `shmlkv/polymarket-copy-trading-bot` 53; `BallesJr/polymarket-copy-trader` 0 stars, 1,520 commits, the only one with measured results [15]. A vendor review of ~12 repos: polling latency 30-90 s, no idempotent resubmission, single RPC, "maintenance half-life ~6 weeks", 60-120 engineering hours to harden [33][M].

**Frameworks / backtesting.** `nautechsystems/nautilus_trader` 29,201: L2 deltas, quotes, trades, resolution events; MARKET and LIMIT only; batch <= 15 orders; `PolymarketFeeModel` = `shares * rate * (p(1-p))^exponent` with maker rebates; `PolymarketDataLoader` [18]. `evan-kolberg/prediction-market-backtesting` 1,200 | mixed GPL-3.0 / LGPL-3.0 / MIT | 2026-05-16: Nautilus extension with fee, slippage, latency and queue-position models; PMXT and Telonex loaders; Kalshi research-only because historical L2 is unavailable [19]. `agent-next/polymarket-paper-trader` 394 | MIT; `braedonsaunders/homerun` 181; `ent0n29/polybot` 1,020 | MIT | Java + ClickHouse + Redpanda, no quantified results [29]. `pmxt-dev/pmxt` 2,158 | MIT: "CCXT for prediction markets", 15+ venues, local sidecar or hosted writes (Polymarket, Opinion, Limitless) [27]. ccxt's repo description now says "crypto exchanges and prediction markets"; Polymarket coverage unverified [16].

**Data.** `Jon-Becker/prediction-market-analysis` 3,848 | MIT: 36 GiB compressed Polymarket + Kalshi markets and trades [21]. `warproxxx/poly_data` 2,343 | GPL-3.0: v2 streams V2 `OrderFilled` via Envio HyperSync (token mandatory); the old pipeline "no longer returns complete data" after April 2026 [22]. `nahrek/polyledger` 623 | MIT | created 2026-09-02: V1 + V2 fills into one DuckDB file, exposes the `builder` field [23]. `SII-WANGZJ/Polymarket_data` 831 | MIT (1.1B records). Hugging Face `TimeSeventeen/Polymarket-v1`: 1.20B trades, 1.30M markets, $61B, 2022-11-21 -> 2026-04-28, CC BY-SA 4.0; the paper finds tick-rule classification "near-random" [24][H]. `pmxt-dev/polymarket-orderbook-collector` 22 | no licence: Rust WS -> ClickHouse -> hourly Parquet [47]. Official partners: Goldsky (+ ClickHouse CryptoHouse), Dune, Allium [10].

**AI agents.** `alsk1992/CloddsBot` 2,808 | MIT: monetises through a compute API, a 5% marketplace fee and $1 token launches, not through trading [30][S]. `caiovicentino/polymarket-mcp-server` 674 | MIT. `sterlingcrispin/nothing-ever-happens` 987 | CC0 (buys NO everywhere, "mostly a meme").

**Noise.** Keyword-stuffed descriptions are common: `radioman/polymarket-arbitrage-trading-bot` (account created 2016, C++, 522 stars), `txthinkin/...` 198 stars / 118 forks, `a2871031921/...` 34 stars / 158 forks [16]. `Novals83/5min-btc-polymarket` (1,313) and `FrondEnt/PolymarketBTC15mAssistant` (1,190) were created and last pushed on the same day. Stars are not a quality signal here (inference).

## 2. Analytics and tooling products

- **Terminals**: betmoar (0 bps, $2.23B lifetime, UMA dispute dashboard) [1][3][13]; traderline; SpreadCore (5 bps taker, median ticket $81.80); Stand (0 bps, $209M lifetime, 142 users in Sep) [1][3]; Kairos ($0 platform fee, $2.5M seed led by a16z crypto, spans Kalshi / Polymarket / Hyperliquid / Predict.fun) [40][S]; TradeFox (AllianceDAO, CMT Digital) [11].
- **Telegram / copy bots**: PolyCop (12,732 lifetime users), Polygun (9,941), Kreo (8,923, 0 bps), Polycule (3,106; $560k from AllianceDAO, Jun 2025; site shows no notice while volume is ~0) [1][11][50], PolyBot (2,580, 0 bps).
- **Wallet trackers / alerts**: PolyTrack $10/week, $99.99/year or $99.99 lifetime, 8 severity rules, states it does not place trades [38][S]; PolyInsider $5/week [13]; Polysights "Insider Finder", no public pricing on the landing page [39]; a 1.5 ETH/year premium appears only in a search summary (unverified) [12]. Hashdive and Stand pricing not retrievable (empty page / 403). An affiliate roundup lists 9 of 11 analytics tools as "Paid" with no prices [43][M].
- **Data vendors**: key fact 15; pmxt.dev hosted API with "3 years of OHLCV" [27][S].
- **Funding (Chainstory, 2026-04-09)** [11][C]: Based $11.5M Series A (Pantera, Feb 2026); FiammaLabs $4M; DoubleUp $4M at $40M; UnifAI $7M; Semantic Layer $5M; Predex $0.5M; Bullpen undisclosed (6th Man). Only 25 of 114 builders have a visible founder.

## 3. Service-business models and evidence they earn

| Model | Evidence | Tag |
|---|---|---|
| Builder fee on routed retail flow | Key facts 5-6. Fee-charging apps with users: MetaMask, RedotPay, polymtrade, PolyCop, Bagel, Polygun | H (derived) |
| Builder with 0 bps | betmoar, Kreo, Stand, Gate, PolyBot: revenue must come from "weekly USDC rewards based on volume (subject to approval)" and grants for Verified builders [5], or elsewhere; rate undisclosed. Chainstory's "0.5% to 1% of attributed volume" and the "$2.5 million" grant fund are estimates [11] | C, unverified |
| Relayer quota | Gas-free relayer; Unverified 100 tx/day, Verified 10,000/day, Partner unlimited; leaderboard lags up to 24 h [5][6] | H |
| Referral | Key fact 16; payout totals in E2 | H |
| Data / API resale | $39-$249/month list prices [35][36]; no revenue disclosed; Dome exit by acquisition [37] | S |
| Alerts / signals | $5-10/week [13][38]; no subscriber or revenue numbers found | S |
| Bots-as-a-service | polysyncer, polybot.trading, PolyCop: marketing only, except PolyCop's volume [2] | M / H |
| UMA delegation | uma.rocks at zero [41]; proposer economics in E3 | H |
| Vaults / funds / credit / hedging | No disclosed TVL or fees at any product fetched [42] | H (absence) |
| LaaS for sponsors, research sold to funds, media | Nothing verifiable found | gap |

**Where sources disagree.** SEO pages claim builder volume was "roughly 16%" of Polymarket trading in March 2026 [45][M]; $612M [2] against $10.5-12.2B (E4) is 5-6% (derived). An X post listed betmoar at $101M per 30 days [44][S]; the API shows $136.8M-$328.8M for every month from Feb to Aug 2026 [2]. Chainstory (Apr 2026) gives betmoar $817M lifetime [11]; the API gives $2.23B today [1].

## 4. Copy-trading reality

- **Cost floor**: ~1.6-2.0% all-in fees on entry for bot-routed taker fills (key fact 9) plus the exit leg; a leader grinding a 3% edge leaves almost nothing. The fees are hard data; the "spread business" framing is a Medium post that returned 403 [48].
- **Latency**: taker delay on crypto markets was cut 250 ms -> 50 ms on 2026-08-17 [9][H] (vendor explainer [34][M]); detection dominates anyway (minutes in [15]; 30-90 s polling in OSS bots [33]).
- **What followers cannot see**: secondary wallets, iceberg accumulation, merge exits [14]. Since 2026-08-10 `REDEEM` rows are per outcome and positions carry `entryFeesUsdc`; Data API v2 (2026-09-04) adds `/v2/user-pnl` [9].
- **Identification limits**: "public fills do not identify the quote lifecycle required to infer market making, spoofing, or strategic withdrawal" (13.36M fills, 77,204 addresses) [25][H]; only 88 of 12,708 markets gave a computable information-leakage score [26][H].
- **Measured uplift**: [15] only; the SSRN +1.62 pp result is in E4 [55] (SSRN returned 403 to me).
- **Demand**: copy-bot MAU fell 55-98% from peak (key fact 7); the product category is shrinking.

## 5. Gaps — asked for, not found (absence = not in fetched directories or vendors)

Demand signal: "Polymarket itself doesn't give you much data. You see a price, a chart, and a trade button" [49][C].

1. Historical L2 before Nov 2025 for Polymarket and before May 2026 for Kalshi [36][19][35].
2. Quote-lifecycle data (placements / cancels by wallet) [25].
3. A follower-realised PnL audit of copy products; no vendor publishes one.
4. Entity resolution across a trader's wallets [14].
5. Flow analytics keyed on the on-chain `builder` field [4][3]; none of 170+ listed tools advertises it [12][13].
6. Ground-truth aggressor side in live feeds [24] (E1: ~41% mislabelled).
7. A maintained Hummingbot connector [46].
8. A vault with disclosed TVL, fees and audited track record [42].
9. An independent cross-venue matched-event API after Dome's exit (pmxt, PolyRouter, Probalytics remain) [27][36].

## What a builder who already runs LP / cross-venue arb / resolution-sniping / copy-trading bots is likely to UNDERESTIMATE

1. **Order flow is labelled by app, on-chain and for free.** `builder` tags MetaMask, RedotPay and Bitget fills (100% taker, median $2-5, paying 4% + platform fee) as uninformed retail, and PolyCop / Polygun fills as follower flow [3][4]. It is a toxicity feature for quoting and a detector of copy cascades (inference; no PnL evidence).
2. **Your own flow is labelled too.** Nautilus hard-codes its code [18]; any builder code exposes fills, maker addresses and `owner` ids to everyone [3]. Do not route proprietary strategies through a labelled code.
3. **The money is in distribution, not tooling.** One wallet integration charging 4% out-earns every analytics and copy product combined (key fact 6). A solo team without an audience is the median builder: ~$30k/month routed [2].
4. **Copy trading is a declining business as well as a weak strategy**: -77% volume in four months [2]. Build selection and audit, not another mirror.
5. **Builder revenue is revocable and transparent**: codes can be disabled, "automated" or "self-referred" flow forfeits fees, rates are public and can be undercut to 0 bps by funded terminals [4][3].
6. **Dependency risk**: legacy SDKs archived within months, a Goldsky-based pipeline silently incomplete after V2 [22], Dome acquired and closed [36][37], a lookalike SDK with 7x the official repo's stars [17]. Pin by commit and verify npm scope and maintainers.
7. **Public copy-target data is structurally incomplete** [14][25]; PnL rank is not skill (E4).
8. **Referral pays for at most 30 days per user** [7]; it is an acquisition rebate, not an annuity. Perps referral (20%, uncapped) is the better-paying line [8].
9. **The listed fund, credit and hedge layer does not exist yet** [41][42]; outside capital has no verified on-ramp — an opening and a regulatory question.

## Could not verify / open questions

- Why MetaMask, RedotPay (400 bps) and Axiom (300 bps) exceed the documented cap; whether `feeUsdc` semantics are the same for every builder [3].
- Whether leaderboard `volume` counts one or both sides, and whether today's fee rates applied in earlier months (all revenue figures are derived).
- The weekly USDC reward rate for Verified builders; betmoar's and Stand's actual revenue.
- Cause of the April-to-August copy-bot collapse and of Polycule's fall to ~0 (no notice on its site [50]).
- Whether `@polymarkets/clob-client-v2` is malicious (not inspected).
- Revenue or subscriber counts for any signal group, newsletter or data vendor; any liquidity-as-a-service deal with market sponsors; research sold to funds.
- Hashdive, Stand, Polymarket Analytics, predicts.guru pricing (403 / 429 / empty pages).
- Whether any tool clusters wallets or classifies flow by builder code (absence is from directories only).
- Whether the [15] experiment's fills would have been achievable live (paper trading).

## Source ledger

| n | URL | Publisher | Date | Supports | F/S |
|---|---|---|---|---|---|
| 1 | https://data-api.polymarket.com/v1/builders/leaderboard | Polymarket Data API | queried 2026-09-20 | builder volume, users, verified flag | F |
| 2 | https://data-api.polymarket.com/v1/builders/volume?timePeriod=MONTH | Polymarket Data API | queried 2026-09-20 | monthly volume and users per builder | F |
| 3 | https://clob.polymarket.com/builder/trades (spec: https://docs.polymarket.com/api-reference/trade/get-builder-trades.md) | Polymarket CLOB API / docs | queried 2026-09-20 | per-fill builder and total fees, ticket sizes, taker share | F |
| 4 | https://docs.polymarket.com/programs/builders/fees.md | Polymarket docs | undated | caps, formula, rate-change rules, on-chain attribution, revocation | F |
| 5 | https://docs.polymarket.com/programs/builders/tiers.md | Polymarket docs | undated | tiers, relayer limits, weekly rewards | F |
| 6 | https://docs.polymarket.com/programs/builders/overview.md | Polymarket docs | undated | benefits, 24 h leaderboard lag | F |
| 7 | https://docs.polymarket.com/programs/referral-program.md | Polymarket docs | undated | referral terms | F |
| 8 | https://docs.polymarket.com/perps/referral-program.md | Polymarket docs | undated | perps referral terms | F |
| 9 | https://docs.polymarket.com/changelog/predictions.md | Polymarket docs | to 2026-09-04 | taker delay, Data API v2, redeem rows | F |
| 10 | https://docs.polymarket.com/resources/blockchain-data.md | Polymarket docs | undated | official data partners | F |
| 11 | https://www.chainstory.co/the-invisible-ecosystem-who-actually-builds-on-polymarket/ | Chainstory | 2026-04-09 | 114 builders, Q1 concentration, funding, Based ARR | F |
| 12 | https://defiprime.com/definitive-guide-to-the-polymarket-ecosystem | DeFi Prime | 2026-01-11 | 170+ tools directory | F |
| 13 | https://github.com/aarora4/Awesome-Prediction-Market-Tools | GitHub list | pushed 2026-09-03 | tool catalogue, some prices | F |
| 14 | https://news.polymarket.com/p/copycat | Polymarket (The Oracle) + Stand.Trade | 2026-04-24 | concealment tactics, most-copied wallets | F |
| 15 | https://github.com/BallesJr/polymarket-copy-trader | GitHub | snapshot 2026-08-12 | measured copy experiment | F |
| 16 | GitHub search API (queries: `polymarket`, `org:Polymarket`, copy trading, kalshi arbitrage, hummingbot, orderbook recorder) | GitHub | queried 2026-09-20 | stars, licences, push dates | F |
| 17 | https://github.com/dev-polymarket/clob-client-v2 ; https://registry.npmjs.org/@polymarkets%2fclob-client-v2 ; https://api.npmjs.org/downloads/point/last-month/@polymarket/clob-client-v2 | GitHub / npm | queried 2026-09-20 | lookalike SDK metadata and downloads | F |
| 18 | https://nautilustrader.io/docs/latest/integrations/polymarket/ | Nautech Systems | undated | adapter scope, hard-coded builder code | F |
| 19 | https://github.com/evan-kolberg/prediction-market-backtesting | GitHub | pushed 2026-05-16 | backtesting models, vendors | F |
| 20 | https://github.com/warproxxx/poly-maker | GitHub | pushed 2026-07-09 | MM bot, warning | F |
| 21 | https://github.com/Jon-Becker/prediction-market-analysis | GitHub | pushed 2026-09-20 | 36 GiB dataset | F |
| 22 | https://github.com/warproxxx/poly_data | GitHub | pushed 2026-09-08 | V2 pipeline, HyperSync | F |
| 23 | https://github.com/nahrek/polyledger | GitHub | created 2026-09-02 | DuckDB indexer, builder field | F |
| 24 | https://arxiv.org/abs/2606.04217 | arXiv, Qin & Yang | 2026-06-02 | Polymarket-v1 dataset, classification error | F |
| 25 | https://arxiv.org/abs/2605.11640 | arXiv, Nechepurenko | 2026-05-12, rev. 2026-07-30 | identification limits of fills | F |
| 26 | https://arxiv.org/abs/2605.00459 | arXiv, Nechepurenko | 2026-05-01 | information-leakage score coverage | F |
| 27 | https://github.com/pmxt-dev/pmxt ; https://pmxt.dev | pmxt | pushed 2026-07-18 | unified API | F |
| 28 | https://github.com/Polymarket/polymarket-cli | Polymarket | pushed 2026-05-26 | CLI scope, warning | F |
| 29 | https://github.com/ent0n29/polybot | GitHub | pushed 2026-02-20 | architecture | F |
| 30 | https://github.com/alsk1992/CloddsBot | GitHub | pushed 2026-09-18 | monetisation | F |
| 31 | https://github.com/HarrierOnChain/Prediction-Markets-Trading-Bot-Toolkits | GitHub | pushed 2026-09-07 | copy bot, managed-service status | F |
| 32 | https://github.com/sssobolevski/polymarket-bots | polbots.com list | undated | 115 bots, 14 categories | F |
| 33 | https://www.polysyncer.com/blog/polymarket-copy-trading-bots-github | Poly Syncer (vendor) | undated | OSS copy-bot defects | F |
| 34 | https://polybot.trading/blog/polymarket-taker-delay-250ms-to-50ms | PolyBot (vendor) | 2026 | taker-delay explainer (confirmed by [9]) | F |
| 35 | https://telonex.io | Telonex | undated | coverage, prices | F |
| 36 | https://probalytics.io ; https://probalytics.io/pricing | Probalytics | undated | coverage, prices, Dome shutdown claim | F |
| 37 | https://domeapi.io ; https://domeapi.io/blog | Dome | 2026-02-19 | acquisition by Polymarket | F |
| 38 | https://polytrack.cash | PolyTrack | undated | prices | F |
| 39 | https://www.polysights.xyz/ | Polysights | undated | features | F |
| 40 | https://kairos.trade | Kairos | undated | $2.5M seed, fees | F |
| 41 | https://www.uma.rocks | UMA.rocks | (c) 2024 | 0 UMA delegated | F |
| 42 | https://www.polyfund.so ; https://gondor.fi ; https://polyhedg.com | product sites | undated | status of fund / credit / hedge products | F |
| 43 | https://coincodecap.com/polymarket-analytics-tools | CoinCodeCap (affiliate) | 2026-01-15, upd. 2026-08-03 | no prices disclosed | F |
| 44 | https://x.com/top7ico/status/2043666799137280146 | X, @top7ico | 2026 (exact date unverified) | 30-day builder volumes | S |
| 45 | https://www.botforkalshi.com/blog/polymarket-builder-program-guide ; https://polymart.app/blog/polymarket-builders-program | SEO blogs | 2026 | "16%" share claim | S |
| 46 | https://github.com/hummingbot/hummingbot (directory `hummingbot/connector/exchange`) | Hummingbot | queried 2026-09-20 | no Polymarket connector | F |
| 47 | https://github.com/pmxt-dev/polymarket-orderbook-collector | pmxt | created 2026-07-31 | recorder architecture | F |
| 48 | https://medium.com/@shailamie/copy-trading-on-polymarket-is-a-spread-business-choose-your-bot-accordingly-2026-fa59cce51857 | Medium | Aug 2026 | "copy tax" framing | S (403) |
| 49 | https://stacymuur.substack.com/p/polymarket-trading-tools-masterclass | Substack (paywalled) | 2026-01-19 | native UI lacks data | F |
| 50 | https://www.polycule.trade | Polycule | undated | no incident notice | F |
