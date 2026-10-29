# No Negative Echo

Version **2.0.0**. A Codex skill for direct expression, useful collaboration, public value writing and root-cause repairs. Chinese and English modules are read by task. [中文](README.md).

## Behavior

- Answer the current question and carry corrections into subsequent output.
- Continue authorized work, report substantive findings and verify the actual usage path.
- Organize public value introductions around capabilities, mechanisms and supported benefits.
- Repair the source of a defect and align implementation, configuration and documentation.

Problem analysis, historical comparisons, risk reviews and migration notes serve their stated purposes. Commits and PRs describe current behavior and include relevant triggering conditions, compatibility effects and verification.

## Install

```bash
git clone https://github.com/HNNUYUXUAN/no-negative-echo.git
cd no-negative-echo
python -I -B scripts/install_skill.py --expected-provenance-sha256 41e324f77249235fc34c61388ceba3dd9230938bf19b14eb1af21c4f1eaddf4f --agent codex
```

For an existing upstream installation follow the source migration steps in [INSTALL.md](INSTALL.md). Invoke `$no-negative-echo` and open a fresh session after an update. Daily instruction use requires the Codex host; Python 3.10+ supports installation, optional scanning and development tests.

## Evidence

See [VALIDATION.md](VALIDATION.md), [research.md](research.md), and the fork prompts, rubrics and replay results under `evals/`. `python evals/run_fork_replay.py` launches 40 independent Codex CLI text tasks using the current account quota and writes intermediate logs outside the repository. Manual content injection is evaluated separately from native activation. Deterministic tests do not prove model efficacy.

Maintained by HNNUYUXUAN. Based on [LB623/no-negative-echo](https://github.com/LB623/no-negative-echo), commit `eba9f1d2`, with original attribution and [MIT License](LICENSE) retained.
