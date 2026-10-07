---
name: file-family-plan
description: Owner rule 2026-10-06 16:11: every page tab is a file next to its subject (x.index.md, x.example.md, x.questions.md, views, meta); definition in vision/plans/file-set.md, waiting for the owner's go
metadata:
  type: project
  modified: 2026-10-06T16:17:41.453Z
---
The owner (2026-10-06 16:11, input in-20261006-1611) set: every tab on the File Tree page is a file next to its subject, named with the subject's name without its last extension: `vision.index.md` (How it works, replacing `vision.md.index.md`), the file itself, `vision.example.md`, `vision.questions.md`, custom views `vision.{type}.{name}.view.html` (also as templates for a category of files), plus metadata with the mapping for every file and folder. They asked us to suggest more (maybe a changelog), define everything, raise questions, then do it.

Our definition (proposed): /mnt/project-files/vision/plans/file-set.md. Adds `x.meta.json` (Details tab: about, kind, state/status, git/secret/generated, writers/readers, changes_when, related files with how, sources, features, views, How it works check moved out of the index.md front matter, tree number), `x.changelog.json` (Changes tab, seeded from decisions and inputs), `x.schema.json` for config and data files. Folder families sit inside the folder (`configs/configs.index.md`). Same-base clash keeps the extension (`run.js.index.md`); reserved endings; templates in `apps/project-IDE/views/` with `views.json`; views run sandboxed in the tab and hand edits back. Default: family files become the one source and file-tree.md becomes an overview built from them. D-049 (20:47) added Details fields `update_with` (what must change with the file, and how) and `inherits` (knowledge from above).

Owner 17:29 (in-20261006-1729): views are custom interfaces with their own logic per kind of file (every SKILL.md one skill view); shared views optional; changelog is JSON (`x.changelog.json`: change id shared across files, task, by, input, decision, description, logic_changed, parts_changed, other_files, commit). Asked if schema.json is covered by examples: we said keep it only for config/data files as the rules source, Example field notes built from it. Second card ~17:35: Schema, then go (recommended) / Example only, go / Not yet. Nothing renamed yet. When the owner picks: record a D-049, then do the 8 steps in file-set.md (tools index_files.py, build_map.py, enrich.py, tabs.py, page, skills file-index, ide-build, ide-sync, knowledge-intake, both agents).

Owner 21:04 (in-20261006-2104, D-050): `x.tests.json` + Tests view with Run for every code file, skill, agent, subagent (in the plan); one job per code file is decided and written into conventions, common prompt, SI template, CLAUDE.md, vision, README, rebuild prompt; our build scripts and server break it, split = plan step 7. Plan has 'Where this goes once it is built' (own note file-family.md proposed).

**Why:** the owner wants each tab to be a real document anyone can open, with no double extensions.

**How to apply:** don't rename until the owner picks; keep the 1611 input's Processed into "in progress" until done. Related: [[file-tree-explorer-sync]], [[claude-folder-docs-layout]].
