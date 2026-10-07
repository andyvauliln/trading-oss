---
about: agent-os/agents/prediction-market-agents/tests/scripts/[test-id].test.[js|py]
node: n-19.12.2.2
basis: 9045f3c4a378
written: 2026-10-01T00:57:42Z
by: summary-worker
confirmed: 2026-10-07T18:57:42Z
---
# [test-id].test.[js|py]

## Summary

The pattern for one script test of the domain level: a normal node (`.js`) or pytest (`.py`) file named after its id, such as `t-scripts-001`, that runs on fixture data with no network and no secrets. Each one has an entry in this folder's `tests.config.json`.

## Keep in mind

- When you write a script test, use fixture data only: no network calls and no secrets.
