---
about: agent-os/agents/system/scripts/subagents.link/[domain-name]/
node: n-14.4.1
basis: 175d8be1c9ed
written: 2026-10-07T19:01:11Z
by: knowledge-base-agent
---
# [domain-name]/

## Summary

One folder link per domain, named after the domain's folder and pointing at that domain's `scripts/` [19.3]. Through it the system reads the domain's own scripts and, one `subagents.link/` further down, those of the levels below it. It is read-only, built by relink from the folder tree, listed in no links file, and removed when the domain goes.
