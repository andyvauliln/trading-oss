---
name: github-sync-plan
description: Repo layout decided (D-041, D-043, D-045, D-047): the GitHub repo is the file tree with apps/project-IDE/, no root CLAUDE.md or researches/; the owner gives the GitHub project next, then the first sync
metadata:
  type: project
  modified: 2026-10-05T15:40:32.797Z
---
The owner (2026-10-05) wants the planning project in GitHub so this cloud project and a Claude Code on their own server both work on it with the full context (D-040). Plans: /mnt/project-files/vision/plans/github-sync.md (layout, first-sync mapping table vision/ -> repo paths, how a round works) and plans/server-ide.md.

**Layout (D-041, moved by D-043 at 15:17):** repo = the tree: root README.md [1] only (no root CLAUDE.md: it is agents/system/.claude/CLAUDE.md [10.1.5], draft vision/.claude/CLAUDE.md, D-045); agents/ (system/.claude/ holds knowledge-base-agent, project-ide-agent, skills knowledge-intake, file-index, vision-doc, readme-doc, ide-build with the build scripts, ide-sync; the people docs README and vision in agents/system/docs/ with the topic notes, D-047); the repo's researches/ studies move at the sync into agents/system/research/ [54.2, 54.3] and agents/prediction-market-agents/research/ [54.1] (D-045); apps/ [43] with apps/project-IDE/ [53] (current-ui/ page + data, server/ [53.3], data/ [53.2] = inputs, decisions, changelog, tree notes, knowledge map, sources, page-store [53.2.7], overrides, memory, plans, archive) and apps/trading-ui/ [45], empty (D-045); .secrets/ never in git. Every node gets its .index.md next to it.

**Server page (D-042 wish, D-043 built):** vision/server/ = server.py (stdlib; serves the page, page store as JSON files, write-through of file/How it works edits, 127.0.0.1 only + Host/Origin check), claude_bridge.py (claude-agent-sdk ClaudeSDKClient, cwd agents/system so the nested .claude agents/skills load, add_dirs repo, setting_sources project+local, skills all, allow list + PreToolUse hook: .secrets denied, outside repo / ask_owner words -> can_use_tool -> page Allow/Refuse; logs to agents/system/logs/subagents/project-ide-agent/), server.config.json, README.md. Tested 2026-10-05 on a scratch copy: real request listed 2 agents + 6 skills; push and outside-repo read asked and were refused. Claude Code started at the repo root does NOT see agents/system/.claude/ (that is why it starts in agents/system); verified 2026-10-06 that started in agents/system it loads agents/system/.claude/CLAUDE.md. D-044: a page Delete runs Claude Code with the target; one `git rm`/`rm` of exactly that path (absolute, alone) is auto-allowed; the bridge reports changed files also after commits; write-through writes only fields that changed.

**NEXT:** the owner names the GitHub project; then build the repo tree from vision/ per the mapping table (plus vision/server/ -> apps/project-IDE/server/), switch the build scripts' paths, build fresh, commit to the thread branch, PR. Still ask before pushing. Open: who merges; server setup; how the claude.ai link gets server changes.

**Why:** the project memory and the shared folder are invisible to a Claude outside this project.

**How to apply:** nothing is pushed until the owner says go. When it lands, the repo copy is the source and vision/.claude/memory/ the shared notes. Related: [[file-tree-explorer-sync]], [[claude-folder-docs-layout]].
