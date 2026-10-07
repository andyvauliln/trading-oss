---
about: trading-os/[name].index.md
node: n-51
basis: 36c920bbc199
written: 2026-10-05T13:25:49Z
by: knowledge-base-agent
---
# [name].index.md

## What it is

The How it works of one file or folder, in a short Markdown file of its own. Every file has one next to it, named after it with `.index.md` added, such as `run.js.index.md`. Every folder has one inside it, named after the folder, such as `configs/configs.index.md`. It tells someone new to the project, in one read, what the thing is and how it works.

## Who looks after it

The knowledge base agent writes them with its `file-index` skill, from the deepest files up to the root. The owner can edit any of them on the File Tree page; the agent writes the edit into the file at the next sync and keeps it.

## When and how it changes

When a file's notes, the knowledge that applies to it, or the How it works of something inside it changes, the file is out of date. The agent finds every such file, deepest first, and either rewrites it or confirms it is still right. A short code in the file's header records what it was written from, so the agent can tell.

## Who uses it, and when

- The owner reads it first when they open a file or folder on the File Tree page.
- Every agent reads a folder's index file before it works in that folder.
- A new Claude session reads them to understand a part of the system fast.

## Where it is mentioned

The knowledge base agent's instructions and its `file-index` skill, the README's description of how the project is laid out, and the file tree.

## Related knowledge

- Each doc's own skill says what its How it works says under each heading.
- The map of knowledge to files says what each index file is written from.
- While the system is planned, files that already exist as drafts, such as the README and the vision, keep their index file right next to them. The rest sit in a copy of the planned folder tree and move next to the real files when the system is built. In the repository a file nobody has written yet exists only as its index file, and a placeholder folder such as `[agent-name]/` holds only its index file.

## Keep in mind

- When you change a file or folder, refresh its index file and then its parents', from the deepest up.
- When the owner has edited an index file, keep their words and write around them.
- When you rename or remove a file or folder, move or archive its index file with it.
