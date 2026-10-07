---
about: agent-os/agents/prediction-market-agents/tests/scripts/run-tests.system.link.js
node: n-19.12.2.3
basis: 537dcc2be7f5
written: 2026-10-01T00:57:42Z
by: summary-worker
confirmed: 2026-10-07T18:57:42Z
---
# run-tests.system.link.js

## Summary

A file link to the shared `run-tests` script. Run from here as `node tests/scripts/run-tests.system.link.js`, it presets kind `scripts` and this folder's `tests.config.json`, runs every enabled test or the one named with `--id`, and writes the results back to the config and to the domain's `logs/tests.jsonl`. `create-agent` adds this link at every level, and relink builds it.
