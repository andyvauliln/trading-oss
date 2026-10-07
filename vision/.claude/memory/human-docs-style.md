---
name: human-docs-style
description: Owner rule (2026-10-01): docs the owner reads must be plain, book-like prose with no [n] refs, ids or decision codes; relations stay in agent-only notes
metadata:
  type: feedback
  modified: 2026-10-01T08:02:58.694Z
---
Docs and page summaries the owner reads must read like a well-written book: plain language a non-technical person understands, only the important things for that layer, from the common picture down to specific files. No `[2.1]`-style numbers, no D-0xx or input ids, no hashes, minimal file-path noise. No pointers to other docs or sections (summarise what the reader needs in place, or give the concrete detail), except the two set by the owner 2026-10-06 (D-048): the vision ends by naming the README, and the README names the vision once and gives each part's own docs path; and no attribution or history ("the owner later said", dates, earlier versions): only facts as they are now (owner, 2026-10-01 09:08). Relations, decisions, tags and sources are for agents only and live in a separate agent-notes layer the owner never has to open. The rebuild prompt (D-048) is for AI and follows its own skill (exact paths, no [n] refs). Every agent layer (system, domain, strategy, trading agent) gets the same set of docs in the same format, each with its own specifics (How it works, a feature map and other topic docs).

**Why:** the owner was angry (2026-10-01 08:00) that the D-033 docs and summaries were full of [n] links and technical noise and hard to follow; they had asked for human docs before.

**How to apply:** before showing the owner any doc, summary or reply, strip reference numbers and ids and write it for a non-technical reader. Confirm a plan and show one example before large rewrites (owner asked for that order). Related: [[knowledge-intake-every-input]].
