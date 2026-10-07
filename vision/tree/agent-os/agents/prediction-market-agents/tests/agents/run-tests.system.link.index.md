---
about: agent-os/agents/prediction-market-agents/tests/agents/run-tests.system.link.js
node: n-19.12.1.3
basis: 1272c9f52185
written: 2026-10-01T00:57:42Z
by: summary-worker
confirmed: 2026-10-07T18:57:42Z
---
# run-tests.system.link.js

## Summary

A file link to the shared `run-tests` script. Run from here as `node tests/agents/run-tests.system.link.js`, it presets kind `agents` and this folder's `tests.config.json`, runs every enabled test or the one named with `--id`, and writes the results back to the config and to the domain's `logs/tests.jsonl`. `create-agent` adds this link at every level, and relink builds it.
