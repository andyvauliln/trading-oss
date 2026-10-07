---
name: knowledge-intake-every-input
description: Standing rule: every owner input (and Claude's answer to it) and every system change goes through the knowledge-intake flow into vision/docs/
metadata:
  type: feedback
  modified: 2026-09-30T19:57:52.075Z
---
Every owner message that says how the system should be, in the project chat, a thread or the File Tree page, and every change to the planned system's files, is processed by the knowledge agent flow (D-033): store it word for word in /mnt/project-files/vision/docs/inputs/ (+ index.json row), place the knowledge in the right doc, ripple, record (decisions.md, changelog.md), rebuild the map, refresh the How it works files. The spec is docs/README.md; the steps are vision/.claude/skills/knowledge-intake/SKILL.md and file-index/SKILL.md (How it works, one `{name}.index.md` per file and folder, D-039); the agent is vision/.claude/agents/knowledge-base-agent.md.

A question and Claude's answer are one input: store the answer under `## Answer` in the same input file and file its knowledge too (owner, 2026-09-30 18:41). Summaries carry up to four "Always keep in mind" lines (owner, 2026-09-30 16:03); the system-wide list lives in overview.md.

**Why:** the owner wants one hierarchical knowledge base that always reflects the current system, with no separate Decisions/Concepts/Rules lists to maintain by hand (2026-09-30 15:33).

**How to apply:** whichever thread handles an owner input also runs knowledge-intake for it (or forwards it to the "Interactive file tree UI" thread, which owns the docs). Don't leave knowledge only in chat. Related: [[file-tree-explorer-sync]].
