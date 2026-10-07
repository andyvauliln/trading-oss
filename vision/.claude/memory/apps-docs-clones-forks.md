---
name: apps-docs-clones-forks
description: Owner rule 2026-10-06 22:06 (D-055): every app has docs/ with vision, README, rebuild prompt; research clones in apps/temp/ never committed; apps we use are forked (main ours, upstream follows source)
metadata:
  type: project
---
The owner (2026-10-06 22:06, in-20261006-2206, D-055): every app in `apps/` has its own `docs/` with `vision.md`, `README.md`, `rebuild-prompt.md`; for an outside app these three are its only metadata for now. A repo cloned for research goes to `apps/temp/<name>/` (clone in `repo/`, ignored by .gitignore; `docs/` only on request; findings go to the studying agent's research/; delete when done). An app we use is forked on GitHub and kept in `apps/<name>/` with `docs/` and `repo/` (fork as git submodule, proposed); in the fork `main` is ours, `upstream` follows the source and is merged into main from time to time. `index/apps.md` [2.18.5] lists every app. Later, on request: skill `adopt-app` (name proposed) that turns an app fully into the system's way, kept up like any skill.

Written into: conventions v0.3 "Apps and outside code" (conv-apps), architecture, file-tree v1.29 ([43], [53.4]-[53.4.3] the IDE's own docs, [55] apps/temp/, [48], [2.18.5]), the three doc skills (App outline and length), README, rebuild prompt. Plan: vision/plans/2026-10-06-2206-apps-docs-clones-forks.md (steps 1-4 done; 5 IDE docs with the docs at every level; 6 first outside app; 7 adopt-app on request).

**Why:** outside code needs a clear home, and every app should explain itself like the system.

**How to apply:** never commit a research clone; change a used app only on our fork's main. Related: [[general-system-plan]], [[github-sync-plan]].
