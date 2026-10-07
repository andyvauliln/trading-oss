---
name: full-context-for-ai
description: Owner's purpose for the IDE and docs (2026-10-06, D-049): every AI gets a file's whole context, ripples changes to everything related, files what it learns, and answers every owner question in the docs
metadata:
  type: feedback
  modified: 2026-10-06T20:58:38.701Z
---
The owner (2026-10-06 20:47, in-20261006-2047, D-049): the custom IDE, the File Tree page and the docs exist so the owner can manage, analyse and view the system, and so AI always has all related context to make changes precisely. Docs must be right for developers and AI. On any change the AI knows which related files, agents, skills, docs, indexes and logic to update and how; a file deep in the hierarchy (a helper's skill) gets the knowledge from the levels above; knowledge from every session and input is spread where it belongs; every owner question finds its place in the docs with an explanation of how exactly that thing works.

Written into: vision (What the owner sees and does; principle "Every AI works with the whole picture"), README (knowledge base; project IDE), rebuild prompt part 17, knowledge-base-agent (job, when it runs, step 2), project-ide-agent, knowledge-intake (scope, questions, ripple step 5), CLAUDE.md, plans/file-set.md (Details fields `update_with`, `inherits`).

**Why:** the owner builds by vibecoding and needs every AI session to act with the full picture, without re-asking.

**How to apply:** before changing a planned file run `tools/build_map.py --context <node>` (knowledge from folders above included); after it, bring everything related in line in the same round; file what a session learned even with no file change; for every owner question, write the explanation into the doc or How it works file where they should have found it, not only into the input's Answer. Related: [[knowledge-intake-every-input]], [[file-family-plan]], [[human-docs-style]].
