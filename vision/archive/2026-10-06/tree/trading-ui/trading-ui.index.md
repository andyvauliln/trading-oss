---
about: trading-os/trading-ui/
node: n-45
basis: e790cf5100e6
written: 2026-10-05T13:25:49Z
by: knowledge-base-agent
confirmed: 2026-10-05T15:38:31Z
---
# trading-ui/

## Summary

The trading dashboard: a Next.js API and web app where the owner will watch and control the trading system. It will show each agent in full (parts, logs, performance, data used and produced, every decision, every improvement being tested) and let the owner create an agent from a plain input, read a report on each new strategy variant and approve it before it starts, approve or reject a live account, stop or delete agents, and comment or ask an agent questions. It reaches every level's files from the system down through `subagents.link/`. It is built later; the owner's File Tree page is in `apps/project-IDE/`. Open: whether it reads files directly or through an API layer, and how it is accessed.

## Keep in mind

- When an action touches live money, it needs the owner's approval in the UI; nothing else can grant it.
