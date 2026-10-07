# Trading OS: File tree (v1.15)

> Skeleton of the folder layout from the owner's v0.2 input (see `vision.md` §7). Every object is numbered. We will go through them one by one: the owner answers the open questions and this file is updated. Names in `[brackets]` are placeholders. One example agent (`pm-momentum-v1-agent-opus55-test`, named per D-012) is fully expanded. "Momentum" is only a placeholder modification name.

## 1. Tree

```text
trading-os/                                   # [0] repo/workspace root
├── .gitignore                                # [48] ignores secrets, local Claude settings/memory, build junk; each entry commented (D-028)
├── .secrets/                                 # [47] SECRETS STORE (D-023): git-ignored, chmod 700, outside agents/
│   ├── test/                                 # [47.1] test/paper keys
│   │   └── .env                              # [47.1.1] ALL test keys in one file (D-027); agents may read/update it
│   ├── live/                                 # [47.2] live keys, only for owner-approved accounts
│   │   └── .env                              # [47.2.1] same keys, live values; owner only; later phase (D-027)
│   └── secrets.index.json                    # [47.3] metadata only (ref, kind, env, used by, rotate_by); never values
├── README.md                                 # [1] entry point; points to agents/system/docs/ [2]
├── agents/                                   # [4] all domains; every child is a domain (system is one)
│   ├── system/                               # [10] SYSTEM-LEVEL AGENT (standard folder [2.7.1]) + shared files + subagents.link/ to each domain (D-030)
│   │   ├── .claude/                          # [10.1] system-domain Claude Code
│   │   │   ├── CLAUDE.md                     # [10.1.5] system manager prompt: all domains + system development (was [10.3]) (D-024: inside .claude/)
│   │   │   ├── settings.json                 # [10.1.6] permissions (deny .secrets/live/**, D-027), hooks, env, model, statusLine, outputStyle; committed
│   │   │   ├── settings.local.json           # [10.1.7] personal overrides; git-ignored
│   │   │   ├── rules/                        # [10.1.8] topic rules; `paths:` frontmatter; subfolders ok
│   │   │   │   └── [topic].md
│   │   │   ├── skills/                       # [10.1.2] skills: one folder each
│   │   │   │   └── [skill-name]/SKILL.md     # + supporting files
│   │   │   ├── commands/                     # [10.1.9] single-file prompts, /name
│   │   │   │   └── [command-name].md
│   │   │   ├── agents/                       # [10.1.1] sub-agents (own context/tools)
│   │   │   │   ├── sys-self-improvement-agent.md # [10.1.1.1] self-improvement sub-agent, this level (D-018)
│   │   │   │   ├── sys-docs-agent.md         # [10.1.1.2] system-support sub-agent, e.g. docs (D-026; replaces [10.2] folders)
│   │   │   │   └── [subagent-name].md
│   │   │   ├── workflows/                    # [10.1.10] workflow scripts; each becomes /<name>
│   │   │   │   └── [workflow-name].js
│   │   │   ├── output-styles/                # [10.1.11]
│   │   │   │   └── [style-name].md
│   │   │   ├── agent-memory/                 # [10.1.12] `memory: project` sub-agent memory (incl. SI, proposed)
│   │   │   │   └── [subagent-name]/MEMORY.md
│   │   │   └── agent-memory-local/           # [10.1.13] `memory: local`; git-ignored
│   │   ├── docs/                             # [2] SHARED DOCS (D-017) + own docs + subagents.link/ (D-030)
│   │   │   ├── README.md                     # [2.1] docs index: what each file is, read order
│   │   │   ├── vision.md                     # [2.2] owner's inputs, summarised and structured (was [3])
│   │   │   ├── overview.md                   # [2.3] how the whole OS works, with diagrams
│   │   │   ├── glossary.md                   # [2.4] shared vocabulary for owner and agents
│   │   │   ├── roadmap.md                    # [2.5] phases, current focus, next steps
│   │   │   ├── decisions.md                  # [2.6] decision log: what was decided, why, when
│   │   │   ├── conventions.md                # [2.7] naming (incl. .link rule), formats, config keys
│   │   │   ├── safety.md                     # [2.8] hard limits, secrets, live-money approval rules
│   │   │   ├── changelog.md                  # [2.9] system-level changes over time
│   │   │   ├── feature-map.md                # [2.12] feature/logic area -> files that implement it
│   │   │   ├── file-tree.md                  # [2.13] this document: annotated tree + example agent (was [6])
│   │   │   ├── data-schemas.md               # [2.14] shape of every JSON/MD file
│   │   │   ├── flows.md                      # [2.15] data flows + user (owner) flows
│   │   │   ├── metrics.md                    # [2.16] how agents are measured, compared, promoted
│   │   │   ├── inputs/                       # [2.10] owner inputs archived verbatim
│   │   │   │   └── YYYY-MM-DD-[topic].md     # [2.10.1] one raw input per file
│   │   │   ├── how-to/                       # [2.11] step-by-step runbooks
│   │   │   │   ├── create-agent.md           # [2.11.1] create + integrate a new agent
│   │   │   │   ├── add-worker.md             # [2.11.2] add a worker/sub-agent + subscriptions
│   │   │   │   ├── add-platform-or-model.md  # [2.11.3] add/route a platform or model
│   │   │   │   ├── promote-to-live.md        # [2.11.4] test -> live with owner approval
│   │   │   │   ├── stop-or-delete-agent.md   # [2.11.5] stop, retire, delete an agent
│   │   │   │   └── add-or-change-link.md     # [2.11.9] link a file from anywhere, then relink (D-031)
│   │   │   ├── common/                       # [2.17] common knowledge shared by all agents
│   │   │   │   ├── agent-architecture.md     # [2.17.1] how agents work inside (was [7])
│   │   │   │   ├── shared-mechanics.md       # [2.17.2] triggers, modes, symlinks, run loop, logs (was [9])
│   │   │   │   ├── common-prompt.md          # [2.17.3] base prompt every agent's CLAUDE.md builds on
│   │   │   │   └── self-improvement-templates.md     # [2.17.4] templates SI agents build strategies from
│   │   │   ├── index/                        # [2.18] index of all things (was catalog [8])
│   │   │   │   ├── agents.md                 # [2.18.1] every agent: type, domain, route, mode, status
│   │   │   │   ├── workers.md                # [2.18.2] every worker: source, schedule, output, subscribers
│   │   │   │   ├── subagents.md              # [2.18.3] every sub-agent: input, output, route
│   │   │   │   ├── services.md               # [2.18.4] every acting service: test/live, accounts
│   │   │   │   ├── apps.md                   # [2.18.5] every cloned repo in apps/
│   │   │   │   └── models.md                 # [2.18.6] platforms, models, status, who routes to them
│   │   │   └── subagents.link/               # [2.20] one folder link per domain (D-030)
│   │   │       └── [domain-name]/            # [2.20.1] -> that domain's docs/ [19.6]
│   │   ├── configs/                          # [11] shared configs (JSON) + subagents.link/ (D-030)
│   │   │   ├── system.config.json            # [11.1] global: modes, risk, schedules, triggers, accounts, notifications, domains
│   │   │   ├── system.workers.json           # [11.10] system's own jobs: when, where it runs, platform, model (D-029; was workers.config.json)
│   │   │   ├── models.config.json            # [11.11] platforms + which model each agent/sub-agent/worker uses
│   │   │   ├── system.links.json             # [11.13] system's own file links: what, from where (D-031; format for every level)
│   │   │   └── subagents.link/               # [11.2] one folder link per domain (D-030)
│   │   │       └── [domain-name]/            # [11.2.1] -> that domain's configs/ [19.2], incl. its workers file
│   │   ├── scripts/                          # [14] shared scripts; kind by folder + suffix; + subagents.link/
│   │   │   ├── system/                       # [14.1] *.system.*: create-agent, run-agent, scheduler, run-job, relink, check-links, notifier, run-tests
│   │   │   ├── workers/                      # [14.2] *.worker.*: shared data collectors
│   │   │   ├── decisions/                    # [14.3] *.decision.*: shared buy/sell/risk-check blocks
│   │   │   └── subagents.link/               # [14.4] one folder link per domain (D-030)
│   │   │       └── [domain-name]/            # [14.4.1] -> that domain's scripts/ [19.3]
│   │   ├── logs/                             # [15] shared logs by source + subagents.link/ (D-030)
│   │   │   ├── system/                       # [15.1] scheduler, triggers, relink + link checks, errors, costs
│   │   │   ├── services/[service]/           # [15.2] acting services (test/live actions)
│   │   │   ├── workers/[worker]/             # [15.3] shared worker runs
│   │   │   ├── subagents/[subagent]/         # [15.4] sub-agent calls
│   │   │   └── subagents.link/               # [15.5] one folder link per domain (D-030)
│   │   │       └── [domain-name]/            # [15.5.1] -> that domain's logs/ [19.4]
│   │   ├── data/                             # [16] shared data by source + subagents.link/ (D-030)
│   │   │   ├── system/                       # [16.1] registry, run state, read cursors, links index (D-031)
│   │   │   ├── workers/[worker]/             # [16.2] shared worker outputs
│   │   │   ├── subagents/[subagent]/         # [16.3] sub-agent outputs
│   │   │   └── subagents.link/               # [16.4] one folder link per domain (D-030)
│   │   │       └── [domain-name]/            # [16.4.1] -> that domain's data/ [19.5]
│   │   ├── tests/                            # [10.8] system tests (D-025); run by run-tests [14.1]
│   │   │   ├── agents/                       # [10.8.1] tests of the prompt + sub-agents (LLM behaviour)
│   │   │   │   ├── tests.config.json         # [10.8.1.1] every agent test: enabled, last_run, last_result, next_action
│   │   │   │   ├── [test-id].test.md         # [10.8.1.2] scenario, fixtures, expected behaviour
│   │   │   │   └── run-tests.system.link.js  # [10.8.1.3] -> [14.1] run-tests; runs this folder's tests.config.json (--kind agents preset)
│   │   │   ├── scripts/                      # [10.8.2] tests of scripts
│   │   │   │   ├── tests.config.json         # [10.8.2.1] every script test (same fields)
│   │   │   │   ├── [test-id].test.[js|py]    # [10.8.2.2]
│   │   │   │   └── run-tests.system.link.js  # [10.8.2.3] -> [14.1] run-tests; runs this folder's tests.config.json (--kind scripts preset)
│   │   │   └── subagents.link/               # [10.8.3] one folder link per domain (D-030)
│   │   │       └── [domain-name]/            # [10.8.3.1] -> that domain's tests/ [19.12]
│   │   ├── research/                         # [10.9] system research history (D-025)
│   │   │   ├── index.json                    # [10.9.1] every item: question, status, results, decisions, links
│   │   │   ├── [research-id]-[slug]/         # [10.9.2] one folder per item: README.md + artifacts
│   │   │   └── subagents.link/               # [10.9.3] one folder link per domain (D-030)
│   │   │       └── [domain-name]/            # [10.9.3.1] -> that domain's research/ [19.13]
│   │   ├── package.json                      # [10.4] JS deps (shared scripts)
│   │   ├── requirements.txt                  # [10.5] Python deps (shared scripts)
│   │   ├── init.sh                           # [10.6] installs the git hooks, runs relink for the whole project (D-031)
│   │   ├── start.sh                          # [10.7] starts the scheduler (all jobs, D-029) + system session
│   ├── prediction-market-agents/             # [19] DOMAIN-LEVEL AGENT (standard folder [2.7.1])
│   │   ├── .claude/                          # [19.1] domain-level Claude Code
│   │   │   ├── CLAUDE.md                     # [19.1.5] DOMAIN OWNER prompt (was [19.7]) (D-024: inside .claude/)
│   │   │   ├── settings.json                 # [19.1.6] permissions (deny .secrets/live/**, D-027), hooks, env, model, statusLine, outputStyle; committed
│   │   │   ├── settings.local.json           # [19.1.7] personal overrides; git-ignored
│   │   │   ├── rules/                        # [19.1.8] topic rules; `paths:` frontmatter; subfolders ok
│   │   │   │   └── [topic].md
│   │   │   ├── skills/                       # [19.1.2] skills: one folder each
│   │   │   │   └── [skill-name]/SKILL.md     # + supporting files
│   │   │   ├── commands/                     # [19.1.9] single-file prompts, /name
│   │   │   │   └── [command-name].md
│   │   │   ├── agents/                       # [19.1.1] sub-agents (own context/tools)
│   │   │   │   ├── pm-self-improvement-agent.md # [19.1.1.2] self-improvement sub-agent, this level (D-018)
│   │   │   │   └── [subagent-name].md
│   │   │   ├── workflows/                    # [19.1.10] workflow scripts; each becomes /<name>
│   │   │   │   └── [workflow-name].js
│   │   │   ├── output-styles/                # [19.1.11]
│   │   │   │   └── [style-name].md
│   │   │   ├── agent-memory/                 # [19.1.12] `memory: project` sub-agent memory (incl. SI, proposed)
│   │   │   │   └── [subagent-name]/MEMORY.md
│   │   │   └── agent-memory-local/           # [19.1.13] `memory: local`; git-ignored
│   │   ├── configs/                          # [19.2] domain config + file links
│   │   │   ├── prediction-market-agents.workers.json # [19.2.1] domain jobs: when, where it runs, platform, model (D-029)
│   │   │   ├── prediction-market-agents.links.json   # [19.2.3] domain file links: what, from where (D-031)
│   │   │   └── subagents.link/               # [19.2.2] one folder link per strategy agent (D-030)
│   │   │       └── [agent-name]/             # [19.2.2.1] -> that strategy's configs/ [21.2]
│   │   ├── scripts/                          # [19.3] domain scripts + file links
│   │   │   ├── relink.system.link.js         # [19.3.2] -> [14.1] relink; relinks this agent (D-031)
│   │   │   └── subagents.link/               # [19.3.1] one folder link per strategy agent (D-030)
│   │   │       └── [agent-name]/             # [19.3.1.1] -> that strategy's scripts/ [21.3]
│   │   ├── logs/                             # [19.4] domain session + domain SI logs
│   │   │   └── subagents.link/               # [19.4.1] one folder link per strategy agent (D-030)
│   │   │       └── [agent-name]/             # [19.4.1.1] -> that strategy's logs/ [21.4]
│   │   ├── data/                             # [19.5] domain data + file links
│   │   │   └── subagents.link/               # [19.5.1] one folder link per strategy agent (D-030)
│   │   │       └── [agent-name]/             # [19.5.1.1] -> that strategy's data/ [21.5]
│   │   ├── docs/                             # [19.6] domain docs + file links
│   │   │   └── subagents.link/               # [19.6.1] one folder link per strategy agent (D-030)
│   │   │       └── [agent-name]/             # [19.6.1.1] -> that strategy's docs/ [21.6]
│   │   ├── tests/                            # [19.12] domain tests (D-025); run by run-tests [14.1]
│   │   │   ├── agents/                       # [19.12.1] tests of the prompt + sub-agents (LLM behaviour)
│   │   │   │   ├── tests.config.json         # [19.12.1.1] every agent test: enabled, last_run, last_result, next_action
│   │   │   │   ├── [test-id].test.md         # [19.12.1.2] scenario, fixtures, expected behaviour
│   │   │   │   └── run-tests.system.link.js  # [19.12.1.3] -> [14.1] run-tests; runs this folder's tests.config.json (--kind agents preset)
│   │   │   ├── scripts/                      # [19.12.2] tests of scripts
│   │   │   │   ├── tests.config.json         # [19.12.2.1] every script test (same fields)
│   │   │   │   ├── [test-id].test.[js|py]    # [19.12.2.2]
│   │   │   │   └── run-tests.system.link.js  # [19.12.2.3] -> [14.1] run-tests; runs this folder's tests.config.json (--kind scripts preset)
│   │   │   └── subagents.link/               # [19.12.3] one folder link per strategy agent (D-030)
│   │   │       └── [agent-name]/             # [19.12.3.1] -> that strategy's tests/ [21.12]
│   │   ├── research/                         # [19.13] domain research history (D-025)
│   │   │   ├── index.json                    # [19.13.1] every item: question, status, results, decisions, links
│   │   │   ├── [research-id]-[slug]/         # [19.13.2] one folder per item: README.md + artifacts
│   │   │   └── subagents.link/               # [19.13.3] one folder link per strategy agent (D-030)
│   │   │       └── [agent-name]/             # [19.13.3.1] -> that strategy's research/ [21.13]
│   │   ├── package.json                      # [19.8]
│   │   ├── requirements.txt                  # [19.9]
│   │   ├── init.sh                           # [19.10] setup; runs relink for this agent (D-031)
│   │   ├── start.sh                          # [19.11] starts the domain session
│   │   └── strategy-1-agent/                 # [21] STRATEGY-LEVEL AGENT (standard folder [2.7.1])
│   │       ├── .claude/                      # [21.1] strategy-level Claude Code
│   │       │   ├── CLAUDE.md                 # [21.1.5] STRATEGY MANAGER prompt (was [21.7]) (D-024: inside .claude/)
│   │       │   ├── settings.json             # [21.1.6] permissions (deny .secrets/live/**, D-027), hooks, env, model, statusLine, outputStyle; committed
│   │       │   ├── settings.local.json       # [21.1.7] personal overrides; git-ignored
│   │       │   ├── rules/                    # [21.1.8] topic rules; `paths:` frontmatter; subfolders ok
│   │       │   │   └── [topic].md
│   │       │   ├── skills/                   # [21.1.2] skills: one folder each
│   │       │   │   └── [skill-name]/SKILL.md # + supporting files
│   │       │   ├── commands/                 # [21.1.9] single-file prompts, /name
│   │       │   │   └── [command-name].md
│   │       │   ├── agents/                   # [21.1.1] sub-agents (own context/tools)
│   │       │   │   ├── pm-strategy-1-self-improvement-agent.md # [21.1.1.1] self-improvement sub-agent, this level (D-018)
│   │       │   │   └── [subagent-name].md
│   │       │   ├── workflows/                # [21.1.10] workflow scripts; each becomes /<name>
│   │       │   │   └── [workflow-name].js
│   │       │   ├── output-styles/            # [21.1.11]
│   │       │   │   └── [style-name].md
│   │       │   ├── agent-memory/             # [21.1.12] `memory: project` sub-agent memory (incl. SI, proposed)
│   │       │   │   └── [subagent-name]/MEMORY.md
│   │       │   └── agent-memory-local/       # [21.1.13] `memory: local`; git-ignored
│   │       ├── configs/                      # [21.2] strategy config + file links
│   │       │   ├── strategy-1-agent.workers.json # [21.2.1] strategy jobs, e.g. the strategy session and its SI run (D-029)
│   │       │   ├── strategy-1-agent.links.json   # [21.2.3] strategy file links: what, from where (D-031)
│   │       │   └── subagents.link/           # [21.2.2] one folder link per trading agent (D-030)
│   │       │       └── [agent-name]/         # [21.2.2.1] -> that agent's configs/ [27]
│   │       ├── scripts/                      # [21.3] strategy scripts + file links
│   │       │   ├── relink.system.link.js     # [21.3.2] -> [14.1] relink; relinks this agent (D-031)
│   │       │   └── subagents.link/           # [21.3.1] one folder link per trading agent (D-030)
│   │       │       └── [agent-name]/         # [21.3.1.1] -> that agent's scripts/ [30]
│   │       ├── logs/                         # [21.4] strategy session + strategy SI logs
│   │       │   └── subagents.link/           # [21.4.1] one folder link per trading agent (D-030)
│   │       │       └── [agent-name]/         # [21.4.1.1] -> that agent's logs/ [34]
│   │       ├── data/                         # [21.5] strategy data: cross-variant history
│   │       │   └── subagents.link/           # [21.5.1] one folder link per trading agent (D-030)
│   │       │       └── [agent-name]/         # [21.5.1.1] -> that agent's data/ [35]
│   │       ├── docs/                         # [21.6] strategy definition, docs + file links
│   │       │   └── subagents.link/           # [21.6.1] one folder link per trading agent (D-030)
│   │       │       └── [agent-name]/         # [21.6.1.1] -> that agent's docs/ [46]
│   │       ├── tests/                        # [21.12] strategy tests (D-025); run by run-tests [14.1]
│   │       │   ├── agents/                   # [21.12.1] tests of the prompt + sub-agents (LLM behaviour)
│   │       │   │   ├── tests.config.json     # [21.12.1.1] every agent test: enabled, last_run, last_result, next_action
│   │       │   │   ├── [test-id].test.md     # [21.12.1.2] scenario, fixtures, expected behaviour
│   │       │   │   └── run-tests.system.link.js # [21.12.1.3] -> [14.1] run-tests; runs this folder's tests.config.json (--kind agents preset)
│   │       │   ├── scripts/                  # [21.12.2] tests of scripts
│   │       │   │   ├── tests.config.json     # [21.12.2.1] every script test (same fields)
│   │       │   │   ├── [test-id].test.[js|py] # [21.12.2.2]
│   │       │   │   └── run-tests.system.link.js # [21.12.2.3] -> [14.1] run-tests; runs this folder's tests.config.json (--kind scripts preset)
│   │       │   └── subagents.link/           # [21.12.3] one folder link per trading agent (D-030)
│   │       │       └── [agent-name]/         # [21.12.3.1] -> that agent's tests/ [49]
│   │       ├── research/                     # [21.13] strategy research history (D-025)
│   │       │   ├── index.json                # [21.13.1] every item: question, status, results, decisions, links
│   │       │   ├── [research-id]-[slug]/     # [21.13.2] one folder per item: README.md + artifacts
│   │       │   └── subagents.link/           # [21.13.3] one folder link per trading agent (D-030)
│   │       │       └── [agent-name]/         # [21.13.3.1] -> that agent's research/ [50]
│   │       ├── package.json                  # [21.8]
│   │       ├── requirements.txt              # [21.9]
│   │       ├── init.sh                       # [21.10] setup; runs relink for this agent (D-031)
│   │       ├── start.sh                      # [21.11] starts the strategy session
│   │       └── pm-momentum-v1-agent-opus55-test/       # [23] EXAMPLE agent variant (standard folder [2.7.1])
│   │           ├── .claude/                            # [24] agent-level Claude Code (own files only; no .claude links, D-030)
│   │           │   ├── CLAUDE.md                       # [24.5] trading agent prompt (was [37]) (D-024: inside .claude/)
│   │           │   ├── settings.json                   # [24.6] permissions (deny .secrets/live/**, D-027), hooks, env, model, statusLine, outputStyle; committed
│   │           │   ├── settings.local.json             # [24.7] personal overrides; git-ignored
│   │           │   ├── rules/                          # [24.8] topic rules; `paths:` frontmatter; subfolders ok
│   │           │   │   └── [topic].md
│   │           │   ├── skills/                         # [25] skills: one folder each
│   │           │   │   └── [skill-name]/SKILL.md       # + supporting files
│   │           │   ├── commands/                       # [24.9] single-file prompts, /name
│   │           │   │   └── [command-name].md
│   │           │   ├── agents/                         # [26] sub-agents (own context/tools)
│   │           │   │   └── [subagent-name].md
│   │           │   ├── workflows/                      # [24.10] workflow scripts; each becomes /<name>
│   │           │   │   └── [workflow-name].js
│   │           │   ├── output-styles/                  # [24.11]
│   │           │   │   └── [style-name].md
│   │           │   ├── agent-memory/                   # [24.12] `memory: project` sub-agent memory (incl. SI, proposed)
│   │           │   │   └── [subagent-name]/MEMORY.md
│   │           │   └── agent-memory-local/             # [24.13] `memory: local`; git-ignored
│   │           ├── configs/                            # [27] own configs + file links
│   │           │   ├── pm-momentum-v1-agent-opus55-test.config.json  # [27.2] own config: mode, risk, strategy
│   │           │   ├── pm-momentum-v1-agent-opus55-test.workers.json # [27.4] own jobs: main run, workers, one-off jobs (D-029)
│   │           │   ├── pm-momentum-v1-agent-opus55-test.links.json   # [27.3] own file links: what, from where (D-031; was the `links` section of [27.2])
│   │           │   ├── system.config.link.json         # [27.1] -> [11.1] system/configs/system.config.json
│   │           │   └── models.config.link.json         # [27.1] -> [11.11] system/configs/models.config.json
│   │           ├── scripts/                            # [30] own scripts + file links; kind in suffix
│   │           │   ├── get-polymarket-data.worker.py   # [31] worker: fetch market data
│   │           │   ├── clean-data.system.js            # [32] system script: clean/normalise
│   │           │   ├── make-buy.decision.js            # [33] decision script (buy/sell)
│   │           │   ├── risk-check.decision.link.js     # [30.1] -> [14.3] system/scripts/decisions/risk-check.decision.js
│   │           │   ├── relink.system.link.js           # [30.3] -> [14.1] relink; the agent reruns it after editing its links file (D-031)
│   │           │   └── run-tests.system.link.js        # [30.2] -> [14.1] system/scripts/system/run-tests.system.js (D-025)
│   │           ├── logs/                               # [34] own logs + file links (only if needed)
│   │           │   ├── runs.jsonl, run-[date].md       # own run logs
│   │           │   ├── polymarket-prices.worker.link.log  # [34.1] -> [15.3] system/logs/workers/polymarket-prices/latest.log
│   │           │   └── tests.jsonl                     # [34.2] one line per test run (D-025)
│   │           ├── data/                               # [35] own data + file links
│   │           │   ├── get-polymarket-data/            # [35.2] own outputs, one folder per producer
│   │           │   ├── polymarket-prices.link.json     # [35.1] -> [16.2] system/data/workers/polymarket-prices/latest.json
│   │           │   ├── news-digest.link.md             # [35.1] -> [16.3] system/data/subagents/news-digest/latest.md
│   │           │   ├── markets-catalog.link.json       # [35.1] -> [19.5] its domain's data/markets-catalog/latest.json (@domain, D-031)
│   │           │   └── whale-signals.link.json         # [35.1] -> an agent in another domain: [other-agent]/data/whale-signals/latest.json (D-031)
│   │           ├── docs/                               # [46] own docs + file links
│   │           │   ├── README.md, strategy.md, changes.md, decisions.md, notes.md  # [46.2]
│   │           │   ├── safety.link.md                  # [46.1] -> [2.8] system/docs/safety.md
│   │           │   └── agent-architecture.link.md      # [46.1] -> [2.17.1] system/docs/common/agent-architecture.md
│   │           ├── tests/                              # [49] agent tests (D-025); run by run-tests [14.1]
│   │           │   ├── agents/                         # [49.1] tests of the prompt + sub-agents (LLM behaviour)
│   │           │   │   ├── tests.config.json           # [49.1.1] every agent test: enabled, last_run, last_result, next_action
│   │           │   │   ├── [test-id].test.md           # [49.1.2] scenario, fixtures, expected behaviour
│   │           │   │   └── run-tests.system.link.js    # [49.1.3] -> [14.1] run-tests; runs this folder's tests.config.json (--kind agents preset)
│   │           │   └── scripts/                        # [49.2] tests of scripts
│   │           │       ├── tests.config.json           # [49.2.1] every script test (same fields)
│   │           │       ├── [test-id].test.[js|py]      # [49.2.2]
│   │           │       └── run-tests.system.link.js    # [49.2.3] -> [14.1] run-tests; runs this folder's tests.config.json (--kind scripts preset)
│   │           ├── research/                           # [50] agent research history (D-025)
│   │           │   ├── index.json                      # [50.1] every item: question, status, results, decisions, links
│   │           │   └── [research-id]-[slug]/           # [50.2] one folder per item: README.md + artifacts
│   │           ├── package.json                        # [38] JS deps + npm scripts
│   │           ├── requirements.txt                    # [39] Python deps
│   │           ├── init.sh                             # [40] setup; runs relink for this agent (D-031)
│   │           └── start.sh                            # [41] start one run / the scheduler
│   └── copy-trading-agents/                  # [42] copy trading domain (same shape as [19])
├── apps/                                     # [43] cloned GitHub repos used by us/agents
│   └── [some-github-repo]/                   # [44] one cloned repo
└── trading-ui/                               # [45] Next.js API + UI: monitoring and control
```

Note: the shared docs [2] now live in the system domain at `agents/system/docs/` (D-017); section numbers [2.x] are kept, and `docs/…` below means that folder. The owner's input first placed `vision.md` under top-level `docs/` [2.2]. Everything under `docs/` other than `vision.md` is **proposed**, except where the owner asked for it (feature-map, file-tree, data-schemas, flows, metrics, common, index, per-agent docs). This file is `docs/file-tree.md` [2.13]. `agents/docs/` [5] was merged into it; the top-level `docs/` was then moved into the system domain (D-017). **Every symlinked file or folder has `.link` in its name** (owner rule, see [2.7]); `A -> B` in the tree means A is a symlink to B. **Layout rule (D-013–D-016):** `agents/` holds domains only, and `system/` is one of them. Every agent has the same folders (`configs/`, `scripts/`, `logs/`, `data/`); each holds the agent's own files plus **individual file links** to only the files its logic needs (D-020). Each agent lists those links in its own `configs/[name].links.json`, and the shared `relink` script builds them (D-031). The system domain holds shared files. Every level's content folders also hold `subagents.link/[child-name]/` folder links to its direct children's folders of the same kind (D-030, [2.7.4]); `.claude/` folders are not linked. The current working copies live in `/mnt/project-files/vision/` until the tree exists.

## 2. Objects

Each object lists its **purpose**, **contents**, **writers / readers** and **open questions**.

### [0] `trading-os/` (root)
- **Purpose:** the workspace holding the whole OS.
- **Contents:** the objects below.
- **Writers / readers:** owner, system-support agents.
- **Open:** Is this one git repo or several (e.g. per agent, `apps/` separate)? Where does it run (local machine, VPS)?

### [1] `README.md`
- **Purpose:** entry point for humans and agents: what the OS is and where things are.
- **Contents:** short summary, links into `agents/system/docs/` ([2.1], [2.2], [2.13], [2.17], [2.18]), how to start the system/UI. After D-017 it is the only doc at the repo root.
- **Writers / readers:** system-support agents write it. Everyone reads it.
- **Open:** Should it also double as the root `CLAUDE.md` for agents working at the root?

### [2] `agents/system/docs/` (moved from top-level `docs/` by D-017; numbers kept)
- **Purpose:** the shared docs of the whole OS (self-support logic), living in the system domain like the other shared folders (`configs/`, `scripts/`, `logs/`, `data/`). This is the first place any agent or person reads to understand the system.
- **Pattern (D-017, same as D-014/D-015; links per D-020):** shared docs are real files here; every agent has its own real `docs/` [46] with individual file links [46.1] to the shared docs it needs; and [2.20] `subagents.link/` holds one folder link per domain's `docs/` (D-030); each domain's docs link on to its strategies' and each strategy's to its agents', so every agent's docs can be reached from here.
- **Scope:** vision, how it works, rules, decisions, roadmap, runbooks, schemas, flows, metrics, common agent knowledge [2.17], the index of all things [2.18], and the links to each domain's docs [2.20].
- **Repo root:** only `README.md` [1], which points here. **Root `docs/`? No strong reason to keep it.** Repo-level dev docs (how to work on this repo) fit here too, e.g. in `how-to/`. The one caveat is that some tools look for docs at the root (GitHub shows the root README; Claude Code loads a root `CLAUDE.md`), and a short root `README.md` covers that.
- **Writers / readers:** the owner gives inputs; the system-support docs sub-agent [10.1.1.2] `sys-docs-agent` (D-026) writes the files. All agents read them through [46.1] (read-only); the UI reads them here.
- **Contents:** [2.1]–[2.18], [2.20]. ([2.19] retired.)
- **Format:** Markdown only (vision §10). Every file starts with a title and version, and ends with a changelog.

### [2.1] `docs/README.md` (proposed)
- **Purpose:** index of `docs/`, so an agent knows what to read and in which order.
- **Outline:** What this folder is · Read order (vision → overview → file-tree → feature-map → conventions → safety → flows → data-schemas → metrics → common/ → index/) · File list with one line each · How docs get updated.
- **Writers / readers:** docs agent writes it. Everyone reads it first.
- **Updated:** whenever a file is added, removed or renamed in `docs/`.

### [2.2] `docs/vision.md` (was [3])
- **Purpose:** all owner inputs, summarised and structured; the "what and why" of the system; context for any agent.
- **Outline:** as the current `vision.md`: What it is · Building blocks · Requirements · Domains · Ideas under evaluation · Open questions · Folder layout · Agent types · Routing · Data and triggers · Test/live · UI · Workflow · Undecided ideas · Changelog.
- **Writers / readers:** docs agent, from owner input. The owner confirms. All agents read it.
- **Updated:** after each new owner input (the raw input goes to [2.10] first).

### [2.3] `docs/overview.md` (proposed; today's `overview.md`)
- **Purpose:** how the whole OS works end to end: the "how" behind the vision, with diagrams.
- **Outline:** The idea in one paragraph · Components (workers, data, agents, self-improvement, UI, platforms) · Data flow · Agent run loop and triggers · Self-improvement wheel · Test vs live · Where things live (links to [2.13], [2.15]).
- **Writers / readers:** docs agent writes it. New agents and the owner read it.
- **Updated:** when vision or architecture changes. Agent-internal detail belongs in [2.17.1], not here.

### [2.4] `docs/glossary.md` (proposed)
- **Purpose:** one meaning per term, so the owner, agents and the UI use the same words.
- **Outline:** alphabetical terms. Seed list: agent, main agent, main domain agent, sub-agent, worker, system-support agent, self-improvement agent, strategy, modification/variant, domain, platform, model, route, test mode, live mode, run, trigger, important file, subscription, champion/challenger.
- **Writers / readers:** docs agent writes it. Everyone reads it.
- **Updated:** when a new term appears in inputs or docs.

### [2.5] `docs/roadmap.md` (proposed)
- **Purpose:** what is built now, next and later; keeps agents working on the right thing.
- **Outline:** Current phase and goal · Now (in progress) · Next · Later (e.g. Codex, Kimi 3, OpenRouter connection, more domains) · Done.
- **Writers / readers:** the owner sets priorities; main domain agents and the docs agent update status. System-support agents read it before choosing work.
- **Updated:** when priorities change or an item is finished.

### [2.6] `docs/decisions.md` (proposed)
- **Purpose:** append-only log of decisions, so settled questions are not reopened and agents know why things are as they are.
- **Outline:** one entry per decision: ID and date · Decision · Why · Alternatives considered · Source (link to [2.10] input or vision question) · Status (active/superseded).
- **Writers / readers:** docs agent records owner decisions. System-support and self-improvement agents may add proposals marked "pending owner". Everyone reads it.
- **Updated:** each time an open question is resolved (e.g. every "[resolved]" mark in vision §6).
- **Seed entries (owner decisions so far):** D-001 keep symlinks for shared things (vision §7) · D-002 every symlinked file/folder has `.link` in its name · D-003 per-agent docs live centrally in `docs/agents/` and are symlinked into the agent folder as `docs.link/` · D-004 `docs/` is the single docs root, with `common/`, `index/`, `data-schemas.md`, `flows.md` and `metrics.md` added · D-005 data as JSON/MD files for now · D-006 configs are of two types for now: one global `system.config.json` and one config per agent. Per-agent configs live centrally and are linked into agents as `config.link.json` (direction proposed). The exact shape and the common/individual split are to be decided with example agents · D-007 workers are just scripts in `scripts/` (no `workers/` folder); scripts are workers, decisions or system scripts, system-level or per agent; workers are defined in config (`workers.config.json`) · D-008 sub-agents are Claude Code subagents under `.claude/agents/`; only system-wide ones for now · D-009 logs are central by source (system, services, workers, subagents, agents), some linked into agents · D-010 data is central by source (system, workers, subagents, agents), some linked into agents · D-011 model/platform routing is config in a separate `models.config.json`; no `platforms-and-models/` folder · D-012 every agent has a globally unique name (unique across all domains), used as its ID in folder names, configs, logs, data, docs, indexes and the UI · *Interpretation of the owner's 2026-09-29 input:* D-013 `system` is a domain like the trading domains; domains sit directly under `agents/` (`trading-domains/` removed) · D-014 every agent (system and trading) has the same folders (`configs/`, `scripts/`, `logs/`, `data/`) holding its own real files plus a `system.link/` folder link to the system folder of the same kind; links are to folders, not files. **Supersedes** D-006's central per-agent config location, and the agent-log/agent-data part of D-009 and D-010 (shared logs/data stay central by source) · D-015 the system domain has the same folders holding the shared files, plus `agents/[agent-name].link/` views of every agent's folder of the same kind (one view over everything) · D-016 `.claude/` exists at every domain level (including system) and at every strategy level for trading agents; agent-level `.claude/` links them in (link mechanism proposed). Extends D-008 (not only system-wide sub-agents any more). **Status:** D-006 (location part), D-009 (agent logs part) and D-010 (agent data part) are marked *superseded* · D-018 no separate domain-agent or SI-agent folders: the domain owner is a sub-agent in the domain-level `.claude/agents/` ([19.1.1.1], was [20]), and self-improvement is a sub-agent at every `.claude/` level (system [10.1.1.1], domain [19.1.1.2], strategy [21.1.1.1]; was [22]), each scoped to its level; their memory/state lives in `agents/system/data/subagents/[name]/` (proposed) · D-025 every level's agent folder has `tests/` (`agents/` + `scripts/`, each with a `tests.config.json` listing every test with enabled, last run, result, next action) run by a shared `run-tests` script, and `research/` (`index.json` history + one folder per item); at the folder root next to `scripts/` (placement proposed; alternative: inside `.claude/`). Research moves out of `data/` · D-024 every `.claude/` (all levels) follows the standard Claude Code layout ([2.7.2]): `CLAUDE.md` inside `.claude/` (moved from the folder root), `settings.json`, `settings.local.json`, `rules/`, `skills/`, `commands/`, `agents/`, `workflows/`, `output-styles/`, `agent-memory/`, `agent-memory-local/`; generic placeholders only for now. Proposed: SI memory moves to `.claude/agent-memory/[si-name]/MEMORY.md` (updates D-022). Parent → child links stay in `agents/` and `skills/` · D-023 secrets live in a git-ignored repo-root `.secrets/` (test/ and live/ separated, one `.env` file per account or platform, metadata index without values); agents and configs only hold `secret_ref`s; scripts load values at execution time via `load-secret` (checks the agent's config and mode); secrets are never linked into agent folders, never logged and never put in LLM context (Claude Code deny rule); later upgrade path to OS keychain / password manager / vault with the same refs (all proposed) · D-022 three levels of agents, each a folder with the **identical** standard structure ([2.7.1]: `.claude/`, `configs/`, `scripts/`, `logs/`, `data/`, `docs/`, `CLAUDE.md`, `package.json`, `requirements.txt`, `init.sh`, `start.sh`): system (manages all domains and system development), domain (responsible for its domain), strategy (one concrete strategy); trading variants keep the same structure. The system also holds the shared files and per-agent views (folder links, not copies). Reconciles D-018: the domain's `CLAUDE.md` is the domain owner (sub-agent file retired); SI stays a sub-agent per level, with its memory in that level's `data/` (supersedes the D-018 memory proposal). *Updated by D-024:* `CLAUDE.md` moved into `.claude/`; SI memory proposed in `.claude/agent-memory/` · D-021 no `.claude` links from the domain level down to strategies' agents and skills ([19.1.3]/[19.1.4] retired). The D-019 "every run starts at `agents/system/`" proposal is withdrawn; proposed instead: each level runs in its own folder, a trading agent runs in its own folder, and higher-level sub-agents hand results to agents as data files linked per D-020. Open: whether system → domain [10.1.3]/[10.1.4] and strategy → agent [21.1.3]/[21.1.4] links stay · D-020 inside an agent's `configs/`, `scripts/`, `logs/`, `data/`, `docs/`, links are **individual file links** (`[name].link.[ext]`) only to the files its logic needs, from any folder (system, domain, strategy, other agents' outputs). They are chosen by create-agent and updated by the self-improvement sub-agent, and listed in the config's `links` section. **Supersedes** D-014's folder-only `system.link/` rule for agents and answers the D-019 follow-up. The system views and D-019 `.claude` down-links stay folder links · D-019 `.claude` links go parent → child only: system `.claude` links to each domain's (and system agent's) `.claude`, domain to its strategies', strategy to its agents'; agents have no upward links; runs start from the top so a session sees every level below (proposed). Supersedes the upward-link part of D-016. Open: apply the same rule to `system.link/` in configs/scripts/logs/data/docs? · D-017 docs follow the same pattern: each agent has a real `docs/` with `docs/system.link/` → `agents/system/docs/`; the shared docs (formerly top-level `docs/`) move to `agents/system/docs/`, which also holds `agents/[agent-name].link/` views; the repo root keeps only `README.md`. **Supersedes D-003** (and the location part of D-004). · D-026 system-support agents are sub-agents in `agents/system/.claude/agents/` (e.g. `sys-docs-agent.md`), not folders; [10.2] retired and the system `.claude` down-links to them dropped · D-027 test secrets live in one file `.secrets/test/.env` (all keys, prefixed per account/platform) that agents may read and update; `live/.env` mirrors the keys with owner-only values in a later phase; scripts get only the keys their config declares via the shared loader (updates D-023's one-file-per-ref layout) · D-028 `.gitignore` is the real commented file shown in [48] · D-029 every agent (system, domain, strategy, variant) has its own jobs file `configs/[name].workers.json` ([name] = the domain for a domain agent, else the agent name): each job is a script or an AI run (agent, sub-agent, skill, workflow, command) with on/off, schedule (every, cron, once on a date, after another job, manual), where it runs (local headless, cloud, desktop, GitHub Actions), platform (Claude Code, Cursor, Codex, none), model and, for AI runs, prompt, workspace, skill and tool limits; the system's `configs/workers/[domain]/` links every workers file by domain; one central scheduler runs them (format and scheduler proposed). Supersedes D-007's single `workers.config.json` (now [11.10] `system.workers.json`) and the [28] `workers` section; updates D-011 (a job may name its model, else its route applies) · D-030 every level (system, domain, strategy) uses one template for each of its content folders (`configs/`, `scripts/`, `logs/`, `data/`, `docs/`, `tests/`, `research/`): the level's own files, plus `subagents.link/` holding one folder link per direct child agent, named after the child's folder and pointing at the child's folder of the same kind (system → domains, domain → strategies, strategy → its trading agents; trading agents have none). Replaces the system's flat views of every agent (`agents/[agent-name].link/` in [2.20], [11.2], [14.4], [15.5], [16.4]; D-015/D-017) and the jobs view [11.12] (D-029). Links inside a `.link` folder need no `.link` of their own (amends D-002). No `.claude` folder is linked at any level for now: [10.1.3], [10.1.4], [21.1.3], [21.1.4] removed (pauses D-019) · D-031 every agent (system, domain, strategy, variant) has its own links file `configs/[name].links.json` saying which files it links, from where (the system, its own domain or strategy, another domain, or any other agent by unique name) and where they appear in its folders; the shared `relink` script [14.1] builds all links from these files plus the child links (D-030), removes stale ones and checks them. It runs when a links file changes (scheduler watch), at review time (git pre-commit, after pull or merge, owner approval in the UI), when an agent edits its own links file (it reruns relink; a Claude Code hook does it too) and from create-agent/init.sh. Replaces the `links` section of the agent config (D-020's file-link rules stay) and link building in `init.sh`; format and triggers proposed

### [2.7] `docs/conventions.md` (proposed)
- **Purpose:** rules that make hundreds of agents consistent and machine-readable.
- **Outline:** **Agent naming (D-012):** every agent's name is globally unique (across all domains) and is its **ID** everywhere: folder [23], its config file [27.2], its docs [46], its entry in its parent's `subagents.link/` folders (D-030), index [2.18.1], UI, and in routes [11.11].
  - **Format (proposed, from the owner's pattern):** `[domain]-[modification]-v[N]-agent-[platform-model]-[test|live]`, lowercase `a-z 0-9 -`, max 64 characters. Examples: `pm-momentum-v1-agent-opus55-test`, `ct-whale-follow-v3-agent-composer25-live`. Domain codes: `pm` prediction markets, `ct` copy trading, `sys` system-wide. The strategy family is recorded in config and index, not in the name.
  - **Non-trading agents (proposed):** `[domain]-[scope]-[role]-agent`, e.g. `sys-docs-agent`; the same format is used for sub-agent names (e.g. `pm-strategy-1-self-improvement-agent`), and sub-agent names are unique too (checked against [2.18.1] and [2.18.3]).
  - **Clone / variant (proposed):** a clone always gets a new name. A changed config, prompt or code bumps `v[N]`; a different model changes the `[platform-model]` part. The new agent records `parent` in its config and index.
  - **Rename (proposed):** never. The name is a permanent ID. Test → live creates a new agent (`…-live`) with `parent` = the test agent; the test agent keeps running or is retired.
  - **Reuse (proposed):** names are never reused, even after deletion (retired names stay in [2.18.1]).
  - **Enforced by:** the registry [2.18.1] and the check in `create-agent.system.js` [14.1].
 · **Tests and research (D-025):** every level has `tests/` and `research/` at its folder root, see [2.7.3] · **Secrets (D-023):** `secret_ref` = `[test|live]/[name]` (e.g. `test/polymarket-acct-1`) → file `.secrets/[test|live]/[name].env`; names are unique; values never appear in configs, docs, data, logs, prompts or links · **Folder layout (D-013–D-016):** `agents/[domain]/`, with `system` as a domain; every agent has `configs/`, `scripts/`, `logs/`, `data/`, `docs/` (plural names everywhere); shared docs in `agents/system/docs/` (D-017) · Script names `[name].[kind].[ext]` with kind `worker` / `decision` / `system`, plus matching sub-folders in [14] · Languages (JS/TS, Python) · Data files (JSON/MD layout, dates, naming) · Config files (`*.config.json`, `*.workers.json` and `*.links.json`; shared [11.1], [11.10], [11.11], [11.13], per agent [27.2], its jobs file [27.4] (D-029) and its links file [27.3] (D-031)) and keys (mode, schedule, route, important files) · **Symlinks: `.link` rule** (owner decision D-002): every symlinked file or folder has `.link` in its name. **Agent links are individual file links (D-020):** `[name].link.[ext]` inside `configs/`, `scripts/`, `logs/`, `data/`, `docs/`, one per needed file, listed in the agent's links file `configs/[name].links.json` [27.3] (D-031; format in [11.13]). `[name]` is the target's base name, with a short source hint if two would clash (e.g. `polymarket-prices.link.json`, `risk-check.decision.link.js`, `safety.link.md`). **Child links (D-030):** in every level that has child agents, each content folder (`configs/`, `scripts/`, `logs/`, `data/`, `docs/`, `tests/`, `research/`) holds `subagents.link/[child-name]/`, a folder link to that child's folder of the same kind (system → domains, domain → strategies, strategy → its trading agents). Links directly inside a `.link` folder are named after the child only, without `.link` of their own: the folder name marks them (amends D-002). These are the only folder links. **No `.claude` links** at any level for now (D-030; D-019's down-links are paused). Tools never follow `.link` folders recursively: a scan of `agents/**` sees every real file once, and anything that wants a child's files goes down one `subagents.link/` at a time. Anything without `.link` is a real file owned by that folder. Only the shared `relink` script [14.1] creates or removes links (D-031); `init.sh` [40] and everything else calls it · Log format · Doc format (version + changelog).
- **[2.7.1] Standard agent folder (D-022):** every agent folder has the **identical structure**, at every level: the system [10], each domain [19], each strategy [21] and each trading variant [23]. System-support roles are sub-agents, not folders (D-026).
  ```text
  [agent-folder]/
  ├── .claude/             # standard Claude Code folder, see [2.7.2]
  ├── configs/             # [agent-id].config.json + [agent-id].workers.json (D-029) + [agent-id].links.json (D-031) + file links (D-020) + subagents.link/
  ├── scripts/             # own *.worker.* / *.decision.* / *.system.* + file links + subagents.link/
  ├── logs/                # own logs + file links + subagents.link/
  ├── data/                # own data (outputs, history) + file links + subagents.link/
  ├── docs/                # README, strategy/role, changes, decisions, notes + file links + subagents.link/
  ├── tests/               # D-025: agents/ + scripts/, each with tests.config.json; see [2.7.3]; + subagents.link/
  ├── research/            # D-025: index.json + [research-id]-[slug]/; see [2.7.3]; + subagents.link/
  ├── package.json         # JS deps + npm scripts
  ├── requirements.txt     # Python deps
  ├── init.sh              # setup; runs relink for this agent (its file links + its entries in the parent's subagents.link/)
  └── start.sh             # start this agent's session / run
  ```
- **[2.7.4] Same template in every content folder (D-030):** each of `configs/`, `scripts/`, `logs/`, `data/`, `docs/`, `tests/`, `research/` holds the level's **own** files and, if the level has child agents, `subagents.link/` with one folder link per child, named after the child's folder, pointing at the child's folder of the same kind. Example for docs:
  ```text
  agents/system/docs/                                   # system's own docs [2]
  └── subagents.link/prediction-market-agents/          # [2.20.1] -> agents/prediction-market-agents/docs/
  agents/prediction-market-agents/docs/                 # domain's own docs [19.6]
  └── subagents.link/strategy-1-agent/                  # [19.6.1.1] -> .../strategy-1-agent/docs/
  agents/prediction-market-agents/strategy-1-agent/docs/        # strategy's own docs [21.6]
  └── subagents.link/pm-momentum-v1-agent-opus55-test/  # [21.6.1.1] -> that agent's docs/ [46]
  ```
  - Trading agents (variants) have no children, so no `subagents.link/`.
  - The links are made by `relink` [14.1] from the folder tree (the child's `init.sh` [40] runs it at creation) and removed by relink once the child's folder is gone (`stop-or-delete` [2.11.5]). They are not listed in any links file.
  - Links are read-only views: a parent reads its children's files through them and writes only its own files.
  - `.claude/` folders are **not** linked at any level for now (D-030).
- **[2.7.5] Links file per agent (D-031):** every agent (system, domain, strategy, variant) has `configs/[name].links.json` ([name] as for the workers file: `system`, the domain name, or the agent name): [11.13], [19.2.3], [21.2.3], [27.3]. Each entry says where the link appears in the agent's own folders (`to`) and which file it points at (`from`): something in the system, its own domain or strategy, another domain, or any other agent by its unique name. The shared `relink` script [14.1] builds every link from these files plus the child links [2.7.4]. Format and rules in [11.13]; when relink runs in [14.1].
- **[2.7.2] Standard `.claude/` folder (D-024):** the same at every level (system [10.1], domain [19.1], strategy [21.1], variant [24]). The tree shows only generic placeholders; concrete skills, commands, rules and sub-agents are added later. The only named sub-agent is each level's self-improvement placeholder (D-018).
  ```text
  .claude/
  ├── CLAUDE.md               # [x.5]  the level's prompt (inside .claude/, not at the folder root)
  ├── settings.json           # [x.6]  permissions (incl. deny .secrets/live/**, D-023/D-027), hooks, env, model, statusLine, outputStyle; committed
  ├── settings.local.json     # [x.7]  personal overrides; git-ignored [48]
  ├── rules/[topic].md        # [x.8]  topic-scoped instructions; `paths:` frontmatter loads them only for matching files; subfolders ok
  ├── skills/[skill-name]/SKILL.md   # [x.2] reusable prompts (/name or auto-invoked) + supporting files
  ├── commands/[command-name].md     # [x.9] single-file prompts, /name
  ├── agents/[subagent-name].md      # [x.1] sub-agents with own context window/tools
  ├── workflows/[workflow-name].js   # [x.10] dynamic workflow scripts, each becomes /<name>
  ├── output-styles/[style-name].md  # [x.11]
  ├── agent-memory/[subagent-name]/MEMORY.md  # [x.12] memory for sub-agents with `memory: project`
  └── agent-memory-local/            # [x.13] same for `memory: local`; git-ignored [48]
  ```
  - Numbering: `x` = the level's `.claude` number ([10.1], [19.1], [21.1], [24]); for the variant, skills is [25] and agents is [26].
  - **Relink hook (D-031, proposed):** each level's `settings.json` [x.6] has a `PostToolUse` hook: when Claude edits or writes a `configs/*.links.json`, the hook runs `relink` for that agent, so the links follow the file even if the session forgets.
  - **No `.claude` links (D-030, for now):** no level links another level's `.claude/`. The D-019 down-links ([10.1.3]/[10.1.4], [21.1.3]/[21.1.4]) are removed; each session sees only its own `.claude/`, and a parent that needs a child's skill or sub-agent reads it by path.
  - **SI memory (D-024, proposed):** each level's self-improvement sub-agent uses `memory: project`, so its memory lives in that level's `.claude/agent-memory/[si-name]/MEMORY.md` ([x.12]). Research goes to the level's `research/` ([2.7.3], D-025); cross-variant history stays in `data/`. This updates the D-022 memory note.
  - **The system-level agent is the one exception in content:** its `configs/`, `scripts/`, `logs/`, `data/`, `docs/` also hold the shared files. Like every level, it reaches its children (the domains) through `subagents.link/` [2.7.4]; strategies and agents are one or two steps further down (D-030).
  - **Level agent IDs (proposed, D-012):** level folders keep their structural names, and their IDs live in config and the index: `sys-system-agent` (for `system/`), `pm-domain-agent` (for `prediction-market-agents/`), `pm-strategy-1-agent` (for `strategy-1-agent/`).
- **[2.7.3] Standard `tests/` and `research/` (D-025; placement proposed):** every level's agent folder has both at the folder root, next to `scripts/`: system [10.8]/[10.9], domain [19.12]/[19.13], strategy [21.12]/[21.13], and variant [49]/[50]. *Alternative:* inside `.claude/` (`.claude/tests/`, `.claude/research/`), which is how "every claude layer" could also be read. The root was picked because tests target scripts and data as well as prompts, and `.claude/` keeps Claude Code's own layout (D-024).
  ```text
  tests/
  ├── agents/                    # tests of the level's CLAUDE.md and sub-agents (LLM behaviour)
  │   ├── tests.config.json      # registry + state of every agent test
  │   ├── [test-id].test.md      # scenario: input/fixtures, expected behaviour, how it is graded
  │   └── run-tests.system.link.js   # link to the shared run-tests [14.1]; runs this folder's config (kind agents)
  └── scripts/                   # tests of the level's scripts
      ├── tests.config.json      # registry + state of every script test
      ├── [test-id].test.[js|py]
      └── run-tests.system.link.js   # same link; runs this folder's config (kind scripts)
  research/
  ├── index.json                 # history of every research item
  └── [research-id]-[slug]/      # one folder per item
      ├── README.md              # question, method, results, decisions
      └── [artifacts]            # datasets, charts, backtest outputs, notes
  ```
  - **Running tests (proposed):** one shared script `run-tests.system.js` [14.1]. **Each test folder has its own runner link** (owner request, v1.11): `tests/agents/run-tests.system.link.js` and `tests/scripts/run-tests.system.link.js` (D-020 file links, [x.1.3]/[x.2.3]), so the script that runs a config sits next to it. The script reads where it was called from (the link's path): called from `tests/agents/` it presets `--kind agents` and that folder's `tests.config.json`; from `tests/scripts/` it presets `--kind scripts`; from the level's `scripts/` [30.2] it runs both. So `node tests/agents/run-tests.system.link.js` runs every enabled agent test of that level, and `--id`/`--schedule` still narrow it. `run-tests [--kind agents|scripts] [--id …] [--schedule …]` reads the level's `tests.config.json` files, runs every `enabled` test that matches, writes back `last_run`, `last_result`, `last_duration_ms`, `fail_count`, and appends one line per test to the level's `logs/tests.jsonl`. **How an agent test runs:** for each `t-agents-*` entry, run-tests copies the test's fixtures into a temporary copy of the level's folder, starts Claude Code headless there (`claude -p` with the scenario from `[test-id].test.md`, the level's own `.claude/`, the model from [11.11]), forces `mode: test` in the effective config, and gives it no secrets (`load-secret` refuses inside a test run; `.secrets/**` is denied anyway). It captures the transcript, the files written and any decision calls, then grades them: script checks from the test file first, a judge sub-agent only for fuzzy expectations. Never live, never real orders. They are graded by script checks or a judge sub-agent. The owner toggles `enabled` from the UI (written to the config file).
  - **Research (proposed):** research that D-022/D-024 kept in the level's `data/` now goes here. The level's SI sub-agent is the main writer. It opens an item (`planned`/`running`), keeps artifacts in its folder, closes it with `results_summary` and `decisions`, and links the variants/changes/tests it led to (`related`). Its `.claude/agent-memory/` keeps only lessons and pointers (e.g. `r-0001`), not the research itself. Cross-variant `changes.md` stays in the strategy's `data/`.
  - **IDs:** tests `t-[agents|scripts]-NNN`, research `r-NNNN`; unique within the level, referenced across the system as `[agent-id]/[id]` (D-012); never reused. Schemas in [2.14].
- **Writers / readers:** docs agent writes it; the owner approves changes. The create-agent logic, all agents and the UI read it.
- **Updated:** when a convention is added or changed (and recorded in [2.6]).

### [2.8] `docs/safety.md` (proposed)
- **Purpose:** the rules no agent may break: money, keys and approvals.
- **Outline:** Test vs live (every acting service reads its mode from config) · Live-money approval (only the owner, via the UI) · Hard risk limits enforced in code · **Secrets and wallets (D-023):** stored only in [47] `.secrets/`, test and live separated; referenced by `secret_ref` only; loaded by scripts at execution time via `load-secret` [14.1], never in LLM context, prompts, docs, data or logs; never linked into agent folders; only the owner adds live keys (proposed); rotation rules · External text is untrusted · What self-improvement may change without approval · Stop/kill switch.
- **Writers / readers:** the owner decides; the docs agent writes it down. Every agent reads it; executors and risk checks implement it.
- **Updated:** only on explicit owner decision.

### [2.9] `docs/changelog.md` (proposed)
- **Purpose:** system-level history: what changed in the OS, when and why (not per-agent changes, which stay in agent folders/logs).
- **Outline:** reverse-chronological entries: Date · Change · Area (docs, system, domain, UI, routing) · Link to decision/input.
- **Writers / readers:** system-support agents append entries. The owner and the UI read it.
- **Updated:** on every system-level change.

### [2.10] `docs/inputs/` (proposed)
- **Purpose:** verbatim archive of every owner input, the source of truth behind vision, decisions and roadmap.
- **Contents:** [2.10.1] `YYYY-MM-DD-[topic].md`, one input per file: header (date, channel, topic), the raw text unchanged, then "Processed into" links (vision sections, decisions).
- **Writers / readers:** docs agent saves each input on receipt; it never edits the raw text. Agents read it when the summaries are unclear.
- **Updated:** on every new owner input.

### [2.11] `docs/how-to/` (proposed)
- **Purpose:** step-by-step runbooks that agents (and the owner) follow for recurring operations. These are what makes "create a new agent based on this input" repeatable (vision §13).
- **Contents:**
  - [2.11.1] `create-agent.md` (same steps for a new domain or strategy agent, D-022): input → pick domain/strategy → name per [2.7] and check it is unique in [2.18.1] (D-012) → scaffold the standard agent folder (`.claude/`, `configs/`, `scripts/`, `logs/`, `data/`, `docs/`, `tests/` with two empty `tests.config.json` and a runner link `run-tests.system.link.js` next to each, `research/` with an empty `index.json`; D-025) → write its own config [27.2] → write its links file `[agent-name].links.json` [27.3] with the file links its logic needs, plus the default `scripts/relink.system.link.js` (D-031) → run `init.sh` [40], which runs `relink` (its file links + its entries in the parent's `subagents.link/` folders, D-030) → scaffold its `docs/` [46] (README, strategy, changes) → set its route in [11.11] `models.config.json` → write its jobs file `[agent-name].workers.json` [27.4] (at least the main run; its parent sees it through `configs/subagents.link/`, D-030) → test mode → `run-tests` passes [2.11.7] → register in index [2.18] and UI → first run.
  - [2.11.2] `add-worker.md`: check existing workers/data first (index [2.18.2]) → write the script (shared [14.2] or agent-local [30]) → add it as a job to the owning agent's workers file (shared workers: [11.10] `system.workers.json`; otherwise the agent's own, e.g. [27.4]; D-029) with schedule, where it runs, platform and model → mark its output as `on_change` for agents that must restart on it → add the data file link to each reader's links file [27.3]; relink runs on the change (D-031).
  - [2.11.3] `add-platform-or-model.md`: add to [11.11] `models.config.json` → set status (supported/later) → route objects → test run.
  - [2.11.4] `promote-to-live.md`: criteria (incl. all enabled tests passing, `before_promote` tests run; D-025, proposed) → owner approval in UI → funded account → switch mode → monitoring.
  - [2.11.6] `add-account-or-secret.md` (D-023, proposed): owner creates the key/wallet → adds a `KEY=value` line (prefixed per account/platform) to [47.1] `test/.env`, or for live the owner adds it to [47.2] `live/.env` (chmod 600; D-027) → adds metadata to [47.3] → adds the `secret_ref` to [11.1] `accounts` or [11.11] `platforms` (live: owner approval) → adds the key names to that agent's `secret_keys` → test run with test keys → `check-links` passes. Rotation: new file under the same ref, update `rotate_by`, delete the old key at the venue.
  - [2.11.7] `add-or-run-tests.md` (D-025, proposed): pick the level and kind (`agents` for prompt/sub-agent behaviour, `scripts` for code) → write the test file ([test-id].test.md with scenario, fixtures and expected behaviour, or [test-id].test.js|py) → add an entry to that `tests.config.json` (id, target, schedule, owner, `enabled`) → run `node tests/[agents|scripts]/run-tests.system.link.js --id [test-id]` (the link in that test folder) → check the written-back `last_result` and `logs/tests.jsonl` → set `next_action` if it fails. Enable/disable from the UI or by editing `enabled`.
  - [2.11.8] `record-research.md` (D-025, proposed): add an item to the level's `research/index.json` (status `planned`) → create `research/[research-id]-[slug]/README.md` (question, method) → run it, keeping artifacts in that folder (`running`) → write `results_summary` and `decisions` (`done` or `abandoned`) → link what it led to in `related` (new variant, `changes.md`, tests, decision log [2.6]) → the SI sub-agent saves a pointer in its `agent-memory/`.
  - [2.11.9] `add-or-change-link.md` (D-031, proposed): find the file to read (index [2.18]; the links index [16.1] shows who else reads it; prefer a stable `latest.*` output) → add or change one entry in your own links file [27.3]: `to`, `from`, `why`, `required` → relink runs by itself (hook or scheduler watch), or run `node scripts/relink.system.link.js` → check its report: the link exists and points where you expect → if a change to that file should restart your main run, add it to that job's `on_change` [27.4]. To remove a link, delete its entry or set `enabled: false`; relink removes the symlink.
  - [2.11.5] `stop-or-delete-agent.md`: stop → close/flatten positions (live) → archive the agent folder (its own logs/data live there now) → run `relink`: it removes the agent's entries from the parent's `subagents.link/` folders (D-030) and warns every agent whose links file still points at its files (D-031) → mark retired in index [2.18]; the archived folder keeps its docs [46] for history.
- **Writers / readers:** docs agent and system-support agents write them. The create-agent script [14], main domain agents and self-improvement agents follow them.
- **Updated:** when the process changes. Scripts in [14] should match these steps.

### [2.12] `docs/feature-map.md` (proposed; owner request)
- **Purpose:** map each feature/logic area to the folders and files that implement it, so any agent can find where a piece of logic lives and what a change will touch.
- **Outline:** Agent-type legend · one table per feature area (data collection, pre-analysis, subscriptions and triggers, run loop, decision and execution test/live, self-improvement wheel, agent creation, routing, UI, logging and analytics, docs/self-support, safety and risk). Each table has the columns: logic in plain words · files/folders with [n] numbers · owning agent type. It ends with a gaps list (features with no files yet).
- **Writers / readers:** docs agent / system-support agents write it. All agents read it before changing things; self-improvement agents read it to locate what to change; the owner reads it to review.
- **Updated:** whenever a feature or file is added, moved, renamed or removed (keep in sync with [2.13] `file-tree.md`).
- **Draft:** `/mnt/project-files/vision/feature-map.md`.

### [2.13] `docs/file-tree.md` (this document; was [6])
- **Purpose:** the annotated, numbered tree of the whole OS, plus one fully expanded example agent. It is where every folder and file is explained, and it is the basis for going through objects one by one with the owner.
- **Outline:** header (version, how to read, placeholders) · Tree (code block with [n] numbers and inline # comments) · Objects: one section per [n] with purpose, contents, writers/readers, open questions · Changelog.
- **Writers / readers:** docs agent / system-support agents write it after owner answers. The owner reviews it. All agents read it to know where things are; the create-agent logic [2.11.1] follows its example-agent layout.
- **Updated:** whenever a folder or file is added, moved, renamed or removed. It stays in sync with [2.12] `feature-map.md`: every [n] referenced there must exist here. Numbers are never reused, and moved objects keep a stub.
- **Open:** Should a drift check compare it with the real folders automatically?

### [2.14] `docs/data-schemas.md` (owner request)
- **Purpose:** the shape of every JSON/MD file in the system, so workers, agents, scripts and the UI read and write the same format.
- **Outline:** General rules (encoding, timestamps, IDs, file naming, versioning of schemas) · Worker outputs (per worker: path, fields, example) · Sub-agent outputs · Configs ([11.1] `system.config.json` sections, workers files in the [11.10] format (D-029), links files in the [11.13] format and the links index [16.1] (D-031), [11.11], the agent config [27.2]) · Routing ([11.11] `models.config.json`) · Run logs and decision records · Portfolio/positions (once placed) · Index entries [2.18] · **Tests config** `tests.config.json` (D-025): `schema_version`, `level` (agent id), `kind` (agents|scripts), `tests[]` with `id`, `name`, `target` (file under test), `file` (test file), `enabled`, `schedule` (manual | on_change | interval:[x] | before_promote), `owner` (who maintains it), `last_run`, `last_result` (success | fail | error | skipped | never), `last_duration_ms`, `fail_count`, `notes`, `next_action` (what should be done) · **Research index** `research/index.json` (D-025): `schema_version`, `level`, `items[]` with `id`, `slug`, `topic`, `question`, `status` (planned | running | done | abandoned), `started`, `finished`, `ran_by`, `requested_by`, `folder`, `results_summary`, `decisions[]` (`decision`, `by`, `approved_by`, `date`, `decision_ref`), `links[]` (files used/produced), `related` (`variants`, `changes`, `tests`, `research`), `tags` · Owner comments/questions from the UI · MD file templates (run summary, memory note, changes).
- **Writers / readers:** whoever adds or changes a file type updates its schema (system-support, domain or SI agent). Every script, agent and the UI API read it.
- **Updated:** whenever a JSON/MD file type is added or its fields change; a change is recorded in [2.9].
- **Open:** Should schemas also exist as machine-checkable JSON Schema files (e.g. `agents/system/configs/schemas.link/`), with this MD as the readable view?

### [2.15] `docs/flows.md` (owner request)
- **Purpose:** every flow step by step. **Data flows:** how data moves through the system. **User flows:** what the owner does and what happens next.
- **Outline:** *Data flows:* worker → data store → `.link` → agent · sub-agent pre-analysis · trigger (interval / important file change → cancel and restart) · run loop → decision → action (test/live) · logs → UI · self-improvement wheel (analyse → new config → new test agent) · outside-world signals (new model/harness/news) → routing update. *User flows:* create an agent from input · review performance · approve/reject a funded account · stop/delete · comment / ask a question / "do better" · review a proposed change. Each flow has a diagram, the files touched ([n] numbers) and the owning agent type.
- **Writers / readers:** docs agent / system-support agents write it. The owner reads it to review behaviour; agents and the UI build on it.
- **Updated:** whenever a flow changes. It stays consistent with [2.12] feature-map (the same files per feature).

### [2.16] `docs/metrics.md` (owner request)
- **Purpose:** how agents are measured and compared, and the rules for promotion, demotion and retirement.
- **Outline:** Metrics (PnL, win rate, drawdown, calibration, cost per run / token cost, latency, errors; exact set open, vision §6.8) · How each is computed and from which files ([34], [35]) · Comparison rules (same period, same capital, test vs test) · Promotion rules: challenger → champion, test → live candidate (then owner approval, [2.11.4]) · Demotion/retirement rules · Dashboards in the UI that show them.
- **Writers / readers:** the owner sets targets and thresholds; system-support/SI agents propose changes as "pending owner" in [2.6]. SI agents, domain agents and the UI read it.
- **Updated:** when a metric or rule changes (owner decision).

### [2.17] `docs/common/` (owner request: "common things")
- **Purpose:** knowledge shared by every agent, written once and read by all. It replaces the former `agents/docs/architecture.md` [7] and `shared.md` [9].
- **Contents:**
  - [2.17.1] `agent-architecture.md` (was [7]): how an agent works inside: folder parts, run loop, sub-agents, memory, how it gets data.
  - [2.17.2] `shared-mechanics.md` (was [9]): triggers and cancel-and-restart, test/live modes, `.link` symlinks and `relink` (D-031), logging, config merge order.
  - [2.17.3] `common-prompt.md` (proposed): the base prompt every agent's `.claude/CLAUDE.md` ([24.5] and the level equivalents) builds on (v0.1 "common prompt"), including the rule "after editing your links file, run relink" (D-031).
  - [2.17.4] `self-improvement-templates.md` (proposed): templates that SI sub-agents ([10.1.1.1], [19.1.1.2], [21.1.1.1]) use to build a strategy's improvement logic (vision §8).
- **Writers / readers:** system-support agents write; changes to [2.17.3] need owner approval (proposed). All agents read it; agent `CLAUDE.md` files link to it.
- **Updated:** when shared behaviour changes.
- **Resolved (D-017, D-020):** an agent links the individual common docs it needs into its `docs/` [46.1] (e.g. `agent-architecture.link.md`).

### [2.18] `docs/index/` (owner request: "indexes of all things")
- **Purpose:** one index per kind of thing, so the owner, agents and the UI can find anything. It replaces the former catalog [8].
- **Contents (one line per item, with path and [n] type):**
  - [2.18.1] `agents.md`: **the registry of agent names (D-012)**: one row per agent ever created, including retired ones, so names are never reused. Fields: name (unique ID), type (system/domain/strategy level agent, main/variant, support; D-022), domain, strategy, parent, route, mode, status (active/paused/retired), funded yes/no, created date, path (its docs are in `[path]/docs/`). If a JSON registry is chosen, it is the source and this MD is generated from it.
  - [2.18.2] `workers.md`: every job from all workers files (found by scanning `agents/**/configs/*.workers.json`, real files only; D-029/D-030): owner agent, type, schedule, where it runs, platform, model, on/off, output path, readers.
  - [2.18.3] `subagents.md`: every sub-agent (unique name, D-012): level (system/domain/strategy) and path of its `.claude/agents/` file, role (pre-analysis, domain owner, self-improvement), input, output, memory/state path ([16.3]), schedule, route, used by.
  - [2.18.4] `services.md`: every acting service, its test/live mode and account refs (never secrets).
  - [2.18.5] `apps.md`: cloned repos in [43], version, used by.
  - [2.18.6] `models.md`: platforms/models, status (default/supported/later), what routes to them (view of [11.11]).
- **Writers / readers:** create/stop scripts [14] and system-support agents update it on every add/remove. Everyone reads it; the UI lists from it.
- **Updated:** whenever an agent, worker, sub-agent, service, app or model is added, changed or retired.
- **Open:** Hand-written MD, or generated from a JSON registry (e.g. `agents/system/data/registry.json`) that the UI also reads? (Proposed: JSON is the source, MD is generated.)

### [2.19] (retired: central per-agent docs)
- D-017 (supersedes D-003): each agent's docs are now real files in its own `docs/` [46]. The system reaches them through [2.20] `subagents.link/` and the links below it (D-030).

### [2.20] `agents/system/docs/subagents.link/` (D-030; was the `agents/` view of every agent, D-017)
- **Purpose:** one folder link per domain, [2.20.1] `[domain-name]/` → that domain's `docs/` [19.6]. The domain's docs link on to its strategies' ([19.6.1]) and each strategy's to its agents' ([21.6.1]), so all docs can be read from here, level by level ([2.7.4]).
- **Writers / readers:** `relink` [14.1] adds the link from the folder tree (the domain's `init.sh` [19.10] runs it) and removes it after `stop-or-delete`. Read by the UI, the system session, SI sub-agents and the docs agent.

### [3] (moved to [2.2])
- Kept as a number so the other object numbers stay stable.

### [4] `agents/` (D-013)
- **Purpose:** all domains. Every direct child is a domain: `system/` [10], `prediction-market-agents/` [19], `copy-trading-agents/` [42], and more later. **My choice:** a flat `agents/[domain]/` (no `domains/` or `trading-domains/` level), because every child is a domain anyway. The old `trading-domains/` [18] is retired.
- **Shape of a domain:** `.claude/` (domain level, D-016), then agents and (for trading domains) strategy folders. The system domain also holds the shared `configs/`, `scripts/`, `logs/`, `data/` [11]–[16].
- **Belongs elsewhere:** nothing doc-related: shared docs are in the system domain [2], agent docs in each agent [46]; cloned repos → `apps/` [43]; the UI → `trading-ui/` [45]; secrets → repo-root `.secrets/` [47], outside `agents/` (only `secret_ref`s in [11.1] and [11.11]; D-023).
- **Writers / readers:** the create-agent script [14.1] creates agent folders; the domain agent [19.1.5] and SI sub-agents [21.1.1.1] create variants; agents run here.
- **Resolved (D-026):** system-support agents are sub-agents in the system `.claude/agents/` ([10.1.1.2]), not folders; [10.2] is retired.
- **Levels (D-022):** three levels of agents, each a folder with the standard structure [2.7.1]: **system** [10] (manages all domains and system development), **domain** [19] (responsible for its domain), **strategy** [21] (responsible for one concrete strategy). Under a strategy sit its trading variants [23], same structure.

### [5] (merged into [2])
- `agents/docs/` was merged into the shared docs [2] (now `agents/system/docs/`) so docs are not duplicated. [6] → [2.13], [7] → [2.17.1], [8] → [2.18], [9] → [2.17.2].

### [6] (moved to [2.13])
- The file tree covers the whole OS, so it lives in the shared docs [2].

### [7] (moved to [2.17.1])

### [8] (moved to [2.18])
- The catalog became the index: one file per kind of thing.

### [9] (moved to [2.17.2])

### [10] `agents/system/` (system domain, D-013 / D-015)
- **Purpose:** the system domain and the **system-level agent** (D-022): it manages all domains and the development of the system. It has the standard agent folder [2.7.1]; the only difference is that it (a) holds the **shared** files every agent uses and (b), like every level, links to its children: each content folder has `subagents.link/[domain-name]/` → that domain's folder of the same kind ([2.7.4], D-030). Strategies and agents are reached one level further down each time. This replaces the flat views of every agent (D-015).
- **Child links, not copies:** `data/subagents.link/[domain-name]/` etc. are **folder links** to each child's real folder. Copies would duplicate data and drift out of date.
- **Level files (D-022):** [10.1.5] `.claude/CLAUDE.md` is the system manager prompt (oversees domains, system health, system development, answers owner questions about the whole system) · [10.4] `package.json`, [10.5] `requirements.txt` for the shared scripts · [10.6] `init.sh` installs the git hooks and runs relink for the whole project (D-031) · [10.7] `start.sh` starts the scheduler [14.1] (every agent's jobs, D-029) and the system session.
- **Contents:** [10.1] `.claude/` · [2] `docs/` · [11] `configs/` · [10.1.5] `.claude/CLAUDE.md`, [10.4]–[10.7] level files · [14] `scripts/` · [15] `logs/` · [16] `data/` · [10.8] `tests/`, [10.9] `research/` (D-025, [2.7.3]) · [10.2] system-support agents.
- **Belongs here:** anything shared by two or more agents. Anything for one agent stays in that agent's folder (real files). **Promotion rule (proposed):** when a second agent needs an agent-local thing (e.g. [31]), it moves into the matching shared folder here, and agents that need it get a file link to it (D-020).
- **Link mechanics (proposed):**
  - All links use relative paths and always have `.link` in the name ([2.7]).
  - **Agent links are individual file links (D-020, supersedes D-014's folder links for agents):** inside an agent's `configs/`, `scripts/`, `logs/`, `data/`, `docs/`, each link points to **one file** its logic needs, from any folder: system (e.g. [11.1], [14.3], [16.2]), domain or strategy level, or another agent's outputs. Examples: [27.1], [30.1], [34.1], [35.1], [46.1]. There are no `system.link/` folders in agents any more.
  - **Which links (D-031):** each agent lists them in its own links file `configs/[name].links.json` ([11.13] system, [19.2.3] domain, [21.2.3] strategy, [27.3] variant). `create-agent` [14.1] writes the first version; afterwards the agent itself, its SI sub-agent or the owner edit it. A link may come from anywhere under `agents/`: the system, the agent's own domain or strategy, another domain, or another agent (by unique name). The shared `relink` script [14.1] builds every link from these files.
  - **Stable targets (proposed):** producers keep a stable file per output (e.g. `latest.json`, `latest.md`, `latest.log`), so file links do not break when dated files rotate.
  - **No `.claude` links (D-030, for now):** the D-019 down-links [10.1.3]/[10.1.4] and [21.1.3]/[21.1.4] are removed; the domain level never had any (D-021).
  - **Child links (D-030):** every level's content folders hold `subagents.link/[child-name]/` → the child's folder of the same kind: system [11.2.1], [14.4.1], [15.5.1], [16.4.1], [2.20.1], [10.8.3.1], [10.9.3.1] → domains; domain [19.2.2.1], [19.3.1.1], [19.4.1.1], [19.5.1.1], [19.6.1.1], [19.12.3.1], [19.13.3.1] → strategies; strategy [21.2.2.1], [21.3.1.1], [21.4.1.1], [21.5.1.1], [21.6.1.1], [21.12.3.1], [21.13.3.1] → its agents.
  - `relink` [14.1] creates the agent's file links **and** its entries in the parent's `subagents.link/` folders, and removes links nobody wants any more. `init.sh` [40] and `create-agent` call it; after `stop-or-delete` it removes the deleted agent's entries. When it runs is listed in [14.1].
  - **Loops:** agents now hold only file links, so the old `system.link/` → view → agent cycle is gone. The `subagents.link/` entries are folder links, so tools must still **not follow `.link` folders recursively**. `check-links.system.js` [14.1] checks for cycles, broken links, symlinks that neither have `.link` nor sit in a `.link` folder, folder links outside `subagents.link/`, `subagents.link/` entries that are not a direct child's folder of the same kind, any `.claude` link, and any mismatch with [27.3].
  - Agents treat every linked file as **read-only** and write only to their own real files.
- **When shared files change (proposed):** configs are read at the start of each run, so a change applies from the next run of every agent. The kill switch in [11.1] `modes` is checked before every action.
- **Open:** Should changes to shared configs require owner approval before they reach live agents?
- **Resolved (D-020, answers the D-019 follow-up):** agents have no `system.link/` folders. They hold individual file links to exactly what they need, chosen at creation and by self-improvement. The system views stay as they are. `.claude` keeps D-019 (parent → child folder links); D-020 applies only to `configs/`, `scripts/`, `logs/`, `data/`, `docs/`, so the two rules do not overlap. *Later (D-030):* the system views became per-level `subagents.link/` folders and the `.claude` links were removed.

### [10.1] `agents/system/.claude/` (D-008, D-016)
- **Purpose:** the system domain's Claude Code level: system-wide sub-agents [10.1.1] (`[subagent-name].md`, e.g. news-digest pre-analysis) incl. [10.1.1.1] `sys-self-improvement-agent.md` (D-018: improves the system itself: shared scripts, configs, routing, docs; reacts to new models/harnesses), and system-wide skills [10.1.2] (proposed). Sub-agents' models come from [11.11]; their outputs go to [16.3] and their logs to [15.4].
- **Writers / readers:** system-support agents write; domain-owner/SI sub-agents propose.
- **Down-links (removed, D-030):** [10.1.3]/[10.1.4] are gone for now; no level links another level's `.claude/`. System-support roles are sub-agents in this `.claude/agents/` itself ([10.1.1.2], D-026).
- **~~Runs always start from the top~~ (D-019 proposal, withdrawn by D-021):** the domain level no longer links down to strategies, so a session started at `agents/system/` cannot see the strategies and agents.
- **How levels and agents run now (proposed, D-021), the simplest option:** **each level runs in its own folder.**
  - The system session runs at `agents/system/` (system SI, pre-analysis sub-agents).
  - Each domain session runs at its domain folder (domain owner, domain SI).
  - Each strategy session runs at its strategy folder (strategy SI; it reads its agents' files through its `subagents.link/` folders, D-030).
  - A trading agent runs in **its own folder**: `run-agent` [14.1] starts Claude Code there, with its `.claude/CLAUDE.md` [24.5], its own `.claude/` and its file links (D-020).
  - **How an agent gets shared things:** higher-level sub-agents do not run inside agent sessions. They run in their own level's session and write outputs (e.g. `news-digest/latest.md`), which the agent links as data files (D-020, e.g. [35.1] `news-digest.link.md`). Shared rules and knowledge reach it the same way, as doc/config file links.
  - **Not chosen:** copying shared skills into agents at create time, because copies drift and miss self-improvement updates.
- **Full contents (D-024):** standard `.claude/` [2.7.2]: [10.1.5] `CLAUDE.md` (system manager), [10.1.6] `settings.json`, [10.1.7] `settings.local.json`, [10.1.8] `rules/`, [10.1.2] `skills/`, [10.1.9] `commands/`, [10.1.1] `agents/`, [10.1.10] `workflows/`, [10.1.11] `output-styles/`, [10.1.12] `agent-memory/` (incl. the system SI memory, proposed), [10.1.13] `agent-memory-local/`.
- **Resolved (D-030):** the remaining `.claude` down-links are removed for now; a level reads a child's skills or sub-agents by path if it needs them.
- **Open (D-021):** if an agent needs a shared **skill** (not just outputs), may it get an individual file link in its own `.claude/skills/` (D-020 style)? That would be an upward link, which D-019 forbids for `.claude`.

### [10.1.3], [10.1.4], [21.1.3], [21.1.4] (retired: `.claude` down-links, D-030)
- Owner decision D-030: for now no `.claude` folder is linked at any level. The system → domain links [10.1.3]/[10.1.4] and the strategy → agent links [21.1.3]/[21.1.4] (D-019) are removed; the domain → strategy links [19.1.3]/[19.1.4] were already gone (D-021). Levels see each other's files through `subagents.link/` in their content folders instead ([2.7.4]).

### [10.2] (retired: `agents/system/[sys-agent-name]/` folders, D-026)
- Owner decision D-026: system-support work (vision §8 type 1: development, docs, improvement, analysis, research) gets no agent folder under `agents/system/`. Each role is a Claude Code sub-agent file in the system's `.claude/agents/` ([10.1.1.2], e.g. `sys-docs-agent.md`, `sys-improvement-agent.md`), like the domain owner and SI roles (D-018). The system `.claude` has no down-links to them. Shared system files stay in the system agent's own `configs/`, `scripts/`, `logs/`, `data/`, `docs/`. If a support role ever needs its own files and runs, it becomes a normal agent with the standard folder [2.7.1] under its domain.

### [10.1.1.2] `agents/system/.claude/agents/sys-docs-agent.md` (D-026)
- **Purpose:** example system-support sub-agent: writes and maintains the shared docs [2] from owner inputs. Other support roles (development, improvement, analysis, research) are sibling `.md` files here. Model from [11.11]; outputs to [16.3], logs to [15.4].

### [11] `agents/system/configs/` (D-006 as amended by D-014)
- **Purpose:** the shared configs, in JSON (D-005): [11.1] `system.config.json`, [11.10] `system.workers.json` (the system's own jobs, D-029), [11.11] `models.config.json`, [11.13] `system.links.json` (the system's own file links, D-031); plus [11.2] `subagents.link/` with each domain's `configs/` (D-030), which also shows each domain's jobs files by domain.
- **Direction (D-014, supersedes D-006's central per-agent location):** each agent's own config is a **real file in the agent folder** ([27.2]); the agent links the shared config files it needs ([27.1], D-020); the system reaches each domain's configs through [11.2.1], and the strategies' and agents' one `subagents.link/` further down each time (D-030).
- **Not decided (open):** the exact shape of the files, and which settings are common vs individual (to be worked out with example agents).
- **Merge rule (proposed), lowest to highest priority:** global [11.1] → agent [27.2] → owner overrides from the UI [45] (stop, pause, approve).
  - Objects deep-merge by key; arrays and single values are replaced by the higher layer.
  - Jobs come only from each agent's own workers file (D-029: [11.10], [19.2.1], [21.2.1], [27.4]). Routes come from [11.11] unless a job names its model.
  - **Safety exceptions:** risk caps can only be **tightened** by the agent layer. **Live** needs both the global live allowlist and an owner-approved account; an agent can never switch itself to live. The **kill switch** overrides everything and is checked before every action. **Secrets** appear in no config, only references.
  - At run start `run-agent` [14.1] writes the merged result to the agent's logs [34] as `effective-config.json`.
- **Writers / readers:** system-support agents write the shared files; changes to `modes`, `risk` and `accounts` need owner approval (recorded in [2.6]). All agents, scripts and the UI read. Shapes go in [2.14].
- **Numbering:** [11.3]–[11.9] (v0.6 drafts) are retired.

### [11.1] `system.config.json` (D-006; sections proposed)
- **Purpose:** the single place for everything controllable globally, except jobs (each agent's workers file, D-029) and routing [11.11].
- **Sections (proposed outline):**
  - `defaults`: timezone, currency, log level, run timeout, data retention, languages; `by_agent_type` (system/domain/strategy/main/sub/support/SI: allowed actions, memory on/off).
  - `modes`: `default_mode: "test"`, `kill_switch`, per-service test/live, `live_allowlist`.
  - `risk`: hard caps at global (max total live capital, max daily loss, drawdown stop), per-agent (max capital, position %, open positions, orders/hour) and per-venue level. Agents may only tighten these.
  - `schedules`: scheduling defaults for every workers file: time zone, default run intervals per agent type, max concurrent runs, quiet hours, which `run_on` targets are allowed, daily AI cost cap. (Each job's own schedule is in its agent's workers file, D-029.)
  - `triggers`: important/unimportant file patterns, debounce, min time between restarts, max restarts per hour, `on_unimportant: "wait_next_run"`.
  - `accounts`: trading accounts (id, venue, mode, funded, `approved_by_owner`, assigned agent, max capital, `secret_ref`).
  - `notifications`: channels and events → severity (live trade, risk limit hit, agent error, promotion proposed, kill switch).
  - `domains`: per domain (prediction-markets, copy-trading, …): venues, fees, market filters, default workers, tighten-only risk.
- **Writers / readers:** system-support agents; owner approval for `modes`, `risk` and `accounts`. Read by everything.
- **Updated:** when a global setting changes. A section is split out into its own file once it gets long (next candidate: `accounts`).

### [11.10] `system.workers.json` (D-029; was `workers.config.json`, D-007)
- **Purpose:** the system agent's own **jobs**: everything the system runs on a schedule or on demand, such as the shared data collectors [14.2], relinking and link checks, tests, index rebuilds and its sub-agent runs (SI [10.1.1.1], docs [10.1.1.2]). Every other agent has the same file for its own jobs in its `configs/` (domain [19.2.1], strategy [21.2.1], agent [27.4]), all in this format. The system sees each domain's file through [11.2] `subagents.link/` (D-030), and deeper ones one level down at a time.
- **What a job is (D-029):** either a plain **script** (`platform: none`) or an **AI run** on a coding-agent platform: the agent itself (`agent`: its main run, in its own folder), a `subagent`, a `skill`, a `workflow` or a slash `command`.
- **Job fields (proposed):** `id` (unique in the file) · `enabled` (turn off without deleting) · `purpose` · `type` (script | agent | subagent | skill | workflow | command) · `run` (the command for a script; the sub-agent, skill, workflow or command name otherwise) · `schedule` · `timezone` · `run_on` (local | cloud | desktop | github-actions) · `platform` (none | claude-code | cursor | codex) · `model` (`route` = take it from [11.11]) · `effort` · for AI runs: `prompt` (text, or `@path` to a prompt file), `workspace` (the folder it runs in; default the owner agent's folder), `allowed_tools`, `permission_mode`, `max_turns`, `max_cost_usd` · `secret_keys` (local runs only) · `inputs`, `outputs` · `on_change` (paths whose change starts the job; for the main run it cancels and restarts the current run) · `timeout`, `retries`, `concurrency` (skip | queue | restart) · `mode` (test | live; live needs owner approval) · `notify` (never | failure | always). The file's `defaults` fill in anything a job leaves out.
- **`schedule` (proposed, one short string):** `every 15m` / `every 6h` / `every 1d` · `cron 0 22 * * 1-5` · `once 2026-11-03 20:00` (runs one time, then shows as done) · `after [job-id]` (when that job succeeds) · `manual` (only from the UI or a command). Time zone from the job, else the file's `defaults`, else [11.1] `defaults.timezone`.
- **Where it runs (`run_on`, proposed):** `local` (default): headless on the machine that runs the scheduler [14.1], with the local files, links and test secrets. `cloud`: the platform's own cloud (Claude Code routines, Codex cloud, Cursor background agents): a fresh copy of the repo, no local files, no secrets; Claude Code routines run at most hourly. `desktop`: a Claude desktop scheduled task; it runs only while the app is open. `github-actions`: a scheduled workflow in the repo. The scheduler runs `local` jobs itself and registers the others on their platform.
- **How AI runs start (proposed):** `run-job` [14.1] builds the platform's headless command in the job's `workspace`: Claude Code `claude -p`, Cursor `cursor-agent -p`, Codex `codex exec`, with the job's model, prompt, tools, permission mode and turn limit. Adding a platform later means adding one command template to `run-job`.
- **Rules (proposed):** a `live` job needs owner approval and a live-allowed agent ([11.1] `modes`). `cloud`, `desktop` and `github-actions` jobs get no `secret_keys` and cannot trade. To pause a job, set `enabled: false`; never delete it to pause. Runtime state (last run, result, next run, fail count) is not written here: the scheduler keeps it in [16.1] `scheduler-state.json` and logs every run to the owner agent's `logs/jobs/[job-id]/`, so this file changes only when someone changes a job.
- **Writers / readers:** the owner (UI [45]: turn on/off, change when, where, platform, model); the owner agent's domain or SI sub-agents propose changes. Read by the scheduler and `run-job` [14.1], the index [2.18.2] and the UI.
- **Updated:** whenever a job is added, changed, rescheduled, turned off or removed.
- **Open:** Which machine runs the `local` scheduler: the owner's computer or a small always-on server? Should the scheduler create cloud routines by itself, or should the owner confirm each one?

### [11.11] `models.config.json` (D-011)
- **Purpose:** which platform/model/effort each agent, sub-agent and AI-using worker uses, plus the list of platforms and their status (vision §9).
- **Key fields (proposed):** `{ "platforms": { "claude-code": { "status": "default", "secret_ref" }, "cursor": { "status": "supported" }, "openrouter": { "status": "supported-not-connected" }, "codex": { "status": "later" }, "kimi": { "status": "later" } }, "models": { "opus-5.5": { "platform": "claude-code", "effort": "xhigh" }, "sonnet-5.5": {...}, "composer-2.5": {...} }, "defaults_by_type": { "main": "opus-5.5", "domain": "opus-5.5", "si": "opus-5.5", "sub": "composer-2.5", "worker": "composer-2.5", "support": "sonnet-5.5" }, "routes": { "[agent|subagent|worker name]": "[model]" } }`
- **Rule (proposed):** the route is `routes[name]`, else `defaults_by_type[type]`. A job in a workers file may name its own model instead (D-029); `model: "route"` uses this file. It must name a platform whose status allows use. The platform/model in an agent's name must match its route (check in [14.1]).
- **Writers / readers:** system-support agents write; SI agents propose route changes (a route change = a new test variant). The run scripts, the index [2.18.6] and the UI read it.
- **Updated:** when a model/platform is added or its status changes ([2.11.3]), or a route changes.

### [11.13] `system.links.json` (D-031)
- **Purpose:** the system agent's own file links, and the **format every level uses**. Every agent has the same file in its `configs/`: domain [19.2.3], strategy [21.2.3], variant [27.3] (`[name]` as for the workers file: `system`, the domain name, or the agent name). For each link it says which file, from where, where it appears and why. The system's own list is short (e.g. a domain's market catalog for the system dashboard); most links sit in trading agents.
- **Fields (proposed):** `schema_version` · `agent` · `links[]`, one entry per link: `enabled` (off = relink removes the symlink but keeps the entry) · `to` (where the link appears, inside the agent's own `configs/`, `scripts/`, `logs/`, `data/`, `docs/`, `tests/` or `research/`; the name carries `.link`, e.g. `data/whale-signals.link.json`) · `from` (the file it points at, see below) · `why` · `required` (true: a missing target is an error and the agent's main run does not start; false: a warning, and no link is made until the file exists) · `added_by` (create-agent, the agent itself, its SI sub-agent, owner) · `added` (date).
- **`from` (proposed):** a path under `agents/`, or a short form: `@system/…` (the system folder), `@domain/…` (the agent's own domain), `@strategy/…` (its own strategy), `@[name]/…` (any domain or agent by its unique name, D-012, looked up in the registry [2.18.1], so the entry keeps working if that folder moves). Examples: `@system/data/workers/polymarket-prices/latest.json`, `@domain/data/markets-catalog/latest.json`, `@copy-trading-agents/data/top-traders/latest.json` (another domain), `@ct-whale-follow-v3-agent-composer25-live/data/whale-signals/latest.json` (an agent in another domain).
- **Rules (proposed):** file links only (D-020): `from` is one real file; if it is itself a link, relink points at the real file behind it, so there are no chains. Never anything in `.secrets/` (D-023) or in any `.claude/` (D-030). `to` is always inside the agent's own folders, never inside `subagents.link/`. Links are relative symlinks and read-only for the agent. Child links (`subagents.link/`, D-030) are **not** listed here: relink builds them from the folder tree.
- **Writers / readers:** create-agent writes the first version; then the agent itself, its SI sub-agent and the owner (UI) edit it. `relink` and `check-links` [14.1] read it; the links index [16.1] and the UI show who links what.
- **Open:** Commit the symlinks themselves to git (a fresh clone works at once; the pre-commit hook keeps them in step), or git-ignore them and let relink rebuild them after every clone and pull? Proposed: commit them. May an agent link any file of another agent, or only files that agent lists as `outputs` of its jobs (a public contract)?

### [11.12] (retired: `configs/workers/` jobs view; merged into [11.2], D-030)
- D-030: every level's `configs/` has `subagents.link/[child]/`, so the system sees each domain's configs, including its workers file, in [11.2.1], and the strategies' and agents' files one level further down each time. The scheduler finds every workers file by scanning `agents/**/configs/*.workers.json` (real files only).

### [11.2] `agents/system/configs/subagents.link/` (D-030)
- **Purpose:** one folder link per domain, [11.2.1] `[domain-name]/` → that domain's `configs/` [19.2], including its workers file [19.2.1] and its own `subagents.link/` [19.2.2] to its strategies. The system, the UI and SI agents read configs and jobs domain by domain from here ([2.7.4]).
- **Was:** the central home of per-agent config files (D-006 direction, superseded by D-014), then a flat view of every agent's configs (D-015), then also the jobs view [11.12] (D-029). D-030 replaced both with this folder.

### [12] (moved: workers are scripts)
- D-007: shared worker scripts are in [14.2]. Their jobs are in [11.10] `system.workers.json` (D-029).

### [13] (moved to [10.1.1])
- D-008: sub-agents are Claude Code subagents in `.claude/agents/`.

### [14] `agents/system/scripts/` (D-007, D-015)
- **Purpose:** the shared scripts (JS/TS or Python) plus [14.4] `subagents.link/` to each domain's scripts (D-030).
- **Naming (proposed):** kind by sub-folder and by suffix `[name].[kind].[ext]`, where kind is `worker`, `decision` or `system`.
- **Contents (proposed):**
  - [14.1] `system/`: `*.system.js|py`, e.g. `create-agent` (**uniqueness check point for D-012**: validates the name format [2.7], rejects any name already in the registry [2.18.1] including retired ones, reserves the name, then scaffolds the folder and runs `init.sh`), `run-agent` (starts Claude Code in the agent's own folder (proposed, D-021), merges config, writes `effective-config.json`), `scheduler` (D-029; was `trigger-watcher`: finds every workers file by scanning `agents/**/configs/*.workers.json` (real files only, D-030), runs due jobs, watches `on_change` files with cancel-and-restart for main runs, registers cloud/desktop/GitHub jobs on their platform, keeps state in [16.1] `scheduler-state.json`, logs to [15.1]), `run-job` (D-029: runs one job: the script, or the platform's headless command in the job's workspace with its model, prompt and tools; passes only the job's `secret_keys` via `load-secret`; logs to the owner agent's `logs/jobs/[job-id]/`), `relink` (D-031: builds every link in the project from the links files ([11.13] format, found by scanning `agents/**/configs/*.links.json`, real files only) plus the child links from the folder tree (D-030): creates missing links, fixes changed ones, removes `.link` symlinks that no file lists, then runs the `check-links` rules; writes the links index [16.1] `links.index.json` (every link: owner agent, `to`, real target, required, status) and logs each change to [15.1]; re-runnable and safe at any time, one run at a time (lock). Options: `--agent [name]` (one agent; what `scripts/relink.system.link.js` presets when called from an agent folder), `--changed [files]` / `--staged` (works out which agents the changed files affect: a links file, an added, removed or moved agent folder, or a moved or deleted link target, using the links index), `--check` (report only; exit 1 if anything is wrong). **When it runs:** (1) a links file changes: the `relink` job in [11.10] watches `agents/**/configs/*.links.json` (`on_change`) and runs `--changed`, plus one full run a day; (2) review time: git hooks installed by the system `init.sh` [10.6]: `pre-commit` runs `--staged` and blocks the commit if a required link is broken, `post-merge` and `post-checkout` run `--changed` after a pull or branch switch, and the owner approving a change in the UI runs it too; (3) the agent itself: after editing its links file it runs `node scripts/relink.system.link.js` (rule in [2.17.3]), and a `PostToolUse` hook in its `.claude/settings.json` does it automatically ([2.7.2]); (4) `create-agent`, `init.sh` [40] and `stop-or-delete`), `check-links` (run by relink after every change and hourly on its own: broken links, cycles, symlinks without `.link` outside a `.link` folder, any `.claude` link (none for now, D-030), `subagents.link/` entries that are not a direct child's folder of the same kind, and any link or copy whose target is inside [47] `.secrets/` (D-023: never allowed)), `load-secret` (D-023: resolves a `secret_ref` for the calling script at execution time, only if that agent's config references it and, for `live/`, only if the agent is live-allowed with an owner-approved account; returns the value to the process only, never to logs or the LLM), `notifier`, `run-tests` (D-025: runs a level's tests from its `tests.config.json` files, writes results back and to that level's `logs/tests.jsonl`; linked into each level's `scripts/` as `run-tests.system.link.js` and into each `tests/agents/` and `tests/scripts/` folder as `run-tests.system.link.js`, which presets the kind and that folder's config; agent tests run Claude Code headless in test mode with no secrets, see [2.7.3]).
  - [14.2] `workers/`: `*.worker.py|js`, shared data collectors; each runs as a job in [11.10] `system.workers.json` (D-029).
  - [14.3] `decisions/`: `*.decision.js|py`, shared buy/sell and risk-check building blocks that agents' decision scripts [33] call.
  - [14.4] `subagents.link/` (D-030): [14.4.1] `[domain-name]/` → that domain's `scripts/` [19.3].
- **Writers / readers:** system-support agents write the shared scripts; domain/SI agents propose. Agents link the individual scripts they need ([30.1], D-020).
- **Scheduler (proposed, D-029):** one central `scheduler` process for all agents, started by [10.7] and kept alive by the OS (launchd/systemd); agents' `start.sh` only does one run. Where it runs is open in [11.10].

### [15] `agents/system/logs/` (D-009 as amended by D-014 / D-015)
- **Purpose:** shared logs by source, plus [15.5] `subagents.link/` to each domain's logs (D-030); the UI starts here and goes down level by level.
- **Contents:** [15.1] `system/` (scheduler, triggers, relink and link checks, errors, costs) · [15.2] `services/[service]/` · [15.3] `workers/[worker]/` (shared workers) · [15.4] `subagents/[subagent]/` · [15.5] `subagents.link/` (D-030): [15.5.1] `[domain-name]/` → that domain's `logs/` [19.4].
- **Agent side:** each agent's own logs are real files in its `logs/` [34], and it links only the shared log files it needs ([34.1], D-020; read-only). This replaces the v0.8 "agent logs central, only own logs linked" default.
- **Open:** Log format (JSONL + MD run summary?) and retention?

### [16] `agents/system/data/` (D-010 as amended by D-014 / D-015)
- **Purpose:** shared data by source, plus [16.4] `subagents.link/` to each domain's data (D-030).
- **Contents:** [16.1] `system/` (registry, run state, read cursors, `scheduler-state.json` with every job's last run, result and next run, D-029; `links.index.json` with every link in the project: owner agent, where it appears, real target, required, status, written by relink, D-031) · [16.2] `workers/[worker]/` (shared workers) · [16.3] `subagents/[subagent]/` · [16.4] `subagents.link/` (D-030): [16.4.1] `[domain-name]/` → that domain's `data/` [19.5].
- **Agent side:** own data is real files in [35]; shared data (e.g. subscribed workers' outputs) is linked file by file ([35.1], D-020). This replaces the per-worker links [36] and the central own-data link [36.1].
- **Open:** How is "new since last run" tracked: file timestamps, or a per-agent cursor in [16.1] (vision §5.2)?

### [17] (moved to [11.11])
- D-011: routing and platforms are in [11.11] `models.config.json`.

### [18] (retired: `trading-domains/`)
- D-013: domains sit directly under `agents/`, and `system/` is one of them.

### [19] `agents/prediction-market-agents/`
- **Purpose:** prediction-market domain (Polymarket first) and the **domain-level agent** (D-022), responsible for its domain. It has the standard agent folder [2.7.1]: [19.1] `.claude/`, [19.2] `configs/`, [19.3] `scripts/`, [19.4] `logs/`, [19.5] `data/`, [19.6] `docs/`, [19.1.5] `.claude/CLAUDE.md`, [19.8] `package.json`, [19.9] `requirements.txt`, [19.10] `init.sh`, [19.11] `start.sh`, [19.12] `tests/`, [19.13] `research/` (D-025, [2.7.3]).
- **[19.1.5] `.claude/CLAUDE.md` = the domain owner (D-022 reconciles D-018):** the domain's own prompt now carries the domain-owner role (strategies, health, Q&A, owner comments). The separate sub-agent file `pm-domain-owner-agent.md` [19.1.1.1] is retired. The domain SI sub-agent [19.1.1.2] stays in `.claude/agents/`.
- **[19.11] `start.sh`:** starts the domain session in this folder (as the `domain-session` job in [19.2.1], D-029, and on owner questions from the UI).
- **Contents:** [19.1] `.claude/` (domain level, D-016): [19.1.1] `agents/` (domain sub-agents) and [19.1.2] `skills/` (domain skills, e.g. Polymarket API usage). No `.claude` links in or out (D-021, D-030). Its content folders link down to its strategies through `subagents.link/` ([19.2.2], [19.3.1], [19.4.1], [19.5.1], [19.6.1], [19.12.3], [19.13.3]; D-030), and the system links down to them ([11.2.1], [14.4.1], [15.5.1], [16.4.1], [2.20.1], [10.8.3.1], [10.9.3.1]). Also [21] strategies. Domain settings (venues, fees, filters) are in [11.1] `domains`. There is no separate domain-agent folder any more (D-018).
- **Open:** Does it contain only Polymarket, or other venues (Kalshi, etc.) too?

### [19.2.1] `prediction-market-agents.workers.json` (D-029)
- **Purpose:** the domain agent's jobs in the [11.10] format, e.g. the domain session (`agent`, every 4h), the domain SI sub-agent [19.1.1.2] (`subagent`, nightly), domain-wide Polymarket collectors (`script`) and one-off checks on special dates (`once`). The system sees it through [11.2.1] (D-030).

### [19.2.3] `prediction-market-agents.links.json` (D-031)
- **Purpose:** the domain agent's file links in the [11.13] format, e.g. the system's `polymarket-prices` output for the domain session (`@system/data/workers/polymarket-prices/latest.json`) or another domain's data it wants to compare against. The system sees it through [11.2.1] (D-030).

### [19.3.2] `relink.system.link.js` (D-031)
- **Purpose:** file link to the shared `relink` [14.1]. Run from here it relinks only this agent: its file links from [19.2.3] and its entry in the system's `subagents.link/` folders. Every level has one ([21.3.2], [30.3]); the system runs [14.1] directly.

### [19.2.2], [19.3.1], [19.4.1], [19.5.1], [19.6.1], [19.12.3], [19.13.3] `subagents.link/` (domain level, D-030)
- **Purpose:** in each of the domain's content folders, one folder link per strategy agent, named after the strategy's folder ([19.2.2.1], [19.3.1.1], [19.4.1.1], [19.5.1.1], [19.6.1.1], [19.12.3.1], [19.13.3.1] `[agent-name]/`), pointing at that strategy's folder of the same kind ([21.2], [21.3], [21.4], [21.5], [21.6], [21.12], [21.13]). The domain session and the domain SI read their strategies' configs, jobs, logs, data, docs, tests and research here ([2.7.4]).
- **Built by:** `relink` [14.1] from the folder tree (the strategy's `init.sh` [21.10] runs it); removed by relink after `stop-or-delete` [2.11.5]. Read-only for the domain.

### [19.1.3], [19.1.4] (retired: domain → strategy `.claude` links)
- D-021 (owner: no links from the domain level to strategies' agents and skills). The domain session runs at the domain folder with its own sub-agents only.

### [19.1.1.1] (retired: `pm-domain-owner-agent.md`)
- D-022: the domain owner role moved into the domain's own [19.1.5] `.claude/CLAUDE.md`, since the domain folder is now an agent itself.

### [19.1.1.2] `pm-self-improvement-agent.md` (D-018; proposed)
- **Purpose:** self-improvement at domain scope: compares strategies and their variants across the domain, proposes new strategies/variants, and spots domain-wide issues.
- **Memory / state (proposed, D-024 updates D-022):** memory in [19.1.12] `.claude/agent-memory/pm-self-improvement-agent/MEMORY.md` (`memory: project`); research in [19.13] `research/` (D-025); logs in [19.4]. The system sees them through its `subagents.link/` folders (D-030).

### [20] (retired: `main-domain-agents/`)
- D-018: the domain owner became the sub-agent [19.1.1.1]; D-022 then moved the role into the domain's own [19.1.5] `.claude/CLAUDE.md`.

### [21] `strategy-1-agent/`
- **Purpose:** one strategy family and the **strategy-level agent** (D-022), responsible for one concrete strategy. It has the standard agent folder [2.7.1]: [21.1] `.claude/`, [21.2] `configs/`, [21.3] `scripts/`, [21.4] `logs/`, [21.5] `data/`, [21.6] `docs/` (incl. the strategy definition), [21.1.5] `.claude/CLAUDE.md` (strategy manager prompt: runs and compares its variants, coordinates its SI sub-agent), [21.8] `package.json`, [21.9] `requirements.txt`, [21.10] `init.sh`, [21.11] `start.sh` (starts the strategy session), [21.12] `tests/`, [21.13] `research/` (D-025, [2.7.3]). It holds its strategy-level Claude Code [21.1] ([21.1.1] strategy sub-agents incl. the SI sub-agent [21.1.1.1]; [21.1.2] strategy skills; D-016; no `.claude` links, D-030) and all its variants [23]. Its content folders link to its trading agents through `subagents.link/` ([21.2.2], [21.3.1], [21.4.1], [21.5.1], [21.6.1], [21.12.3], [21.13.3]; D-030).
- **Open:** Should the folder carry a real strategy name (e.g. `market-making/`)? Where is the strategy definition itself (template) stored: [21.1.2] as a skill, or in [21.6] `docs/` (proposed)?

### [21.2.1] `strategy-1-agent.workers.json` (D-029)
- **Purpose:** the strategy agent's jobs in the [11.10] format, e.g. the strategy session that compares its variants (`agent`, daily) and its SI sub-agent [21.1.1.1] (`subagent`, nightly). The domain sees it through [19.2.2.1] (D-030).

### [21.2.3] `strategy-1-agent.links.json` (D-031)
- **Purpose:** the strategy agent's file links in the [11.13] format, e.g. the domain's market catalog (`@domain/data/markets-catalog/latest.json`) to compare variants market by market. The domain sees it through [19.2.2.1] (D-030).

### [21.3.2] `relink.system.link.js` (D-031)
- **Purpose:** the same link as [19.3.2]: run from here it relinks only the strategy agent (its file links from [21.2.3] and its entry in the domain's `subagents.link/` folders).

### [21.2.2], [21.3.1], [21.4.1], [21.5.1], [21.6.1], [21.12.3], [21.13.3] `subagents.link/` (strategy level, D-030)
- **Purpose:** in each of the strategy's content folders, one folder link per trading agent (variant), named after the agent ([21.2.2.1], [21.3.1.1], [21.4.1.1], [21.5.1.1], [21.6.1.1], [21.12.3.1], [21.13.3.1] `[agent-name]/`), pointing at that agent's folder of the same kind ([27], [30], [34], [35], [46], [49], [50]). The strategy session and its SI sub-agent compare variants from here ([2.7.4]).
- **Built by:** `relink` [14.1] from the folder tree (the agent's `init.sh` [40] runs it at creation); removed by relink after `stop-or-delete` [2.11.5]. Read-only for the strategy.

### [21.1.1.1] `pm-strategy-1-self-improvement-agent.md` (D-018; was [22])
- **Purpose:** self-improvement at strategy scope, as a Claude Code sub-agent in the strategy's `.claude/agents/`. It runs from time to time, reads the variants' logs/data/docs (through the strategy's own `subagents.link/` folders [21.4.1], [21.5.1], [21.6.1], D-030), past research ([21.13], variants' [50]), outside news and owner comments, then creates new test variants via create-agent [2.11.1]. It records each investigation in [21.13] `research/` and adds or runs tests ([21.12], variants' [49]) for what it changes (D-025). Goal: fast, cheap, efficient, simple, understandable, profitable; fix bugs; test. Templates come from [2.17.4].
- **Levels (D-018):** every `.claude/` level has its own SI sub-agent, scoped to that level: system [10.1.1.1], domain [19.1.1.2], strategy [21.1.1.1].
- **Runs (proposed):** as the `strategy-si` job (`type: subagent`) in the strategy's workers file [21.2.1] (D-029); defaults from [11.1] `schedules`. Model from the job, else [11.11].
- **Memory / state (proposed, D-024 updates D-022):** memory in [21.1.12] `.claude/agent-memory/pm-strategy-1-self-improvement-agent/MEMORY.md` (`memory: project`); research in [21.13] `research/` (D-025); `changes.md` (cross-variant history) in [21.5] `data/`; logs in [21.4]. Each variant's own change record stays in its [46] `changes.md`.
- **Open:** Can it retire variants or only create them?

### [22] (retired: `pm-strategy-1-self-improvement-agent/` folder)
- D-018: now the strategy-level sub-agent [21.1.1.1]; its memory moved to [16.3] (proposed).

### [23] `pm-momentum-v1-agent-opus55-test/` (example; renamed per D-012)
- **Purpose:** one main agent = one harness/platform/model + mode. It runs one run at a time and makes decisions.
- **Shape (D-014, D-022):** the standard agent folder [2.7.1]; every agent has the same folders: `.claude/` [24], `configs/` [27], `scripts/` [30], `logs/` [34], `data/` [35], `docs/` [46], `tests/` [49], `research/` [50] (D-025), each with its own real files plus individual file links to what its logic needs (D-020); plus `.claude/CLAUDE.md` [24.5] (D-024), `package.json`, `requirements.txt`, `init.sh`, `start.sh`.
- **Naming:** a globally unique name that is its ID everywhere (D-012). Format per [2.7]: `[domain]-[modification]-v[N]-agent-[platform-model]-[test|live]` (proposed).
- **Resolved (proposed):** switching test → live creates a new agent (new unique name `…-live`, `parent` = this one); names are never changed.

### [24] `.claude/` (agent level)
- **Full contents (D-024):** standard `.claude/` [2.7.2]: [24.5] `CLAUDE.md`, [24.6] `settings.json`, [24.7] `settings.local.json`, [24.8] `rules/`, [25] `skills/`, [24.9] `commands/`, [26] `agents/`, [24.10] `workflows/`, [24.11] `output-styles/`, [24.12] `agent-memory/`, [24.13] `agent-memory-local/`. Same pattern at [19.1.5]–[19.1.13] and [21.1.5]–[21.1.13].
- **Purpose:** the agent's own Claude Code config: its own skills [25] and sub-agents [26] only. **No `.claude` links** in or out (D-030, for now).
- **How it runs (proposed, D-021):** `run-agent` starts Claude Code in this agent's own folder. It uses its own skills/sub-agents plus its file links (D-020). Outputs of system/domain/strategy sub-agents reach it as linked data files (see [10.1]).
- **Open:** What does a Cursor-routed variant use instead (`.cursor/`)?

### [25] `.claude/skills/`
- **Purpose:** agent-specific skills (real files). Not linked from anywhere (D-030).
- **Open:** Which skills should be common to every agent (and so live at system level [10.1.2])?

### [25.1], [25.2], [25.3] (retired: upward skill links)
- D-019: replaced by parent → child links [10.1.4], [21.1.4] ([19.1.4] later retired by D-021; the rest removed by D-030).

### [26] `.claude/agents/`
- **Purpose:** the agent's own Claude Code sub-agents (D-008; real files, later). Not linked from anywhere (D-030).

### [26.1], [26.2], [26.3] (retired: upward sub-agent links)
- D-019: replaced by parent → child links [10.1.3], [21.1.3] ([19.1.3] later retired by D-021; the rest removed by D-030).

### [27] `configs/` (real folder; was `config.link.json`)
- **Purpose:** the agent's configs (D-014). [27.2] `[agent-name].config.json` is the agent's own config; [27.4] `[agent-name].workers.json` is its jobs file (D-029); [27.3] `[agent-name].links.json` is its links file (D-031); [27.1] are file links to the shared config files it needs (e.g. `system.config.link.json`, `models.config.link.json`; D-020). Its strategy sees this folder through [21.2.2.1] (D-030).
- **[27.2] sections (proposed, shape open):** `agent` (name, type, domain, strategy, parent) · `mode` (test/live request; live still needs owner approval) · `capital_and_risk` (tighten-only) · `strategy` (strategy-specific parameters). No `route`: routes live in [11.11].
- **Writers / readers:** create-agent [14.1] scaffolds it; the SI sub-agent [21.1.1.1] and the domain agent [19.1.5] write new variants' configs; the agent itself reads it (write access open). The UI shows and compares configs via [11.2].
- **Updated:** on creation and on each tested change (a changed config = a new variant, recorded in [46] `changes.md`).
- **Open:** Which settings are individual vs common (to be decided with example agents)? May the agent edit its own config?

### [27.3] `pm-momentum-v1-agent-opus55-test.links.json` (D-031; was the `links` section of [27.2], D-020)
- **Purpose:** every file link this agent wants, in the [11.13] format: which file, from where (the system, its domain or strategy, another domain, another agent), where it appears in its own folders, and why. `relink` [14.1] builds the links from it and `check-links` verifies them.
- **Example links:** `configs/system.config.link.json` ← `@system/configs/system.config.json` · `data/polymarket-prices.link.json` ← `@system/data/workers/polymarket-prices/latest.json` · `data/markets-catalog.link.json` ← `@domain/data/markets-catalog/latest.json` · `data/whale-signals.link.json` ← `@ct-whale-follow-v3-agent-composer25-live/data/whale-signals/latest.json` (an agent in another domain) · `scripts/risk-check.decision.link.js` ← `@system/scripts/decisions/risk-check.decision.js` · `scripts/relink.system.link.js` ← `@system/scripts/system/relink.system.js`.
- **Writers:** `create-agent` [14.1] at creation; then the agent itself (it reruns relink after each edit, D-031), its strategy SI sub-agent [21.1.1.1] and the owner. Reading a shared worker's output adds the matching data link here.
- **Change log (proposed):** each added (`+ to <- from: why`) or removed (`- to: why`) link is written to [46] `changes.md` under `Links`.
- **Open:** Is a link change a new variant (D-012), or may small additions (one more data file) happen in place? D-031 lets the agent edit its own file; whether that bumps `v[N]` is still open.

### [27.4] `pm-momentum-v1-agent-opus55-test.workers.json` (D-029)
- **Purpose:** the trading agent's jobs in the [11.10] format: its main run (`agent`, e.g. every 15m, restarted when an important data link changes via `on_change`; replaces [28]), its own worker [31] (`script`), and one-off jobs on special dates (`once`, e.g. an hour before a market resolves). Its strategy sees it through [21.2.2.1] (D-030).
- **Rule (proposed):** a change to a job's logic (prompt, model, tools, inputs) is a config change and makes a new variant (D-012); the owner turning a job on or off or moving its time does not.

### [28] (moved to [27.4]: the agent's workers file)
- D-029: the agent's jobs, its run interval and the files whose change restarts a run (`on_change`, was the important-files list) are in its own workers file [27.4]. Global defaults stay in [11.1] `schedules` and `triggers`.

### [29] (retired: `docs.link/`)
- D-017: replaced by the agent's real `docs/` folder [46].

### [30] `scripts/` (real folder)
- **Purpose:** the agent's own scripts (D-007) in JS/TS or Python; kind by suffix `.worker.`, `.decision.`, `.system.`. [30.1] are file links to the shared scripts it uses, e.g. `risk-check.decision.link.js` → [14.3] (D-020); [30.3] `relink.system.link.js` → [14.1] relink (D-031). Its strategy sees this folder through [21.3.1.1] (D-030).
- **Rule (proposed):** own scripts write logs to the agent's [34] and data to its [35.2]; an own worker runs as a job in the agent's workers file [27.4] (D-029).
- **Open:** Are there other kinds besides worker/decision/system?

### [30.2] (retired)
- `workers.link/` is no longer needed: shared workers are reached via [30.1].

### [30.3] `relink.system.link.js` (D-031)
- **Purpose:** file link to the shared `relink` [14.1]. Called from here it presets `--agent` to this agent, so `node scripts/relink.system.link.js` rebuilds only this agent's links and its entries in its strategy's `subagents.link/`. The agent runs it after editing [27.3]; the hook in its `settings.json` [24.6] runs it too. Same link at every level: [19.3.2], [21.3.2].

### [31] `get-polymarket-data.worker.py`
- **Purpose:** agent-local worker fetching Polymarket data. It runs as the `get-polymarket-data` job in [27.4] (D-029); output → [35.2] `data/get-polymarket-data/`, logs → [34].
- **Open:** It moves to [14.2] when a second agent needs it (promotion rule [10]). Should that be automatic?

### [32] `clean-data.system.js`
- **Purpose:** clean/normalise raw data before the agent reads it.
- **Open:** Is it agent-local, or should it move to [14.1] as a shared system script?

### [33] `make-buy.decision.js`
- **Purpose:** decision/action step (buy/sell); reads the mode (test/live) from config; may call shared blocks in [14.3] via [30.1].
- **Open:** Is the decision made by code, the LLM, or both (the LLM proposes, code enforces risk limits, vision §5.3)?

### [34] `logs/` (real folder; was `logs.link/`)
- **Purpose:** the agent's own logs: per-run inputs used, reasoning, decisions, actions, cost, `effective-config.json`. [34.1] are file links to shared log files it needs, only if needed (e.g. its data worker's `latest.log`; D-020). Its strategy (and so the UI, level by level) sees this folder through [21.4.1.1] (D-030).
- **Open:** Should it be one JSONL decision log plus an MD run summary per run?

### [35] `data/` (real folder)
- **Purpose:** the agent's own data: [35.2] `[worker-or-source]/`, one folder per producer (own workers, own outputs, decisions). [35.1] are file links to the data files it uses: shared worker outputs [16.2], sub-agent outputs [16.3], or another agent's outputs (D-020). Its strategy sees this folder through [21.5.1.1] (D-030).
- **Open:** Where are portfolio/positions stored (in [35.2], or a ledger, vision §5.4)?

### [36], [36.1], [36.2] (retired)
- The per-worker data links, the central own-data link and the sub-agent data link are replaced by individual file links [35.1] (D-020) and real own data in [35.2] (D-014).

### [46] `docs/` (agent's own docs, real folder; D-017)
- **Purpose:** the agent's own docs, in its folder like its configs/scripts/logs/data.
- **Contents:** [46.2] `README.md` (what it is, parent variant, route, mode) · `strategy.md` · `changes.md` (exactly what differs from its parent / what is being tested) · `decisions.md` (notable decisions summary; raw decisions stay in [34]) · `notes.md` (owner comments and answers). [46.1] are file links to the shared docs it needs (e.g. `safety.link.md`, `agent-architecture.link.md`; D-020).
- **Writers / readers:** create-agent [14.1] scaffolds it; the agent itself, its strategy SI sub-agent [21.1.1.1] and the domain agent [19.1.5] update it. The owner and the UI read it here, or from its strategy through [21.6.1.1] (D-030).
- **Updated:** on creation, on every change tested, and when the owner comments.
- **Resolved:** the "what changed in this variant" record is `changes.md` here; the strategy SI sub-agent keeps the cross-variant history in [21.5] `data/` (D-022/D-025).
- **Open:** Should the agent be allowed to edit its own docs, or only its SI/domain agent?

### [37] (moved to [24.5]: `CLAUDE.md` now sits inside `.claude/`, D-024)
- Level equivalents moved the same way: [10.3] → [10.1.5], [19.7] → [19.1.5], [21.7] → [21.1.5].

### [24.5] `.claude/CLAUDE.md` (trading agent prompt; D-024)
- **Purpose:** the main agent's instructions: strategy, run loop, allowed actions, links to config/docs. Every level has one: [10.1.5] system manager, [19.1.5] domain owner, [21.1.5] strategy manager, [24.5] trading agent.
- **Open:** Is it composed from the common prompt [2.17.3] plus an agent prompt (v0.1 idea): by `@import`/link, or copied in at creation?

### [38] `package.json`
- **Purpose:** JS/TS dependencies and npm scripts (`start`, `test`).
- **Open:** Should dependencies be per agent or shared via a workspace at the root?

### [39] `requirements.txt`
- **Purpose:** Python dependencies.
- **Open:** Should each agent have its own venv, or share one?

### [40] `init.sh` (every level has one: [10.6], [19.10], [21.10], [40])
- **Purpose:** setup, re-runnable: install deps, then run `relink --agent [self]` [14.1] (D-031), which builds the agent's file links from its links file [27.3] ([27.1], [30.1], [30.3], [34.1], [35.1], [46.1]; D-020) and its entry in each of its parent's `subagents.link/` folders (D-030: a trading agent in its strategy's [21.2.2.1]–[21.13.3.1], a strategy in its domain's, a domain in the system's); register in the index [2.18] and UI. The system's `init.sh` [10.6] also installs the git hooks that run relink at review time, and runs relink for the whole project.
- **Resolved (D-031):** links are rebuilt automatically after every change to a links file, by `relink` [14.1], without re-running `init.sh`.
- **Open:** Is it generated by the create-agent script [14]?

### [41] `start.sh` (every level has one: [10.7], [19.11], [21.11], [41])
- **Purpose:** start the agent: one run. The central scheduler [14.1] calls it for the agent's main-run job in its workers file (D-029, proposed); the owner can also run it by hand.

### [42] `copy-trading-agents/`
- **Purpose:** copy-trading domain; same shape as [19] (its own domain-level `.claude/`, domain agents, strategies with strategy-level `.claude/`).
- **Open:** Which wallets/traders are copied first?

### [43] `apps/`
- **Purpose:** GitHub repos cloned for our or agent use.
- **Open:** Pinned versions? Can agents clone new repos on their own?

### [44] `apps/[some-github-repo]/`
- **Purpose:** one cloned repo.
- **Open:** Does the Polymarket suite v2 go here?

### [47] `.secrets/` (D-023; proposed design)
- **Purpose:** the single store for private keys, wallet keys, API keys and tokens for trading accounts [11.1] `accounts` and platforms [11.11] `platforms`.
- **Location (proposed):** repo root, **outside `agents/`**, so no agent or level session (which run inside `agents/…`) has it in its folder, and no `subagents.link/` or file link reaches it. Git-ignored via [48]. Folder `chmod 700`, files `chmod 600`, owned by the user that runs the scripts. Stronger option: keep it outside the repo entirely (e.g. `~/.trading-os/secrets/`) with the same layout.
- **Contents (D-027 updates D-023):** [47.1] `test/.env` holds **all** test keys in one file (`KEY=value`, keys prefixed per account/platform, e.g. `POLYMARKET_ACCT1_API_KEY`); [47.2] `live/.env` will mirror it with the same key names and live values (later phase; the owner decides per key which values stay the same and which change, e.g. real-money accounts). Splitting into one file per account can come later if the file gets unwieldy. [47.3] `secrets.index.json` with metadata only: `{ "[ref]": { "kind": "wallet|api-key|token", "env": "test|live", "used_by": ["[account-id]"], "created", "rotate_by" } }`, never values.
- **Access (D-027):** agents and the dev workflow may read and update `test/.env` (safe test credentials; content grows with the project, no fixed schema yet). Nobody but the owner writes `live/.env`; agents never get write access to it. Each level's `.claude/settings.json` denies `.secrets/live/**` (not all of `.secrets/**` any more).
- **Loading (proposed, D-027):** nothing opens the file inline. An agent or worker declares the keys it needs in its own config (e.g. `"secret_keys": ["POLYMARKET_ACCT1_*"]`). The shared loader `load-secret` [14.1] (shell + Python twin) reads `.secrets/[test|live]/.env` and exports only those keys into the child process of that run: `load-secret POLYMARKET_ACCT1_* -- python3 scripts/get-polymarket-data.worker.py`. The mode comes from `TRADING_OS_ENV` (default `test`); `live` is refused unless the run is owner-approved. A missing key fails fast with the key name. The loader logs only key names, mode and result, never values.
- **Editing from a UI (owner request):** create/edit keys from the local trading UI [45] (it runs next to the files; values never leave the machine). The planning explorer page cannot and should not hold secret values.
- **Access rule (proposed):**
  - Agents never get a link or copy of anything in here; `check-links` [14.1] fails on any link or file whose target is inside `.secrets/`.
  - Configs hold only key names (`secret_keys`, D-027) or refs ([11.1] `accounts`, [11.11] `platforms`), never values.
  - Scripts that act (executor/decision [14.3], [33]; workers that call private APIs) call `load-secret` [14.1] at execution time. It returns the value only if that agent's config references the ref, and `live/` refs only if the agent is live-allowed with an owner-approved account ([11.1] `modes`, `accounts`).
  - **Live values never in LLM context:** they are passed to the script process only (env injection), never into prompts or Claude Code sessions. Each level's `.claude/settings.json` ([10.1.6], [19.1.6], [21.1.6], [24.6]) denies `.secrets/live/**`. Test values may be seen by an agent that updates `test/.env` (D-027); they are still never copied into configs, docs, data or logs.
  - **Never logged:** loggers redact anything resolved by `load-secret`; [2.14] schemas forbid secret fields in data/logs.
- **Test vs live:** separate folders and separate refs. A test agent can never resolve a `live/` ref.
- **Rotation (proposed):** `rotate_by` in [47.3]. The notifier warns before expiry. Rotation writes a new value under the same ref (configs stay unchanged), then revokes the old key at the venue. Runbook in [2.11.6].
- **Writers / readers:** only the owner writes keys (live ones for sure; test ones possibly via a system-support agent, open). Only `load-secret` reads.
- **Upgrade path (later):** replace the file backend of `load-secret` with the OS keychain, a password manager CLI (e.g. 1Password) or a vault (e.g. HashiCorp Vault). The `secret_ref` scheme and the configs stay the same.

### [48] `.gitignore` (D-028)
- **Purpose:** keep secrets, local state and generated files out of git. Each entry carries a comment saying why (D-028).
- **Content:**
  ```text
  # Secrets: never commit credentials (D-023, D-027)
  .secrets/
  *.env

  # Claude Code local overrides: machine-specific settings, not shared (D-024)
  **/.claude/settings.local.json

  # Claude Code local agent memory: local scratch state, not source of truth
  **/.claude/agent-memory-local/

  # Dependency and build artifacts: regenerated, not source
  node_modules/
  __pycache__/
  *.pyc
  dist/
  build/

  # OS/editor noise
  .DS_Store
  *.swp

  # open: large runtime content (logs/data) may need excluding once volume is known, see [0]
  # agents/**/data/**/raw/
  # agents/**/logs/**/*.log
  ```
- **Open:** Which runtime folders (logs, data) should also be git-ignored? This depends on the repo question in [0].

### [49] `tests/` (agent level; D-025, placement proposed)
- **Purpose:** the agent's tests, so every change (by the owner, create-agent or the SI sub-agent) can be checked before and after it runs. Same at every level: [10.8], [19.12], [21.12]. Layout and rules in [2.7.3], fields in [2.14].
- **Contents:** [49.1] `agents/`: tests of [24.5] `CLAUDE.md` and [26] sub-agents ([49.1.2] scenario files, [49.1.1] `tests.config.json`, [49.1.3] runner link). [49.2] `scripts/`: tests of [31]–[33] and linked scripts ([49.2.2] test files, [49.2.1] `tests.config.json`, [49.2.3] runner link). Results are written back to the configs and appended to [34.2] `logs/tests.jsonl`.
  - [49.1] `agents/`: tests of the agent's prompt and sub-agents. Run with `node tests/agents/run-tests.system.link.js [--id t-agents-001]`. Each test runs Claude Code headless in a temporary copy of the agent folder on the test's fixtures, in test mode, with no secrets, and is graded by script checks or a judge sub-agent (see [2.7.3]).
  - [49.1.3] `run-tests.system.link.js`: file link to the shared [14.1] `run-tests.system.js`. Because it is called from `tests/agents/`, it presets `--kind agents` and reads [49.1.1] `tests.config.json` in this folder.
  - [49.2] `scripts/`: tests of the agent's scripts and linked scripts. Run with `node tests/scripts/run-tests.system.link.js`; each `[test-id].test.[js|py]` runs with node or pytest on fixture data, no network, no secrets.
  - [49.2.3] `run-tests.system.link.js`: the same link; called from `tests/scripts/`, it presets `--kind scripts` and reads [49.2.1].
  - [30.2] `scripts/run-tests.system.link.js` stays: it runs both kinds (used by the scheduler, `before_promote` and `npm test`).
- **Writers / readers:** create-agent scaffolds empty configs. The SI sub-agent and system-support agents add tests. The owner enables/disables tests from the UI. `run-tests` writes the state fields. The UI, the SI sub-agent and promote-to-live [2.11.4] read them.
- **When tests run (proposed):** per test `schedule`: `manual`, `on_change` (the target file changed; via the scheduler [14.1]), `interval:[x]`, `before_promote`.
- **Open:** Is a backtest (strategy on past data) a test here, a research item [50], or both (research runs it, a test guards the result)? Should a failing test block the agent's runs, or only promotion?
- **Example** `tests/scripts/tests.config.json`:
  ```json
  {
    "schema_version": 1,
    "level": "pm-momentum-v1-agent-opus55-test",
    "kind": "scripts",
    "tests": [
      {
        "id": "t-scripts-001",
        "name": "make-buy respects max position size",
        "target": "scripts/make-buy.decision.js",
        "file": "tests/scripts/t-scripts-001.test.js",
        "enabled": true,
        "schedule": "on_change",
        "owner": "pm-strategy-1-self-improvement-agent",
        "last_run": "2026-09-29T10:00:00Z",
        "last_result": "fail",
        "last_duration_ms": 420,
        "fail_count": 1,
        "notes": "cap ignored when two signals arrive in one run",
        "next_action": "fix the cap check in make-buy, then re-run"
      }
    ]
  }
  ```

### [50] `research/` (agent level; D-025)
- **Purpose:** the history of research done for this agent: what was asked, what was found, what was decided. Same at every level: [10.9], [19.13], [21.13] (strategy-level research on its variants usually lives at [21.13]).
- **Contents:** [50.1] `index.json`, one entry per item. [50.2] `[research-id]-[slug]/`, one folder per item with `README.md` (question, method, results, decisions) and its artifacts.
- **Writers / readers:** mainly the level's SI sub-agent. Also the owner (requests), domain/strategy agents and system-support agents. The UI shows the index; the SI reads past items before starting new ones, so it does not repeat work.
- **Replaces:** research kept in the level's `data/` (D-022/D-024).
- **Example** `research/index.json` entry:
  ```json
  {
    "id": "r-0001",
    "slug": "momentum-window-length",
    "topic": "signal tuning",
    "question": "Does a 6h momentum window beat 24h on the markets this agent trades?",
    "status": "done",
    "started": "2026-09-20T09:00:00Z",
    "finished": "2026-09-22T18:00:00Z",
    "ran_by": "pm-strategy-1-self-improvement-agent",
    "requested_by": "owner",
    "folder": "research/r-0001-momentum-window-length/",
    "results_summary": "6h window: higher hit rate in test mode, more trades, similar drawdown.",
    "decisions": [
      { "decision": "create variant v2 with a 6h window", "by": "pm-strategy-1-self-improvement-agent", "approved_by": null, "date": "2026-09-22", "decision_ref": null }
    ],
    "links": ["data/get-polymarket-data/2026-09.json", "logs/runs.jsonl"],
    "related": { "variants": ["pm-momentum-v2-agent-opus55-test"], "changes": ["pm-momentum-v2-agent-opus55-test/docs/changes.md"], "tests": ["t-scripts-001"], "research": [] },
    "tags": ["momentum", "window"]
  }
  ```

### [45] `trading-ui/`
- **Purpose:** Next.js API + UI for monitoring and control (vision §12).
- **Open:** Does it read the JSON/MD files directly or through an API layer? How is it accessed (local only, auth)?

---

## Changelog

- **v0.1** – initial skeleton from owner's v0.2 input.
- **v0.2** – detailed [2] `docs/`: proposed files [2.1]–[2.11] with purpose, outline, writers/readers and update rules; `vision.md` moved from [3] to [2.2].
- **v0.3** – added [2.12] `docs/feature-map.md` (owner request): maps features/logic to files; draft created.
- **v0.4** – moved this file from [6] `agents/docs/file-tree.md` to [2.13] `docs/file-tree.md` (owner request); [6] is now a stub; updated references and the [2.1] read order.
- **v0.5** – owner input: added [2.14] `data-schemas.md`, [2.15] `flows.md`, [2.16] `metrics.md`, [2.17] `docs/common/`, [2.18] `docs/index/`, [2.19] `docs/agents/` (per-agent docs, central; agent folder links in via [29] `docs.link/`). Merged `agents/docs/` [5] into `docs/` ([7]→[2.17.1], [8]→[2.18], [9]→[2.17.2]). New `.link` naming rule for every symlink (recorded in [2.7], decision D-002 in [2.6]); example agent renamed/added links [26.1], [27.1], [29], [30.1], [30.2], [34.1], [36], [36.1].
- **v0.6** – detailed [4] `agents/` and [10] `agents/system/` (what belongs where, `.link` mechanics via `init.sh`, promotion rule, when shared changes apply) and [11] `configs/` with proposed files [11.1]–[11.9] and a merge order (defaults → agent type → domain → strategy → agent → owner runtime; risk tighten-only; live only via allowlist + approved account; `effective-config.json` per run). The logs-link direction is still open.
- **v0.7** – owner decision D-006: configs collapsed to two types: [11.1] `system.config.json` (the v0.6 files [11.1]–[11.9] became its sections; [11.3]–[11.9] retired) and [11.2] per-agent configs, central in `configs/agents/[domain]/[agent-name].config.json`, linked into the agent as [27] `config.link.json` (direction proposed). [27.1] is now `system.config.link.json`; [28] is now the `workers` section of the agent config. Merge rule simplified to global → agent → owner UI with the same safety exceptions (proposed). [17] no longer holds routing. The shape and the common/individual split are still open.
- **v0.8** – owner decisions D-007–D-011: [12] workers → scripts [14.2] + definitions in [11.10] `workers.config.json`; [13] sub-agents → Claude Code [10.1.1] in `agents/system/.claude/` (location proposed); [15] logs and [16] data are organised by source ([15.1]–[15.5], [16.1]–[16.4]) and linked into agents as needed (settles the logs-link question: [34] is now `logs.link/`, [34.1] retired); [17] → [11.11] `models.config.json`, and [11.1] no longer has `routing`. Scripts [14] now have sub-folders `system/`, `workers/`, `decisions/` plus a suffix rule; [33] renamed `make-buy.decision.js`; [30.2] retired; new links [25.1], [36.1], [36.2].
- **v0.9** – owner decision D-012: every agent has a globally unique name that is its ID everywhere. Added the naming rule and proposed format to [2.7] (clone → new name/version, no renames, test → live = new agent, no reuse); [2.18.1] is the registry that enforces it; [14.1] `create-agent` is the check point; [2.11.1] and [23] updated.
- **v1.0** – owner input (interpreted as D-013–D-016): `agents/` holds domains only, and `system/` [10] is a domain ([18] `trading-domains/` retired). Every agent has the same real folders `configs/` [27], `scripts/` [30], `logs/` [34], `data/` [35], each with `system.link/` ([27.1], [30.1], [34.1] reinstated, [35.1]). The system domain holds the shared files plus the views [11.2.1], [14.4.1], [15.5.1], [16.4.1] of every agent. `.claude/` at domain ([10.1], [19.1]) and strategy ([21.1]) levels, linked into agents ([25.1]–[25.3], [26.1]–[26.3]). New: [10.2] system-support agents, [27.2] own config file, [35.2] own data. Retired: [36], [36.1], [36.2]. Renamed per D-012: [22], [23]. Added link-cycle rule. Supersedes D-006 (location), D-009/D-010 (agent part).
- **v1.1** – owner decision D-017 (supersedes D-003): docs follow the same pattern as configs/scripts/logs/data. The shared docs [2] moved from top-level `docs/` to `agents/system/docs/` (numbers [2.x] kept; the root keeps only `README.md` [1]). New: agent `docs/` [46] with [46.1] `system.link/` and [46.2] own files; system view [2.20] / [2.20.1]. Retired: [2.19], [2.19.1], [29] `docs.link/`.
- **v1.2** – owner decision D-018: [20] `main-domain-agents/` → domain-owner sub-agent [19.1.1.1] `pm-domain-owner-agent.md`; [22] SI agent folder → SI sub-agents at every `.claude/` level ([10.1.1.1], [19.1.1.2], [21.1.1.1]); their memory/state in [16.3] (proposed); [2.18.3] extended; [20], [22] retired.
- **v1.3** – owner decision D-019: `.claude` links go parent → child only. New down-links [10.1.3]/[10.1.4] (system → domains, system agents), [19.1.3]/[19.1.4] (domain → strategies), [21.1.3]/[21.1.4] (strategy → agents); agent `.claude` [24] holds own files only; upward links [25.1]–[25.3], [26.1]–[26.3] retired. Proposed: runs start at `agents/system/` with an allowlist for the target branch. Open question added in [10]: same rule for `system.link/` folders? `init.sh` [40], `check-links` [14.1] and [2.7] updated.
- **v1.4** – owner decision D-020: agents' `system.link/` folders replaced by individual file links (`[name].link.[ext]`) to only the files each agent needs, from any folder; the list lives in the new `links` section [27.3] (proposed), is set by create-agent, updated by the SI sub-agent, rebuilt by `init.sh` [40] and checked by `check-links` [14.1]; link changes are logged in [46] `changes.md` (new variant, proposed). [27.1], [30.1], [34.1], [35.1], [46.1] redefined as file-link sets; example agent shows concrete links. The D-019 follow-up question is resolved. The system views and `.claude` down-links are unchanged.
- **v1.5** – owner decision D-021: domain → strategy `.claude` links [19.1.3]/[19.1.4] removed (stubs). The "runs start at `agents/system/`" proposal is withdrawn; proposed instead: each level runs in its own folder, a trading agent runs in its own folder ([14.1] `run-agent`, [24]), and higher-level sub-agents deliver outputs as data files linked per D-020. Open questions added in [10.1]: keep [10.1.3]/[10.1.4] and [21.1.3]/[21.1.4]? File links for shared skills in agent `.claude`?
- **v1.6** – owner decision D-022: three levels of agents (system [10], domain [19], strategy [21]) plus variants [23], all with the identical standard folder, now defined in [2.7.1]. Added level files [10.3]–[10.7], [19.2]–[19.11], [21.2]–[21.11]. Domain `CLAUDE.md` [19.7] is the domain owner, so [19.1.1.1] is retired. SI memory moved to the level's own `data/` ([19.5], [21.5]). System views stay folder links (not copies) and now cover all levels.
- **v1.7** – owner request D-023: secrets store [47] `.secrets/` at repo root (git-ignored; `test/`, `live/`, metadata index [47.3]) and [48] `.gitignore`. `load-secret` and a secrets rule added to `check-links` [14.1]. Safety outline [2.8], conventions [2.7] (`secret_ref` scheme) and a new runbook [2.11.6] `add-account-or-secret.md` updated. All proposed.
- **v1.8** – owner decision D-024: full standard `.claude/` at every level ([2.7.2]; [10.1.5]–[10.1.13], [19.1.5]–[19.1.13], [21.1.5]–[21.1.13], [24.5]–[24.13]) with generic placeholders. `CLAUDE.md` moved inside `.claude/` ([10.3], [19.7], [21.7], [37] → [x.5]; [37] stub). SI memory proposed in `.claude/agent-memory/` (updates D-022). `.gitignore` [48] extended. Template [2.7.1] updated.
- **v1.9** – owner request D-025: `tests/` and `research/` in the standard agent folder at every level ([2.7.3]; [10.8]/[10.9], [19.12]/[19.13], [21.12]/[21.13], [49]/[50]), shared `run-tests` [14.1] linked as [30.2], results in [34.2]. Schemas in [2.14], how-tos [2.11.7]/[2.11.8], create-agent and promote-to-live updated. Research moved out of `data/`.
- **v1.10** – fix: [46] cross-variant history points to [21.5] (was stale [16.3]).
- **v1.12** – owner edits from the explorer: D-026 [10.2] support-agent folders retired, support roles are sub-agents ([10.1.1.2] `sys-docs-agent.md` added; [10.1.3]/[10.1.4] only link domains). D-027 test secrets in one `.secrets/test/.env` ([47.1.1], [47.2.1] now `.env`), agent read/update access to test only, loader via `secret_keys` + `load-secret`, UI editing in [45]. D-028 `.gitignore` [48] shows the real commented file.
- **v1.13** – owner request D-029: every agent has a jobs file `configs/[name].workers.json` (format in [11.10]): scripts or AI runs (agent, sub-agent, skill, workflow, command) with on/off, schedule (every, cron, once on a date, after a job, manual), where it runs (local, cloud, desktop, GitHub Actions), platform (Claude Code, Cursor, Codex), model and AI-run parameters. [11.10] `workers.config.json` → `system.workers.json`; new [11.12] `configs/workers/[domain]/` links every workers file by domain; new [19.2.1], [21.2.1], [27.4]; [28] moved to [27.4]; [14.1] `trigger-watcher` → `scheduler` + `run-job`; state in [16.1] `scheduler-state.json`; [11.1] `schedules`, [11.11] rule, [2.11.1], [2.11.2], [2.14], [2.18.2], [40], [41] updated.
- **v1.14** – owner decision D-030: one template for every level's content folders ([2.7.4]): own files + `subagents.link/[child-name]/` → the child's folder of the same kind. System: [2.20], [11.2], [14.4], [15.5], [16.4] renamed from `agents/` views to `subagents.link/` (one link per domain), new [10.8.3], [10.9.3]. Domain: new [19.2.2], [19.3.1], [19.4.1], [19.5.1], [19.6.1], [19.12.3], [19.13.3]. Strategy: new [21.2.2], [21.3.1], [21.4.1], [21.5.1], [21.6.1], [21.12.3], [21.13.3]. No `.claude` links for now: [10.1.3], [10.1.4], [21.1.3], [21.1.4] retired. Jobs view [11.12] merged into [11.2]; the scheduler scans `agents/**/configs/*.workers.json`. `.link` rule amended (links inside a `.link` folder); [2.7], [2.7.1], [2.7.2], [2.11.1], [2.11.5], [2.18.2], [10], [10.1], [14.1] `check-links`, [40] updated.
- **v1.15** – owner request D-031: every agent has a links file `configs/[name].links.json` (format in the new [11.13] `system.links.json`; new [19.2.3], [21.2.3]; [27.3] turned from the `links` section of [27.2] into the variant's own file): which file, from where (system, own domain or strategy, another domain, any agent by unique name), where it appears, why, required. New shared `relink` script [14.1] builds every link from these files plus the child links, removes stale ones, runs the `check-links` rules and writes the links index [16.1]; it runs on a links-file change (scheduler watch), at review time (git pre-commit, post-merge, post-checkout; owner approval in the UI), when an agent edits its own links file (it reruns relink; `PostToolUse` hook in `settings.json`) and from create-agent/init.sh. New relink links [19.3.2], [21.3.2], [30.3]; new runbook [2.11.9]. Updated [2.6], [2.7], [2.7.1], [2.7.2], [2.7.4], [2.7.5], [2.11.1], [2.11.2], [2.11.5], [2.14], [2.17], [10], [11], [11.10], [15], [16], [27], [30], [40]; `init.sh` now only calls relink. Fixed a stale [11.12] reference in [2.11.1].
- **v1.11** – owner request: every `tests/agents/` and `tests/scripts/` folder gets its own runner link `run-tests.system.link.js` → [14.1] ([10.8.1.3]/[10.8.2.3], [19.12.1.3]/[19.12.2.3], [21.12.1.3]/[21.12.2.3], [49.1.3]/[49.2.3]); called from a test folder it presets the kind and that folder's `tests.config.json`. [30.2] stays for running both kinds. Described how agent tests run (headless Claude Code on fixtures in a temp copy, test mode, no secrets). Updated [2.7.3], [2.11.7], [14.1], [49].
