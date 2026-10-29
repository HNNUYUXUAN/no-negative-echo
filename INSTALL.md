# Fork installation

Runtime version: 2.1.0. For host paths and invocation, see [Harness integration](docs/en/harnesses.md) / [中文接入说明](docs/zh-CN/harnesses.md). For an existing fork installation, preserve a backup outside discovery before upgrading; see [Maintenance](docs/en/maintenance.md).

The complete runtime directory includes its MIT license and referenced modules. The installer uses only files in this checkout and the Python standard library. A retained checkout can be installed offline. An official host installer can also install the complete runtime directory without running this repository's Python installer.

## Source migration from LB623

The fork has package identity `io.github.hnnuyuxuan.no-negative-echo`. An existing LB623 package is a separate source identity. Before migration, verify its provenance and every listed file against the recorded upstream baseline, and check for extra or user-modified files. Preserve conflicts for review.

Move the verified old directory to a unique backup outside all skill-discovery directories. Install the fork into the now-vacant target using the pinned digest below. If installation fails, preserve any partial new directory for diagnosis and restore the saved upstream directory. Compare copied bytes after activation. To roll back later, preserve the fork outside discovery and restore the verified backup; open a fresh session.

The same skill name remains available to callers. Never silently accept an unrelated same-name package.

# Install no-negative-echo

Install only the runtime Skill from
<https://github.com/HNNUYUXUAN/no-negative-echo>. Do not inspect, modify, or install
unrelated skills, packages, repositories, or host configuration.

## Default installation

If the host provides an official Skill installer, use it to install the
repository's `no-negative-echo/` subdirectory. On Codex, prefer
`$skill-installer` and verify discovery in a new session.

Otherwise, use the bundled installer:

1. Select the preset for the current local host:

   | Host | Preset | Default destination |
   |---|---|---|
   | Codex CLI / Codex desktop | `codex` | `~/.agents/skills` |
   | Claude Code | `claude` | `~/.claude/skills` |
   | Cursor | `cursor` | `~/.cursor/skills` |
   | Gemini CLI | `gemini` | `~/.gemini/skills` |
   | GitHub Copilot CLI | `copilot` | `~/.copilot/skills` |

   These presets apply to local hosts with persistent filesystems. Do not guess
   a destination for cloud, review, web, or ephemeral agents.

2. Clone the repository into a new temporary directory, then run from its root:

   ```bash
   python3 -I -B scripts/install_skill.py \
     --expected-provenance-sha256 7f5afc287bf98e3d52cdb33c934ed9385c800aa96276600b1cfc6a0967bff714 \
     --agent HOST_PRESET
   ```

   Replace `HOST_PRESET` with one value from the table. Python 3.10+ and Git
   must already be installed. Do not install dependencies, use elevation, or
   request credentials.

3. Treat exit status 0 plus the printed `Installed no-negative-echo to ...`
   path as successful file installation. If the host cannot reload Skills in
   the current session, report that discovery needs a new session; do not run
   unrelated work merely to prove activation.

4. Remove only the temporary clone created for this installation.

The bundled installer performs the package checks itself: it validates the
provenance marker, exact runtime manifest and file hashes, known conflicting
user-level locations, destination, staging, locking, and post-copy bytes. For a
normal release installation, do **not** duplicate that work by reading every
repository Python file, running the repository test suite, enumerating unrelated
Skill directories, or inspecting unrelated `package.json` files.

## Custom destinations and audits

For a custom destination, use only a documented Skill root for that host:

```bash
python3 -I -B scripts/install_skill.py \
  --expected-provenance-sha256 7f5afc287bf98e3d52cdb33c934ed9385c800aa96276600b1cfc6a0967bff714 \
  --skills-dir /absolute/path/to/skills \
  --discovery-root /absolute/path/to/skills
```

Add another `--discovery-root` only for a discovery root documented for that
host and relevant workspace. Do not search the whole machine for possible roots.

The provenance digest provides byte integrity, not publisher authentication.
Use a signed immutable release and a separately trusted digest when publisher
identity must be authenticated.

Run the repository's complete test suite or perform source review only when the
user explicitly requests an audit or the installation is part of a
high-assurance release process. If a local source has been modified or its
provenance is unrecognized, let the installer fail closed; audit that source as
a separate task instead of silently expanding a normal installation.

## Report

Return only the information needed to act on the result:

- file installation: succeeded or failed;
- installed path, or `none`;
- source commit;
- host discovery: verified or requires a new session;
- exact warning or recovery path printed by the installer, if any.

Do not claim current-session activation without host-native evidence.
