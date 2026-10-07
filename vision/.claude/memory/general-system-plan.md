---
name: general-system-plan
description: Owner 2026-10-06 21:43 (D-051..D-054): plan every change (change-plan skill, plans/), features files, docs hierarchy across levels, general system not a trading OS; plan waits for the owner
metadata:
  type: project
---
The owner (2026-10-06 21:43, in-20261006-2143) decided four things, recorded as D-051 to D-054:

- D-051, in force now: every change request gets a stored plan before it is built; after the build its knowledge moves to the files that own it and the plan is archived. Skill draft `vision/.claude/skills/change-plan/SKILL.md` [10.1.2.8]; plans in `vision/plans/` (later `apps/project-IDE/data/plans/` [53.2.5]) named `YYYY-MM-DD-HHMM-<subject>.md`, `plans/index.json` (4 plans). Written into CLAUDE.md every round, vision principle, README knowledge base, rebuild prompt. Questions and small fixes need no plan.
- D-052: features as their own files in `features/` in the docs of the system and every agent, small inside big, map written on the feature side and built on the file side; replaces feature-map.md.
- D-053: vision → README → rebuild prompt at every level; parents sum up children; updates climb to the top; a rebuild prompt at every level. Since 2026-10-07 (owner asked why agents had none) the tree lists rebuild-prompt.md in every domain [19.6.4], strategy [21.6.4] and trading agent [46.4] docs, plus the agent's vision [46.3]; not written yet.
- D-054: no longer called the Trading OS; the top level is general; agents of any kind (trading, social media, management), each kind with its own levels and a parent. Name open ("the system" until named); repo keeps `trading-oss`.

The master plan: `vision/plans/2026-10-06-2143-general-system.md` (step 1 done). Open for the owner: the name; kinds as a folder level `agents/trading/` (recommended, card posted 2026-10-06 ~22:05) or a label; test names `{target}.{check}.test.md` (recommended) vs `t-agents-NNN`; order of work.

**Why:** the owner wants every change thought through first and one system for agents of every kind.

**How to apply:** write a plan with change-plan for every change request before building; don't restructure or rename until the owner says go; when they do, rewrite the docs once (plan step 5). Related: [[file-family-plan]], [[full-context-for-ai]], [[knowledge-intake-every-input]].
