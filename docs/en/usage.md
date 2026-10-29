# Use no-negative-echo

[中文](../zh-CN/usage.md) · [Harness integration](harnesses.md) · [README](../../README_EN.md)

Install the complete skill or provide its text through the integration guide. State the intended result, required material and acceptance criteria. After loading `SKILL.md`, the host selects modules for the task. Chinese conversations use `zh-CN`; other conversations default to `en`.

## Start with a task

```text
Use no-negative-echo to introduce this tool to prospective users:
it backs up local directories daily, stores only changed blocks,
and restores by date. Explain the capabilities, method and practical use
in about 50 words.
```

An acceptable example:

> Daily incremental backups store changed blocks from local directories, reducing duplicate storage. Restore by date to recover the version you need.

Check that all three capabilities remain, benefits follow from the supplied mechanism, and quantified promises have data. This example illustrates acceptance; actual wording can vary.

## Match the task

| Task | Supply | Check the result |
|---|---|---|
| Answers and corrections | Current question and accepted facts or constraints | Answer addresses the question; subsequent results apply corrections |
| Ongoing collaboration | Authorized scope, deliverable and acceptance criteria | Work progresses within scope; progress and completion have evidence |
| Public writing | Audience, format, implemented capabilities and measured or usage evidence | Outcomes, methods and benefits are clear; applicability is accurate |
| Root-cause repairs | Minimal reproduction, expected behavior, accessible source and tests | Repair addresses the source, implementation and explanation agree, and the usage path passes |

For an engineering task: “Fix inconsistent task state; inspect its source and update paths, then verify start, stop and state reading.” During corrections, supply the new fact directly, such as “The server returns task state; use it as the single source,” and carry it into implementation and explanation.

## Select what to load

The entry point routes to four bilingual modules that can be combined. Use expression for ordinary answers, add public-copy for writing, engineering for code, and collaboration for tool work. Resolve relative paths from the skill directory.

The text scanner checks contents and filenames for specified terms and helps find known omissions. Run `python /path/to/no-negative-echo/scripts/check_surface.py --help` for its interface. Assess semantics, facts and task completion against the actual artifacts.

Progress messages lead with a task action, finding or blocker; incorporate a single brief skill mention when the host requires one. Check each sentence of finished copy for new information and consolidate paraphrases. Migration steps follow established interface responsibility: verify the product's grouping outcome when the actor is unspecified, and preserve caller-side grouping when the source explicitly requires it.

## Feedback, upgrades and recovery

Reports should include skill version, host and model, invocation, minimal input, actual output and expected behavior. Remove sensitive data first. See the [evaluation protocol](../../evals/evaluation-protocol.md) for behavioral cases.

Before upgrading, preserve custom edits and an old copy outside discovery roots. Use that version's [INSTALL.md](../../INSTALL.md), then repeat a representative task in a fresh session. Compare files when conflicts occur; recovery is covered in the [maintenance guide](maintenance.md).
