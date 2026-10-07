---
about: agent-os/agents/system/logs/subagents.link/
node: n-15.5
basis: a1b161628712
written: 2026-10-07T19:01:11Z
by: knowledge-base-agent
---
# subagents.link/

## Summary

The system's view of its domains' logs: one folder link per domain, each pointing at that domain's `logs/`. The UI starts at the system's `logs/` and goes down through these links one level at a time, reading every agent's logs without copies. Relink builds and removes them from the folder tree; they are read-only and listed in no links file.

## Keep in mind

- When you scan logs, never follow these links recursively; go down one `subagents.link/` at a time.
