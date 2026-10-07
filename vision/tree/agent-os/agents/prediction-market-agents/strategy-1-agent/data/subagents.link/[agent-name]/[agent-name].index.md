---
about: agent-os/agents/prediction-market-agents/strategy-1-agent/data/subagents.link/[agent-name]/
node: n-21.5.1.1
basis: dbc3f5f07aae
written: 2026-10-01T00:56:59Z
by: summary-worker
confirmed: 2026-10-07T19:05:50Z
---
# [agent-name]/

## Summary

One folder link per trading variant, named after the variant and pointing at that variant's `data/`. The strategy reads each variant's outputs here when it compares variants; it never writes there. `relink` makes the link when the variant is created and removes it when the variant is deleted.
