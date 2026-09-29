import json, copy, os, re, glob
S=os.path.dirname(os.path.abspath(__file__))
ROOT="/home/superuser/trading/trading-oss/researches/prediction-market-research"
OUT=ROOT+"/_evidence"
D="/home/superuser/.claude-faridagazizov/projects/-home-superuser-trading-githab-project-research/72b8b8fc-4e1c-419e-976d-1ffb565d3403/subagents/workflows/wf_580b5c88-98f"

# ---- pull the speculative critic from the journal if it has finished
labels={}; res={}
for line in open(D+"/journal.jsonl"):
    j=json.loads(line)
    if j.get("type")=="started": labels[j["agentId"]]=j["label"]
    if j.get("type")=="result":
        r=j.get("result", j.get("value"))
        if isinstance(r,str):
            try: r=json.loads(r)
            except Exception: pass
        res[labels.get(j["agentId"],"?")]=r
crit_s=res.get("critic:speculative")
print("speculative critic finished:", bool(crit_s))
if crit_s: json.dump(crit_s, open(f"{S}/critic_speculative.json","w"), indent=1)

est_doc=json.load(open(f"{OUT}/S0-strategy-list-established.json"))
E=est_doc["strategies"]
est_raw={s["slug"]:s for s in json.load(open(f"{S}/consolidate_established.json"))["strategies"]}
sp=json.load(open(f"{S}/consolidate_speculative.json"))
cands=json.load(open(f"{OUT}/S1-discovery-candidates.json"))

def new(slug,name,category,maturity,one_line,scope,merged_from,**kw):
    d=dict(slug=slug,name=name,category=category,maturity=maturity,one_line=one_line,scope=scope,key_evidence=[],sub_variants=[],merged_from=merged_from); d.update(kw); return d

P=[copy.deepcopy(s) for s in sp["strategies"]]
for s in P:
    if s["slug"]=="sponsor-and-inform-niche-models":
        s["merged_from"]=s.get("merged_from",[])+["platform-surface: Sponsor-to-trade and market origination","services: Market proposal, sponsorship and brand-partnership brokerage"]
        s["extra_scope"]="Also absorb the two market-origination candidates dropped from the established band (sponsor-to-trade / market origination for a private model; market proposal, sponsorship and brand-partnership brokerage). Note that markets are created only by Polymarket's team, so origination runs through proposals and sponsorship."
crit_missing=[]
if crit_s:
    for m in crit_s.get("missing",[]):
        m=copy.deepcopy(m); m.setdefault("key_evidence",[]); m.setdefault("sub_variants",[]); m.setdefault("merged_from",[]); m["from_critic"]=True
        crit_missing.append(m)
P+=crit_missing
# non-AI experimental strategies that the established consolidator pushed to this band
P.append(new("logit-space-belief-vol-quoting","Control-theoretic / belief-volatility-aware quoting in logit space","Market-making","Experimental",
  "Quote binary contracts with an inventory-control model defined on log-odds, with a structural belief-volatility term that widens before scheduled information and near the 0 / 1 boundaries.",
  "Non-AI experimental market-making model. Cover the papers (control-theoretic quoting in logit space; belief-volatility-aware quoting), what was shown in simulation or on Kalshi only, why binary payoff boundaries break Avellaneda-Stoikov style assumptions, how it would plug into an existing Polymarket quoting bot as a fair-value / spread module, and a cheap validation: replay on recorded Polymarket books vs the owner's current quoting logic (metric: spread capture net of adverse selection per unit inventory risk). Boundary: practical event market making is file event-market-making-spread-carry.",
  ["academic: Control-theoretic quoting in logit space","adjacent-transfer: Belief-volatility-aware quoting"]))
P.append(new("inplay-behavioural-fades","In-play behavioural fades and state-model trading (underreaction drift, panic fade, insurance demand)","Directional trading","Experimental",
  "Trade documented in-play behavioural patterns in live sports markets: underreaction drift after scoring events, overreaction panic fades, late-game 'insurance demand', and win-probability state models against the live price.",
  "Non-AI experimental. Cover each pattern with its evidence (Kalshi papers, Betfair simulations, a marketing-grade +39% claim: say which is which), why executable taker PnL was negative in the papers and whether a maker-skew implementation could survive, Polymarket live-sports order delay and the sports taker fee (0.05 since 2026-07-10: check evidence pack E1), data needs (licensed live feed), and validation by replaying recorded in-play books. Boundary: feed-latency taking is sports-inplay-feed-latency-taking; model-driven holding is sports-model-driven-taking.",
  ["academic: In-play underreaction drift","adjacent-transfer: In-play state-model trading","adjacent-transfer: Final-minutes 'insurance demand'","traders: In-play panic-fade ladder"]))
P.append(new("flow-fading-and-leadlag-statarb","Flow-dislocation fading, counter-trading bad wallets and cross-market lead-lag stat-arb","Arbitrage","Experimental",
  "Provide liquidity against price dislocations caused by uninformed flow, fade the systematically worst wallets, and trade lead-lag relations between related contracts or between Polymarket and external assets.",
  "Non-AI (or LLM-filtered) experimental stat-arb family. Cover: fading flow-driven dislocations (evidence is play-money or absent on Polymarket), counter-trading the worst wallets (premise supported, strategy untested), Granger + LLM-filtered lead-lag across related contracts (Kalshi backtest without costs), cross-market stat-arb, and prediction-market signals as alpha or hedge for external markets (small out-of-sample gains). For each: mechanism, why it may not survive fees and spread, and one cheap leakage-free backtest on public trade history. Boundary: cross-VENUE lead-lag quoting is cross-venue-leadlag-signals; logical constraints are combinatorial-logical-arbitrage and semantic-market-graph-relative-value.",
  ["academic: Fading flow-driven price dislocations","traders: Counter-trading the worst wallets","academic: Granger + LLM-filtered lead-lag","adjacent-transfer: Cross-market lead-lag and stat-arb","academic: Prediction-market signals as alpha or hedge"]))
P.append(new("settlement-window-and-regime-edges","Settlement-window and microstructure regime edges (TWAP end-window, tick-size switches, void rules)","Arbitrage","Purely theoretical",
  "Price the mechanical details nobody models: the averaging window of the settlement price feed in short crypto markets, tick-size regime switches near price extremes, and void / cancellation rules in sports and esports.",
  "Purely theoretical / single-operator evidence. Cover: Chainlink TWAP end-window pricing in crypto up/down markets (regime only weeks old, weighting unpublished), tick-size and other microstructure regime-change events as predictable liquidity shocks, void / cancellation-rule pricing (50c refunds, DNP grading) in esports and sports. For each: the exact rule text (evidence packs E1 / E3), the hypothesised mispricing, why nobody is known to exploit it, and a cheap on-chain / order-book test. Boundary: generic latency taking is short-crypto-latency-taker.",
  ["platform-surface: Chainlink-TWAP end-window pricing","platform-surface: Microstructure regime-change events","onchain-bots: Void / cancellation-rule pricing"]))
perps=copy.deepcopy(est_raw["perps-lp-rewards-basis"]); perps["maturity"]="Experimental"; perps["moved_from_band"]="established"
perps["extra_scope"]="Moved here by the critic: the venue launched 2026-09-03, there is no third-party PnL, US / Canada are blocked and evidence pack E1 scoped perps out. Keep it short and honest; the main risk is restating docs."
P.append(perps)
P.append(new("event-hedge-desk-structured-products","Event-hedge desk and hedged baskets on Polymarket rails","Service & data business","Purely theoretical",
  "Sell event-risk hedges or packaged baskets (tariffs, elections, rate decisions, weather) to businesses and investors, laying the risk off on Polymarket / Kalshi and earning a structuring margin.",
  "A speculative SERVICE business dropped by the consolidator for regulatory risk: include it, flagged. Cover: who has real event exposure, what the basket / hedge product looks like, depth limits on Polymarket vs the notional a business needs, precedent (Kalshi hedging marketing, weather derivatives, OTC event swaps), the regulatory wall (swap dealing, CFTC, broker / adviser registration, offshore venue access) per evidence pack E9, and the cheapest validation (customer discovery + paper pricing against live books, no capital). Boundary: managed vaults and data products are data-analytics-api-products.",
  ["wildcard: Event-hedge desk and hedged baskets on Polymarket rails"], flags="Highest regulatory risk in the survey: likely requires licensing; offshore venue access for clients is a legal problem."))


# ---- orchestrator decisions on the speculative critic's report (2026-09-20)
MERGE={"information-partitioned-delphi-panel":("internal-agent-prediction-market","MERGED per critic: this file is now the 'diversity-engineered synthetic crowd' (internal market + information-partitioned Delphi panel). Both are bounded by the same constraint (agent correlation rho ~0.70, effective N ~1.4) and need the same ablation harness (rho=1.0 control, plain logistic aggregator, independent-vote arm). Cover both mechanisms in sub-sections; the absorbed entry is under 'absorbed'."),
       "decision-body-member-twins":("elite-selection-bargaining-simulators","MERGED per critic: this file is now 'small decision bodies' with a public-vote section (member twins: FOMC dissents, legislative whip counts on pivotal members, courts) and a secret-vote / bargaining section, plus the critic's bilateral deadline-bargaining sub-variant (deals, strikes, shutdown ends, ceasefire extensions). Be honest about tradable capacity (e.g. $4.3k volume on FOMC dissents vs $8.07M on the decision). The absorbed entry is under 'absorbed'."),
       "external-forecaster-sourcing":("market-anchored-selective-deference","ABSORBED per critic: external-forecaster sourcing is 'a task, not a file': cover it here as a sub-variant (an 8-week test of adding public benchmark forecasters, or a subsidised play-money mirror market, as one more expert inside the stacker; token-mining and staked tournaments are out of scope). Also: the day-zero opening-quote sub-variant is an LP business: cross-reference file genesis-window-new-listing-liquidity instead of covering it here. The absorbed entry is under 'absorbed'.")}
bys={s["slug"]:s for s in P}
for srcslug,(tgt,note) in MERGE.items():
    if srcslug in bys and tgt in bys:
        a=bys[srcslug]; t=bys[tgt]
        t.setdefault("absorbed",[]).append(a)
        t["merged_from"]=(t.get("merged_from") or [])+(a.get("merged_from") or [])
        t["key_evidence"]=(t.get("key_evidence") or [])+(a.get("key_evidence") or [])
        t["extra_scope"]=(t.get("extra_scope","")+" "+note).strip()
        P.remove(a)
EXTRA={"settlement-window-and-regime-edges":"Critic cross-band note: since 2026-08-07 crypto up/down markets settle on a Chainlink Data Streams TWAP (60 s window), while Kalshi settles on an average of 60 one-second CF Benchmarks prints: near expiry the contract is an ASIAN digital, not a European one; averaging compresses terminal variance. Price that explicitly.",
       "flow-fading-and-leadlag-statarb":"Critic: also absorb the two statistical sub-variants removed from crowd-price-path-simulation: benchmark-gap under-reaction drift (0.64-for-one) and dislocation fade in low-prominence markets, plus the hour-of-day 'sleeping crowd' variant. FACT CHECK from the critic: the 817-market shock experiment ran on Manifold (play money), not Polymarket.",
       "evaluation-promotion-allocation-metalayer":"Critic: by its own text this is shared INFRASTRUCTURE, not alpha. Keep the file (the owner's Agent OS needs exactly this), label it honestly as infrastructure in Category / Maturity, and keep 'changelog-reactive re-optimisation' (competitor-adaptation lag after rule changes) as its only alpha-bearing sub-variant."}
for s in P:
    if s["slug"] in EXTRA: s["extra_scope"]=(s.get("extra_scope","")+" "+EXTRA[s["slug"]]).strip()
CROSS={"genesis-window-new-listing-liquidity":"From the speculative critic: day-zero LLM-priced opening quotes belong here (TimeSeek BSS +0.167 at open+1; IMDEA study of ~160k contracts: first-trade median spreads politics 8c, geopolitics 10c, crypto 19c, economy 21c, compressing mostly within the first hour; ~300k new markets a month). Cover the LLM fair-value variant as a sub-section.",
       "derivatives-implied-relative-value":"From the speculative critic: 'options-implied density vs BTC threshold ladders' is an established cross-venue quant trade (evidence pack E5 measures a 5.6-point gap with a ~4-hour half-life, which may be a premium): cover it here.",
       "recurring-count-mention-counter-markets":"From the speculative critic: the NO-side laddered maker overlay in mention markets (structural YES overpricing; only self-reported profit record) belongs here, not in the speculative speaker-twin file. The speaker-twin itself has negative evidence (Brier 0.1470 vs 0.1402 for the market)."}
for s in E:
    if s["slug"] in CROSS: s["cross_band_note"]=CROSS[s["slug"]]

for i,s in enumerate(P):
    s["n"]=f"{50+i:02d}"; s["band"]="speculative"; s["file"]=f"{s['n']}-{s['slug']}.md"
json.dump({"band":"speculative","numbering":"50+ speculative / experimental / theoretical","strategies":P,
           "critic":{k:crit_s.get(k) for k in ("merge_or_split","misclassified","weakest_entries")} if crit_s else None,
           "consolidator_dropped":sp["dropped"]}, open(f"{OUT}/S0-strategy-list-speculative.json","w"), indent=1)

# ---- per-strategy briefs with the matching raw discovery candidates
def norm(x): return re.sub(r"[^a-z0-9]+"," ",x.lower()).strip()
allc=[(lens.split(":")[1], c) for lens,v in cands.items() for c in v.get("candidates",[])]
os.makedirs(f"{OUT}/strategies", exist_ok=True)
for f in glob.glob(f"{OUT}/strategies/*.json"): os.remove(f)
unmatched=0; total=0
crit_s_notes=[]
if crit_s: crit_s_notes=crit_s.get("merge_or_split",[])+crit_s.get("misclassified",[])+crit_s.get("weakest_entries",[])
for s in E+P:
    raw=[]
    for mf in s.get("merged_from",[]) or []:
        total+=1
        lens,_,nm=mf.partition(":")
        key=norm(nm if _ else mf)[:32]
        hit=[c for l,c in allc if key and (norm(c["name"]).startswith(key) or key in norm(c["name"]))]
        if not hit: unmatched+=1
        for c in hit:
            if c not in raw: raw.append(c)
    b=copy.deepcopy(s); b["raw_discovery_candidates"]=raw
    if s["band"]=="speculative": b["critic_notes"]=[n for n in crit_s_notes if any(k in n for k in [s["slug"]]+[a["slug"] for a in s.get("absorbed",[])])]
    json.dump(b, open(f"{OUT}/strategies/{s['n']}-{s['slug']}.json","w"), indent=1)
print("merged_from matched:", total-unmatched, "/", total)

# ---- index for cross-references + the args for stage 2 / stage 3
with open(f"{OUT}/S0-index.md","w") as fh:
    fh.write("# Index of strategy files (for cross-references)\n\n01-49 established / emerging; 50+ speculative / experimental / theoretical. Flagged = ToS-violating, illegal or manipulative (survey level only).\n\n")
    for band,lst in (("Established / emerging",E),("Speculative / experimental / theoretical",P)):
        fh.write(f"## {band}\n\n| File | Strategy | Category | Maturity (hypothesis) | One line |\n|---|---|---|---|---|\n")
        for s in lst:
            fh.write(f"| {s['file']} | {s['name']} | {s['category']} | {s['maturity']} | {s['one_line'].replace('|','/')} |\n")
        fh.write("\n")
items=[{"n":s["n"],"slug":s["slug"],"file":s["file"],"band":s["band"],"deepen":bool(s.get("deepen"))} for s in E+P]
K=5  # parallel workflow slices (interleaved so every slice mixes both bands and finishes at about the same time)
slices=[items[i::K] for i in range(K)]
files=[s["file"] for s in E+P]
chunks=[files[i:i+10] for i in range(0,len(files),10)]
json.dump({"stage2_slices":slices,"stage3_chunks":chunks,"all_items":items}, open(f"{ROOT}/_pipeline/args.json","w"), indent=1)
print("established:",len(E),"speculative:",len(P),"(from critic:",len(crit_missing),") total files:",len(items))
for s in P: print(" ", s["file"], "| critic-add" if s.get("from_critic") else "")
