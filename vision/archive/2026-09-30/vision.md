# Trading OS: Vision (v0.19)

> Status: draft for owner confirmation. Sections 1–4 and 7–13 are requirements (v0.1 brief + v0.2 input). Section 5 lists ideas under evaluation (not decided). Section 6 lists open questions; items marked **[resolved v0.2]** or **[partly resolved v0.2]** are answered by the v0.2 input. The folder skeleton is detailed in `file-tree.md`.

## 1. What it is

A personal **Trading OS**: an agentic system that runs hundreds of trading agents of different types across several domains. Agents share a common base and differ by domain, strategy and configuration.

The system does five things:

1. Continuously collects data from many sources.
2. Lets each agent consume only the data relevant to it.
3. Lets agents decide and act.
4. Improves agents over time.
5. Makes it cheap to run many strategy/configuration variants side by side and see which ones work.

## 2. Building blocks

### 2.1 Workers (and sub-agents)

- Run periodically, as scheduled scripts or agents.
- Watch sources and prepare data.
- Write their output into the shared **Data** store.
- Examples: important-events collector, news, prices, errors, running a sub-agent.

### 2.2 Data

- The central store of everything workers produce.

### 2.3 Strategy agents

- Each agent belongs to a domain and is subscribed to the data it needs.
- Knows which data relates to it, and how and when to get it.
- Runs periodically; each run takes all new data since the last run.
- Owner's initial idea: the needed files are symlinked into the agent's folder.
- Context compression is needed (approach TBD).

### 2.4 Agent run loop

**Read data → Analysis → Decision → Action**

Possible decisions/actions:

- Buy, sell, sell all.
- Wait for needed information; set a reminder / schedule the next run.
- Collect additional data or do research (create and run a new sub-agent).
- Create, subscribe to, unsubscribe from, configure and schedule workers.

### 2.5 Agent folder (one per agent)

- Config
- Common config
- Docs
- Logs
- Common prompt
- Agent prompt
- Memory
- Self-improvement strategy
- List of workers and subscriptions
- Trading accounts
- Data
- Previous run and next runs info
- Current portfolio
- Analytics

## 3. Requirements for every agent

- Has a **self-improvement strategy**, which is itself variable and testable.
- Has a **test mode**, and backtesting where possible.
- Runs with **different configurations**: initial capital, risk-management strategy, personal settings, domain settings.
- Purpose: run and compare many variants, combine strategies, keep what works.
- **Shared base behaviour** plus domain- and strategy-specific parts.

## 4. Domains

- **Prediction markets** – up to ~80 ways to make money: market making, outcome probability analysis, agents that model and simulate futures, etc.
- **Crypto / bitcoin trading** – technical and other approaches.
- **Copy trading.**
- **Content-driven** – e.g. take one YouTuber, extract everything they say, and trade on it.
- **Combinations** – blend strategies (e.g. by best win rates).
- More domains later.

## 5. Ideas under evaluation (not decided)

1. **Strategy vs instance.** Strategies are templates; instances are configured runs (strategy version + capital + risk policy + model + mode). Experiments generate instances.
2. **Pull instead of symlinks.** Subscriptions with a per-agent read cursor; workers don't know about agents; easy replay for backtests.
3. **Agents decide, a separate layer executes.** Agents emit typed intents → code-enforced risk checks → executor (live / paper / shadow / backtest, same interface). Test mode becomes a config setting.
4. **Ledger owns the portfolio.** Agents see a read-only snapshot.
5. **Not every strategy fits a periodic LLM loop.** Market making and arbitrage need fast, event-driven code. Strategy kinds: code, LLM, hybrid.
6. **Champion/challenger self-improvement.** Self-improvement produces challengers that are tested against the current champion before promotion.
7. **Compress context upstream.** Shared digests are built once; each agent filters them; each run ends with a short memory note.
8. **LLM backtests can leak** (the model may know the future). Paper/shadow trading is the honest test.
9. **External text is untrusted input.** Hard risk limits live in code.
10. **Meta-agents.** Ensembles and capital allocators that consume other agents' signals.
11. **Worker requests.** Check existing data first; limits against duplicate workers.

## 6. Open questions

1. First domain, and 2–3 MVP strategies? **[partly resolved v0.2]** first domain in the layout is prediction markets (Polymarket, `strategy-1`); copy trading is next. The MVP strategies are still open.
2. **[partly resolved v0.2]** Every service has a test and a live mode (§11), and the owner approves giving an agent a funded account through the UI (§12). Still open: paper trading first? When does real money start, and with what capital limits?
3. Scale: number of concurrent agents, run frequency, LLM budget?
4. Venues/accounts: jurisdiction, KYC, API access?
5. Relation to the existing Polymarket suite v2 (liquidity provision, cross-platform arbitrage, resolution sniping, copy trading): reuse, keep separate, or replace?
6. Language/stack, hosting, storage? **[partly resolved v0.2]** scripts in JS/TS and Python; data as JSON and MD files for now; UI in Next.js. Hosting is still open.
7. **[partly resolved v0.2]** The owner approves or rejects funding a live account, and can stop or delete agents from the UI. Still open: which other actions need human approval? Which notification channel?
8. **[partly resolved v0.2]** Self-improvement may change anything in the agent (config, prompts, code, model/platform), always through a new test agent. Goals: fast, cheap, efficient, simple, understandable, profitable. Still open: what may self-improvement change without owner approval, and what are the success metrics (PnL, win rate, drawdown, calibration)?
9. How much autonomy do agents have to create workers/sub-agents, and with what limits?
10. History retention?
11. Keys and wallets: management and isolation? **[partly resolved v0.14]** proposed design in D-023 (§7); the exact location and who adds test keys are still open.
12. Dashboard/UI needs? **[resolved v0.2]** see §12.

## 7. Folder layout (v0.2)

The top level is `README.md`, `agents/` (domains: `system/` plus the trading domains; the shared docs incl. this vision are in `agents/system/docs/`), `apps/` (cloned GitHub repos), and `trading-ui/` (Next.js). Shared things live in the system domain `agents/system/` and are linked into each agent folder (see D-013–D-017 below). The full numbered skeleton is in `file-tree.md`.

Resolves the v0.1 idea "needed files are symlinked into the agent's folder": the owner keeps symlinks, for configs, workers, subagents, scripts, logs and data. §5.2 (pull instead of symlinks) remains an open alternative.

**Owner decisions (v0.3):**
- Every symlinked file or folder has `.link` in its name (e.g. `system.link/`, `[agent-name].link/`).
- `docs/` is the single docs root. It also holds common knowledge (`docs/common/`), an index of all things (`docs/index/`: agents, workers, sub-agents, services, apps, models), `data-schemas.md`, `flows.md` (data and user flows) and `metrics.md`.
- ~~Per-agent docs live centrally in `docs/agents/[domain]/[agent-name]/`. Each agent folder links to them as `docs.link/`.~~ (superseded by D-017)

**Owner decision (v0.4), D-006:** configs come in two types for now: one global `agents/system/configs/system.config.json` (sections for modes/kill switch, risk, workers and schedules, triggers, model routing, accounts and platform connections, notifications, domains; long sections are split into their own files later) and one config per agent. Proposed default: per-agent configs live centrally in `agents/system/configs/agents/[domain]/[agent-name].config.json`, and each agent folder links to its own as `config.link.json`. **Open:** the exact shape, and which settings are common vs individual. This will be decided with concrete example agents.

**Owner decisions (v0.5):**
- **D-007:** workers are just scripts. All scripts live in `scripts/`: workers, decision (buy/sell) and system scripts, either system-level or per agent. Workers are defined in config (`workers.config.json`: which exist, schedule, how they run, purpose).
- **D-008:** sub-agents are Claude Code subagents under `.claude/agents/`. For now only system-wide ones exist (proposed location `agents/system/.claude/`).
- **D-009:** logs are organised centrally by source (system, services, workers, subagents, agents), and some are linked into agents.
- **D-010:** data is organised the same way (system, workers, subagents, agents), and some is linked into agents.
- **D-011:** model/platform routing is config in a separate `models.config.json`. There is no `platforms-and-models/` folder.
- **D-012 (v0.6):** every agent has a **globally unique name** (unique across all domains). The name is its ID in folder names, configs, logs, data, docs, indexes and the UI. Proposed format: `[domain]-[modification]-v[N]-agent-[platform-model]-[test|live]`. Clones get a new name, names are never changed or reused, and test → live creates a new agent. The agents index is the registry, and the create-agent script checks it (see `file-tree.md` [2.7], [2.18.1], [14.1]).

**Owner decisions (v0.7), as interpreted from the owner's input:**
- **D-013:** `system` is a domain like the trading domains. Domains sit directly under `agents/` (`agents/system/`, `agents/prediction-market-agents/`, `agents/copy-trading-agents/`).
- **D-014:** every agent (system and trading) has the same folders: `configs/`, `scripts/`, `logs/`, `data/`. Each holds the agent's own real files ~~plus a `system.link/` folder link to the system folder of the same kind. Links are to folders, not files.~~ (link part superseded by D-020) This supersedes the central per-agent config location (D-006) and the per-agent part of central logs/data (D-009, D-010).
- **D-015:** the system domain has the same folders holding the shared files, plus `agents/[agent-name].link/` views of every agent's folder of the same kind, giving one view over everything.
- **D-016:** `.claude/` exists at every domain level (including system) and at every strategy level. ~~Each agent's own `.claude/` links them in.~~ (link direction superseded by D-019)
- **D-019 (v0.10):** `.claude` links go **parent → child only**. Order: system first, then domains, then strategies, then agents. The system `.claude` links to each domain's `.claude`, ~~each domain to its strategies',~~ (removed by D-021) each strategy to its agents'. Lower levels never link up. ~~Proposed: every run starts at the top (`agents/system/`), so a session sees all levels below, limited by an allowlist to the target agent's branch.~~ (withdrawn by D-021) ~~**Open:** should the same parent-down-only rule apply to the `system.link/` folders?~~ Answered by D-020.
- **D-020 (v0.11):** inside an agent's `configs/`, `scripts/`, `logs/`, `data/`, `docs/` there are **no folder links**. Instead there are **individual file links** (`[name].link.[ext]`) only to the files that agent's logic needs, from any folder: system, domain, strategy, or other agents' outputs such as worker data. The set is decided by create-agent at creation and updated by the self-improvement sub-agent afterwards. Proposed: the list lives in a `links` section of the agent's config, `init.sh` rebuilds the links from it, and each change is logged in the new variant's `docs/changes.md`. `.claude` keeps D-019's parent → child folder links, and the system views of all agents stay as they are.
- **D-021 (v0.12):** no `.claude` links from the domain level down to strategies' agents and skills. Proposed instead of "run from the top": each level (system, domain, strategy) runs its own sub-agents in its own folder; a trading agent runs in its own folder; higher-level sub-agents hand their outputs to agents as data files linked per D-020. **Open:** do the remaining system → domain and strategy → agent `.claude` links still need to exist?
- **D-022 (v0.13):** there are three levels of agents, and **every agent folder has the identical file structure**: `.claude/`, `configs/`, `scripts/`, `logs/`, `data/`, `docs/`, `CLAUDE.md`, `package.json`, `requirements.txt`, `init.sh`, `start.sh`. The levels are the **system** (manages all domains and system development), each **domain** (responsible for its domain) and each **strategy** (responsible for one concrete strategy); the trading variants under a strategy have the same structure. The system also holds its own docs/configs/etc. plus all agents' data (and configs, logs, scripts, docs) in per-agent subfolders; these are folder links (views), not copies. Reconciling D-018: the domain's own `CLAUDE.md` is now the domain owner (the separate sub-agent file is removed). Self-improvement stays a sub-agent at each level, with its memory in that level's own `data/`. *(D-024: `CLAUDE.md` now sits inside `.claude/`; SI memory proposed in `.claude/agent-memory/`.)*
- **D-023 (v0.14, owner request; design proposed):** secrets (private keys, wallet keys, API keys) live in a git-ignored repo-root `.secrets/`, outside `agents/`. It has `test/` and `live/` kept separate, one `.env` file per account or platform, and a metadata index without values. Configs hold only `secret_ref`s. Scripts load a value at execution time via `load-secret`, and only if the agent's config references it; `live/` refs also need an owner-approved live account. Secrets are never linked into agent folders, never logged, and never put in LLM context. Rotation keeps the same refs. Later upgrade path: OS keychain, a password manager, or a vault.
- **D-024 (v0.15, owner structure; placeholders only):** every `.claude/` folder (system, domain, strategy, trading variant) follows the standard Claude Code layout: `CLAUDE.md` (moved **inside** `.claude/` from the folder root), `settings.json` (permissions incl. the `.secrets/**` deny rule, hooks, env, model, statusLine, outputStyle; committed), `settings.local.json` (personal, git-ignored), `rules/` (`paths:` frontmatter), `skills/[name]/SKILL.md`, `commands/`, `agents/`, `workflows/*.js`, `output-styles/`, `agent-memory/[subagent]/MEMORY.md` (`memory: project`), `agent-memory-local/` (`memory: local`, git-ignored). Only generic placeholders for now; concrete logic is filled in later. Proposed: SI memory moves to `.claude/agent-memory/` (updates D-022). Parent → child links stay in `.claude/agents/` and `.claude/skills/`.
- **D-025 (v0.16, owner request; placement and fields proposed):** every level (system, domain, strategy, trading variant) has **`tests/`** with `agents/` (tests of the prompt and sub-agents) and `scripts/` (tests of scripts). Each has a `tests.config.json` listing every test: enabled, schedule, owner, last run, last result, notes and what should be done next. One shared `run-tests` script runs the tests from the config and writes the results back and to logs. Every level also has **`research/`** with an `index.json` history of research items (question, status, who ran it, results, decisions, links, related variants/changes/tests) and one folder per item. Both sit at the level's folder root next to `scripts/` (alternative: inside `.claude/`). Research previously kept in `data/` moves here; the SI sub-agent is the main writer.
- **D-026 (v0.17, owner edit):** system-support roles (docs, development, improvement, analysis, research) are sub-agents in `agents/system/.claude/agents/` (e.g. `sys-docs-agent.md`), not agent folders.
- **D-027 (v0.17, owner edit):** all test keys live in one `.secrets/test/.env` that agents may read and update; `live/.env` mirrors the keys with owner-only values in a later phase; scripts get only the keys their config declares, through the shared loader.
- **D-028 (v0.17, owner edit):** the repo `.gitignore` is a real, commented file (secrets, local Claude settings and memory, build junk).
- **D-029 (v0.17, owner request; format proposed):** every agent (system, domain, strategy, trading variant) has its own jobs file `configs/[name].workers.json`, where it can see, change and turn off everything it runs. A job is a plain script or an AI run (the agent itself, a sub-agent, skill, workflow or command) with a schedule (every N, cron, once on a special date, after another job, manual), where it runs (local headless, cloud, desktop, GitHub Actions), the platform (Claude Code now; Cursor or Codex later), the model, and for AI runs the prompt, workspace, skill and tool limits. The system config folder links every agent's workers file by domain (`configs/workers/[domain]/`) so all domain jobs are visible in one place, and one central scheduler runs them. Replaces the single `workers.config.json` of D-007.
- **D-030 (v0.18, owner decision):** every level (system, domain, strategy) uses **one template in each content folder** (`configs/`, `scripts/`, `logs/`, `data/`, `docs/`, `tests/`, `research/`): the level's own files, plus `subagents.link/` with one folder link per direct child agent, named after the child and pointing at the child's folder of the same kind. Example for docs: `agents/system/docs/subagents.link/[domain-name]/` → that domain's docs; `[domain]/docs/subagents.link/[agent-name]/` → a strategy's docs; a strategy's `docs/subagents.link/[agent-name]/` → a trading agent's docs. Trading agents have no children, so no `subagents.link/`. This replaces the system's flat views of every agent (D-015) and the jobs view by domain (D-029). For now, no `.claude` folder is linked at any level (pauses D-019).
- **D-031 (v0.19, owner request; format proposed):** every agent layer (system, domain, strategy, trading variant) has its own links config `configs/[name].links.json` saying **what is linked from where**: each entry names where the link appears in the agent's own folders and which file it points at, which can be in the system, the agent's own domain or strategy, **another domain**, or **any other agent** (by its unique name). For example, a strategy agent can link another agent's or another domain's data if it needs it. One shared `relink` script builds every link in the project from these files (plus the child links of D-030), removes links nobody lists and checks them. It runs when any links file changes, at the moment changes are reviewed (before a commit, after a pull or merge, when the owner approves a change), and when an agent edits its own links file (it reruns relink; a Claude Code hook also does it automatically). Replaces the `links` section of the agent config (D-020's file-link rules stay).
- **D-017 (v0.8, supersedes D-003):** docs follow the same pattern. Each agent has a real `docs/` (README, strategy, changes, decisions, notes) with `docs/system.link/` → `agents/system/docs/`. The shared docs (formerly the top-level `docs/`: vision, overview, file-tree, feature-map, conventions, decisions, index, common, how-to, …) move to `agents/system/docs/`, which also holds `agents/[agent-name].link/` views of every agent's docs. The repo root keeps only `README.md`, pointing there.
- **D-018 (v0.9):** there are no separate folders for domain agents or self-improvement agents. The **domain owner** is a Claude Code sub-agent in the domain-level `.claude/agents/` (e.g. `pm-domain-owner-agent.md`), with the same responsibilities (strategies, health, Q&A, owner comments). **Self-improvement** is a sub-agent at every `.claude/` level (system, domain, strategy), each scoped to its level (e.g. `sys-self-improvement-agent`, `pm-self-improvement-agent`, `pm-strategy-1-self-improvement-agent`). Proposed: their long-lived memory/state lives in `agents/system/data/subagents/[name]/`. The agent types in §8 stay the same; the domain and SI types are now sub-agents.

Agent folder naming: globally unique, format `[domain]-[modification]-v[N]-agent-[platform-model]-[test|live]` (D-012, proposed). Each agent folder contains `.claude/` (skills, agents), `configs/` (own config, its jobs file `[name].workers.json` (D-029) and its links file `[name].links.json` (D-031) + file links; D-014, D-020), `docs/` (own docs + file links; D-017, D-020), `scripts/` (`*.worker.*`, `*.system.*`, `*.decision.*`), `logs/`, `data/<worker-or-source>/`, `CLAUDE.md`, `package.json`, `requirements.txt`, `init.sh`, `start.sh`.

## 8. Agent types

1. **System-support agents.** Development, documentation, improvement, analysis and research of the system itself.
2. **Sub-agents (worker + AI).** Take data from workers and pre-analyse it for main agents.
3. **Main agents.** Run a strategy and make decisions, in test or live mode.

Within a domain there are also:
- **Main domain agent.** Owns the whole domain: finds, analyses, creates and updates strategies and their self-improvement agents; is responsible for the domain making money and running smoothly; answers the owner's questions about system state and addresses the owner's comments.
- **Per-strategy self-improvement agent** (e.g. `pm-self-improvement-agent`). A long-lived agent with memory. It runs from time to time and takes in the latest agent logs, data, research, outside-world information and the owner's comments. It runs research when needed. Its behaviour is dynamic per strategy but built from shared templates. Goal: make the strategy fast, cheap, efficient, simple, understandable and profitable; fix bugs and issues; test.

A main agent is one harness/platform/model combination. It runs one run at a time and pulls whatever it needs from workers or sub-agents to make a decision.

## 9. Model and platform routing

Every AI-using object (agent, sub-agent, AI worker) gets an explicit route: "object X does these things with this platform/model". This is configured in `agents/system/platforms-and-models/`.

| Platform / model | Status | Use for |
|---|---|---|
| Claude Code, Opus 5.5, xhigh effort | default | thinking, planning, intelligent tasks, main agents, analysis, improvements |
| Claude Code, Sonnet 5.5, medium effort | supported | unimportant tasks |
| Cursor, Composer 2.5 | supported | easy jobs, data handling, light analysis, filtering; mostly workers and sub-agents; high-token but non-intelligent work |
| OpenRouter, free-model rotation | supported, not connected yet | unimportant things |
| Codex | later | – |
| Kimi 3 | later | – |

The platform/model is part of the agent's name, so variants differing only by model can run side by side.

## 10. Data and triggers

- **Data:** JSON and MD files for now.
- **Triggers:** agents run on an **interval**, or when an **important** watched file changes.
  - An important change **cancels the current run** (if any) and starts a new one with the new information.
  - An unimportant change waits for the next scheduled run.
  - Which files and changes are important is configured per agent (see `file-tree.md`).

## 11. Test and live modes

Every service that performs an action has a **test mode** and a **live mode**, and takes the mode from configuration. The mode is also part of the agent's name.

## 12. UI (trading-ui)

Built with Next.js (API + UI), for monitoring and analysis of all agents and the system. The owner can:
- Create a new agent from a plain input ("create a new agent based on this input").
- See each agent's performance.
- Approve or reject giving it an account with money; stop and delete agents.
- Leave comments; ask the agent questions (answered by AI); say what to do better.
- See the agent in full: all components, logs, performance, data used and produced, every decision made, and every improvement and exact change being tested.

## 13. Workflow: the self-improvement wheel

1. **Create.** The owner or the system provides an input for a new agent. The system knows how to create the agent and integrate it (folder, config, routing, workers, subscriptions, UI registration).
2. **Run.** The agent runs in test mode on interval/file triggers.
3. **Analyse.** The self-improvement logic analyses the agent and does extra research if needed.
4. **Reconfigure.** It produces a new configuration (or code/prompt change) as a **new test agent**.
5. **Watch outside world.** It also takes in external signals such as related news, a new harness or a new model. It updates the related logic and spawns new agents to test the new configuration.
6. **Owner in the loop.** The owner sees everything in the UI, comments, approves live funding, and stops or deletes agents.

The wheel turns continuously, and the system analyses and improves itself.

## 14. Undecided ideas from v0.2 input (not requirements yet)

1. Exact template(s) used to build per-strategy self-improvement agents.
2. How "important" file changes are declared (per-file flag, per-worker, per-subscription).
3. Whether each variant is a full folder copy or a thin folder over shared code (symlinks); how that interacts with §5.1 (strategy vs instance).
4. OpenRouter free-model rotation policy.
5. How system-support agents are scheduled and routed.

---

## Changelog

- **v0.1** – initial brief.
- **v0.14** – owner request D-023: secrets store and access rules (proposed) (§7, §6 Q11).
- **v0.13** – owner decision D-022: three level agents (system, domain, strategy) + variants, all with the identical standard folder; domain `CLAUDE.md` = domain owner; SI memory in each level's `data/` (§7).
- **v0.12** – owner decision D-021: no domain → strategy `.claude` links; runs happen per level / in the agent's own folder (proposed) (§7).
- **v0.11** – owner decision D-020: agents link individual files they need (listed in config `links`), not folders; answers the D-019 follow-up (§7).
- **v0.10** – owner decision D-019: `.claude` links parent → child only; runs start from the top (proposed); open question on `system.link/` folders (§7).
- **v0.9** – owner decision D-018: domain owner and self-improvement become sub-agents in the `.claude/` levels (no own folders); memory in system data (proposed) (§7).
- **v0.8** – owner decision D-017: docs follow the same pattern (agent's real `docs/` + `system.link/`; shared docs moved to `agents/system/docs/`; root keeps only `README.md`); supersedes D-003 (§7).
- **v0.7** – owner decisions D-013–D-016 (interpreted): system as a domain; same folders for every agent with `system.link/`; system views of all agents; `.claude/` per domain and strategy; D-006/D-009/D-010 partly superseded (§7).
- **v0.6** – owner decision D-012: globally unique agent names used as IDs everywhere (§7).
- **v0.5** – owner decisions D-007–D-011: workers are scripts + `workers.config.json`; sub-agents are Claude Code subagents (system-wide `.claude/`); logs and data central by source, linked into agents as needed; routing in `models.config.json` (§7).
- **v0.4** – owner decision D-006: two config types (one global `system.config.json`, one per-agent config linked in as `config.link.json`, central location proposed); shape and common/individual split open (§7).
- **v0.3** – owner decisions: `.link` naming for all symlinks; `docs/` as the single docs root with `common/`, `index/`, `data-schemas.md`, `flows.md`, `metrics.md`; per-agent docs central in `docs/agents/`, linked into agent folders as `docs.link/` (§7; details in `file-tree.md` v0.5).
- **v0.2** – merged owner input: folder layout (§7, `file-tree.md`), agent types (§8), model/platform routing (§9), JSON/MD data and interval + file-change triggers with cancel-and-restart (§10), test/live for all services (§11), UI (§12), self-improvement wheel and agent-creation workflow (§13), undecided items (§14). Marked resolved/partly resolved open questions 1, 2, 6, 7, 8, 12.
- **v0.15** – owner decision D-024: standard `.claude/` layout at every level, `CLAUDE.md` inside `.claude/`, SI memory in `agent-memory/` (proposed) (§7).
- **v0.16** – owner request D-025: per-level `tests/` (configs + run-tests) and `research/` (index + items) (§7).
- **v0.17** – D-026–D-028 recorded (owner edits from the explorer); owner request D-029: a jobs file `[name].workers.json` in every agent's `configs/`, linked by domain in the system config (§7).
- **v0.18** – owner decision D-030: own files + `subagents.link/[child]/` in every level's content folders; no `.claude` links for now (§7).
- **v0.19** – owner request D-031: a links config `[name].links.json` in every agent's `configs/` (what is linked from where, across agents and domains) and a shared `relink` script run on change, at review time and by the agent itself (§7).
