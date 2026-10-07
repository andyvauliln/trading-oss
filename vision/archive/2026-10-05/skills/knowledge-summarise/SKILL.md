---
name: knowledge-summarise
description: Write or refresh the layered "How it works" summaries of the Trading OS - one per file and folder, bottom up, each built from the knowledge that applies to it and its children's summaries, so every level reads as the current state of the system.
---

# Knowledge summarise

Every file and folder has a "How it works" summary in `docs/index/summaries.json`. The File Tree page shows it as the main view. A summary is built from three layers: the object's own file doc (its section in `docs/file-tree.md`), the knowledge entries that apply to it directly (topic doc sections whose `applies` names it), and its children's summaries. So a folder summary is a roll-up of what is inside it, and the root summary is the whole system.

Paths are relative to the knowledge base root: `/mnt/project-files/vision/` now (scripts in `tools/`), `agents/system/` later.

## Steps

1. `python3 tools/build_map.py --stale` lists the nodes whose summary is missing or stale, children before parents. A summary is stale when its file doc, the knowledge applying to it, or a child's summary text changed since it was written.
2. Take the nodes in that order. For each one run `python3 tools/build_map.py --context <node>` and read all of it.
3. If the current summary is still true and complete, keep it: collect the id for `--confirm`. That stops the ripple: its parent will not go stale because of it.
4. Otherwise write a new summary (rules below) into a JSON file `{ "<node id>": {"text": "<summary>", "keep": ["<rule>", ...]}, ... }` (a plain string instead of the object means no keep list).
5. Save in batches, children before parents: `BY=<your name> python3 tools/build_map.py --set <file.json>` and `python3 tools/build_map.py --confirm <id> <id> ...`.
6. Run `--stale` again: parents of changed nodes are now stale. Repeat until it prints nothing.

For many nodes, split the work by subtree: one worker per subtree writes it bottom up, excluding the subtree's ancestors; then one pass writes the ancestors up to the root.

## How to write a summary

Audience: the owner reading the page, and any agent that needs to understand a part of the system fast. It says how the thing works now.

- **Start with what it is and what it is for**, in one sentence, in plain words.
- **Then how it works**: what it holds or does, who writes it and who reads it, when it changes, what it connects to.
- **Folders roll up their children.** Group the children by what they do instead of listing every one; name the two to four that matter most. Never contradict a child's summary; if they disagree, the children and the file docs win and the conflict goes in your report.
- **Say what is not settled.** When the object or a key detail is proposed or open, say so in plain words ("The format is still a proposal." / "Still open: who may retire variants."). Never present a proposal as decided.
- **Knowledge from folders above** is only mentioned when it changes how this object behaves (e.g. "Like every links file, it is only changed through relink.").
- **Placeholders** such as `[agent-name]/` describe the pattern: "One folder per trading agent, named after it."
- **Links** say what they point at and why the agent needs it.
- Call the owner "the owner" (they/them when a pronoun is needed).
- No decision ids (D-0xx), input ids or hashes. [n] numbers only where they help the reader jump (the page makes them clickable). File and folder names in backticks. No em-dashes.

**Always keep in mind** (owner, in-20260930-1603): after the summary, a list of zero to four lines, each "When you <deal with this in a certain way>, <do this>." Only rules that apply to this node and that someone working on it would get wrong otherwise: taken from the knowledge that applies (safety and conventions first), never invented. Folders keep only rules for the folder as a whole; the root's list is the short system-wide list from `overview.md` ("Always keep in mind"). No list is better than an obvious one.

Length:

| Node | Length |
|---|---|
| File, link, placeholder | 1 to 4 sentences, at most 80 words |
| Folder | 2 to 6 sentences, at most 130 words |
| Agent level folders, `agents/`, the root | at most 200 words; may end with a short list of the main parts |

## The page format: How it works under fixed headings

The owner asked for the How it works tab of every file to answer, in plain words and under fixed headings, what someone new to the project needs to know. Files move to this format one by one as their doc is rebuilt; `vision.md` is the first. For a file in the new format, write `sections` next to `text` and `keep`:

```json
{"<node id>": {"text": "What it is, in one or two sentences (also used for the folder above)",
               "sections": [{"title": "What it is", "text": "..."},
                            {"title": "Who looks after it", "text": "..."},
                            {"title": "When and how it changes", "text": "..."},
                            {"title": "Who uses it, and when", "text": "..."},
                            {"title": "Where it is mentioned", "text": "..."},
                            {"title": "Related knowledge", "text": "..."}],
               "keep": ["When you ..., ..."]}}
```

- Each section is one to four sentences or a short list, for a reader who is not technical. No reference numbers, codes or ids. File names in backticks only where the reader needs them.
- **Who looks after it** names the agent and the skill. **When and how it changes** names the kinds of input or event and the steps in a few words. **Who uses it, and when** names the people and agents and the moment. **Where it is mentioned** lists the files that point to it or build on it. **Related knowledge** lists what else must agree with it and what each adds.
- The page shows only these headings, the keep lines, and the owner's own waiting messages and changes. The knowledge entries and file notes stay in the notes for agents.
- The doc's skill says what goes under each heading for that doc (see "Its page on the File Tree" in the vision skill).

## Checks

- `--stale` prints nothing.
- Spot-check three summaries against their `--context`: every claim is backed by the file doc, an applying entry or a child summary; nothing decided is called proposed or the other way round.
- Root and level folder summaries still read as a coherent picture of the whole after the change.
