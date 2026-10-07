---
about: trading-os/agents/system/docs/index/summaries.json
node: n-2.18.9
basis: 4517f2ea5b93
written: 2026-10-01T01:08:49Z
by: summary-worker
---
# summaries.json

## Summary

The How it works summary of every file and folder, with an optional "Always keep in mind" list and the basis it was written from, when and by whom. The `knowledge-summarise` skill writes it children first through `build_map.py`: `--set` for a new text, `--confirm` when a summary is still right, which stops the ripple. A summary whose basis no longer matches the knowledge map is stale. The File Tree page shows it as the main view. Format proposed.

## Keep in mind

- When summaries go stale, rewrite children before parents, so each folder rolls up current child summaries.
- When you save a summary, go through `build_map.py --set` or `--confirm`, so its basis is recorded with it.
