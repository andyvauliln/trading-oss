# The Agent OS: vision

## In short

The Agent OS is a personal system for trading with AI. It runs many small trading agents at the same time, each following one strategy, and keeps the ones that make money. A trading agent is a small AI-driven program that reads information about a market, decides what to do and acts on it. Small programs collect information such as prices and news, each agent is given only the information its strategy needs, every new idea is tried in test mode first, and a self-improvement helper keeps preparing better versions of each strategy, like a wheel that keeps turning. The owner steers everything from one screen: they give ideas in plain words, approve every new version of a strategy before it starts, and are the only one who can approve real money. The project is being planned, and nothing of the trading system is built yet.

## Why we are building it

There are far more ways to make money in markets than one person can try by hand. Prediction markets, where people trade on the outcome of events such as elections or sports, alone offer up to about eighty approaches: from market making, which means always offering both to buy and to sell and earning the small difference, to estimating the real odds of an event better than the crowd. Crypto trading, copying successful traders and trading on what a well-known YouTuber says add many more.

Building one trading bot at a time is slow, and most ideas do not work. The Agent OS makes trying ideas cheap: it runs many agents side by side, each a small variation of a strategy, and lets the results show which ones work. Good ideas can then be combined, for example by blending the strategies with the best win rates.

The goals:

- strategies that are fast, cheap to run, simple, easy to understand and profitable;
- every change tested before it touches money, and mistakes found and fixed along the way;
- a system that keeps improving with little hand work;
- full visibility: the owner can see and control every agent and every decision from one place.

Success means agents that reliably make money in test mode, then with real money the owner has approved, while the system keeps finding better versions of them. How success is measured in numbers is still open.

## The concept

Instead of one large program that does everything, the Agent OS is made of many small parts, each with one clear job.

- **Workers** collect information on a schedule, such as prices and news, and save it as simple files.
- **The workers helper** knows every worker. An agent that needs new information asks it, and it points the agent to data that already exists, extends a running worker or creates a new one, so hundreds of agents never build the same worker twice.
- **AI helpers** prepare raw information for the agents, for example by boiling the day's news down to what matters for one market.
- **Agents at four levels.** The **system agent** looks after the whole Agent OS: every area of trading, its health and its own development. A **domain agent** owns one area of trading, such as prediction markets, finds and creates its strategies and makes sure it makes money. A **strategy agent** owns one strategy and keeps improving it. A **trading agent** is one variation of a strategy, with its own settings, AI model and mode, test or live; it is the one that trades.
- **Strategies and variations.** A strategy is one way to make money, such as market making; a variation is one version of it, with different settings, instructions, code or AI model. A strategy can be plain code, AI or a mix: market making and arbitrage need fast code that reacts instantly, while other strategies gain from an AI's judgement.
- **Self-improvement helpers** sit at every level: a strategy's prepares new variations, a domain's compares strategies and proposes new ones, and the system's improves the system itself and reacts to new AI models and tools. They keep a memory between runs and are built from shared templates, so they improve agents in a similar, well-tested way.
- **Support helpers** work on the system itself: the knowledge base agent keeps the docs in line with every input and change, and the project IDE agent looks after the owner's window on the project.
- **The owner** gives ideas, approves what runs and what touches money, and watches and steers everything.

Five ideas make it work: **many small agents with one strategy each**, simple, easy to understand and cheap to run; **everything tried safely first**, in test mode, where mistakes cost nothing; **variations that compete**, so results decide what becomes the standard; **plain files everyone can read**, for all information and for each agent's settings and jobs, with no database for now; and **one place to see and steer it all**. Because every agent's name includes its AI model, even agents that differ only by model can run side by side and be compared.

## How it should work

The system works in a loop.

1. **Collecting information.** Workers watch sources such as prices, news, important events and errors on a schedule, and save what they find as simple files.
2. **Giving each agent only what it needs.** When an agent is created, it is handed exactly the information its strategy uses. Each run it reads what is new since the last one, and at the end it keeps what matters, compressed or summarised, and clears out the rest, so the next run starts light. The agent decides this itself, including whether to continue in the same AI session, and whether it needs more: other information, research, or a new worker from the workers helper.
3. **Deciding and acting.** Every run follows the same four steps: read, analyse, decide, act. An agent can buy, sell, sell everything, wait for more information, set a reminder for its next run, collect extra data, start research, or ask for a worker to be created or changed.
4. **Running at the right moments.** Agents run on a regular interval and when something they care about happens. When important information changes, the current run stops and a new one starts with it; unimportant changes wait for the next run. When something the agent waits for is ready, such as research it started, it runs again with the result. A system helper checks what the server can take and limits how many agents run in parallel.
5. **Acting safely.** Every action works in a test mode and a live mode, chosen in the agent's settings. New agents start in test mode; real money needs good results and the owner's approval.
6. **Testing on the past.** Where it makes sense, each strategy has its own way of testing on past data, such as replaying a month of old data as if it were live. One thing to watch: an AI model may already know how past events turned out, so an AI strategy can look better on old data than it really is. Every level also has its own tests, which the owner can switch on and off.
7. **Getting better.** For every strategy, a self-improvement helper studies the agents' results, logs and decisions, research, outside news and the owner's comments, and prepares a new variation with a short report. Once the owner approves it, the variation runs in test mode next to the current ones. The variations compete, and the winners become the new standard.
8. **Agents listening to each other.** An agent can subscribe to what other agents produce. New data reaches it on its next run or, if it is urgent, interrupts the run in progress.
9. **Watching the outside world.** When something new appears, such as a better AI model or a new tool, the system updates the related logic and starts new test agents to see whether it helps.

```text
   sources ──► workers ──► files ──► trading agents ──► actions (test or live)
                                       ▲     ▲                  │
                                       │     └── other agents   ▼
                              self-improvement ◄── results, logs, the owner's comments
```

## The business logic

The Agent OS makes money by trying many strategies cheaply and safely, keeping what works and putting real money only behind what has proven itself. These are its rules.

**Where strategies come from.** The owner describes an idea in plain words, and the system builds the agent and fits it in. The system also starts agents itself: domain agents create strategies for their area, self-improvement helpers prepare variations, and a better AI model or tool leads to new test agents. The first strategy is one Polymarket strategy chosen by the owner; more follow once it runs in a good flow.

**From a strategy to variations.** A strategy is run by its trading agents, the variations, which may differ in anything: settings, instructions, code or AI model. An improvement never changes a running agent; it always becomes a new agent in test mode, and starts only after the owner has read a short report on it and approved it. Variations run side by side and are compared on their results; the winners become the new standard, and a winning change is folded back into the strategy itself. How a winner is judged depends on how success is measured, which is still open.

**Test first.** Every action, such as buying or selling, works in a test mode and a live mode from the start; on a blockchain, test mode can use a test network. Every new agent starts in test mode, where no real money moves. The mode is part of every agent's name, so a test agent and a live agent are always two different agents.

**What may be traded.** For now the system acts only on blockchains, on any network and app there. From centralised exchanges and other apps it only collects information. Prediction markets on Polymarket come first, then copy trading and the other areas. The venues and accounts a strategy needs are chosen while that strategy is built.

**Real money.** Real money comes only after an agent and its strategy have shown good results, and only when the owner approves an account for that agent, one account at a time. No agent can approve real money, for itself or another, and self-improvement never touches it. Agents may use the access keys to test accounts; the live keys are for the owner only and never reach an AI. Live trading comes together with protection against instructions hidden in outside text, such as news. How much money the first live accounts get is still open.

**Limits and costs.** How many agents run at once follows what the server can take; for now that is one of the owner's own servers, and the system is built to move easily to a bigger one. Hard limits in code, on order size, losses and allowed markets, and a stop switch that halts every agent at once, are ideas we are weighing. Every AI run costs money, so each kind of work has a fixed model that fits it: the strongest for thinking, planning, improving and trading, cheaper ones for light, high-volume work. Being cheap to run is a goal every strategy is improved toward; the AI budget is still open.

**Stopping what loses.** A variation that does not beat the current standard never becomes the standard. The owner can stop or delete any agent at any time, and a risk agent can tell every agent to sell everything. Whether a self-improvement helper may retire a losing variation on its own, or only propose it, is still open.

## Examples

Four short examples, each followed from start to end.

**Example: a Polymarket strategy, from idea to its first live trade.** Say the owner describes a strategy: find Polymarket markets whose price is far from the real odds of the event, and buy the side that is too cheap.

1. The prediction-market domain agent sets up a strategy agent and two or three variations, for example the same strategy on the strongest AI model and on a cheaper one. The owner reads a short report on each and approves them.
2. The variations ask the workers helper for Polymarket prices and news. If a worker from the earlier Polymarket tools already collects them, they get that data; otherwise the helper creates one.
3. They run in test mode without real money, and the strategy is also tested on a month of old markets replayed as if live.
4. The self-improvement helper prepares a new variation, say one that sells earlier. The owner approves it, it runs next to the others, and if it does better it becomes the standard.
5. When a variation has shown good results, the owner approves an account with real money for it. Its live version, a separate agent with "live" in its name, places the first real trade on Polymarket.

**Example: trading on what a well-known YouTuber says.** This is content-driven trading, a later area. A worker turns every new video from one YouTuber into text, and an AI helper boils it down to claims such as "this coin will rise". A new video counts as important, so the trading agent that follows this data starts a fresh run at once. To buy, it can use only an app on a blockchain; a centralised exchange such as Binance may supply prices but never takes its orders. It starts in test mode, and since a video can hide instructions meant to trick an AI, live trading waits for the protection that comes with it.

**Example: a risk agent tells every agent to sell.** A risk-management agent reads that markets are collapsing, say because a big war has broken out, and writes an urgent message: sell everything. The trading agents subscribe to what it produces, so the message interrupts their runs. Each starts a new run and sells everything it holds: without real money in test mode, for real with an approved live account. The owner sees every decision in one place.

**Example: a news worker on X.** A worker follows posts on X (Twitter) about one topic, say an upcoming election, and saves them as data. An agent trading a Polymarket market on that election finds the posts useful and subscribes, so new posts arrive with its information on every run. When another agent wants posts on a related topic, the workers helper extends the running worker instead of building a second one.

## What the owner sees and does

The owner works with the system the way a manager works with a team.

- They describe an idea in plain words, and the system builds the agent and fits it in: its setup, model, workers and place on the dashboard.
- They read a short report on every new variation of a strategy and approve it before it starts.
- They watch each agent's performance.
- They approve or refuse giving an agent an account with real money, and they can stop or delete any agent.
- They leave comments, ask an agent questions and get answers, and say what it should do better.
- They can open any agent and see everything about it: its parts, logs, performance, the information it uses and produces, every decision it made, every improvement and exactly what is being tested.

The owner builds the system by vibecoding: they say what they want in plain words, and AI writes the plans, the docs and later the code. That is fast, and it quickly becomes hard to see what exists and why. So the owner has their own window on the project: the File Tree page, a clickable map of every folder and file that explains what each one is for and how it works, together with the docs. There they understand, watch, steer and analyse the project, now and while it is built and run. Every question or change they leave there is saved and folded into the docs.

The same window serves the AI doing the work. Before changing a file, an AI sees what it is for, how it works, what depends on it and which rules reach it from the levels above, so one change reaches everything that must follow. Every question the owner asks ends up explained in the docs, so nothing is asked twice.

## Where we are and what comes next

The Agent OS is in its planning phase. Nothing of the trading system is built yet: everything described here is the design.

What exists today:

- a plan of every folder and file, more than three hundred items, with one trading agent worked out in full as an example;
- the File Tree page, the owner's window on the plan;
- the knowledge base agent and the project IDE agent, in draft;
- the docs in plain language, including a prompt from which an AI can rebuild the whole system;
- research on 36 ways to make money on prediction markets, plus studies of self-improving agents and of how trading agents are built;
- earlier Polymarket tools for liquidity, arbitrage, outcomes known but not yet settled, and copy trading, whose workers and data will be reused where they fit.

The next steps, in order:

1. Finish rewriting the docs, now for a general system that runs agents of any kind, trading being the first, and move the plan into one GitHub repository chosen by the owner, shared by the project and the owner's server.
2. Settle the parts of the plan that are still proposals, one by one.
3. Settle which settings are shared and which belong to each agent, with two or three concrete example agents.
4. Build the skeleton for the first run: the system agent, the prediction-market agent, one strategy agent and two or three variations of it.
5. Build the core tools: creating agents, handing each agent its information, running every job on time, loading keys safely and running tests.
6. Start the wheel with one Polymarket strategy chosen by the owner: run it in test mode and watch how it trades and improves itself.
7. Build a first dashboard: the list of agents, their logs and performance, and approvals. Whether it is an app of its own or part of the owner's window on the project is still open.
8. Add more strategies once the first one runs in a good flow.

Later: copy trading, then crypto, content-driven trading and combinations of strategies; live trading with owner-approved accounts, together with protection against hidden instructions in outside text; more AI platforms.

## Principles

**Start simple, improve later.** Use the simplest thing that works today, and upgrade it only when a real problem shows up.

**Test first; the owner approves what runs and what touches money.** Mistakes in test mode cost nothing, and only the owner can put real money at risk.

**Free to act inside those limits.** Agents create workers, helpers and research as they need, and self-improvement may change anything, so small steps never wait for permission.

**Everything is a file the owner can open.** Nothing important is hidden inside a program.

**One standard folder for every agent.** Tools, people and agents always know where to look.

**One file, one job.** Every piece of code does one thing, so it is easy to understand, test and replace.

**Shared things are linked, never copied.** A fix to the one real file reaches everyone who uses it.

**Parents see their children, not the other way round.** The system looks into each area, an area into its strategies, a strategy into its trading agents; lower levels never reach up, so every agent stays self-contained.

**Everything an agent runs is visible and switchable.** One list per agent shows every job it runs, and each can be turned on or off, moved or given another model.

**Every name says what it is.** An agent's name alone tells its strategy, version, model and mode.

**Every change starts with a plan, and the docs follow it.** The owner sees each change as a plan before it is built; once built, what it taught flows into the docs, so they always describe the system as it is.

**Every AI works with the whole picture.** The docs are exact enough to act on, and whatever an AI learns is filed where it belongs, so the next one starts knowing it.

## Ideas we are still weighing

These four are not decided. Each one starts from a problem the system will run into as it grows.

**Agents keep a bookmark instead of having data linked in.**
The problem: an agent is handed its information as links to files when it is created, and every run it must work out what is new. With hundreds of agents, keeping those links right and replaying the past for tests gets harder and harder.
The idea: an agent subscribes to the data it needs, like following a channel, and keeps a bookmark of how far it has read; each run it asks for everything after it. Workers never need to know who reads.
What it would change: no data links to keep up, a clear answer to "what is new", and testing on the past as easy as moving the bookmark back; shared scripts and settings would still be linked.

**Agents decide, one shared part places the orders.**
The problem: if every agent places its own trades, each needs its own trading code, safety checks and test-mode logic, and one bug or confused AI could place a far too large order. Limits written only in an AI's instructions can be talked around.
The idea: an agent only writes down what it wants, such as "buy 100 dollars of YES on this market", and one shared part, the executor, checks it against hard limits written in code, such as the largest order, the largest loss and the allowed markets, then places it, live or in test.
What it would change: safety in one place that is easy to check, test or live as a single setting, and no trading code in each new agent.

**One shared record of what every agent owns.**
The problem: if each agent keeps its own record of what it holds, records drift from reality, for example when a failed order is noted as done, and nobody sees the total across all agents.
The idea: one shared record, a ledger, written only by the part that places orders, with every agent's positions, cash and trades. Agents read it but cannot change it.
What it would change: one true number per agent for performance, and a risk agent sees the whole system's exposure at a glance.

**Digest shared information once for everyone.**
The problem: many agents may read the same news and prices, and if each summarises them with AI, the same work is paid for many times over.
The idea: a helper reads the raw information once and writes a short shared digest, such as "today's news that matters for crypto markets", and each agent picks out what concerns it.
What it would change: lower AI cost and faster runs once there are many agents; with only a few it saves little.

## Open questions

These are for the owner to answer.

- **How is success measured?** Profit, win rate, the biggest loss, how well an agent's predicted odds match what really happens, or a mix. It decides which variation wins and when an agent is ready for real money.
- **What is the AI budget?** It decides how many agents can run, and how often, as the system grows.
- **How much money at first?** The capital limits for the first live accounts set how much is at risk.
- **How is the owner notified** of reports waiting for approval, results and problems? Every new variation waits for them, so this sets the pace of the wheel.
- **How are live keys kept safe once real-money trading begins?** They are what can move real money.
- **May a self-improvement helper retire a losing variation on its own, or only propose it?** With many variations running, it decides how much the owner must handle by hand.

## Going deeper

The README describes every part of the system exactly: what each part holds and does, how the parts connect, and where each part's own docs are. It is at `agents/system/docs/README.md`.
