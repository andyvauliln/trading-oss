---
name: agent-os-trading-domain
description: Since 2026-10-07 everything about trading lives in the prediction-market domain and the system level is general (D-056, D-058); where the trading files and notes are
metadata:
  type: project
  modified: 2026-10-07T19:16:51.479Z
---
The owner (2026-10-07 09:04) asked that everything about trading move "down to prediction market domain" and that "another trading domain later should be just templated" from it. Done 2026-10-07 (plan 2026-10-07-0904-agent-os step 4, File Tree page v46).

- System level keeps only what holds for any agent: test/live for outside actions, owner approval to go live, general stop switch `modes.kill_switch`, tighten-only limits in code, key rules, outside text as data, levels, new versions, SI never live, cost/speed/error/test metrics.
- pm holds: config [19.2.4] `prediction-market-agents.config.json` (`risk.domain`/`per_agent`, accounts, venues, fees, filters, currency, order stop switch `kill_switch`, trade notifications); `scripts/decisions/` [14.3]; polymarket-prices worker [19.3.5] with logs [19.4.2], order logs [19.4.3], data [19.5.3]; notes `trading-*.md` [19.6.5]-[19.6.14], `doc-outlines.md` [19.6.15], `common/` [19.6.16], `how-to/` [19.6.17], `index/accounts.md` [19.6.18.1]; research [54.3]. Planning copies in vision/docs/prediction-market-agents/; its `trading-vision-notes.md` has no tree node (folds into the domain vision at step 5).
- Knowledge tags: a moved section keeps its id; a split keeps the general part under the old id and the trading part as `tr-<id>`.
- Copy-trading [42] retired with the whale-signals and top-traders links. Since 2026-10-09 (D-059) pm sits at `agents/trading/prediction-market/` [19] inside `agents/trading/` [56], which has only `docs/` [56.1]; the owner named `agents/trading/copytrading/` as the next trading domain.
- Words: the system says "agent" and "version"; strategy, variant, champion/challenger and money words are pm's. Research index uses `related.agents`. Env `AGENT_OS_ENV`.
- D-058 defaults are proposed. Open for the owner: what the order stop switch does with open positions (default: close them and unfund, `tr-safe-open`); owner-only trading-safety and trading-prompt.

**Why:** the Agent OS is for agents of any kind; trading is one domain.
**How to apply:** write system-level text in general terms (a "for example, in the prediction-market domain" is fine); anything about money, markets or orders goes in pm; a new trading domain is a copy of pm. Related: [[general-system-plan]], [[file-tree-explorer-sync]].
