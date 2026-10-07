---
about: trading-os/agents/system/.claude/agents/[subagent-name].md
node: p-trading-os-agents-system-.claude-agents-subagent-name-.md
basis: a761f593900a
written: 2026-10-01T00:54:17Z
by: summary-worker
---
# [subagent-name].md

## Summary

The pattern for every further system-level sub-agent: one Markdown file each, named `[domain]-[scope]-[role]-agent.md` with the scope left out at system level (format proposed). System-support roles such as development, improvement, analysis and research are added this way, as sub-agents rather than folders. The frontmatter carries `name`, `description`, `tools` and `memory`; the model comes from [11.11], not from the file.

## Keep in mind

- When you add a sub-agent, check its name is free in the registry [2.18.1] and the sub-agent index [2.18.3].
