# Local models: when and how

*Companion to Chapter 2, "Your Agent Stack", of* 1 Person, Billion Dollar Conglomerate *(2026 edition). Last reviewed: September 2026. Everything about hardware, models and runtimes here is as of late 2026 and will date quickly: check the linked official documentation before you buy or install anything.*

## What this is

The updated version of the 2025 draft's local setup. The first draft built a "command center" on the founder's own machine: local models, a home-made memory database and a home-made server tying them together. This folder keeps the useful core of that idea and drops the rest. It covers:

1. when running an open model on your own hardware makes sense, and when it does not;
2. a general setup path with an open-model runtime;
3. how to point the **same instruction files** your cloud agents read at a local model;
4. [`ask_local.py`](ask_local.py), a small script that sends your context files and a brief to a local model.

## When local makes sense

Chapter 2's advice is a hybrid: rent frontier agents for the work that needs them, run a local model for the specific jobs where privacy, volume or independence justify it, and keep your context in plain files so either can use it.

| Reason | Local is a good fit when... | Example job |
|---|---|---|
| Confidential or regulated data | A customer contract or the law forbids sending the data outside, or you handle health, legal or financial records | Summarizing client files; extracting fields from contracts |
| High-volume, simple work | The job is narrow, repeated thousands of times, and a small model does it well enough | Sorting feedback, tagging tickets, extracting invoice fields, transcription |
| Offline and sovereign work | Your internet is unreliable, or you want no dependency on a foreign provider | Anything that must keep running when the connection drops |
| Learning and experimentation | You want to understand how these systems behave | Trying prompts, comparing models, testing a golden set |

**When it does not.** Long, multi-step agent work and complex coding, where the frontier models on providers' servers still lead. And saving money: once hardware and your own time are counted, running models at home usually does not. As of late 2026, a capable local setup costs several thousand dollars, and memory prices rose sharply in 2026 because AI data centers are absorbing a large share of the world's memory chips.

## The questions to answer before buying anything

- [ ] Which specific jobs will run locally? Write them down. "Everything" is not an answer.
- [ ] What volume per month? Use the [cost worksheet](../cost-worksheet.md) to compare with the same job on a cloud small tier.
- [ ] Does a small open model do the job well enough? Test it first on a rented or borrowed machine, or on a laptop with a small model, using a golden set (below).
- [ ] What is the rule for which data may leave the machine, and how will folder structure enforce it?
- [ ] Who maintains it? Updates, backups and security are now your job for this machine.

---

## A general setup path

The steps below are deliberately generic. Runtimes change fast; follow the current official documentation for the one you choose.

### 1. Choose hardware by memory

The size of model you can run is set mostly by memory: on a desktop with unified memory shared by the processor and graphics, or on the memory of a dedicated graphics card. More memory runs larger models; faster memory runs them faster. Small models for sorting and extraction run on a good laptop. Models close to the frontier need workstation-class machines. Appendix A of the book lists example machines and prices as of late 2026.

### 2. Install an open-model runtime

A runtime is the program that loads an open model and serves it on your machine. As of late 2026, a widely used example is **Ollama**, which runs on macOS, Windows and Linux and has an engine for Apple Silicon.

- Official site and downloads: <https://ollama.com>
- Documentation: <https://github.com/ollama/ollama> (see the docs folder and README)

Install it following the official instructions for your operating system. Other runtimes exist; the rest of this guide works with any runtime that serves a model over a local web address.

### 3. Choose and download a model

- Pick an **open-weight** model sized for your memory and your job. Examples of local-class open models as of late 2026 include Google's Gemma 4 family, Qwen3.8-27B and OpenAI's gpt-oss models (see Appendix A).
- **Read the license.** Many open models use permissive licenses that allow commercial use; some models, especially some image models, do not. Check before any commercial use.
- Download models only from the runtime's official library or the model maker's official page.
- **Pin the version.** Record the exact model name and tag you tested, so an update cannot change behavior silently (security baseline rule 5).

### 4. Test it by hand

Run the model from the runtime's command line or app and give it three real examples of the job. If it cannot do three by hand, it will not do three thousand in a script.

### 5. Serve it on your machine only

Runtimes serve the model at a local web address (for Ollama, by default, on `localhost` port 11434; check the current docs). Keep it that way:

- [ ] The runtime listens only on your own machine, not on your network or the internet.
- [ ] No keys, passwords or customer card data in any file the model reads.
- [ ] The machine has full-disk encryption, a strong login and two-factor sign-in on its accounts.
- [ ] Confidential data lives in a folder that no cloud-syncing tool or cloud agent can reach.

### 6. Connect your tools

Many runtimes, including Ollama, also offer an endpoint that follows the same request format as a widely used cloud API ("OpenAI-compatible"). That lets scripts and some agent tools switch between a cloud model and a local one by changing an address and a model name. Some coding and work agents can be pointed at a local model this way; check each tool's documentation for local-model support. As of late 2026, recent Ollama releases also describe a one-command way to start a coding agent against a local model; see the Ollama documentation for the current form.

---

## Pointing the same instruction files at a local model

Your context kit and agent instructions are plain Markdown files (see [context-kit/](../../context-kit/README.md)). That is what makes them portable. There are three ways to use them with a local model.

**1. A harness that supports local models.** If your agent tool can use a local model, nothing changes: it reads the project's instruction file (`AGENTS.md`, `CLAUDE.md` or its equivalent) at the start of every task, whichever model sits underneath.

**2. A script.** For batch jobs (sorting, tagging, extraction), send the instruction file and the relevant context files as the standing instructions, and the item to process as the request. [`ask_local.py`](ask_local.py) does exactly this, with no dependencies beyond Python 3. Its default address (Ollama's `http://localhost:11434/v1/chat/completions`, the OpenAI-compatible endpoint) was verified 2026-09-26 against a local server, in both `--brief` and `--each` modes. Some reasoning models include their thinking text in the answer; if yours does, strip it or choose a model setting that leaves it out before a script checks the output.

**3. By hand.** Paste the instruction file at the top of a conversation in the runtime's app. Fine for experiments; not for anything recurring.

Three adjustments make local models behave better with your files:

- **Send less.** Local models often have smaller context windows than frontier models. Send the instruction file plus only the files the job needs (for a tagging job: the glossary and the tag list, not the whole kit).
- **Be more explicit.** Small models follow examples better than descriptions. Put two or three worked examples of the output in the instruction file.
- **Ask for a fixed format.** For extraction, ask for one line per item in a fixed format, so a script can check it.

## Test before you trust: the golden set

Before a local model takes over a job, run the same [golden set](../../playbooks/golden-sets/) through the cloud agent and the local model and compare (the [verification checklist](../../playbooks/verification-checklist.md) explains how golden sets work). Keep the local model on the job only if it matches the answers you know are right. Rerun the golden set whenever you change the model, its version or the instruction file.

| Case | Right answer | Cloud result | Local result | Match? |
|---|---|---|---|---|
| [Example 1] | [Known answer] | [Result] | [Result] | [Yes / no] |

## Where this breaks

- **Local for the wrong reason.** To save money, usually not. For privacy, volume or independence, yes.
- **A stale model.** Open models improve fast. Review your choice every six months against Appendix A.
- **An exposed runtime.** A model server reachable from the internet is an open door. Keep it on the local machine.
- **Unread licenses.** Check commercial terms before you use a model in the business.
- **Two sets of instructions.** If the local job gets its own copy of the rules, the copies drift apart. Point both at the same files.

## Related files

- [Cost worksheet](../cost-worksheet.md): compare local and cloud per task.
- [Permission matrix](../permission-matrix.md): list the local runtime and what it can read, like any other agent.
- [Agent instructions template](../../context-kit/agent-instructions.md).
