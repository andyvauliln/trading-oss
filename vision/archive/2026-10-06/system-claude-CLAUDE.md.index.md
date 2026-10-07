---
about: trading-os/agents/system/.claude/CLAUDE.md
node: n-10.1.5
basis: 91ac182077a5
written: 2026-10-01T00:52:45Z
by: summary-worker
confirmed: 2026-10-05T09:48:25Z
---
# CLAUDE.md

## Summary

The system agent's prompt: instructions for the system manager, who runs all domains and the development of the system. It is planned as the common prompt [2.17.3] plus a system part: all domains, system health, system development and the owner's questions about the whole system; the system agent also plans each new domain. The prompt text is a proposal; how the common part gets in (an `@import` of a linked copy, or a copy at creation) is still open.

## Keep in mind

- When you add a rule about money or risk, put the hard limit in code (the decision scripts and risk check), not only in this prompt.
- When you change something every level should follow (role, read order, rules, safety), change the common prompt [2.17.3], not just this file.
