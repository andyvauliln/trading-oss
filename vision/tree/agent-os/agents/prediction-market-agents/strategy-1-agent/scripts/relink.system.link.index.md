---
about: agent-os/agents/prediction-market-agents/strategy-1-agent/scripts/relink.system.link.js
node: n-21.3.2
basis: c32c5d8da89c
written: 2026-10-01T00:56:59Z
by: summary-worker
confirmed: 2026-10-07T19:05:50Z
---
# relink.system.link.js

## Summary

A link to the shared `relink` script, the same as at every level below the system. Run from the strategy folder as `node scripts/relink.system.link.js`, it relinks only the strategy agent: its file links from `strategy-1-agent.links.json` and its entry in the domain's `subagents.link/` folders. The strategy runs it after editing its links file, and the `PostToolUse` hook in its settings runs it too. `create-agent` adds it.

## Keep in mind

- When you edit the strategy's links file, run it and fix anything its report flags before `check ok`.
