# Agent harness integration

[中文](../zh-CN/harnesses.md) · [Usage](usage.md) · [Installer](../../INSTALL.md)

The core consists of readable `SKILL.md` instructions and bilingual modules. The host discovers skills, selects a model, supplies tools and enforces permissions. The skill guides expression and delivery. Daily use needs only text loading; the optional scanner and repository installer use the Python 3.10+ standard library.

## Choose an integration

Paths below come from host documentation or this repository's existing Codex records, checked on 2026-10-29. Each is a skill root: installation creates `no-negative-echo/SKILL.md` beneath it. These are local paths; cloud and ephemeral environments use their product's project configuration.

| Host | User skill root | Repository integration | Evidence |
|---|---|---|---|
| Codex | `~/.agents/skills` | `--agent codex` | Existing Windows text replays and fresh-session invocation; loading evidence is scoped in [Validation](../../VALIDATION.md) |
| Claude Code | `~/.claude/skills` | `--agent claude` | [Official locations and invocation](https://code.claude.com/docs/en/skills); native behavior untested here |
| Cursor | `~/.cursor/skills` | `--agent cursor` | [Official skills guide](https://cursor.com/docs/skills); native behavior untested here |
| Gemini CLI | `~/.gemini/skills` | `--agent gemini` | [Official skills guide](https://geminicli.com/docs/cli/skills/); native behavior untested here |
| GitHub Copilot CLI | `~/.copilot/skills` | `--agent copilot` | [Official skills guide](https://docs.github.com/en/copilot/concepts/customizations/agent-skills); native behavior untested here |
| OpenCode | `~/.config/opencode/skills` | Custom destination below | [Official skills guide](https://opencode.ai/docs/skills/); native behavior untested here |
| WorkBuddy and custom harnesses | Use the host's current configuration | Local file reading or text injection | Recipient validation pending |

See [INSTALL.md](../../INSTALL.md) for commands and the version's checksum. Choose one applicable location. Some hosts also read `.agents/skills` or `.claude/skills`; check whether an existing shared installation is already discovered and keep one effective source.

For project-local OpenCode installation, enter the target project. In Bash, set `SOURCE` to the absolute path of this checkout and `PIN` to the SHA-256 from that version's INSTALL.md:

```bash
SOURCE=/absolute/path/to/no-negative-echo
PIN=REPLACE_WITH_SHA256_FROM_INSTALL_MD
python -I -B "$SOURCE/scripts/install_skill.py" \
  --expected-provenance-sha256 "$PIN" \
  --skills-dir "$PWD/.opencode/skills" \
  --discovery-root "$PWD/.opencode/skills"
```

When an applicable project or user location already contains a same-named skill, include its actual discovery root with another `--discovery-root`. PowerShell users can use absolute paths and a single-line command, for example `C:/Projects/demo/.opencode/skills`.

## Native skills, project instructions and plain text

**Native skills.** Install the complete `no-negative-echo/` directory, retaining references, LICENSE and provenance. Invoke `$no-negative-echo` in Codex or `/no-negative-echo` in Claude Code. Elsewhere, use the host's skill selector or explicitly request “Use no-negative-echo for this task.” `agents/openai.yaml` supplies Codex UI metadata; other hosts can use the standard skill entry point.

**Project instructions only.** Place the complete skill in a chosen project directory, such as `vendor/no-negative-echo/`. Merge a pointer into the existing instructions according to the host's rules, adjusting the path:

```text
This project uses no-negative-echo for answers, collaboration, public writing
and repairs. For relevant tasks, read vendor/no-negative-echo/SKILL.md and
its linked modules for the task and language. Follow host permissions and
the user's authorization.
```

The entry point may be AGENTS.md, CLAUDE.md or another file the host actually loads. Confirm that entry point and retain the project's existing conventions.

**No file tools.** Select the `SKILL.md` section and relevant language modules from [llms-full.txt](../../llms-full.txt) and place their text in permitted task context. Include the high-assurance section when applicable. Record the version and source sections for reproducibility. The llms files supply reading material; the host must still load or inject the content.

## Recipient acceptance

Record three states separately: `files_installed` (matching files), `skill_loaded` (observable host loading) and `task_passed` (an actual acceptable result). If only output is observable, record loading as unknown and evaluate that output separately.

Complete a [usage example](usage.md), then a representative task of your own. Record host/model versions, OS, installation scope, invocation, modules, output or diff, and actual checks. When reporting a problem, include a minimal input and the affected excerpt with sensitive information removed.

For a new host, confirm its official paths, loading and permission rules, validate the integration, then update this table and validation records. The [Agent Skills specification](https://agentskills.io/specification) provides the reusable entry format.
