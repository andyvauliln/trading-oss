# Every Polymarket incentive, reward and subsidy program
_As of 2026-09-20. Evidence pack E2 for the Polymarket strategy survey._

Conventions: **[own query]** = data pulled in this session (2026-09-20, ~17:00 UTC) from public APIs or Polygon logs; **derived** = my arithmetic on cited figures. Affiliate / vendor sources are labelled; treat them as leads.

## Key facts

1. The international venue runs five cash programs, each paid once a day (00:00-00:45 UTC) with a $1 minimum: liquidity rewards, maker rebates, taker rebates (new 28 May 2026), referral, holding rewards [1][7][9][10][13].
2. On-chain payouts over the 8 daily runs of 13-20 Sep 2026 [own query, 24]: taker rebates $2.04M (~$255k/day) > maker rebates $1.50M (~$187k/day) > liquidity rewards $1.01M (~$126k/day) > holding ~$11.6k/day > referral $30.8k total (~$3.8k/day). Taker rebates, four months old, are already the largest line.
3. Liquidity-reward score per order is `S = ((v - s)/v)^2 * b`; sides combine as `Q_min = max(min(Q1,Q2), max(Q1,Q2)/c)` with c = 3.0 when the midpoint is in [0.10, 0.90], and `min(Q1,Q2)` (two-sided only) in the tails; sampled every minute [1].
4. Configured pools are not payouts: 16,719 markets carried reward configs summing to $585k/day on 20 Sep [own query, 4], while actual daily liquidity payouts that week were $108k-$156k [24]. The docs call the August crypto pools "configured reward caps" whose payouts "depend on eligible quoting" [1]; sports rates are "expressed in daily rates" for windows lasting hours [6].
5. Liquidity rewards are concentrated: over 8 days, 4,832 wallets were paid; top 10 took 24.0%, top 100 60.4%, top 500 88.4%; 49% of recipients earned under $10; the median daily payout was ~$5 [24].
6. Maker rebates = 25% of taker fees in most categories, 20% crypto, 15% sports (cut from 25% on 10 Jul 2026), geopolitics fee-free; a maker's share is `fee_equivalent_i / sum(fee_equivalent)` per market, with `fee_equivalent = C * feeRate * p * (1-p)` [6][7][8].
7. Taker rebates: 7 tiers on 30-day weighted volume `wV = size * (1 - price) * category weight`; 3% (Bronze, $2k wV) to 50% (Obsidian, $10M wV); one-off level-up bonuses $10 to $25,000 [9].
8. About half of international taker fees flow back to users: last 30 days fees $34.1M, user-side distributions $17.8M, protocol revenue $16.3M (DefiLlama, on-chain distributor tracking) [22][23].
9. Holding rewards: 3.25% annualized (4% at launch, Sep 2025), hourly random sampling, daily payout, Treasury funded, rate and caps at Polymarket's discretion [13][14]. At least 228 markets in 20 events carry the flag [own query, 15]; ~$11.6k/day is paid to ~48k wallets, implying ~$130M of eligible position value (derived) [24].
10. Anyone can sponsor extra rewards on a market from $0.1/day, same scoring formula, cancellable with refund from the next UTC day; 35 sponsored configs worth $7.5k/day were live [16][4].
11. POLY: no token exists. The help centre (updated 24 Jun 2026) says Polymarket "has not announced plans for any airdrop or token generation event" [29]; the CMO said on 24 Oct 2025 "there will be a token, there will be an airdrop"; Blockratize filed POLY / $POLY trademarks on 4 Feb 2026; no criteria, snapshot or date have been published [30][31].
12. The Columbia study (Nov 2025) put wash trading at ~25% of historical volume (45% in sports), 14% of 1.26M wallets, and tied it to airdrop expectations and zero fees [26][27]. Fees now apply to every category except geopolitics [6].
13. Referral was cut hard: since 28 May 2026 it pays 10% direct / 5% indirect of *net* fees, only for a referee's first 30 days or until Platinum, and requires $10k lifetime volume [10]; in March 2026 it was reported as 30% / 10% of gross [41].
14. Builder codes allow a surcharge of up to 100 bps taker / 50 bps maker on routed orders, additive to platform fees and attributed on-chain [11]; builder volume is concentrated (six builders = 81% of lifetime volume) [35].
15. Polymarket US (QCX) runs a separate stack: maker rebate paid at trade (theta 0.0125 vs taker 0.0695 from 17 Sep 2026), 10/25/50% monthly taker-rebate tiers, a per-second liquidity program that scores each book side independently, volume pools, and application-only MM / LP-stipend programs [37][38][40].
16. Polymarket Perps pays $75k/day in maker rewards plus 6% APR on open interest (entity floor $5M since 7 Sep 2026) and a 20% fee referral [18][19][20].

## 1. Liquidity rewards (international CLOB)

**Formula [1].** v = market max spread (cents), s = order distance from the "size-cutoff-adjusted midpoint", b = "in-game multiplier" (not defined in the docs).
- `S(v,s) = ((v-s)/v)^2 * b`
- `Q_one` = sum of S x size over bids on m and asks on m'; `Q_two` = asks on m and bids on m'.
- Midpoint in [0.10, 0.90]: `Q_min = max(min(Q_one,Q_two), max(Q_one/c, Q_two/c))`, c = 3.0 "on all markets". One-sided quoting earns one third; past a 3:1 imbalance extra size on the heavy side adds a third of its points.
- Midpoint < 0.10 or > 0.90: `Q_min = min(Q_one,Q_two)`, so one-sided scores zero. The help centre words it only as "below $0.10" [5].
- `Q_normal = Q_min / sum(Q_min)` per sample; `Q_epoch` = sum over 10,080 samples; `Q_final = Q_epoch / sum(Q_epoch)`; reward = Q_final x market pool.
- Docs example (v = 3c): 100 @ 1c scores 44.4, 200 @ 2c scores 22.2. Distance dominates size.

**Sampling and cadence.** "Calculated every minute using random sampling" [1]. 10,080 samples is a 7-day epoch, yet both docs and help centre say payouts are daily at ~midnight UTC [1][5]; the docs do not reconcile the two. `/order-scoring` requires an order to have "been live for the required duration" (value unpublished) [3]; the March Madness program stated 3.5 seconds [6].

**Minimum payout.** "A day only pays out if your earnings for that day reach $1"; sub-$1 amounts do not roll over [5]. An affiliate guide says the $1 floor is per market per day [47]; the official wording is per day.

**Where to read pools [2][3].** Gamma market object: `rewardsMinSize`, `rewardsMaxSpread`, `clobRewards[] {rewardsDailyRate, startDate, endDate}`, `holdingRewardsEnabled`. CLOB (public): `GET /rewards/markets/current[?sponsored=true]` (500 per page, `next_cursor`, "LTE=" marks the end) and `GET /rewards/markets/multi` (sortable by `rate_per_day`, `competitiveness`, `spread`, `volume_24hr`, `reward_end_date`). CLOB (L2 auth): `GET /rewards/user?date=`, `GET /rewards/user/percentages` (live share per condition_id), `GET /order-scoring?order_id=`. `GET /rebates/current?date=&maker_address=` returns maker rebates per market.

**How pools are set.** No methodology is published; each market "defines a minimum qualifying order size, maximum qualifying spread, and reward allocation" [1]. Observed: sports use templates (identical rates across games, re-dated daily); news markets are hand-set [4].

**Snapshot 2026-09-20 [own query, 4].**

| Metric | Value |
|---|---|
| Markets with active config | 16,719 |
| Sum of `rate_per_day` | $585,383 |
| Share of configured rate: top 10 / 50 / 100 / 500 markets | 25.5% / 63.5% / 72.9% / 84.3% |
| Median / modal market rate | $3 / $1 per day (5,658 markets at $1) |
| Modal `max_spread`, `min_size` | 4.5c (12,988 markets), 20 shares (12,728) |
| NFL game day | moneyline $15,771; spread / total $11,657; 1H lines $1,886; anytime-TD props $1,371; min size 1,000, max spread 2.5c |
| EPL match | $6,300 per 3-way leg |
| Top non-sports | Russian Duma seats $1,500; "X bankruptcy by 2027/28/29" $1,000 at near-zero volume; Fed October decision $1,000 (2.5c) |
| Top-1,500 markets by rate | NFL 76.8% of configured rate, other sports 4.3%, everything else 18.9% |

**Actual payouts [own query, 24].** Daily liquidity-reward runs, 13-20 Sep 2026 (each pays the previous UTC day): $135.8k, $128.5k, $109.5k, $122.3k, $108.2k, $113.2k, $137.7k, $156.0k, to 2,250-2,510 wallets per day, all in pUSD from distributor `0x2c2795EA295d5Eb51F9121B728eD2eA4e936a709`. The payout for NFL Sunday 13 Sep was $128.5k, nowhere near the ~$400k of NFL rates configured on a comparable Sunday. Other distributors, as labelled by DefiLlama [23]: maker rebates `0x3a9418b2651c8164DB5EBc56F12008137865e0f7` and `0xfdB1b8dC7f5789a0c9A398026585B8B10FbA5507`; taker rebates `0x520BF77D9d34C34a6A9723f50E1Dcb887eD238C5`; holding `0xC536633Ff12ee52e280b2aF2594031060C5aAf41` and `0x607C8c9866Ef3b4665C5a384188706be738d8Bf8`; referral `0x1510565E93c9729410b6e41088E014E312Fd8829` and `0x8a80356b6304a08c24da30b0cf0d85b6907824ee`.

**Best pay per dollar of resting risk.** No official metric exists. `/multi` exposes an undocumented `market_competitiveness` ("competitiveness score of the market") [3]. In the top 1,500 markets by rate, 23.5% of configured rate sat in markets with competitiveness 0, and `rate_per_day / competitiveness` ranged from 0.001 to 283,000 [own query, 4]. Crowded end: long-dated, low-news markets (Euro 2028 winner, 2028 president; competitiveness 2,000-14,000 for $21-62/day). Thin end: daily weather, Truth Social post counts, German state-election brackets, NFL props; these resolve within days and gap. Farmers cluster where jump risk is lowest, so reward per unit of competition is highest exactly where adverse selection is worst. TradoxVPS (vendor blog) made the same density point for the August crypto program: BTC 4-hour markets carried ~8x the per-market budget of BTC 5-minute markets ($269 vs $34 per day) [42].

**Budget history.**
- Announced programs: March Madness "$2M+" [6]; "over $5M" for April 2026 sports (Odaily via Bitget, citing a staff X post) [44]; World Cup $30k per match x 104 (airdrop blog, secondary) [45]; August 2026 crypto TWAP transition $1M (5-minute $550k, 15-minute $350k, 4-hour $100k; ended) [1].
- Lifetime paid per a third-party on-chain aggregator: $36.2M since Nov 2023 to 184,927 wallets; top 10 = $6.26M (17%, derived); top-1% threshold $2,082; top-10% threshold $64 [25].
- The "$12M of LP rewards in 2025" figure appeared only in a search summary: unverified.
- Sources disagree: DefiLlama's international user-side total for April 2026 is $9.1M *including* maker rebates on $32.3M of fees [22], which leaves little room for "over $5M" of sports liquidity rewards actually paid that month. Read announced budgets as caps.

## 2. Maker rebates

Timeline [6]: 5 Jan 2026 fees plus rebates on 15-minute crypto; 16 Jan fee-curve weighting documented; 11 Feb per-market pools ("makers only compete with other makers in the same market"); 18 Feb NCAAB and Serie A; 6 Mar all crypto; 30 Mar Fee Structure V2 (every category except geopolitics); 10 Jul sports fee rate 0.03 to 0.05 and sports rebate 25% to 15%.

Current schedule [7][8]: taker feeRate crypto 0.07, sports 0.05, finance / politics / mentions / tech 0.04, economics / culture / weather / other 0.05, geopolitics 0. Fee = `C * feeRate * p * (1-p)`; peak per 100 shares at 50c: $1.75 / $1.25 / $1.00. Rebate pool = 20% / 15% / 25% of those fees; only filled maker orders count; paid daily in pUSD, $1 minimum. Pine Analytics reported a 50% finance rebate in March 2026 [41]; docs now show 25%. DefiLlama shows ~98% of January 2026 fees returned ($2.57M of $2.62M) [22], consistent with a near-full launch rebate that was later cut (derived).

Lifetime per aggregator: $44.1M since Jan 2026 to 152,244 wallets; top 10 = $6.1M (13.8%, derived) [25]. Week of 13-20 Sep [24]: $162k-$245k/day, 11,387 recipients; top 10 20.0%, top 100 49.3%, top 500 75.7%.

**Stacking.** Liquidity rewards pay for resting quotes whether or not they fill; rebates pay only on fills; they use separate distributor contracts [1][7][23]. Nothing in the docs prevents earning both on the same order, and holding rewards accrue on the resulting inventory in flagged markets [13]. Taker rebates exclude maker fills [9]. Derived yardstick: makers received ~$313k/day (rebates plus rewards), about 30% of the ~$1.03M/day of taker fees [22][24].

## 3. Taker rebates (live 28 May 2026) [9]

`wV = trade size ($) * (1 - entry price) * weight`. Weights: sports 1.0; politics / finance / mentions / tech 1.3; economics / culture / weather / other 1.7; crypto 2.3; geopolitics 0.

| Tier | 30-day wV | Rebate | Level-up bonus |
|---|---|---|---|
| Bronze | $2k | 3% | $10 |
| Silver | $20k | 8% | $50 |
| Gold | $200k | 18% | $250 |
| Platinum | $1M | 32% | $1,500 |
| Diamond | $4M | 44% | $7,500 |
| Obsidian | $10M+ | 50% | $25,000 |

The rebate applies going forward only, tiers are recomputed daily, omnibus wallets are ineligible, and Polymarket may remove rebates for wash trading or self-matching. Aggregator: $28.7M paid to 60,889 wallets since launch [25]. Week of 13-20 Sep: $2.04M, 8,331 recipients, top 10 = 37.5%; two wallets received ~$160k each [24].

## 4. Holding rewards, sponsored pools, boosts

- Position value = YES shares x YES mid + NO shares x NO mid, summed per market (help-centre example: 30,000 x 0.53 + 10,000 x 0.45 = $20,400). It is sampled randomly once per hour and accrues `value * 0.0325 / 365 / 24`; paid daily; Treasury funded; "variable and subject to change" [13]. Launched 24 Sep 2025 at 4% on 13 markets [14]. An affiliate page dated Sep 2026 still quotes 4.00% [47]; DefiLlama's adapter and the help centre agree on 3.25% [13][23].
- Flagged events [own query, 15]: 2028 presidential winner (52 markets), Democratic nominee (51), Republican nominee (42), "what price will BTC / ETH / SOL / XRP / HYPE hit before 2027" (64), 2026 midterm control, "X out before 2027" leader markets, China-Taiwan, Trump impeachment, Maxwell pardon. The Gamma filter parameter is not honoured; the flag is reliable. This is a lower bound from the first 2,100 open markets.
- Because both sides count, a complete set (YES + NO, ~$1) appears to accrue on ~$1 with no directional risk. This is inferred from the formula; unverified with Polymarket.
- Sponsored rewards [16]: deposit into a contract, minimum $0.1/day, same scoring formula, paid at 00:00 UTC, no Polymarket cut stated, cancel refunds from the next UTC day, unspent funds return at resolution. Live: 35 configs, $7,474/day, largest $2,257/day [4]. Telonex case (unknown sponsor, ~$70k on "Jesus returns before 2027", 17 Feb 2026): makers 302 to 639 within a day, HHI 0.164 to 0.041, top-5 maker share 56.5% to 36.9%, top-of-book depth 23.5x [17].
- Boosts: taker-rebate "Bonuses" multipliers are reserved but none is published [9]; the scoring multiplier `b` is undefined [1].

## 5. POLY token / airdrop

- Official line: no token; pUSD is the only platform token [29].
- Dated signals [30][31]: Oct 8 2025 Coplan "$POLY" post; Oct 24 2025 CMO confirmation, to follow the US relaunch; Nov 2025 growth lead warned that sybil-flagged engagement will not count; Feb 4 2026 trademark filings (intent to use); Feb-Jul 2026 teasers from an engineer who cited "legal guidance" and had left the company by Aug 2026. Leadership has been silent since Oct 2025.
- "5-10% of supply" and every eligibility list are community speculation. Traders quoted by Decrypt expect tiered or logarithmic allocation because "a ton of the volume and liquidity rewards are done by such a small percentage of users", and describe farmers moving from $50k self-trades to 100+ wallets [28].
- Comparable airdrops: LayerZero reportedly removed ~59% of wallets and Linea ~40% as sybils. Search snippet only, unverified [48].
- No POLY-launch market is listed on Polymarket [own query, 15].

## 6. Referral, Builder, leaderboards, competitions

- Referral [10]: terms as in key fact 13; clawback for self-referral or linked accounts; omnibus wallets ineligible. Paid $11.3M to 9,329 wallets since Mar 2026 [25], but now ~$2.5k-$6.5k/day to ~300 wallets [24].
- Builder [11][12]: fee = notional x bps; one rate change per 7 days with 3-day notice; rates public; codes revocable for "self-referred or other non-bona fide" flow; Verified tier adds "weekly USDC rewards based on volume (subject to approval)" and grants. The "$2.5M grant fund" and "0.5-1% of attributed volume" figures are third-party estimates (PolyTrack via Chainstory): unverified [35]. Leaderboard [own query, 36]: last month the top 50 builders routed $435.5M (betmoar $88.7M); lifetime betmoar $2.23B, Gate $828M, traderline $552M, PolyCop $362M, MetaMask $317M. Chainstory says Based earns ~$1M/yr from builder rewards; a Polymarket market prices "Based revenue >= $1M before 2027" at 7.5% [35][15].
- Leaderboards carry tier badges [9]; no cash trading competition was found for 2026. CopyGrade (vendor) flags 72% of 193 leaderboard wallets for farming patterns [43].

## 7. Polymarket US and Perps

- US fees [38]: taker theta 0.0695 ($1.74 per 100 contracts at 50c), maker rebate theta 0.0125 ($0.31) credited at trade; taker rebates of 10% / 25% / 50% for prior-month taker volume of $250k / $1M / $10M, paid weekly; "Accelerated Tier Placement" accepts proof of volume on another prediction market.
- US Liquidity Incentive Program [37]: random snapshot every second; `score = DiscountFactor^(ticks from best) * size`; bid and ask are normalized independently ("the spread between your bid and offer doesn't matter"); a side qualifies only when aggregate Target Size is resting; no per-user cap; paid within ~7 business days; $1 minimum. Public `GET api.prod.polymarketexchange.com/v1/incentives` [39]: the first 4,000 markets showed 8,741 active period pools totalling $20.1M configured, e.g. CFB tier-1 live spreads 828 lines x $8,500 and NFL live moneyline 46 games x $32,000 [own query]. These are per-period caps.
- Volume program: pro-rata on taker notional traded between 3c and 97c (example: $100k in-game pool per NBA playoff moneyline, $500 minimum notional). Retail credits: deposit $10 for a $50 credit, refer-a-friend $50 each (maximum 50), non-withdrawable [37]. Market Maker and Liquidity Provider (weekly stipend) programs are application-only with terms redacted in the CFTC filings [40]. US last 30 days: fees $42.3M, user-side $10.6M [22].
- Perps [18][19][20][21]: `raw = maker_score^0.35 * liquidity^0.65 * uptime`; eligibility needs >= 1% of 7-day maker volume; quotes within 20 bps (tier weights 1 / 0.25 / 0.10, $100k cap per tier and side, harmonic mean of sides); maker rebate only above $1B of 30-day volume.

## 8. Farming behaviour, clawbacks, adverse selection

- Columbia [26][27]: wash share peaked near 60% of weekly volume in Dec 2024, fell under 5% in May 2025, was ~20% in Oct 2025; one cluster of 43,000+ wallets produced ~$1M of volume; ~$4.5B flagged in total. Post-fee evidence: Dubach's 600-market panel (Feb-Apr 2026) finds a median self-counterparty share of 0.97% (p99 10.6%); the method differs and gives a lower bound [33].
- Enforcement: every program reserves discretion to adjust, withhold or claw back for wash trading, self-matching and linked accounts [9][10][11][37]. No documented mass clawback was found.
- Net PnL of reward farmers: no public dataset exists. Indirect evidence:
  - Akey et al. (588M trades, $67B): the top 1% of profitable users take 76.5% of profits, and winners predominantly provide liquidity with limit orders [32].
  - Dubach: median maker HHI 0.031 (~32 effective makers; p90 ~8); the Glosten-Harris adverse-selection component has a median near 0 on the top 100 markets, but feed-inferred trade sign matches on-chain direction only ~59% of the time, so toxicity estimates from the public feed are unreliable [33].
  - Nechepurenko: public fills cannot identify quote lifecycle [34].
  - The poly-maker README warns that market making "can lose money" [46].
  - "$200-300/day on $10k" and "40-120% APY" appear only in marketing blogs: unverified [49].

## What a builder who already runs LP / arb / sniping / copy bots is likely to UNDERESTIMATE

1. Taker rebates are the biggest subsidy and they favour mid-priced flow. wV scales with (1 - price), so sniping at 97c earns 3% of notional as wV while an arb leg at 50c earns 50%. Reaching Gold or Platinum removes 18-32% of fee drag on every taker strategy [9][24].
2. Ranking by `rate_per_day` is wrong by ~4x in aggregate and worse per sports market. Use `/rewards/user/percentages` multiplied by pool, and reconcile against on-chain receipts [3][4][24].
3. Competition is not equilibrated (7 orders of magnitude in rate/competitiveness; 23.5% of configured rate uncontested), but the uncontested pools are the gap-risk markets [4].
4. The c = 3 rule and the two-sided requirement in the tails make the weaker side the binding constraint. The US venue scores sides independently; that design difference matters for one-sided inventory strategies [1][37].
5. The $1/day floor plus ~$5 median payouts mean a small account spread over $1-5/day pools forfeits a meaningful share [5][24].
6. Holding rewards accrue on market-making inventory and apparently on complete sets in 228+ markets [13][15].
7. Sponsoring rewards is a cheap, cancellable way to buy depth before entering size; makers doubled within a day in the Telonex case, which also shows how fast a farmer's share dilutes [16][17].
8. Parameters move without notice: sports rebate 25% to 15%, referral 30% gross to 10% net with a 30-day cap, holding 4% to 3.25%, Perps OI floor $1M to $5M [6][10][13][19]. Do not capitalise any of them.
9. Airdrop farming by volume now costs real fees, and self-trading breaches rebate terms. One clean identity with organic multi-program activity is the only defensible posture [9][28][31].
10. Distributor addresses are public, so competitor farm revenue is observable daily, and the new `/v2/user-pnl` endpoint (4 Sep 2026) makes a "reward income vs trading PnL" study of the top 500 recipients feasible. That is the missing adverse-selection dataset [6][23].

## Could not verify / open questions

- Definitions of `b`, the adjusted midpoint, the minimum live duration, and `market_competitiveness`.
- How the daily payout maps to the 10,080-sample epoch.
- The 2025 liquidity-reward budget ("$12M") and the actual paid share of the "$5M April" and World Cup programs.
- Whether sponsored rewards pay via the same distributor; actual US program payouts.
- Distributor labels come from DefiLlama's adapter, not Polymarket docs; my sums match DefiLlama's daily total ($607.9k vs $608k), which shows consistency rather than independent attribution [22][23][24].
- Builder weekly reward pool size; the Based revenue claim.
- Complete-set and neg-risk treatment under holding rewards.
- The Medium "two-week LP postmortem" returned 403 and was not read [49].
- POLY criteria, snapshot and date.

## Source ledger

| n | URL | Publisher | Date | Supports | F/S |
|---|---|---|---|---|---|
| 1 | https://docs.polymarket.com/programs/liquidity-rewards.md | Polymarket docs | undated | formula, c = 3, sampling, $1 minimum, Aug $1M program | F |
| 2 | https://docs.polymarket.com/market-data/market-details.md | Polymarket docs | undated | reward fields on the market object | F |
| 3 | https://docs.polymarket.com/api-reference/rewards/get-multiple-markets-with-rewards.md (plus sibling rewards, rebates, order-scoring pages) | Polymarket API reference | undated | endpoints, `sponsored`, scoring criteria | F |
| 4 | https://clob.polymarket.com/rewards/markets/current and /rewards/markets/multi | Polymarket CLOB API | queried 2026-09-20 | live pool configs | F |
| 5 | https://help.polymarket.com/en/articles/13364466-liquidity-rewards | Polymarket Help | upd. 2026-06-15 | $1/day rule, payout time | F |
| 6 | https://docs.polymarket.com/changelog/predictions.md | Polymarket docs | to 2026-09-04 | fee and rebate timeline, March Madness, 3.5 s rule | F |
| 7 | https://docs.polymarket.com/programs/maker-rebates.md | Polymarket docs | undated | rebate percentages, share formula | F |
| 8 | https://docs.polymarket.com/trading/fees.md | Polymarket docs | undated | fee table | F |
| 9 | https://docs.polymarket.com/programs/taker-rebates.md | Polymarket docs | live 2026-05-28 | tiers, wV, abuse terms | F |
| 10 | https://docs.polymarket.com/programs/referral-program.md | Polymarket docs | eff. 2026-05-28 | referral terms | F |
| 11 | https://docs.polymarket.com/programs/builders/fees.md | Polymarket docs | undated | builder fee caps and policy | F |
| 12 | https://docs.polymarket.com/programs/builders/tiers.md | Polymarket docs | undated | tiers, weekly rewards, grants | F |
| 13 | https://help.polymarket.com/en/articles/13364459-holding-rewards | Polymarket Help | upd. 2026-06-01 | 3.25%, sampling, formula | F |
| 14 | https://www.cryptopolitan.com/polymarket-starts-paying-out-4-rewards/ | Cryptopolitan | 2025-09-24 | launch at 4%, 13 markets | F |
| 15 | https://gamma-api.polymarket.com/markets and /public-search | Polymarket Gamma API | queried 2026-09-20 | holding flag counts; Based market; no POLY market | F |
| 16 | https://help.polymarket.com/en/articles/13755867-sponsor-market-rewards | Polymarket Help | upd. 2026-03-12 | sponsor mechanics | F |
| 17 | https://telonex.io/research/sponsored-liquidity-rewards-jesus-market | Telonex (data vendor) | 2026-02-22 | sponsorship case numbers | F |
| 18 | https://docs.polymarket.com/perps/liquidity-rewards.md | Polymarket docs | undated | Perps $75k/day formula | F |
| 19 | https://docs.polymarket.com/changelog/perps.md | Polymarket docs | to 2026-09-17 | OI rewards 6% APR, $5M floor | F |
| 20 | https://docs.polymarket.com/perps/referral-program.md | Polymarket docs | undated | 20% Perps referral | F |
| 21 | https://docs.polymarket.com/perps/learn-about-trading/fees.md | Polymarket docs | undated | Perps fee tiers | F |
| 22 | https://api.llama.fi/summary/fees/polymarket-international (and /polymarket-us) | DefiLlama API | queried 2026-09-20 | fees, revenue, user-side totals | F |
| 23 | https://github.com/DefiLlama/dimension-adapters/blob/master/fees/polymarket.ts | DefiLlama | undated | distributor addresses, method | F |
| 24 | https://polygon.gateway.tenderly.co and https://polygon-bor-rpc.publicnode.com (eth_getLogs) | Polygon via public RPC | queried 2026-09-20 | daily payouts, concentration | F |
| 25 | https://polyscalping.org/leaderboard (plus /lp /maker /taker /referral /yield) | PolyScalping (third party) | snapshot 2026-09-20 | lifetime totals, top earners | F |
| 26 | https://www.coindesk.com/markets/2025/11/07/polymarket-s-trading-volume-may-be-25-fake-columbia-study-finds | CoinDesk | 2025-11-07 | Columbia study | F |
| 27 | https://decrypt.co/347842/columbia-study-25-polymarket-volume-wash-trading | Decrypt | 2025-11-07 | 14% of wallets, category split | F |
| 28 | https://finance.yahoo.com/news/polymarket-airdrop-farmers-become-more-190103258.html | Decrypt via Yahoo | 2025-10-19 | farmer tactics, trader quotes | F |
| 29 | https://help.polymarket.com/en/articles/13364250-does-polymarket-have-a-token | Polymarket Help | upd. 2026-06-24 | official no-token line | F |
| 30 | https://www.theblock.co/post/388809/polymarket-parent-firm-files-trademark-applications-for-poly-amid-token-launch-plans | The Block | 2026-02-06 | trademarks, CMO statement | F |
| 31 | https://themerkle.com/polymarket-went-silent-on-poly-heres-everything-that-happened-before-that | The Merkle | 2026-08-26 | dated POLY timeline | F |
| 32 | https://cepr.org/publications/dp21615 | CEPR (Akey et al.) | 2026-06-12 | profit concentration, makers win | F |
| 33 | https://arxiv.org/html/2604.24366v2 | arXiv (Dubach) | 2026-08-24 | HHI, spread decomposition, wash share | F |
| 34 | https://arxiv.org/abs/2605.11640 | arXiv (Nechepurenko) | rev. 2026-07-30 | limits of fill data | F |
| 35 | https://www.chainstory.co/the-invisible-ecosystem-who-actually-builds-on-polymarket/ | Chainstory | 2026-04-09 | builder concentration, estimates | F |
| 36 | https://data-api.polymarket.com/v1/builders/leaderboard | Polymarket Data API | queried 2026-09-20 | builder volumes | F |
| 37 | https://docs.polymarket.us/incentives/liquidity.md (plus overview, volume, user-programs) | Polymarket US docs | undated | US programs | F |
| 38 | https://docs.polymarket.us/fees.md | Polymarket US docs | eff. 2026-09-17 | US fees and rebates | F |
| 39 | https://api.prod.polymarketexchange.com/v1/incentives | Polymarket US API | queried 2026-09-20 | US pools | F |
| 40 | https://www.polymarketexchange.com/files/notices/Liquidity%20Provider%20Program%20(2026.03.03).pdf ; https://polymarketexchange.com/files/notices/Market%20Incentive%20Program%20(2026.03.05).pdf | QCX CFTC filings | 2026-03 | stipend program, redacted terms | F (partly decoded) |
| 41 | https://pineanalytics.substack.com/p/polymarket-fee-rollout | Pine Analytics | 2026-03-25 | fee split, earlier referral rates | F |
| 42 | https://tradoxvps.com/polymarket-liquidity-rewards/ | TradoxVPS (vendor) | 2026-08-14 | per-market density arithmetic | F |
| 43 | https://copygrade.com/blog/we-scored-the-polymarket-leaderboard | CopyGrade (vendor) | 2026-06-08 | 72% farming flags | F |
| 44 | https://www.bitget.com/asia/news/detail/12560605333339 | Bitget / Odaily | 2026-04-03 | "$5M" April sports | F |
| 45 | https://airdrops.io/blog/world-cup-2026-prediction-market-airdrops/ | airdrops.io (affiliate) | 2026-06-10 | World Cup $30k per match | F |
| 46 | https://github.com/warproxxx/poly-maker | GitHub README | undated | loss warning | F |
| 47 | https://startpolymarket.com/strategies/reward-farming/ | StartPolymarket (affiliate) | 2026-09-15 | stale 4%, per-market $1 claim | F |
| 48 | https://thedefiant.io/news/defi/layerzero-tells-sybil-farmers-to-out-themselves-or-face-airdrop-exclusion | The Defiant [pre-2025, possibly stale] | 2024 | sybil-filter comparables | S |
| 49 | https://medium.com/@wanguolin/my-two-week-deep-dive-into-polymarket-liquidity-rewards-a-technical-postmortem-88d3a954a058 ; https://www.bravadotrade.com/blog/polymarket-lp-farming | Medium / Bravado (marketing) | undated | anecdotal yields | S |
