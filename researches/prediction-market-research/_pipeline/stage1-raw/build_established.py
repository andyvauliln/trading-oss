import json, copy
import os
S=os.path.dirname(os.path.abspath(__file__))
OUT="/home/superuser/trading/trading-oss/researches/prediction-market-research/_evidence"

est={s["slug"]:s for s in json.load(open(f"{S}/consolidate_established.json"))["strategies"]}
crit=json.load(open(f"{S}/critic_established.json"))
miss={m["slug"]:m for m in crit["missing"]}
critic_notes=crit["merge_or_split"]+crit["misclassified"]+crit["weakest_entries"]
def notes_for(*keys):
    return [n for n in critic_notes if any(k in n for k in keys)]

def child(parent, slug, name, scope, **kw):
    p=copy.deepcopy(est[parent]); p.update(slug=slug, name=name, scope=scope, parent_slug=parent, parent_scope=est[parent]["scope"]); p.update(kw); return p
def keep(src, **kw):
    p=copy.deepcopy(est[src]); p["parent_slug"]=src; p.update(kw); return p
def new(slug, name, category, maturity, one_line, scope, **kw):
    d=dict(slug=slug,name=name,category=category,maturity=maturity,one_line=one_line,scope=scope,key_evidence=[],sub_variants=[],merged_from=[]); d.update(kw); return d
def from_missing(slug, **kw):
    m=copy.deepcopy(miss[slug]); m.setdefault("sub_variants",[]); m.setdefault("merged_from",[]); m.setdefault("key_evidence",[]); m.update(kw); return m

L=[]
L.append(keep("maker-reward-pool-farming", deepen=True, seed="1 market making + 9 incentive farming"))
L.append(keep("event-market-making-spread-carry", deepen=True, seed="1 market making"))
L.append(keep("short-crypto-maker-side", deepen=True, seed="1 market making"))
L.append(keep("sportsbook-anchored-sports-mm", deepen=True, seed="1 market making"))
L.append(from_missing("genesis-window-new-listing-liquidity", seed="new"))
L.append(keep("combos-rfq-market-making", seed="new", extra_scope="Also cover the REQUESTER side (combo taker exploiting correlation mispricing and stale legs), which discovery rated purely theoretical. The critic doubts the 'Emerging' label: keep it only if you can show at least one external (non-Polymarket) combo maker live, else label Experimental."))
L.append(child("cross-venue-arbitrage-leadlag","cross-venue-locked-arbitrage","Cross-venue locked arbitrage (Polymarket vs Kalshi / exchanges / sportsbooks)",
  "Cover ONLY the locked two-leg structure: same event bought on both sides across venues. Go deep on what an existing arb builder underestimates: rule-text and settlement-source mismatch (documented divergent resolutions), capital lock-up and annualised return after fees on both legs, fee asymmetry after Polymarket fee V2, leg risk and partial fills, venue account limits and KYC (one natural person cannot lawfully hold every leg), stablecoin / FX basis, withdrawal latency, tax asymmetry, how crowded it is (hundreds of GitHub repos, paid scanners) and the honest absence or presence of documented realised PnL. The international-vs-US Polymarket order-book gap is a signal note only. Boundary: lead-lag quoting and signals are cross-venue-leadlag-signals; options / futures implied probabilities are derivatives-implied-relative-value.",
  deepen=True, seed="2 cross-platform arbitrage", maturity="Established practice (crowded; realised PnL poorly documented)"))
L.append(child("cross-venue-arbitrage-leadlag","cross-venue-leadlag-signals","Cross-venue lead-lag: follower quoting and price-discovery signals",
  "Cover the NON-locked use of other venues: which venue leads price discovery by category (Kalshi, Polymarket US BBO feed, Betfair, sportsbooks, Pinnacle), follower quoting / stale-quote picking on the lagging venue, using the free Polymarket US BBO or Kalshi book as a fair-value input for international Polymarket quotes, measured lead-lag magnitudes and half-lives, and why this needs no capital on the second venue. Boundary: locked two-leg structures are cross-venue-locked-arbitrage; sportsbook-anchored quoting of sports is sportsbook-anchored-sports-mm (cross-reference, do not repeat).",
  deepen=True, seed="2 cross-platform arbitrage", maturity="Emerging"))
L.append(keep("rebalancing-arbitrage-yesno-negrisk", seed="3 same-platform arbitrage", maturity="Established but effectively closed to newcomers (verify)"))
L.append(keep("combinatorial-logical-arbitrage", seed="3 same-platform arbitrage"))
L.append(keep("options-implied-relative-value", slug="derivatives-implied-relative-value", name="Derivatives-implied relative value (options, futures, merger-arb spreads vs Polymarket)", seed="new",
  extra_scope="WIDENED per critic: besides crypto / equity price ladders vs Deribit / CME option-implied distributions, cover FOMC decision markets vs fed funds futures (FedWatch), economic-data ladders vs nowcasts, M&A / deal-close markets vs merger-arb spreads, and any other listed-derivative reference."))
L.append(keep("short-crypto-latency-taker", seed="new / 5 fast execution", maturity="Established historically, now decayed for non-HFT takers (verify)"))
L.append(child("near-certain-bond-carry","resolution-sniping-post-outcome","Resolution sniping: outcome known, oracle not yet settled",
  "Cover ONLY the post-outcome window: the real-world result is known (or knowable from a primary feed) but the market has not settled. Go deep on what a sniping-bot builder underestimates: the measured gap from outcome to proposal to settlement by category, who still sells at 97-99.9c and why, how automatic / non-UMA resolution (Chainlink price feeds, sports data feeds, the US exchange) has shrunk the opportunity set, tick size and fee regime at price extremes, depth actually available, 'resolved-but-unsettled bonding' economics (median APY, top provider PnL, trade counts), dispute / too-early / clarification tail risk by category and how to size it, capital lock during disputes, first-to-know data sources, and competition. Boundary: PRE-outcome high-probability buying and holding-rewards carry are near-certain-bond-carry; trading the dispute itself is rules-dispute-trading; weather station-feed sniping is detailed in weather-markets (cross-reference).",
  deepen=True, seed="8 resolution sniping", category="Arbitrage / Information edge (speed)", maturity="Established"))
L.append(keep("near-certain-bond-carry", deepen=True, seed="8 resolution sniping (adjacent) + staking-like carry", category="Carry / tail-risk underwriting (closest template category: Arbitrage)",
  extra_scope="NARROWED: the post-outcome 'resolved-but-unsettled' window now has its own file (resolution-sniping-post-outcome); here cover PRE-outcome 95-99.9c harvesting, the settlement-discount term structure, liquidity-crunch / time-value trades, and holding rewards as the closest thing to staking on Polymarket (rate, eligible markets, whether complete sets qualify: verify). The critic notes this is carry / tail-risk underwriting, not arbitrage: break-even flip probability equals the discount."))
L.append(keep("rules-dispute-trading", deepen=True, seed="8 resolution sniping (oracle-lawyering)"))
L.append(keep("uma-side-operations", seed="staking / UMA", extra_scope="Critic: formally Established but economically negligible (reward of a few dollars against three- and four-figure bonds). Say so plainly with numbers; its real value may be the information feed. Include UMA staking / voting yield since the owner's suite covers staking."))
L.append(from_missing("news-event-feed-latency-taking", seed="5 news / event-driven fast execution"))
L.append(child("sports-automated-takers","sports-inplay-feed-latency-taking","In-play sports feed-latency taking",
  "Cover ONLY the speed variant: taking stale in-play quotes using faster score / event feeds than the makers have. Include Polymarket's order-delay rules on live sports, data-licence terms and courtsiding legality, what wallet reconstructions actually show (the critic says the flagship mechanism is unverified and contradicted by evidence pack E4), fees after V2, and who the counterparties are. Boundary: model-driven holding is sports-model-driven-taking; quoting is sportsbook-anchored-sports-mm.",
  seed="5 fast execution / new", maturity="Emerging (flagship claims unverified)"))
L.append(child("sports-automated-takers","sports-model-driven-taking","Model-driven sports taking (pre-game and hold-to-settlement)",
  "Cover ONLY the modelling variant: pre-game and in-game directional positions from ratings / Elo / closing-line-value models, sized and held to settlement; leaderboard sports wallets and their PnL, sharp-book lines as benchmark, bankroll and variance, the sports taker fee (0.05 since 2026-07-10, was 0.03: check evidence pack E1) and the cut in sports maker rebates, capacity. Boundary: feed-latency taking is sports-inplay-feed-latency-taking; quoting is sportsbook-anchored-sports-mm.",
  seed="4 statistical models / 11 expert", maturity="Established"))
L.append(new("statistical-mispricing-models","Statistical / quantitative mispricing models (polls, Elo, base rates, nowcasts, recalibration)","Directional trading","Emerging",
  "Systematic probability models built from public data (poll aggregates, Elo / ratings, base rates, macro nowcasts, scientific ensembles, domain recalibration curves) traded against the Polymarket price when the gap exceeds costs.",
  "This is the owner's seed category 4; the consolidator pushed its candidates out of this band, so rebuild it from the raw candidates. Cover: election / polling models vs market (2024 and 2025-2026 evidence), Elo / ratings models outside sports, base-rate and reference-class models, macro nowcasting for economic-data ladders (CPI, jobs, Fed) incl. Kalshi papers, public-baseline scientific models in niche count markets (flu, hurricanes, disease counts), domain x horizon x trade-size recalibration (e.g. political underconfidence slope ~1.45) and favourite-longshot tilts as a systematic overlay, forecast-to-bet conversion (Kelly / proper betting with fees). Be honest about evidence: most is calibration description or Kalshi backtests without costs, little verified Polymarket PnL. Mine S1-discovery-candidates.json for the candidates named in merged_from. Boundary: sports models are sports-model-driven-taking; weather is weather-markets; count / mention markets are recurring-count-mention-counter-markets; LLM forecasters are llm-forecasting-agents.",
  seed="4 statistical / quantitative models",
  merged_from=["academic: Public-baseline statistical models","adjacent-transfer: Scientific-ensemble edge in niche count markets","adjacent-transfer: Macro nowcasting for economic-data ladders","academic: Domain x horizon x trade-size recalibration model","adjacent-transfer: Domain calibration tilts","adjacent-transfer: Forecast-to-bet conversion layer"]))
L.append(new("llm-forecasting-agents","LLM forecasting agents (direct retrieval-and-reason forecasters trading the gap)","Directional trading","Emerging",
  "An LLM pipeline retrieves news and data, produces a calibrated probability per market and trades the gap to the Polymarket price under deterministic risk limits.",
  "The baseline every speculative multi-agent idea must beat. Cover: state of the art vs market price (ForecastBench, Metaculus AI tournaments, Prophet Arena, live Kalshi / Polymarket LLM trading arenas: mostly negative after costs), open-source Polymarket agents and commercial 'AI quant' products, viral PnL claims and why they are unverified, where LLMs plausibly have edge (long-tail illiquid markets, breadth, rules reading, multilingual sources, speed of text digestion), design choices that matter (retrieval, ensembling, market-price anchoring, extremising, fine-tuning / RL on resolved questions), traps (backtest leakage, knowledge-cutoff contamination, Brier vs PnL, fees and spread), cost per forecast, and a deterministic sizing / risk layer. Primary source: evidence pack E7. Mine S1-discovery-candidates.json for merged_from names. Boundary: simulation / debate / internal-market / self-improving variants live in the speculative band (files 50+): reference, do not repeat.",
  seed="4 statistical models (AI variant)",
  merged_from=["traders: LLM-agent forecasting / 'AI quant' bots","academic: LLM/ML forecaster with proper-scoring-rule sizing","onchain-bots: Model-ensemble news/social probability bots"]))
L.append(keep("weather-markets", seed="4 statistical models (niche)", maturity="Established (small capacity): verify"))
L.append(keep("recurring-count-mention-markets", slug="recurring-count-mention-counter-markets", name="Recurring count, mention and public-counter markets", seed="4 statistical models (niche)",
  extra_scope="WIDENED per critic: the same build applies to any market resolved on a continuously updating public counter: box office, review-aggregator scores, streaming / chart counts, video views, and the LMArena leaderboard for 'best AI model on date X' plus model-release markets (specialist wallets exist: see critic_addition). Say where PnL evidence exists and where it does not.",
  critic_addition=miss.get("tech-ai-model-markets")))
L.append(keep("longshot-selling-flb", seed="4 statistical models (behavioural bias)"))
L.append(keep("discretionary-research-bets", seed="11 discretionary / expert trading"))
L.append(keep("screened-copy-trading", deepen=True, seed="6 copy trading"))
L.append(child("informed-flow-and-insider-trading","whale-informed-flow-tracking","Whale / informed-flow tracking, fast-follow and follower-flow trades",
  "The owner's seed category 7 (whale / wallet tracking and front-running-adjacent). Cover the DETECTION-and-react build only: fresh-wallet / conviction-size / funder-cluster detectors, academic screens and their measured predictive power, fast-follow economics (being exit liquidity, the practitioner who 'did not succeed', copycat bot results), use as a maker quote-pull / toxicity trigger, whale-alert products, PLUS the critic's addition: every V2 fill carries the routing app's builder code, so retail wallet-app flow and copy-bot cascades can be labelled; thin-book front-running of market orders and selling into copy-followers (flag as front-running-adjacent / manipulative where it is). Boundary: the illegal act of trading on MNPI is mnpi-insider-trading; PnL-ranked mirroring is screened-copy-trading.",
  seed="7 whale / wallet tracking", maturity="Emerging", category="Information edge (flow)",
  flags="Front-running-adjacent; deliberately baiting or dumping on followers is manipulative; alert products have triggered builder audits.",
  critic_addition=miss.get("builder-tagged-flow-and-follower-flow")))
L.append(keep("fee-tier-taker-incentives", slug="taker-rebates-fee-tier-overlay", name="Taker rebates, fee tiers and promo extraction (cost overlay)", deepen=True, seed="9 incentive farming",
  maturity="Established programme; an overlay rather than a standalone strategy", extra_scope="Critic: taker rebates are the largest subsidy line on the venue; present this as a module that re-costs every taker strategy at each rebate tier, plus the bounded promo / sign-up / referral extraction part (state whether sportsbook bonus conversion with Polymarket US / Kalshi as the lay leg is real: unverified)."))
L.append(keep("wash-trading-airdrop-farming", slug="wash-trading-airdrop-sybil-farming", name="Wash trading, airdrop and Sybil / multi-account farming (flagged)", deepen=True, seed="10 Sybil / multi-account farming + 9 points / airdrop",
  maturity="Established practice, unrealised payoff", extra_scope="Critic: prevalent but nobody has been paid (no token, no announced airdrop, post-fee loops negative-sum). Write it survey-level plus as a DETECTOR / defence specification for the owner's anti-Sybil work: no evasion how-to. Add the rival-venue points-farming-hedged-on-Polymarket sub-variant (Opinion: volume vs open interest, points value collapse)."))
L.append(child("informed-flow-and-insider-trading","mnpi-insider-trading","Trading on material non-public information (flagged: illegal, survey only)",
  "Survey only. Document that it happens and what happened to the people: cases and enforcement (DOJ / CFTC prosecutions 2026, Maduro-operation soldier, Israeli officers, Google Year-in-Search, OpenAI, teleprompter operator), scale estimates, Polymarket's policy and surveillance, the legal basis, and why it matters to an honest builder: it is the adverse-selection counterparty in geopolitics / mentions / corporate markets and must be priced into every maker and longshot-selling strategy. No how-to. Boundary: detecting and reacting to such flow is whale-informed-flow-tracking.",
  seed="flagged practices", maturity="Established practice (illegal)", category="Information edge (prohibited)"))
mm=child("oracle-input-manipulation","market-manipulation-and-exploits","Outcome / oracle manipulation, governance capture and settlement exploits (flagged: threat model)",
  "Survey-level THREAT MODEL, no how-to. Merge three flagged practices: (1) manipulating the real-world input or resolution source (sensor tampering such as the Paris CDG weather case, staged events, narrative / spoof manipulation); (2) oracle governance capture: UMA voting-power concentration, conflicted voters and proposers, proposal timing against clarifications, documented episodes and what Polymarket did; (3) settlement-atomicity exploits ('ghost fills', bot hunting) and their status after CLOB V2. For each: documented cases, who lost money, detection, enforcement, legal exposure, and the defensive implication for every other strategy in the survey.",
  seed="flagged practices", maturity="Established practice (illegal / prohibited)", category="Manipulation (prohibited)")
mm["parent_scope"]=est["oracle-input-manipulation"]["scope"]+" || GHOST FILLS: "+est["ghost-fills-bot-hunting"]["scope"]
mm["key_evidence"]=est["oracle-input-manipulation"]["key_evidence"]+est["ghost-fills-bot-hunting"]["key_evidence"]+miss["oracle-governance-capture"].get("key_evidence",[])
mm["critic_addition"]=miss["oracle-governance-capture"]
L.append(mm)
L.append(keep("builder-code-routing-business", seed="service & data business"))
L.append(child("data-referral-content-businesses","data-analytics-api-products","Data, analytics, API and infrastructure products",
  "Cover ONLY products: wallet trackers and analytics SaaS, terminals, alert services, historical order-book / leak-free replay datasets, data and API resale, forecast / calibrated-probability feeds, low-latency news feeds, market-integrity surveillance and employee-compliance monitoring, no-code strategy builders, managed vault / fund and OTC intermediary. Give pricing, revenue, users, funding where public, and say plainly where no revenue evidence exists (the critic lists several sub-variants with none). Boundary: fee-on-flow apps are builder-code-routing-business; audience businesses are referral-affiliate-content-businesses.",
  seed="service & data business"))
L.append(child("data-referral-content-businesses","referral-affiliate-content-businesses","Referral, affiliate, creator and content businesses",
  "Cover ONLY audience / distribution businesses: affiliate and referral programmes (Polymarket, Kalshi, Polymarket US), newsletters, paid signal groups, creators, education, media; their unit economics and disclosed numbers; the scam fringe (fake-PnL marketing, drainer copy bots) and FTC disclosure exposure. Boundary: software products are data-analytics-api-products.",
  seed="service & data business"))

for i,s in enumerate(L,1):
    s["n"]=f"{i:02d}"; s["band"]="established"
    s["file"]=f"{s['n']}-{s['slug']}.md"
    s["critic_notes"]=notes_for(s["slug"], s.get("parent_slug") or "~~")
json.dump({"band":"established","numbering":"01-49 established / emerging; 50+ speculative / experimental / theoretical","strategies":L,"all_critic_notes":critic_notes,
           "moved_to_speculative_band":["perps-lp-rewards-basis"]}, open(f"{OUT}/S0-strategy-list-established.json","w"), indent=1)
print(len(L)); [print(s["file"], "| deepen" if s.get("deepen") else "") for s in L]
