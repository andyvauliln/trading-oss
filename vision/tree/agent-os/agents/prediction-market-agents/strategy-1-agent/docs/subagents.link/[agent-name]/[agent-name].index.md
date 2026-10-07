---
about: agent-os/agents/prediction-market-agents/strategy-1-agent/docs/subagents.link/[agent-name]/
node: n-21.6.1.1
basis: ec6ee7474588
written: 2026-10-01T00:58:25Z
by: summary-worker
confirmed: 2026-10-07T19:05:50Z
---
# [agent-name]/

## Summary

One folder link per trading variant, named after the variant and pointing at that variant's `docs/`. The strategy reads each variant's `changes.md` here, the record of what that variant changes against its parent, together with its other docs; it never writes there. `relink` makes the link when the variant is created and removes it when the variant is deleted.
