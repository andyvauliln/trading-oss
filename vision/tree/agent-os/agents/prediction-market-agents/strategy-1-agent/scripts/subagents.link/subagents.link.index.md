---
about: agent-os/agents/prediction-market-agents/strategy-1-agent/scripts/subagents.link/
node: n-21.3.1
basis: f54460c05048
written: 2026-10-01T00:56:59Z
by: summary-worker
confirmed: 2026-10-07T19:05:50Z
---
# subagents.link/

## Summary

The strategy's child links for scripts: one folder link per trading variant, pointing at that variant's `scripts/`, so the strategy session and its self-improvement sub-agent can read each variant's workers, decision scripts and script links when they compare variants or check a code change. `relink` builds the entries from the folder tree and removes them when a variant is deleted; they are read-only and never listed in a links file.

## Keep in mind

- When you want to change a variant's code, make a new test variant; never edit through these links.
