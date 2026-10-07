---
about: agent-os/agents/prediction-market-agents/strategy-1-agent/data/subagents.link/
node: n-21.5.1
basis: fa28cb0cceea
written: 2026-10-01T00:56:59Z
by: summary-worker
confirmed: 2026-10-07T19:05:50Z
---
# subagents.link/

## Summary

The strategy's child links for data: one folder link per trading variant, pointing at that variant's `data/`. Here the strategy's `compare-variants` job is meant to read every variant's metrics snapshot and write the daily variant report, and the UI reads the snapshots level by level the same way (proposed; no metrics script exists yet). `relink` builds the entries from the folder tree and removes them when a variant is deleted; they are read-only and never followed recursively.
