---
about: agent-os/agents/prediction-market-agents/strategy-1-agent/tests/scripts/run-tests.system.link.js
node: n-21.12.2.3
basis: 537dcc2be7f5
written: 2026-10-01T00:58:25Z
by: summary-worker
confirmed: 2026-10-07T19:05:50Z
---
# run-tests.system.link.js

## Summary

A link to the shared `run-tests` script. Called from `tests/scripts/`, it presets the scripts kind and runs the tests listed in this folder's `tests.config.json`, e.g. `node tests/scripts/run-tests.system.link.js`. Results go back into the config and to the strategy's `logs/tests.jsonl`. `create-agent` adds it when it scaffolds the agent.
