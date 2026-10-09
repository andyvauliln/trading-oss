# Handoff: continue the Agent OS planning in Claude Code

Everything from the planning project is in `vision/` (copied 2026-10-07 from the project's shared folder). Nothing is built yet; this is the plan.

## Start here

1. Open Claude Code in this repo and ask it to read, in order:
   - `vision/.claude/memory/MEMORY.md` and the notes it links (project memory: decisions, rules, how we work)
   - `vision/.claude/CLAUDE.md` (draft rules for every AI session)
   - `vision/docs/README.md` (how the knowledge base is laid out)
   - the newest plan: `vision/plans/2026-10-09-0940-trading-folder.md`
2. The File Tree page source is `vision/explorer/file-tree-explorer.html` with `vision/explorer/file-tree.data.json`; open it in a browser from that folder (a local web server: `python3 -m http.server` in `vision/explorer/`).
3. Rebuild after any change (from `vision/tools/`, see its README): `python3 parse.py /tmp/parsed.json`, `DATA_VERSION=N python3 enrich.py /tmp/parsed.json /tmp/ftd.json`, copy the output to `vision/file-tree.data.json` and `vision/explorer/`, then `python3 build_map.py --stale` until it is clean.

## Where things stand

- Done: the name Agent OS; metadata files (`x.index.md`, empty `x.meta.json`); trading moved into the prediction-market domain (D-056 to D-058); all How it works files fresh; the system vision rewritten in general terms (`vision/.claude/docs/vision.md`).
- Done 2026-10-09 (D-061): `researches/` moved to `agents/trading/researches/`; the page build lists every real file in the repo (run `enrich.py` with `REPO_DIR` set to a fresh clone).
- Done 2026-10-09 (D-059): `agents/trading/` holds `prediction-market/` (copy trading next) and `docs/` with trading's vision, README and rebuild prompt (planning copies `vision/docs/trading/`); the system README and rebuild prompt rewritten in general terms. The trading text removed from them is in `vision/archive/2026-10-09/*-trading-parts.md`, for the prediction-market domain's own docs, which are next when the owner asks.
- Owner's words go into `vision/docs/inputs/` word for word (skill `knowledge-intake`); decisions into `vision/docs/decisions.md`.

## Rules to keep

- Never write secret values anywhere; key names only. `.secrets/` never goes in git.
- Call the owner "the owner" (they/them); docs for people are plain prose without ids or codes.
- Ask the owner before restructuring beyond what they asked.
