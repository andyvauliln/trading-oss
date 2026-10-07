---
about: agent-os/agents/prediction-market-agents/strategy-1-agent/scripts/subagents.link/[agent-name]/
node: n-21.3.1.1
basis: f2294b6c14a2
written: 2026-10-01T00:56:59Z
by: summary-worker
confirmed: 2026-10-07T19:05:50Z
---
# [agent-name]/

## Summary

One folder link per trading variant, named after the variant and pointing at that variant's `scripts/`. The strategy reads a variant's own scripts and script links here; it never writes there. `relink` makes the link when the variant is created and removes it when the variant is deleted.
