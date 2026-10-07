---
about: agent-os/apps/project-IDE/server/server.config.json
node: n-53.3.4
basis: f5044654c716
written: 2026-10-05T16:17:55Z
by: knowledge-base-agent
confirmed: 2026-10-07T14:22:08Z
---
# server.config.json

## Summary

The server page's settings: the address and port (only the machine itself), the page and store folders, whether edits are written straight into their files, the keys file and the key names Claude Code gets (values stay in the keys file), where Claude Code starts (`agents/system`), the model (empty means Claude Code's default), the limits for one request, the tools and commands Claude Code may use without asking (reading, searching, moving between folders, editing, committing), the words that always wait for the owner, the paths nothing may touch, and the log folder.

## Keep in mind

- Never put a key's value here: name it, and keep the value in the keys file on the machine.
