---
about: agent-os/agents/
node: n-4
basis: b048af954e00
written: 2026-10-07T19:09:34Z
by: knowledge-base-agent
---
# agents/

## Summary

All agents of the Agent OS, one folder per domain. The system is a domain too: `system/` holds the system agent and everything every agent shares, whatever its domain. `prediction-market-agents/` is the first domain and holds everything about trading; a later trading domain is copied from it. Inside it sit its strategy agents, and inside each strategy its trading agents, one per version being tested.

Every level uses one identical agent folder: `.claude/` with the level's prompt, then `configs/`, `scripts/`, `logs/`, `data/`, `docs/`, `tests/`, `research/` and the level files. Each content folder holds the level's own files, file links to what it reads elsewhere, and `subagents.link/` to its children. Agents are created by `create-agent`, and self-improvement creates new test versions. Secrets, the apps and cloned code live outside this folder.

## Keep in mind

- When you add an agent, give it a unique name and the standard folder through `create-agent`; never copy a folder by hand.
- When an agent needs another agent's file, add a link to its links file; it never writes into another agent's folder.
