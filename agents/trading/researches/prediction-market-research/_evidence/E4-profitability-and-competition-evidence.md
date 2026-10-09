# Who actually makes money on Polymarket: empirical evidence
_As of 2026-09-20. Evidence pack E4 for the Polymarket strategy survey._

Evidence tags: **[H]** hard data (on-chain study, paper, official leaderboard/docs) · **[C]** credible report (named outlet or analyst summarising data) · **[S]** self-reported · **[M]** marketing / affiliate / SEO. "(derived)" = my arithmetic on cited numbers. Fee mechanics live in E1, incentive programs in E2; they are referenced here only where they change who profits.

## Key facts

1. **84.1% of 2.5M addresses have realised PnL <= 0; 2% made > $1k lifetime, 0.32% > $10k, 0.033% (840 addresses) > $100k** (Dune, Apr 2024 - Apr 2026; open positions count as losses, so the loser share is overstated) [6][H]. An earlier cut of 1.7M addresses gave 70% losers and < 0.04% of addresses taking > 70% of $3.7B profits [7][C].
2. **Top 1% of positive-PnL users capture 76.5% of profits** (588M trades, $67B volume, Nov 2022 - Mar 2026). Winners "provide liquidity using limit orders that resolve favorably"; losers "take liquidity using market orders". Insider trading "unlikely" to explain the largest winners [8][H]. About 1,200 accounts (0.05%) took $591M, more than half of all profits, mostly via thousands of probably-automated trades in the last 18 months [9][C].
3. **Only 3.14% of 1.72M accounts are statistically skilled; with market makers (< 0.5% of accounts) they take > 30% of gains. Only 12% of the biggest raw-PnL winners pass the skill test; ~60% of "lucky winners" become losers out of sample; 44% of skilled accounts stay skilled in the hold-out half** (LBS/Yale, $13.76B volume, 2023-2025) [12][13][14][H].
4. **The "$40M arbitrage" headline is $39.69M (derived): $10.58M single-condition + $29.02M neg-risk rebalancing + $0.095M combinatorial**, Apr 2024 - Apr 2025, 17,218 conditions, 41% with at least one opportunity, >= 5c/$ threshold, positions matched within a 950-block window (paper: ~1 h) [1][2][H]. Top-10 addresses = $8.18M = 20.6% (derived); #1 made $2.01M in 4,049 transactions (~$496 each, derived) [1].
5. **A stricter, mechanism-linked reconstruction finds $1.12M of neg-risk arbitrage through Dec 2025** ($1.086M via the NO->YES converter, $32k settlement baskets), ten addresses = 75% of converter profit, and re-running the $40M method on the overlapping window gives $291k. **Median converter profit fell from ~1 USDC per conversion (to Jul 2024) to 0.08 USDC by early 2026** [3][H].
6. **Favourites barely pay: purchases at >= 0.90 earn +0.83c per dollar pooled (+0.28c equal-weighted per market) and are 43.0% of all dollars paid; purchases < 0.10 lose 19.3c per dollar pooled** (560.9M purchases, 591k resolved markets, Nov 2022 - Mar 2026) [19][H].
7. **Favourite-longshot bias is absent in Sports**: sports longshots +2.4% (equal-weight) / +18.1% (pooled), sports favourites -0.23% / +0.14%; it is strong in Politics (-16.3% / -46.2% longshots), Crypto (-14.8%), Culture (-26.5%), Weather (-25.2% equal-weight), Tech (-20.7%) [19][H].
8. **Political prices are underconfident (compressed toward 50%)**: recalibration slope 1.45 on Polymarket; on Kalshi 1.83 at 1 week - 1 month, so a 0.70 political price one week out maps to ~0.83. Sports and crypto sit near 1.0-1.06 [20][H].
9. **Spreads: ~400 bps full quoted spread at mid 0.40-0.60, 1,300-1,800 bps in the lowest-price decile; median effective maker count 32 (HHI-based), ~8 in the most concentrated decile and ~3 at the extreme; L1/L10 depth ratio 0.137** (600-market panel, 30.3B book events, 21 Feb - 15 Apr 2026) [23][H].
10. **Public-feed trade direction matches on-chain truth only 59% of the time** (95% CI 54-66%); effective-spread sign flips on 50-67% of top-100 markets when you switch source [23][H].
11. **Official all-time profit leaderboard (fetched 2026-09-20)**: Theo4 +$22.05M on $43.0M volume; swisstony +$18.42M on $1.85B; Fredi9999 +$16.62M; RN1 +$12.67M on $1.26B; kch123 +$11.35M on $293M [35][H]. Margins on volume (derived): Theo4 51%, swisstony 1.0%, RN1 1.0%, kch123 3.9%.
12. **Informed/insider flow is measurable**: 210,718 flagged wallet-market pairs, 69.9% win rate, ~$143M anomalous profit (Feb 2024 - Feb 2026) [25][H]; 1,950 suspected insider accounts whose trades move price 7-12x more per dollar than skilled trades [12][14][H].
13. **15-minute crypto "latency arb" did not survive the fee regime**: taker fee introduced in the first week of Jan 2026 (press quoted up to ~3.15% at 50c; E1 records the changelog curve) [28][C]; the poster-child wallet 0x8dxd ($313 -> ~$414-438k in a month, 98% "win rate") [27][C] was "inactive since March" per Polymarket's own newsletter [30][C] (and an on-chain reconstruction says 94% of its trades were paired YES+NO buys, not spot-lag snipes [29]). Bots are 55-62% of fast-market volume; 6,189 bot addresses made 56M trades at $6-7 each [31][C].
14. **Professional desks are in**: Jump (~20 staff, equity in Polymarket scaled to capacity provided to the US venue) [42][C]; Wintermute two-sided quoting from 2026-06-01, plus SIG, DRW, Galaxy, Flow Traders [43][C][44][C]; Polymarket is building an in-house desk for RFQ parlays [45][C]. The LBS/Yale co-author expects the skilled share to fall from 3% to below 1% [15][C].
15. **Volume**: ~$9B in 2024 [50]; $1.16B in Jun 2025 [48]; $3.02B Oct 2025 [50]; Mar 2026 $10.5B (Sacra) to $12.2B (DeFi Rate) [50][53]; Jun 2026 international ~$10.3-10.7B ([53]; derived from "-26% to $7.9B in July" [54]); Jul 2026 $12.89B incl. US; Aug 2026 $8.16B (-36.7%) [47]. Kalshi is now 4-5x larger ($37.17B Aug 2026) [47][H/C].
16. **Retail flow is sports + short crypto**: since Jul 2024 Polymarket is 39% sports, 32% politics, 20% crypto (Kalshi 80% sports) [49][C]; median Polymarket user makes 46 trades in six weeks at $6.50 and loses < $2 on ~$600 staked; users with 1,000+ trades: median -$140, 33% lost > $1k, 27% won > $1k [17][H].
17. **World Cup winner market: 194,422 addresses, 66.7% lost; 54 addresses (0.03%) took ~60% of profits ($22.3M); 58k winners averaged $4.85** [18][C].
18. **Wash/self-trade**: ~25% of historical volume, 45% in sports, peaking ~60% of weekly volume in Dec 2024 (Columbia, Nov 2025) [24][C]; 15% of politics volume Dec 2025 - Feb 2026 (Solidus) [16][C]; median per-market self-counterparty share 0.97%, p99 10.6%, max 22.2% in Feb-Apr 2026 [23][H].

## 1. Trader profitability and concentration

- Sergeenkov (Dune, realised PnL from OrderFilled / PayoutRedemption / PositionsSplit / PositionsMerge USDC flows, 10 system addresses excluded): 15.9% profitable; average monthly profit > $5k for 0.26% (~6,600 addresses), of which 53.4% were active one month only and 2.6% (172 addresses) active 13+ months; >= $5k in four consecutive months: 0.015% [6][H]. **Roughly 170 addresses earn a durable salary.**
- PANews / on-chain "six profit models" report (86M transactions, Apr 2024 - Dec 2025): 0.51% of wallets with PnL > $1k; 1.74% with volume > $50k; "90% of orders >= $10k occur above $0.95" [34][C]. The 0.51% vs 2% gap with [6] is unexplained (different cut-offs and PnL definitions).
- Akey, Gregoire, Harvie, Martineau (CEPR DP21615, 2026-06-12): concentration as in Key fact 2; monthly performance "modestly persistent", possibly selection [8][H]. The per-user dataset (daily MTM PnL, ~87 behavioural features, 2022-11-11 -> 2026-03-29) is public on Hugging Face `vgregoire/polymarket-users` [11][H] — the best available training set for wallet-selection models. Press summary: 2,469,589 users, ~30% in profit, 69% losing $650M in total; odds slightly better in weather/tech, slightly worse in sports [10][9][C]. The $650M loss total and the "$591M = more than half of profits" figure come from different secondary reports and do not reconcile; unverified against the paper (SSRN 403).
- Solidus Labs, politics markets Dec 2025 - Feb 2026: 0.55% of profitable maker wallets took 50% of maker gains, 0.26% of winning taker wallets took ~50% of taker gains, ~$8M each of ~$16M [16][C]. Elite takers exist: informed taking pays, uninformed taking does not.
- Pew (11,989 wallets, 10 high-volume events, 7 May - 19 Jun 2026): 58% within +/- $100; 7% > +$1k, 9% < -$1k; sports-first users median 69 trades at ~$9, crypto-first 59 at < $4, politics-first 13 at $6 [17][H].

## 2. Arbitrage profit estimates — and why they disagree

| Study | Window | Method | Profit | Tag |
|---|---|---|---|---|
| Saguillo et al., AFT 2025 [1][2] | Apr 2024 - Apr 2025 | position bundles within ~950 blocks, >= 5c/$ | single-condition long $5.90M, short $4.68M; neg-risk buy-YES $11.09M, sell-YES $0.61M, buy-NO $17.31M, sell-NO $0.004M; combinatorial $95k (4 of 11 dependent pairs, all US-election) | H |
| Gebele, Mutzel, Matthes [3] | all events to Dec 2025 (32,702 events, 259M trades) + CLOB sample 14 Apr - 19 May 2026 | conversions matched within 5 blocks (~10 s), taker fees assumed | $1.12M total | H |
| Cheng, Yang, Zou [4] | 173 NBA games, 75M book snapshots | executable, depth-aware | 7 single-market episodes (median 3.6 s); 290 combinatorial episodes, median 101 bps, 76.9% capped at ~14.8 shares | H |
| Gebele & Matthes [5] | 100k events, 10 venues, 2018-2025 | semantic matching | ~6% of events cross-listed; execution-aware deviations 2-4% on average, persistent | H |

- Reading: the $40M is profit of wallets that assembled a complete set below $1 within the window, not atomic arbitrage; it is dominated by 2024-election politics, "Sports are largely absent" [1]. The strict number is ~35x smaller; [3] attributes the gap to method ([1] used block VWAPs carried forward up to 5,000 blocks).
- Structure of what remains: YES-side violations (no on-chain converter) 2,098 episodes vs 36 NO-side; NO-side episodes median 7.99 s vs 16.15 s YES-side (NO-side n=5) [3]. The unexploited side is the one needing capital locked until settlement.
- DL News on [1]: top-3 wallets 10,200+ bets, $4.2M, typical edge 1-5% [33][C] (my sum of Table 1 top-3: $4.38M).
- Cross-venue: the 2-4% deviations [5] are gross of Kalshi fees, capital lock-up and rule mismatch; no study of *realised* Polymarket-Kalshi arb profit was found.
- The widely repeated "arb window fell from 12.3 s (2024) to 2.7 s (Q1 2026); 73% of arb profit goes to sub-100 ms bots; median spread 0.3%" traces only to an unsourced Medium/SEO chain [57][M]. Do not use as a design number.

## 3. Makers vs takers; market-maker PnL

- Direct Polymarket evidence: winners are limit-order providers whose resting orders resolve favourably [8][H]; market makers are < 0.5% of accounts and sit in the > 30%-of-gains group [13][H]. No paper isolates reward-farming LP PnL net of adverse selection; per-maker dollar figures circulating in press ("~$11.8k per market-maker account") could not be traced to the paper — unverified.
- Longshot purchases by order type: buyer posted the offer -3.5% (equal-weight) vs buyer hit the seller's offer -31.2%; posted-offer longshot buys look good short-term (+3.9% at 5 min, +16.9% at 1 h) but -36.3% at resolution [19][H]. Passive fills capture spread but carry the outcome.
- Kalshi comparator (Burgi, Deng, Whelan): takers lose ~32% on average, makers ~10%; both show favourite-longshot pattern [22][H, snippet only]. Being a maker reduces the loss; it does not by itself create profit.
- Maker population: median 32 effective makers per market, concentrated tail (~3 at the extreme) [23][H]. Public fills cannot identify quote lifecycle, so "is this wallet a market maker?" is not answerable from fills alone [61][H].
- Self-reported LP: @defiance_cr, $10k start, ~$200/day rising to $700-800/day at peak; "80-200% annualised" in new markets [34][S, 2025-era, pre-fee regime].
- Informed flow that LPs face: 1,950 suspected insider accounts [14]; $143M anomalous profits, cases: ~$553k (Iran strike), ~$485k from $38.5k (Maduro), > $1M (Google Year in Search) [25][H]; three new accounts made > $630k on Maduro [12]. Geopolitics is fee-free, so it has no maker-rebate pool [62], and it is where the largest documented cases (Iran, Maduro) sit.
- 44,976 price dislocations (>= 5 pp, concentrated one-sided flow) in 2024-2025; moving a market 5 pp and getting it cited costs ~$0.7-1.0M [26][H].

## 4. Accuracy, calibration, documented biases

- **Favourite-longshot**: Key facts 6-7. Grouping matters: longshots -6.3% per contract, but +4.1% when grouped by parent event (multi-outcome events pay one longshot) [19]. Top-decile habitual longshot buyers supply 26.6% of next-month low-price dollars and 22.6% of gross losses; habitual favourite buyers earn +0.25% vs +0.88% for others [19]. Longshot-buyer classification persists 68.5% at one month, 30.4% at six [19].
- **Fee overlay (derived from [19] and [62])**: taker fee as a share of outlay is feeRate x (1-p). At p=0.95: crypto 0.35%, sports 0.25%, politics 0.20%. Against pooled favourite returns of +0.54% (crypto), +0.14% (sports), +1.42% (politics), +1.83% (finance): **taker-side favourite buying is net negative in sports, marginal in crypto, still positive in politics/finance, fee-free in geopolitics.** The sample predates most fees, so post-fee returns are untested.
- **Domain/horizon calibration** (353M trades, 429k contracts, Kalshi + Polymarket): politics underconfident at every horizon (Kalshi slopes 1.34 at 0-1 h, 1.83 at 2 d - 1 mo, 1.73 at 1 mo+); weather overconfident inside 48 h (0.69-0.97); model explains 87.3% of calibration variance in-sample, 71.5% out-of-sample; about half of raw slope variation is noise; the Kalshi large-trade effect (1.74 vs 1.19) does not replicate on Polymarket [20][H].
- **Partisan skew**: 79 Nov-2024 D-vs-R markets: 97.5% correct at 7 days, 93.7% at 1 day; every miss was a predicted Democrat win that went Republican (3.6% / 6.3% pro-Democrat error) — small, correlated sample, published by Polymarket [21][C].
- **Round-number and generic time-decay effects**: no Polymarket-specific empirical study found (open question).
- **LLM forecasters**: six frontier models live, 12 Jan - 9 Mar 2026: -1.1% average on Polymarket, -22.6% on Kalshi [56][H, snippet]; a "proper betting" rule on AI forecasts made +80.33% (Sharpe 3.35) in one live month on Kalshi — one month, one team [59][S].

## 5. Documented bot profits by type

| Bot type | Evidence | Tag |
|---|---|---|
| Short crypto up/down | 0x8dxd: $313 -> $414-438k, Dec 2025 - 6 Jan 2026, 6,615 predictions, $4-5k clips [27]. Independent on-chain reconstruction: 94% of its trades were symmetric YES+NO buys, median position < $6 — i.e. paired/both-sides structure, not pure spot-lag sniping [29]. Inactive since Mar 2026 [30]. Another bot "$2.2M in two months" via ensemble models [27]. | C / S — sources disagree on what the strategy was |
| Fast-market population | bots 55-62% of 5/15-min volume vs 31% in daily/weekly; 5-min markets $2.3B in ~7 weeks; crypto fees $23.7M in 83 days ($286k/day) [31] — that fee pool is now the bots' cost line | C |
| Neg-risk converters | $1.086M lifetime to Dec 2025, top-10 = 75%, median $0.08/conversion by early 2026 [3] | H |
| Sports, systematic | swisstony +$18.4M / $1.85B [35]; RN1 +$12.7M / $1.26B [35]; both buy underdogs (RN1 53% of trades under 50c, swisstony 60%+ of entries under 50c) [30]; earlier snapshots: swisstony $4.96M on $494M with 353 orders in 30 min (Jan-Mar 2026) [29], ~$45 average profit per position [36]. "Stadium-feed / broadcast-delay" explanations come from X threads [40][39][M/S]; [29] classes 14 of 18 top sports wallets as directional buy-and-hold, not latency | H for PnL, S/M for mechanism |
| Sports, small scale | esports sportsbook-vs-Polymarket bot: $4,973 net on $95,830 volume, 3,858 bets, 6 Jan - 31 Mar 2026; completed two-sided arbs +$8,293, unhedged legs -$3,185; 236 cancelled matches refunded at 50c hurt high-price legs; stopped as "more competition for the market making and fees got introduced" [32] | S (detailed, plausible) |
| End-of-market / "bond" | Sharky6999: ~$1M lifetime, 95% of trades above 80c [30]; one wallet on 2026-04-29 held $11.95M cost basis at 99.47c average entry for $33k unrealised profit, 48% in one Iran market [58] | C / S (snippet) |
| News / LLM bots | no on-chain study isolates them; skilled accounts "react faster to news" [13]; viral "AI agent made six figures in a week" claims had no on-chain verification that I could find | M |
| Domain specialists | fengdubiying $3.13M on League of Legends (74.4% win rate); weather trader entering only at > 77% model probability; one backtested knowledge strategy collapsed forward [29]; ColdMath (city temperatures) [30]; HyperLiquid0xb $1.4M sports [34] | C / S |

## 6. Named traders and firms

- **Theo** (French ex-bank trader): ~$85M across up to 11 wallets on the 2024 election, commissioned "neighbour-effect" polls [37][C, snippet][pre-2025, possibly stale]. Three of his named wallets (Theo4, Fredi9999, PrincessCaro) still hold #1, #3, #16 all-time = $44.8M (derived) [35]. Theo4: $22M from 18 positions (~$1M each) [36].
- **Domer**: geopolitics/elections, ex-poker pro, 5,000+ markets, ~$300M volume; "it's all manual... most of my trades are my orders being matched" [38][S][pre-2025, possibly stale]; 2026: "you are very likely not seeing his full book" [30]. A discretionary *maker*.
- **Category leaders (May 2026 snapshot)**: top-10 politics wallets $94M combined, top-10 sports $60M, top crypto $25M; MonsieurDimanche $15M across nine categories, none > 31% [36][C].
- **kch123** (sports #1 at the time, $10.35M): -$479k over 30 days, 31% win rate over 7 days in Q1 2026 [29] — top sports PnL is high-variance directional.
- **Firms**: Jump [42]; Susquehanna (Kalshi's first institutional MM, Apr 2024; whether it quotes Polymarket is unverified — sources disagree), DRW ($175-200k base trader roles), Akuna (sports quants), Wintermute, Galaxy, Flow Traders; IMC out, Citadel Securities "possible" [43][44][C]. ICE committed $2B ($1B Oct 2025, $600M Mar 2026) [43].
- **Effect on spreads**: no clean before/after measurement exists. Only data point is the Feb-Apr 2026 level (~400 bps mid-book, 13-18% in longshots) [23]. A synthetic study claiming -14% quoted / -19% effective spread after designated-MM activation [43] was withdrawn by its author [63] — do not cite as evidence.

## 7. Volume, OI, traders, market mix

- Active traders: ~462k Jan 2025 -> 242k Jun 2025 while volume per account rose $2.7k -> $4.8k [48][C]; record 688k MAU Feb 2026 [51][C]; ~840k monthly unique wallets by Feb 2026 [46][C]; The Block shows 210,367 for Sep 2026 month-to-date [52][H, partial month].
- Flow by wallet type: wallets with 10,000+ lifetime fills = 35.2% of trades; 11-1,000 fills = 44.7%; one-time traders < 0.2% [46][C].
- Single-day record $425M on 2026-02-28 (Iran); "Khamenei out" $930k -> $39M in 24 h; event markets drew 45-70k unique wallets [46][C].
- Polymarket US: $1.3B Apr -> $1.8B May [50] -> $5.0B Jul 2026 (+54% m/m) while international fell 26% to $7.9B [54][C, snippet].
- OI ~$411-458M and TVL ~$356M (tracker snippets, Sep 2026) [60][C, snippet] — small relative to ~$8-13B monthly volume: capital turns over fast; most volume is short-dated sports/crypto.
- DeFi Rate's month series has visibly broken values (May 2026 $336M, Aug $3.47B) [53]; prefer The Block's series [47].

## 8. Edge-decay ledger

| Edge | Worked | Evidence of decay | Tag |
|---|---|---|---|
| Neg-risk conversion arb | 2024 (election) | median $1 -> $0.08 per conversion by early 2026; 36 NO-side violations vs 2,098 YES-side [3] | H |
| Same-market YES+NO < $1 | 2024 | NBA: 7 episodes in 173 games, 3.6 s [4] | H |
| Spot-lag sniping on 15-min crypto | Q4 2025 | taker fee from the first week of Jan 2026 [28]; flagship wallet dormant since Mar 2026 [30]; subsequent taker-delay and TWAP-settlement changes (see E1) | C |
| Sportsbook-vs-Polymarket esports quoting | Q1 2026 | author quit Apr 2026: competition + fees [32] | S |
| Copying leaderboard PnL | 2024-25 | 60% of lucky winners revert [12]; whales iceberg, merge, use secondary wallets [30] | H / C |
| Being "skilled" at all | 2023-25: 3% of accounts | co-author Jensen expects < 1% as institutions arrive [15] | C (forecast, snippet) |
| Big directional political bets | 2024 | not decayed but non-repeatable: top-3 Theo wallets are one trade [35][37] | H |

## What a builder who already runs LP / cross-venue arb / resolution-sniping / copy-trading bots is likely to UNDERESTIMATE

1. **The executable arb pie is ~$1M, not $40M, and ten addresses own 75% of it** [3]. The under-exploited side is YES-basket violations that lock capital to settlement [3] — a balance-sheet trade, not a latency trade.
2. **Winners are informed makers, not reward farmers.** Profit comes from limit orders that "resolve favorably" [8]; on Kalshi the average maker still loses ~10% [22]. An LP bot without a fair-value model is the counterparty of the 3% skilled flow and ~$143M of informed flow [12][25]. Mark LP PnL at resolution, not at 5 minutes: passive longshot fills show +17% at 1 h, -36% at resolution [19].
3. **Resolution/near-certainty buying earns ~0.3-0.8% gross per dollar** [19]; as a taker it is negative in sports and marginal in crypto after fees (derived, [62]); 43% of all dollars already chase it [19]. It survives maker-side, in politics/finance/geopolitics, with strict rule-reading — and with tail sizing (one wallet: $11.9M at risk for $33k [58]).
4. **Leaderboard PnL is mostly luck or one-offs.** 12% of top winners pass a skill test [12]; 44% persistence is high by fund standards but still a coin flip [13]. Select copy targets with a sign-randomisation test on the public per-user dataset [11], not PnL rank; measured copy uplift is only +1.62 pp vs the follower's own trades [55][H, snippet].
5. **Feed-based flow signals are near noise** (59% direction accuracy) [23]; copy/flow bots need on-chain fills.
6. **Sports is different**: no longshot bias [19], ~1% margins at > $1B scale for the winners [35], 45% historical wash share [24], Kalshi 4-5x bigger with 80% sports [47][49] (the hedge/reference venue), and the retail crowd (World Cup: 66.7% losers, 58k winners averaging $4.85) [18].
7. **Slow-capital statistical biases are better documented than fast ones**: political underconfidence (slope 1.45-1.83) [20] and non-sports longshot overpricing (-15% to -26%) [19] are large, replicated, and not latency-sensitive — but need horizon-matched capital and event-grouped accounting (+4.1% when longshots are grouped by parent event [19]).
8. **Forensic threads misclassify strategies.** 0x8dxd was sold as latency arb; reconstruction shows 94% symmetric buys [29]. Rebuild any "alpha wallet" from fills before cloning it.
9. **Remaining small edges are capacity-capped** (14.8 shares per NBA combo [4]; ~$5k/quarter for a working esports bot [32]) — viable for a solo team because desks ignore them, but they die when fees or a second bot arrive.
10. **Competition is now salaried**: ~20-person Jump team with an equity-for-liquidity deal, Wintermute, DRW, an in-house Polymarket desk [42][43][45]. Expect mid-book spread (400 bps in Q1 2026 [23]) to compress first in high-volume sports/crypto; the 13-18% longshot spreads and the long tail of ~32-maker markets are where a small maker still matters.
11. **Volume is not flow you can trade against**: 15-25% wash [16][24], 35% of trades from 10k+-fill wallets [46], and volume fell 36.7% in one month after the World Cup [47].

## Could not verify / open questions

- Full text of Akey et al. and Gomez-Cram et al. (SSRN 403): per-class dollar PnL of market makers, maker-vs-taker return split, category-level PnL. The "$11.8k per market-maker account" press figure is unverified.
- CNBC 2026-09-14 [15] and Sportico World Cup analysis were not fetchable; quotes come from search snippets.
- No before/after measurement of institutional entry on Polymarket spreads; no named list of Polymarket (international) designated market makers; Susquehanna-on-Polymarket claim unverified.
- No study of realised Polymarket-Kalshi arbitrage PnL, of news/LLM-bot PnL, of round-number clustering, or of post-fee (2026) favourite returns.
- Origin of the "12.3 s -> 2.7 s / 73% sub-100 ms" statistics [57]; "14 of top-20 wallets are bots", "AI agents > 30% of wallet activity", "37% of bot wallets profitable vs 7-13% of humans" — all SEO-chain claims with no primary source found.
- swisstony all-time PnL: $18.4M (official leaderboard) vs $23.6M (Polycopy) on the same day [35]; methodology difference unexplained. Identity/mechanism of swisstony, RN1 and the "$8M in two months" sports bot [39] rest on X threads.
- Monthly active traders for 2026 by month (The Block chart not machine-readable); current OI by category.
- Medium posts (LP post-mortem, 99c "theta harvesting") returned 403; only snippets used [58].

## Source ledger

| n | URL | Publisher | Date | Supports | F/S |
|---|---|---|---|---|---|
| 1 | https://arxiv.org/abs/2508.03474 (and /html/2508.03474) | arXiv / AFT 2025, Saguillo et al. | 2025-08-05 | $40M arb, breakdown, top-10 table, method | F |
| 2 | https://collective.flashbots.net/t/arbitrage-in-prediction-markets-strategies-impact-and-open-questions/5198 | Flashbots Collective (paper authors) | 2025-08-21 | exact per-strategy dollar figures | F |
| 3 | https://arxiv.org/html/2608.00666v1 | arXiv, Gebele, Mutzel, Matthes | 2026-08-01 | $1.12M executable arb, decay, concentration, critique of [1] | F |
| 4 | https://arxiv.org/abs/2605.00864 | arXiv, Cheng, Yang, Zou | 2026-04-22 | NBA arb frequency, duration, capacity | F |
| 5 | https://arxiv.org/abs/2601.01706 | arXiv, Gebele & Matthes | 2026-01-05 | cross-venue 2-4% deviations | F |
| 6 | https://sergeenkov.com/polymarket-profitability/ | A. Sergeenkov (independent, Dune) | 2026-04-06 | 84.1% losers, thresholds, persistence | F |
| 7 | https://finance.yahoo.com/news/70-polymarket-traders-lost-money-192327162.html | Yahoo / Cryptonews (DeFi Oasis data) | 2025-12 | 70% losers, 0.04% take 70% | S |
| 8 | https://cepr.org/publications/dp21615 | CEPR DP21615, Akey et al. | 2026-06-12 | top 1% = 76.5%, makers win | F |
| 9 | https://finance.yahoo.com/markets/crypto/articles/weve-calculated-your-chances-of-winning-money-on-polymarket-155955143.html | Washington Post via Yahoo | 2026-05-11 | 1,200 winners, $591M, automation | F |
| 10 | https://gigazine.net/gsc_news/en/20260525-polymarket-win-or-lose/ | Gigazine | 2026-05-25 | user counts, $650M losses | F |
| 11 | https://www.vincentgregoire.com/polymarket-users-data/ | V. Gregoire | 2026 | public per-user dataset | F |
| 12 | https://www.coindesk.com/markets/2026/04/26/only-3-of-traders-drive-prediction-markets-accuracy-not-the-crowd-study-finds | CoinDesk | 2026-04-26 | LBS/Yale: 3%, 12%, 60%, insiders | F |
| 13 | https://insights.som.yale.edu/insights/wisdom-of-the-few-prediction-markets-are-driven-by-small-number-of-skilled-traders | Yale Insights | 2026-06-10 | classes, 44% persistence, MM < 0.5% | F |
| 14 | https://www.theblock.co/news/ecosystems/2026-04-26-skilled-polymarket-traders-are-a-3-minority-and-everyone-else-funds-their-gains-study-398902 | The Block | 2026-04-26 | 3.14%, 67% losers, 1,950 insiders | F |
| 15 | https://www.cnbc.com/2026/09/14/prediction-markets-efficient-win-lose-beat.html | CNBC | 2026-09-14 | Jensen "3% -> below 1%" | S (403) |
| 16 | https://www.coindesk.com/markets/2026/04/29/a-tiny-group-is-winning-on-polymarket-as-under-1-of-wallets-take-half-the-profits | CoinDesk (Solidus Labs) | 2026-04-29 | maker/taker concentration, 15% wash | F |
| 17 | https://www.pewresearch.org/short-reads/2026/07/22/what-we-know-about-the-typical-polymarket-user/ | Pew Research | 2026-07-22 | typical-user behaviour and PnL | F |
| 18 | https://cryptoslate.com/most-world-cup-traders-won-less-than-5-on-polymarket-while-five-wallets-walked-away-with-millions/ | CryptoSlate (Dune) | 2026-07-21 | World Cup PnL distribution | F |
| 19 | https://arxiv.org/abs/2609.12878 (and /html/2609.12878) | arXiv, Cardozo & Rivero-Wildemauwe | 2026-09-11 | FLB by price, category, order type | F |
| 20 | https://arxiv.org/abs/2602.19520 (and /html) | arXiv, Nam Anh Le | 2026-02-23, v2 2026-08-04 | calibration slopes | F |
| 21 | https://news.polymarket.com/p/red-tilt | Polymarket (The Oracle) | 2026-02-05 | partisan skew 2024 | F |
| 22 | https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5502658 | SSRN, Burgi, Deng, Whelan | 2025-26 | Kalshi makers -10%, takers -32% | S |
| 23 | https://philippdubach.com/posts/the-anatomy-of-a-decentralized-prediction-market-notes-from-the-polymarket-order-book/ (paper: https://arxiv.org/abs/2604.24366) | P. Dubach | 2026-05-02, upd. 2026-08-16 | spreads, depth, makers, wash, 59% | F |
| 24 | https://www.coindesk.com/markets/2025/11/07/polymarket-s-trading-volume-may-be-25-fake-columbia-study-finds | CoinDesk (Columbia study) | 2025-11-07 | 25% wash, 45% sports | S |
| 25 | https://corpgov.law.harvard.edu/2026/03/25/from-iran-to-taylor-swift-informed-trading-in-prediction-markets/ | Harvard Law Forum (Mitts & Ofir) | 2026-03-25 | $143M informed profits, cases | F |
| 26 | https://arxiv.org/abs/2609.06005 | arXiv, Ibrahim & Zaki | 2026-09-05 | 44,976 dislocations, cost to move | F |
| 27 | https://finance.yahoo.com/news/arbitrage-bots-dominate-polymarket-millions-100000888.html | BeInCrypto via Yahoo | 2026-01-06 | 0x8dxd, $2.2M bot | F |
| 28 | https://www.financemagnates.com/cryptocurrency/polymarket-introduces-dynamic-fees-to-curb-latency-arbitrage-in-short-term-crypto-markets/ | Finance Magnates | 2026-01-07 | dynamic fee vs latency arb | F |
| 29 | https://leolabs.me/blog/pm-top20-strategy-patterns/en/ | Leo Labs (independent) | undated; data Jan-Mar 2026 | 40-wallet reconstruction | F |
| 30 | https://news.polymarket.com/p/copycat | Polymarket (The Oracle) + Stand.Trade | 2026-04-24 | copy-trading pitfalls, wallet profiles | F |
| 31 | https://blockchain.news/news/polymarket-fast-markets-volume-bots-fees-analysis | Blockchain.News (Dune) | 2026-04-14 | bot share of fast markets, fees | F |
| 32 | https://kacho.io/polymarket-arbitrage-real-numbers | Kacho (individual) | 2026-06-06 | small-bot real PnL | F |
| 33 | https://www.dlnews.com/articles/markets/polymarket-users-lost-millions-of-dollars-to-bot-like-bettors-over-the-past-year/ | DL News | 2025-08-22 | top-3 arb wallets | F |
| 34 | https://panews.io/articles/c1772590-4a84-46c0-87e2-4e83bb5c8ad9 | PANews | undated on fetch | 0.51%, six models, LP self-report | F |
| 35 | https://polymarket.com/leaderboard/overall/all/profit | Polymarket | fetched 2026-09-20 | all-time top-20 PnL and volume | F |
| 36 | https://www.kucoin.com/news/flash/top-polymarket-traders-use-three-distinct-strategies-to-earn-millions | KuCoin / MarsBit | 2026-05-07 | category leaders, per-position profit | F |
| 37 | https://finance.yahoo.com/news/polymarket-whale-actually-made-85-050139914.html | Yahoo / Fortune | 2024-11 [pre-2025] | Theo $85M, 11 wallets | S |
| 38 | https://www.onchaintimes.com/a-chat-with-domer-the-1-trader-on-polymarket/ | On Chain Times | 2024-10-09 [pre-2025] | Domer method | F |
| 39 | https://phemex.com/news/article/sports-bot-earns-8-million-on-polymarket-by-exploiting-time-lag-55871 | Phemex News (X thread) | 2026-01-25 | "$8M sports bot" claim | F |
| 40 | https://phemex.com/news/article/algorithm-exploits-broadcast-lag-to-turn-5-into-37m-on-polymarket-53969 | Phemex News (X thread) | 2026-01 | swisstony broadcast-lag claim | S |
| 42 | https://www.coindesk.com/business/2026/02/10/jump-trading-to-take-small-stakes-in-polymarket-kalshi-bloomberg | CoinDesk (Bloomberg) | 2026-02-10 | Jump deal | F |
| 43 | https://www.bayes-group.com/insights/prediction-markets-desk-hiring-2026 | Bayes Group (recruiter) | 2026, undated | firms, Wintermute date, ICE | F |
| 44 | https://www.tradermath.org/articles/prediction-markets-trading-at-quant-firms | Tradermath | 2026-08-08 | SIG, DRW, Akuna roles | F |
| 45 | https://www.coindesk.com/business/2025/12/05/polymarket-hiring-in-house-team-to-trade-against-customers-here-s-why-it-s-a-risk | CoinDesk | 2025-12-05 | in-house desk, RFQ parlays | F |
| 46 | https://www.trmlabs.com/resources/blog/how-prediction-markets-scaled-to-usd-21b-in-monthly-volume-in-2026 | TRM Labs | 2026-03-27 | wallets, cohorts, records | F |
| 47 | https://www.theblock.co/news/business/2026-09-02-kalshi-polymarkets-volume-falls-august-413309 | The Block | 2026-09-02 | Jul/Aug 2026 volumes | F |
| 48 | https://www.theblock.co/post/361370/polymarket-hits-1-16-billion-monthly-volume-but-active-trader-count-continues-to-fall | The Block | 2025-07-10 | 2025 volume, active traders | F |
| 49 | https://www.pewresearch.org/short-reads/2026/05/27/trading-volume-on-prediction-markets-has-soared-in-recent-months/ | Pew Research (The Block data) | 2026-05-27 | category mix | F |
| 50 | https://sacra.com/c/polymarket/ | Sacra | 2026 | annual volume, US arm | F |
| 51 | https://phemex.com/news/article/polymarket-achieves-record-688k-monthly-active-users-61052 | Phemex News (CoinDesk) | 2026-02-17 | 688k MAU | F |
| 52 | https://www.theblock.co/data/decentralized-finance/prediction-markets-and-betting/polymarket-active-traders-monthly | The Block Data | fetched 2026-09-20 | Sep 2026 MTD traders | F |
| 53 | https://defirate.com/prediction-markets/volume/polymarket/ | DeFi Rate | 2026-09-20 | monthly series (partly broken) | F |
| 54 | https://en.bloomingbit.io/feed/news/117522 | Bloomingbit | 2026-08 | July split intl/US, June record | S |
| 55 | https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6670318 | SSRN, P. Oliphant | 2026-04-28 | copy trades +1.62 pp | S |
| 56 | https://arxiv.org/html/2604.07355v1 | arXiv, Prediction Arena | 2026-04 | live LLM trading returns | S |
| 57 | https://medium.com/illumination/beyond-simple-arbitrage-4-polymarket-strategies-bots-actually-profit-from-in-2026-ddacc92c5b4f | Medium (SEO) | 2026 | unsourced 12.3 s -> 2.7 s claim | S |
| 58 | https://medium.com/@jacek.jurczynski/picking-up-nickels-at-ninety-nine-cents-d4308907db2c | Medium, J. Jurczynski | 2026 | 99.47c wallet example | S (403) |
| 59 | https://arxiv.org/abs/2607.06166 | arXiv, Gu et al. | 2026-07-07 | forecast-to-profit rule, Kalshi live | F |
| 60 | https://defillama.com/protocol/polymarket | DefiLlama | 2026-09 | TVL; OI from search snippet | S |
| 61 | https://arxiv.org/abs/2605.11640 | arXiv, M. Nechepurenko | 2026-05-12, rev. 2026-07-30 | fills cannot identify market making | F |
| 62 | https://docs.polymarket.com/trading/fees | Polymarket docs | undated, fetched 2026-09-20 | fee formula and category rates | F |
| 63 | https://arxiv.org/abs/2604.10005 | arXiv, S. Dalen | 2026-04-11, withdrawn 2026-07-02 | withdrawn synthetic DMM study | F |

(No source 41: number intentionally unused.)
