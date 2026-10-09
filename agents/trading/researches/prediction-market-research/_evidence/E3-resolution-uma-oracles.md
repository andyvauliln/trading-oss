# Resolution, UMA optimistic oracle and other oracles
_As of 2026-09-20. Evidence pack E3 for the Polymarket strategy survey._

Conventions: **[n]** = source ledger row. "Hard" = on-chain data, source code, official docs, rulebooks, papers. "Soft" = press, affiliate/SEO, self-reported. "Derived" = my arithmetic on cited inputs. Anything I could not confirm is marked _unverified_.

## Key facts

1. **Proposing is no longer permissionless.** UMIP-189 passed 2025-08-06 and moved Polymarket from OOv2 to ManagedOptimisticOracleV2 (MOOV2, Polygon `0x2C0367a9DB231dDeBd88a94b4f6461a6e47C58B1`); only whitelisted addresses can propose, anyone can still dispute [5][6][7]. Polymarket's own docs still say "Anyone can propose" [4] — the docs are stale on this point.
2. **Official parameters today:** bond "typically $750 pUSD", 2-hour challenge window, first dispute → adapter resets and a second proposal round, second dispute → UMA DVM vote; debate 24-48 h + vote ~48 h; disputed total "4-6 days" [1][2][10][11].
3. **Polymarket holds an on-chain manual override.** `UmaCtfAdapter` admin can `flag()` a question and `resolveManually()` with arbitrary payouts after `SAFETY_PERIOD = 1 hours`; also `pause`, `reset` [10]. A chain study to 2025-11-30 counted 17 pause-or-flag events and 10 administrative events across 185,550 questions [16]. It is rarely used, but "the protocol cannot override UMA" (affiliate claim) is false at contract level.
4. **Neg-risk (multi-outcome) markets add a fixed +1 h delay** between `reportPayouts` and `resolveQuestion`, and accept only `[1,0]`/`[0,1]` — no 50/50 payout is valid there [12].
5. **Dispute frequency, hard numbers:** 1,604 disputes on 184,148 oracle requests (~0.87%) through Nov 2025 [16]; UMA says ~1.3% OO-wide [6]; 558 user-disputed of 140,582 events (0.39%), representing $972M of volume [18]; Polymarket spokesperson: 0.2% of contracts reach a UMA vote [23].
6. **Disputes are accelerating:** >1,150 disputed markets in 2026 by mid-May, already above all of 2025 (WSJ via [22][23]); ~2,000 disputed contracts in the prior year and 230 contracts with >$1B volume decided by the process in April 2026 alone (Bloomberg via [24][25]).
7. **Voting power is concentrated and conflicted:** nine wallets ≈ half of all UMA ever voted on Polymarket disputes, out of 6,400+ voting accounts, and they "essentially always voted together and for the winning position" [24][25]; ≥60% of active UMA voters link to Polymarket accounts; in 300+ disputes (~20%) a voter held a position in the market [22][23].
8. **The oracle's economic security is tiny versus value at stake.** UMA market cap ≈ $33-35M at ~$0.39 (Sept 2026) [61]; individual disputed markets: $60M (Strategy), $203.6M (Iran ceasefire extension), $237M (Zelensky suit), $345M (Iran peace) [39][37][30][35].
9. **Polymarket refunded exactly once** (Barron Trump/DJT, June 2024) [41][42] _[pre-2025]_ and explicitly refused after the March 2025 Ukraine-minerals vote: "because this wasn't a market failure, we are not able to issue refunds" [27][28].
10. **Measured profit of pure settlement-gap buying is small.** Gebele & Matthes (data to 2025-12-31, 19.9M trades): top-100 "bonding-trade" makers earn median APY 6.22% (mean 29.08%); median per-trade profit $0.04-$0.07; median hold 0.76-2.0 h; the single best address made $23,616 over 34,994 trades [17].
11. **Near-certain prices embed a priced lock-up discount, not only doubt:** annualized settlement wedge mean 3.06% (min frontier) to 6.89% (0.5-pct frontier); adjusting for it removes 48-88% of the apparent long-horizon miscalibration at P≥0.90 [17].
12. **Fee at the extremes (derived from the official formula `fee = C × feeRate × p × (1−p)`)**: taker fee as a share of the gross edge to $1 equals `feeRate × p` — i.e. ~4% (politics/finance/tech), ~5% (sports, economics, culture, weather, other), ~7% (crypto), 0% geopolitics; makers pay nothing [55].
13. **Price grid floor:** tick 0.01, tightening to 0.001 when price >0.96 or <0.04 [57][56]; best resting bid is 0.999 vs ask 1.000, so minimum harvestable edge is 10 bps per cycle [17]. World Cup markets use a 0.0025 tick (2026-07-02) [44].
14. **Large parts of the book no longer have an oracle gap.** Crypto up/down markets settle automatically via Chainlink Data Streams + Automation (live 2025-09-12) and, since 2026-08-07, a Chainlink TWAP (5-min markets: 60 s window from 2026-08-14) [43][44]; equities/commodities settle on Pyth [47][48]; Polymarket US settles by exchange determination [49][50].
15. **Polymarket US is a different legal object:** Rule 10.4 lets named officers "at their sole discretion" review and "determine the final outcome", reverse for "obvious error"; "Determinations made by the Company are final." Rule 10.5: if the natural person in the payout condition dies or is incapacitated, contracts settle at **last traded prices before the event** [49].
16. **Same event, different winners:** Cardi B halftime — Kalshi settled at last traded price (YES $0.26 / NO $0.74), Polymarket paid YES $1 [52]; Khamenei — Kalshi settled at pre-death last price ($0.02 / $0.29) and reimbursed some traders, Polymarket's contract went through two disputes [54].
17. **LLMs reproduce the DVM's verdict 89.6% of the time once a dispute exists, but cannot predict which markets will be disputed** (accuracy 0.57, F1 0.44) [18].

## 1. Resolution life-cycle today

**Contracts.** UmaCtfAdapter v3.0 `0x157Ce2d6…6a49`, v2.0 `0x6A9D2226…4F74`, v1.0 `0xCB182285…5130` (Polygon) [1]. Route sizes through Nov 2025: standard adapters ~103,280 questions, neg-risk 76,271, legacy 5,829 [16]. One week in April 2026: 99.8% of classified markets resolved via MOOV2, <0.2% OOv2 (search snippet of [19], _not confirmed in fetched text_).

**Who may propose.** Initial whitelist: 37 addresses — Risk Labs and Polymarket staff plus users with 20+ proposals in 3 months at >95% accuracy [5][6]. Rationale data (3 months pre-launch): those 37 had 99.7% accuracy vs 85.8% for everyone else and already made 96% of proposals [6]. Current community-documented bar: ≥5 proposals in the last 6 months, accuracy >95% [8]; monthly snapshot on the 2nd (affiliate [58]). Claimed growth to 177 addresses by Nov 2025 and a 59%/68% fall in wrong proposals/disputes are affiliate-only, _unverified_ [38]. MOOV2 roles: owner sets default proposer whitelist, requester whitelist, min liveness and min/max bond; a "request manager" can revise bond, liveness and whitelist of any unproposed request; managed by Polymarket with a 2/2 multisig with Risk Labs for upgrades [7][9]. Non-whitelisted users can only tag a whitelisted proposer [5]. Trigger for the change: premature proposals that delayed markets up to four days; two proposers lost a combined $32,250 in bonds [5][9].

**Bond, reward, liveness.** Official: bond "usually $750" both sides; liveness 2 h [1][2][3]; adapter default liveness 2 h, with a code comment that high-value questions "should consider a longer liveness period" [10]. Collateral became pUSD on 2026-04-28 (changelog entry 2026-04-17) [44][65]; help-center pages written before still say USDC.e [3]. **Sources disagree:** an affiliate guide dated 2026-09-12 states bond $500 and reward $2 (cut from $5) [58][59]; bonds are per-request parameters under MOOV2 so both can be true for different markets — check `proposalBond` on the request. Reward economics: $2-5 vs $750 at risk means one lost bond ≈ 150-375 correct proposals; author with 50 proposals calls it "a civic contribution" [58]. Front-running another proposer's transaction is said to cause whitelist removal [58] (_soft_).

**Dispute path and second-proposal rule.** First dispute: `priceDisputed` callback resets the question and sends a new OO request ("at most 2 OO Requests at a time"); second dispute sets `refund = true` and the DVM decides [10][11]. Median time from reset to the successor proposal: 300-2,909 s depending on route [16]. Bond outcomes: winner gets own bond + half the loser's [1][2].

**DVM.** 24 h commit + 24 h reveal; quorum GAT 5M UMA; SPAT: 65% of staked UMA must agree or the vote rolls to the next round; wrong or missed vote slashed 0.1% of stake [14]. Votes run every other day, hence the 24-48 h debate window [2].

**"Too early" (P4) and 50/50 (P3).** Too-early: disputer wins the bond, market stays open [2]. In code the OO "ignore price" (`type(int256).min`) makes `resolve()` reset the question; valid prices are only 0, 0.5 ether, 1 ether → payouts `[0,1]`, `[1,1]`, `[1,0]` [10]. 50/50 is "rarely used" [2]; not valid on neg-risk [12]. No source gives P3/P4 frequencies (open question).

**Clarifications.** Published on-chain via the adapter's BulletinBoard mixin [1][10]. Through Nov 2025: 1,570 ancillary-data updates, 1,549 creator-authoritative clarifications; 83.34% arrive after request creation but before the first proposal [16] — i.e. clarifications are a live pre-resolution price event. On Polymarket International the Markets Team only clarifies; on Polymarket US it decides [47].

**Overrides/refunds.** See key facts 3 and 9. A 2024 practitioner note held that "Polymarket clarifications are binding and never overturned" [42] _[pre-2025]_; March 2025 disproved it (section 3).

## 2. Timing, capital lock, and the 95-99.9c gap

- **Floor:** proposal + 2 h (+1 h neg-risk) [1][12]. Disputed: 4-6 days per docs [1]; UMA FAQ says DVM 2-4 days [14]; affiliates say 48-96 h [59]. Zelensky suit took ~9 days and multiple rounds [30].
- **Chain study [16]:** median request→first proposal is 182 s on the legacy route but 176,388-744,151 s (2.0-8.6 days) on modern routes. Caution: the request is created at market initialization, so this mostly measures market life, not event→proposal latency. 29,430 of 185,550 questions were still unresolved at the cutoff.
- **Gebele & Matthes [17]:** "Most markets resolve on the same day as their EndDate"; bonding trades are held a median 0.76-2.0 h.
- **Commercial study [21] (Poly Syncer, 18,427 markets, 2025-05-09→2026-05-08, `settle − event_end`):** median 41 min, p90 6 h 24 m, p99 4 d 5 h, p99.9 11 d; dispute rate 1.0% (184 markets), median dispute adds 49 h. By category (median / p99 / dispute rate): NBA 22 m / 14 h / 0.2%; soccer 28 m / 22 h / 0.3%; crypto price 38 m / 16 h / 0.6%; tech 1 h 24 m / 2 d 14 h / 1.2%; politics horse-race 2 h 48 m / 3 d 6 h / 1.6%; politics policy 4 h 22 m / 9 d 4 h / 3.4%; geopolitics 5 h 16 m / 14 d / 4.8%. **Internally inconsistent** with a 2 h liveness (medians <2 h imply `event_end` is a scheduled timestamp later than the real event, or early proposals); use only for the _ranking_ of categories and the tails. Causes of disputes: ambiguous wording 43%, source conflict 22%, late reversals 14% [21].
- **Dispute mix by category:** sports 31.5%, politics 20.4%, crypto 16.7% of disputed events [18] — sports dominate counts because sports dominate market counts (77.9% of markets resolved in a sampled April 2026 week [19]), not because they are riskier.
- **Price in the gap.** Persistent near-certain contracts quote 1-5 bp under $1 at short horizon and 4-10% under at 180+ days; the discount term structure is positive, falls steeply and flattens by ~20 days; correlation with Aave rates r≈0.37, weak with Treasuries [17]. Neg-risk conversion compresses the discount (NO-basket ≈ 1 − [1−D(τ)]/(n−1)); conversion fees bite hardest at short maturities (∝1/τ) [17]. Kalshi's frontier sits closer to par (interest-bearing collateral) [17].
- **Who is on the other side.** Holders who value recycled capital above the last 0.1-0.3c [17]; press describes retail selling at 0.997-0.999 to cash out [63] (_soft_). In contested markets the seller may be better informed about the vote: in the UFO market a $615,000 buy at 0.998 (gross ~$1,230) was made ~10 h before finalization while two proposals had been disputed [40]; it paid, but that is a 0.2% return on full dispute risk.

## 3. Disputed resolutions 2024-2026 and what happened to holders

| Market | Size | What happened | Holders |
|---|---|---|---|
| Venezuela election (Jul-Aug 2024) _[pre-2025]_ | — | UMA declared González on Aug 5 against the official CNE result | Maduro shares 75c → 0 [33] (snippet) |
| Barron Trump / $DJT (Jun 2024) _[pre-2025]_ | >$1M | UMA voted No repeatedly; Polymarket contradicted UMA | Only refund on record [41][42] |
| Ukraine-US mineral deal before April (Mar 2025) | ~$7M | Largest Yes holder proposed Yes on a weekend (~$3k bonds across rounds) to get ahead of a clarification; DVM: P2 233 voters/12M UMA beat P4 "too early" 235 voters/9M UMA; one holder cast ~5M UMA (~25%) from three accounts. Polymarket issued a clarification against Yes minutes before the vote closed, then a second accepting UMA's Yes | Yes 9-20c → 100c; >$500k moved from No to Yes; no refunds; deal was actually signed end of April [26][27][28][29] |
| Zelensky suit before July (Jun-Jul 2025) | $237M | First resolved Yes, flipped to No over ~9 days of disputes; UMA cited no "credible reporting consensus" although 40+ outlets called it a suit; final 2025-07-08 | Yes $0.19 → $0.04 → 0 [30][31][32] |
| Trump declassifies UFO files in 2025 (Dec 2025) | $16M | Two proposals, two disputes; resolved Yes on Pentagon-hosted artifacts without a presidential order; finalized 2025-12-10 | No → 0 [40] |
| US invades Venezuela (Jan 2026) | $10.5M | Maduro captured 2026-01-03; Polymarket clarification: a "snatch-and-extract mission" is not an operation "intended to establish control" | Settled No; Yes buyers of the headline lost [34] |
| Khamenei out by Feb 28 (Feb-Mar 2026) | $529M+ Iran complex | Disputed twice on Polymarket; Kalshi halted and settled at pre-death last prices | Polymarket reported paid Yes (snippet, _unverified_); Kalshi reimbursed some trades [54] |
| US-Iran ceasefire extended by Apr 22 (Apr 2026) | $203.6M | Rules required confirmation by both governments; Iran never confirmed in its own voice; three dispute rounds → No | Yes traded 0.1-0.3c while world press reported the extension; one trader claimed a $20M+ loss [36][37] |
| Israel-Hezbollah ceasefire extended by Apr 26 | $20.9M | Two rounds → Yes despite literal-criteria objections | [37] |
| MicroStrategy sells BTC by May 31 (Jun 2026) | $60M+ | 8-K on Jun 1 disclosed 32 BTC sold May 26-31; Polymarket clarification: "Confirmation achieved outside of the market's time frame does not qualify"; DVM 98.6% No; the June contract paid Yes | Yes collapsed <1c; individual losses claimed $500k and $35k [39] |
| US-Iran permanent peace deal (Jun 2026) | $345M complex, $66M contract | Dispute over "permanent" vs a 60-day MOU; trading continued during the vote | final outcome not captured [35] |

Fort Knox gold audit ($3.5M, "flagged as manipulated") appears only on an affiliate page — _unverified_ [38]. Combined disputed volume in the April 2026 Iran chain ≈ $489M [37].

**Governance risk and voter economics.** UMA supply 129.9M, cap ~$35M [61]; ~20M UMA staked in 2023 [15] _[pre-2025]_ and ~21M UMA voted in the March 2025 dispute [28] → the stake actually deciding nine-figure markets is worth roughly $8M at current prices (_derived; staked figure stale_). ~420 unique voters per recent vote [6]. Voter APY: UMA FAQ "typically 16-21%" [14]; 28.4% APR at 2023 participation [15]; 7-day unstake cooldown [15]; delegation pool UMA.rocks advertised ~14% (snippet). The 0.1% slash for deviating from the majority is the core of the "vote with the whale" critique [31]. UMA.rocks expelled member "Scout", who admitted voting while holding positions [22]. Risk Labs: "We have never seen any credible evidence of UMA market manipulation" [22]. Reform status: EigenLayer/UMA/Polymarket "next-gen oracle" research announced 2025 [62], reported as largely stalled in May 2026 [24]; Coplan called the process "messy" [22]; an unlaunched POLY token could internalize resolution [60]. **No replacement oracle is live as of this writing** (not found in changelog [44]).

## 4. Non-UMA resolution and what it removes from sniping

- **Chainlink (crypto):** Data Streams + Automation settle "as soon as the clock runs out" [43]; covers 5-min, 15-min, 4-h up/down and, per the oracle guide, crypto price markets generally [47]. Since 2026-08-07 settlement uses a Chainlink-computed TWAP (5-min: 30 s then 60 s from 08-14; 15-min and 4-h: 60 s) [44]; crypto taker delay cut 250 ms → 50 ms on 2026-08-17 [44]. Motive: a Stanford/SMU working paper on ~16,000 five-minute BTC contracts found 821 likely manipulators earning ~$8.2M by pushing Binance spot in the final seconds [45][46]. Claimed $9B+ cumulative volume in Chainlink-settled markets [45] (_soft_). For a sniper: no proposal, no liveness, no 99c window — the residual edge is feed-latency and TWAP modelling, a different strategy.
- **Pyth (TradFi):** daily up/down and close markets on indices, gold, silver, WTI, natgas and a dozen-plus US equities settle on Pyth feeds [47][48].
- **Sports:** still UMA, but through `UmaSportsOracle`: one OO request per game returns home/away scores (UMIP-183 encoding, including cancellations); all Winner/Spread/Total markets of that game resolve from it [13]. One undisputed 2-h window unlocks many markets at once; dispute rates ~0.2-0.3% [21]. The competitive edge is in-play/final-whistle speed, not the oracle.
- **Polymarket US (QCX LLC, CFTC DCM):** Polymarket Clearing settles $1/$0 or per the contract's Settlement Description; outcome = value "determined or declared by the Source Agency at or before the Expiration Time"; discretionary review under Rule 10.4; final, no appeal; last-traded-price settlement on death/incapacity (Rule 10.5); rulebook dated 2026-09-14 [49][50]. Fees: Θ=0.0695 taker, −0.0125 maker; $0.07 per 100 contracts at $0.99 [51]. No bond, no dispute window, no public proposal event to react to.

## 5. Rule ambiguity as a traded factor

- **Evidence the market sometimes prices the rules, not the headline:** ceasefire-extension Yes sat at 0.1-0.3c through unanimous press coverage and resolved No [36][37] — rule readers were right and the headline buyers supplied the liquidity.
- **Evidence it sometimes does not:** Nov 2025 shutdown-end ladder — "Ends Nov 12" peaked at 97c then went to ~1c at midnight because the rule keyed on the ET calendar date of the OPM announcement ($13.1M on that strike, ~$30M on the ladder) [53]. Two live Polymarket shutdown contracts were priced in the logically wrong order (stricter 16.5c > looser 14.5c; only ~$8k volume) [53]. Anecdote (self-reported): "Trump says China" No bought at 25c, exited 95c+ because Q&A was excluded by the rules [64].
- **Cross-venue:** ~6% of events are cross-listed across ten venues and semantically equivalent markets show persistent execution-aware deviations of 2-4% [20]; part of that "arb" is resolution-semantics risk. Structural differences: Kalshi names a source agency with sole discretion and morning-ET cutoffs; Polymarket adds "consensus of credible reporting" and 11:59 pm ET — up to a 13-hour gap in which the two legs settle on opposite sides [53].
- **What UMA voters reward** (practitioner, [42] _pre-2025_): title/"spirit of the market", mainstream reporting over primary sources, consistency with earlier rulings (the May 2025 Zelensky-outfit precedent drove the July vote [30]). 2026 cases add: timing of _confirmation_ beats timing of the _event_ [39]; literal both-parties confirmation beats press consensus [37].
- **Predictability:** once disputed, outcome is ~90% machine-predictable from public text [18]; who gets disputed is not. The tradable signal is therefore the vote, not ex-ante ambiguity screening — and Bloomberg notes traders already "follow whale voting behaviour instead of fundamentals" during disputes [24].

## 6. What a builder who already runs LP / cross-venue arb / resolution-sniping / copy-trading bots is likely to UNDERESTIMATE

1. **Break-even loss rate equals the discount.** Buying at p breaks even at flip probability q = 1−p: 1% at 0.99, 0.1% at 0.999 (_derived_). Category dispute rates run 0.2% (NBA) to 4.8% (geopolitics) [21] and a material share of 2025-26 marquee disputes flipped the "obvious" side. A flat size rule across categories is mis-sized by more than an order of magnitude. Note geopolitics is simultaneously fee-free [55] and the worst tail.
2. **The measured prize is small.** Best observed settlement-liquidity address: $23.6k lifetime over ~35k trades; top-100 median APY 6.22% [17]. Above 0.999 there is no tick left [17][57]. The strategy is a capacity-constrained cash-management sleeve, not an alpha engine, unless you take semantic/dispute risk deliberately.
3. **Capital lock is fat-tailed and correlated.** p99 4 days, p99.9 11 days, geopolitics p99 14 days [21]; disputes cluster in one news complex (Iran chain: seven markets, ~$489M, all 2-3 rounds [37]). Add +1 h on every neg-risk market [12] and a 29k-question unresolved backlog at any time [16].
4. **Your counterparty at 0.998 in a disputed market may be a voter.** ≥60% of active voters trade on Polymarket; ~20% of disputes have a conflicted voter [22][23]; nine wallets decide [24].
5. **Proposal timing is itself an attack surface:** weekend proposal to beat a clarification [28]; clarifications land after request creation in 83% of cases [16]; Polymarket reversed its own clarification within hours [28]. A bot that treats "proposed" as "done" is exposed for the whole 2 h, and a P4 verdict simply reopens the market [10].
6. **No refund backstop** on International [27]; on Polymarket US the exchange can reverse "obvious error" and settle at last traded price on death events [49] — a hedge leg there does not pay $1 in exactly the scenario (assassination/death markets) where International pays $1. Kalshi has the same carve-out [54].
7. **Fees are small at the extremes but not zero:** 4-7% of gross edge for takers; resting bids at 0.99x pay nothing and earn rebates [55] — so the edge belongs to makers with queue priority, and queue position at 0.999 is the real competition.
8. **The opportunity set shrank structurally:** crypto (Chainlink), TradFi (Pyth), Polymarket US (exchange) have no optimistic window; whitelisted/Polymarket-run proposers propose within minutes (affiliate claim [58]; consistent with 96% of proposals coming from the whitelist set [6]); sports are fast and cheap. What remains is politics/geopolitics/culture — precisely where semantic risk lives.
9. **Being a proposer or disputer is not a business:** $2-5 reward vs $750 bond; historic blow-ups of $32k [9][58]. Disputing a wrong proposal pays +$375 but requires being right _in the DVM's eyes_.
10. **Oracle regime change risk:** resolution is the most politically pressured part of the stack (WSJ, Bloomberg, House Oversight, CFTC letter [24][37]); a POLY- or in-house oracle would change bonds, windows and event signatures the bot keys on [60].

## Could not verify / open questions

- Current MOOV2 whitelist size (177?) and post-MOOV2 dispute reduction — affiliate only [38].
- Bond/reward dispersion across live requests ($500 vs $750; $2 vs $5) — needs an on-chain pull of `proposalBond`/`reward`.
- Frequency of P3 (50/50) and P4 outcomes; share of first-round disputes where the second proposal differs; how first-round bonds settle after an adapter reset.
- True event→proposal latency by category ([21] is inconsistent, [16] measures from market creation).
- Current staked UMA and live voter APY (only 2023 and FAQ figures found); whether GAT/SPAT changed.
- Final outcomes of the $345M Iran "permanent peace" market and Khamenei payout amount.
- Whether sports requests use a liveness shorter than 2 h; UMIP-183 details.
- Whether any 2025-26 admin `resolveManually` was used on a traded market (paper [16] counts events but the fetched text did not list them).
- Changelog mention of a `/v2/resolutions` lifecycle endpoint (2026-09-04) appeared in one fetch summary and not in a second — _unverified_ [44].
- WSJ and Bloomberg originals were not fetchable; figures come from syndication/summaries [22]-[25].
- 2024 Venezuela election details rest on a search snippet [33].

## Source ledger

| n | URL | Publisher | Date | Supports | F/S |
|---|---|---|---|---|---|
| 1 | https://docs.polymarket.com/developers/resolution/UMA | Polymarket docs | undated (read 2026-09-20) | bond, 2 h, flows, 4-6 d, adapter addresses | F |
| 2 | https://help.polymarket.com/en/articles/13364551-how-are-markets-disputed | Polymarket Help | upd. 2026-04-05 | debate/vote timing, too-early, 50/50, bond split | F |
| 3 | https://help.polymarket.com/en/articles/13364518-how-are-prediction-markets-resolved | Polymarket Help | upd. 2026-01-11 | $750 bond, 2 h | F |
| 4 | https://docs.polymarket.com/concepts/resolution | Polymarket docs | undated | "Anyone can propose", $750 pUSD | F |
| 5 | https://www.theblock.co/post/366507/polymarket-uma-oracle-update | The Block | 2025-08-12 | UMIP-189, 37 addresses, 4-day delays | F |
| 6 | https://blog.uma.xyz/articles/managed-proposers | UMA blog | 2025-08-12 | 1.3% dispute rate, 99.7/85.8%, 96%, 420 voters | F |
| 7 | https://github.com/UMAprotocol/UMIPs/blob/master/UMIPs/umip-189.md | UMA (GitHub) | 2025-07-29 | MOOV2 roles, address, multisig | F |
| 8 | https://polymarketguide.gitbook.io/polymarketguide/resolution/how-to-participate/propose/whitelist | PolymarketGuide (community) | undated | 5 proposals/6 months, >95% | F |
| 9 | https://polymarketguide.gitbook.io/polymarketguide/case-studies/securing-the-oracle | PolymarketGuide | undated | $32,250 losses, bond management | F |
| 10 | https://raw.githubusercontent.com/Polymarket/uma-ctf-adapter/main/src/UmaCtfAdapter.sol | Polymarket (source) | main, read 2026-09-20 | SAFETY_PERIOD, ignore price, payouts, admin fns | F |
| 11 | https://github.com/Polymarket/uma-ctf-adapter | Polymarket (README) | undated | reset on first dispute, DVM on second | F |
| 12 | https://raw.githubusercontent.com/Polymarket/neg-risk-ctf-adapter/main/docs/NegRiskOperator.md | Polymarket (docs) | undated | 1 h delay, flag, valid payouts | F |
| 13 | https://github.com/Polymarket/uma-sports-oracle | Polymarket (README) | undated | score requests, UMIP-183, market types | F |
| 14 | https://docs.uma.xyz/faqs | UMA docs | undated | 24 h/24 h, GAT, SPAT, 0.1% slash, APY 16-21% | F |
| 15 | https://blog.uma.xyz/articles/how-much-yield-can-you-earn-from-staking-uma | UMA blog | 2023-03-21 [pre-2025] | ~20M staked, 28.4% APR, 7-day cooldown | F |
| 16 | https://arxiv.org/html/2609.15368 | arXiv | 2026-09-14 | chain census of requests, disputes, clarifications, admin events | F |
| 17 | https://arxiv.org/html/2605.31431 | arXiv (Gebele, Matthes) | 2026-05-29 | settlement wedge, bonding-trade P&L, tick bound | F |
| 18 | https://arxiv.org/html/2604.15674 | arXiv (Wen, Zhou, Huang) | 2026-04-17 | 558 disputes, $972M, categories, LLM accuracy | F |
| 19 | https://arxiv.org/html/2605.10400v1 | arXiv (Nechepurenko) | 2026-05-10 | sports 77.9% of resolved; MOOV2 share (snippet) | F |
| 20 | https://arxiv.org/abs/2601.01706 | arXiv (Gebele, Matthes) | 2026-01-05 | 6% cross-listed, 2-4% deviations | F |
| 21 | https://www.polysyncer.com/blog/polymarket-resolution-time-2026 | Poly Syncer (commercial) | 2026-05-07 | timing percentiles by category, dispute causes | F |
| 22 | https://www.financemagnates.com/fintech/polymarkets-arbitration-model-faces-conflict-of-interest-questions/ | Finance Magnates (on WSJ) | 2026-05-18 | 1,150 disputes, 60%, 20%, Scout, quotes | F |
| 23 | https://www.kucoin.com/news/flash/polymarket-disputes-ruled-by-mysterious-uma-token-holders | KuCoin/BlockBeats (on WSJ) | 2026-05-18 | 0.2% spokesperson figure, 300+ conflicted disputes | F |
| 24 | https://www.cryptotimes.io/2026/05/27/only-9-wallets-control-nearly-half-of-uma-voting-power-on-polymarket-bloomberg/ | Crypto Times (on Bloomberg) | 2026-05-27 | nine wallets, 6,400 accounts, 2,000 disputes, stalled reform | F |
| 25 | https://www.bloomberg.com/news/articles/2026-05-26/crypto-whales-dominate-polymarket-disputes-worth-5-billion | Bloomberg | 2026-05-26 | original of 24 | S |
| 26 | https://www.coindesk.com/markets/2025/03/27/polymarket-uma-communities-lock-horns-after-usd7m-ukraine-bet-resolves | CoinDesk | 2025-03-27 | Ukraine minerals: 9%→100%, no refunds | F |
| 27 | https://www.theblock.co/post/348171/polymarket-says-governance-attack-by-uma-whale-to-hijack-a-bets-resolution-is-unprecedented | The Block | 2025-03-26 | "unprecedented", refund refusal | F |
| 28 | https://mrozi.substack.com/p/05m-scam-on-the-mineral-deal-market | mr.ozi (trader Substack) | 2025-03-27 | vote tallies, weekend proposal, two clarifications | F |
| 29 | https://www.oddsshopper.com/articles/prediction-markets/uma-oracle-polymarket-disputes | OddsShopper | 2026-08-15 | 5M UMA/25%, deal signed end of April | F |
| 30 | https://decrypt.co/329210/polymarket-rules-no-237m-bet-zelenskyys | Decrypt | 2025-07-09 | $237M, timeline, precedent | F |
| 31 | https://www.coindesk.com/markets/2025/07/09/this-isnt-decentralized-says-polymarket-power-user-as-zelenskyys-suit-controversy-unfolds | CoinDesk | 2025-07-09 | majority-voting incentive critique | F |
| 32 | https://www.coindesk.com/markets/2025/07/07/polymarket-embroiled-in-usd160m-controversy-over-whether-zelensky-wore-a-suit-at-nato | CoinDesk | 2025-07-07 | Yes $0.19→$0.04, final 07-08 | F |
| 33 | https://rekt.news/hedging-bets | Rekt | 2024 [pre-2025] | Venezuela 2024: Maduro 75c→0 | S |
| 34 | https://defirate.com/news/polymarket-sparks-outrage-settling-10-5m-venezuela-invasion-market-as-no/ | DeFi Rate | 2026-01-07 | invasion market, clarification text | F |
| 35 | https://thenextweb.com/news/polymarket-345-million-iran-peace-deal-dispute-uma-whale-voting | The Next Web | 2026-06-15 | $345M, "permanent", trading during dispute | F |
| 36 | https://coincentral.com/a-77m-dispute-why-polymarkets-resolution-on-the-us-iran-ceasefire-is-becoming-a-scandal/ | CoinCentral | 2026-04-28 | Yes 0.1-0.3c, $20M+ loss claim | F |
| 37 | https://polymarkets.co.il/en/news/polymarket-uma-scandal-explained/ | polymarkets.co.il (affiliate; cites Gamma API) | 2026-05-03 | Iran chain volumes, rounds, outcomes | F |
| 38 | https://polymarkets.co.il/en/guide/uma-disputes/ | polymarkets.co.il (affiliate) | 2026-06-07 | 177 whitelist, Fort Knox — leads only | F |
| 39 | https://www.theblock.co/news/ecosystems/2026-06-04-polymarket-upholds-no-outcome-strategy-bitcoin-sale-market-403600 | The Block | 2026-06-04 | Strategy market, 98.6%, clarification | F |
| 40 | https://cryptoslate.com/polymarket-faces-major-credibility-crisis-after-whales-forced-a-yes-ufo-vote-without-evidence/ | CryptoSlate | 2025-12-10 | UFO market, 0.998 trade | F |
| 41 | https://www.theblock.co/post/302171/polymarket-contradicts-umas-resolution-on-barron-trumps-involvement-with-djt-token | The Block | 2024-06 [pre-2025] | Barron/DJT refund | S |
| 42 | https://ariverwhale.substack.com/p/understanding-uma-and-dispute-resolution | A River Whale (trader Substack) | 2024-10-30 [pre-2025] | voter heuristics, single override | F |
| 43 | https://www.coindesk.com/web3/2025/09/12/polymarket-connects-to-chainlink-to-cut-tampering-risks-in-price-bets | CoinDesk | 2025-09-12 | Chainlink Data Streams + Automation | F |
| 44 | https://docs.polymarket.com/changelog | Polymarket docs | entries to 2026-09-04 | TWAP, taker delay, fees, ticks, pUSD | F |
| 45 | https://genfinity.io/2026/08/12/chainlink-twap-data-streams-polymarket-crypto-markets/ | Genfinity | 2026-08-12 | $8.2M study summary, $9B volume claim | F |
| 46 | https://www.bloomberg.com/news/articles/2026-07-15/polymarket-traders-may-be-manipulating-crypto-bets-study-says | Bloomberg | 2026-07-15 | Stanford/SMU study | S |
| 47 | https://polymarketguide.gitbook.io/polymarketguide/resolution/oracles | PolymarketGuide | undated | Markets Team / UMA / Chainlink / Pyth split | F |
| 48 | https://cointelegraph.com/news/polymarket-expands-into-equities-and-commodities-with-pyth-price-feeds | Cointelegraph | 2026 (undated in snippet) | Pyth markets | S |
| 49 | https://polymarketexchange.com/files/legal/latest/rulebook | QCX LLC d/b/a Polymarket US | 2026-09-14 | Rules 10.4, 10.5, definitions (PDF parsed locally) | F |
| 50 | https://docs.polymarket.us/learn/markets/contract-settlement | Polymarket US docs | undated | $1/$0, Settlement Description, finality | F |
| 51 | https://docs.polymarket.us/fees | Polymarket US docs | eff. 2026-09-17 | US fee coefficients and table | F |
| 52 | https://defirate.com/prediction-markets/how-contracts-settle/ | DeFi Rate | 2026-08-17 | Kalshi vs Polymarket settlement, Cardi B | F |
| 53 | https://www.oddsshopper.com/articles/prediction-markets/kalshi-vs-polymarket-settlement-rules | OddsShopper | 2026-08-15 | shutdown ladder, inverted pricing, cutoff gap | F |
| 54 | https://defirate.com/news/kalshi-halts-khamenei-market-polymarkets-contract-enters-second-dispute/ | DeFi Rate | 2026-03-01 | Khamenei: Kalshi last-price settlement, Polymarket disputes | F |
| 55 | https://docs.polymarket.com/trading/fees | Polymarket docs | undated | fee formula and category rates | F |
| 56 | https://nautilustrader.io/docs/nightly/integrations/polymarket/ | NautilusTrader docs | undated | tick-size change handling, min order | F |
| 57 | https://polyarb-navy.vercel.app/glossary/tick-size | third-party glossary | undated | 0.96/0.04 thresholds | S |
| 58 | https://startpolymarket.com/learn/how-to-propose-resolutions/ | Start Polymarket (affiliate) | 2026-09-12 | $500/$2 claim, snapshot cadence, break-even | F |
| 59 | https://startpolymarket.com/learn/how-markets-resolve/ | Start Polymarket (affiliate) | 2026-09-15 | 48-96 h DVM, $500 bond claim | F |
| 60 | https://www.coindesk.com/markets/2026/04/06/polymarket-reveals-a-full-exchange-upgrade-to-take-control-of-its-own-trading-and-truth | CoinDesk | 2026-04-06 | pUSD, POLY and in-house "truth" | F |
| 61 | https://www.thestockobserver.com/2026/09/09/uma-uma-market-capitalization-reaches-35-26-million.html | Stock Observer (auto-generated) | 2026-09-09 | UMA cap/price/supply | S |
| 62 | https://www.theblock.co/post/342351/eigenlayer-polymarket-and-uma-collaborate-on-developing-next-gen-oracle | The Block | 2025 | next-gen oracle research | S |
| 63 | https://coinedition.com/polymarket-bots-whales-profit-analysis-today/ | Coin Edition | 2025-10-15 | "endgame sweep" description | F |
| 64 | https://medium.com/coinmonks/how-to-trade-polymarket-profitably-in-2026-9-advanced-strategies-and-the-1-754-78-day-30f8de57727b | Medium/Coinmonks (self-reported) | 2026-07 | "Trump says China" anecdote | S |
| 65 | https://help.polymarket.com/en/articles/14762452-polymarket-exchange-upgrade-april-28-2026 | Polymarket Help | 2026-04 | upgrade date | S |
