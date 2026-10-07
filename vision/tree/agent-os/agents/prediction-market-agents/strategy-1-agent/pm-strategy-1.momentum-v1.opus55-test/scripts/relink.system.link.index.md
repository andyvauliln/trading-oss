---
about: agent-os/agents/prediction-market-agents/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/scripts/relink.system.link.js
node: n-30.3
basis: e3856cadf0c3
written: 2026-10-01T00:56:59Z
by: summary-worker
confirmed: 2026-10-07T19:05:50Z
---
# relink.system.link.js

## Summary

A read-only file link to the shared `relink` script [14.1]. Run from here (`node scripts/relink.system.link.js`) it works on this agent only: it rebuilds the links its links file [27.3] lists and its entries in its strategy's `subagents.link/` folders, refuses targets in `.secrets/` or `.claude/`, and prints a `+`, `-`, `=` report ending in `check ok`. The agent runs it after every links-file edit, and the `settings.json` hook runs it too (proposed). Every level below the system has the same link.

## Keep in mind

- When you have edited the links file, run this and read its report; fix anything it flags.
