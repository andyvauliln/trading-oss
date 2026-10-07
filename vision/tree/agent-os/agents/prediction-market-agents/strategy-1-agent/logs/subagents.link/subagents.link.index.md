---
about: agent-os/agents/prediction-market-agents/strategy-1-agent/logs/subagents.link/
node: n-21.4.1
basis: d3abda5c16aa
written: 2026-10-01T00:56:59Z
by: summary-worker
confirmed: 2026-10-07T19:05:50Z
---
# subagents.link/

## Summary

The strategy's child links for logs: one folder link per trading variant, pointing at that variant's `logs/`. Through them the strategy session and its self-improvement sub-agent read every variant's per-run logs (inputs, reasoning, decisions, actions, cost) to compare variants and spot errors. `relink` builds them from the folder tree and removes them when a variant is deleted; they are read-only and never followed recursively.
