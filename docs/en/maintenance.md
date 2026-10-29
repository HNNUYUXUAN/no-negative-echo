# Maintenance and continuity

[中文](../zh-CN/maintenance.md) · [Harness integration](harnesses.md) · [Changelog](../../CHANGELOG.md)

The maintained source is `HNNUYUXUAN/no-negative-echo`. A complete clone contains the runtime package, installer, rule sources, tests and evaluation material. Installation reads local files and the host reads the daily rules. LB623 remains credited in project origins and history. Upstream availability is outside the loading, installation verification and local test paths.

## Keep a maintainable copy

Keep a full Git clone as an ordinary directory and record the commit you use:

```bash
git clone https://github.com/HNNUYUXUAN/no-negative-echo.git
cd no-negative-echo
git rev-parse HEAD
git fsck --full
```

The `.git` directory retains commit history; preserve it and the license when sharing a complete offline checkout. For runtime-only distribution, share the complete `no-negative-echo/` directory, including LICENSE, modules and provenance. Personal records, credentials and configuration outside the release directory remain with their owners.

To continue on another service, create an authorized empty repository, add it as a remote to the preserved clone, and push the needed branches and tags. Distinguish the maintained source from historical origins. For all-ref replication, consult [GitHub's duplication guide](https://docs.github.com/en/repositories/creating-and-managing-repositories/duplicating-a-repository) and check the destination before a mirror write. Repository metadata, issues and attachments require separate migration; Git history preserves source and commits.

## Edit and publish

1. Work in a separate copy. Keep the entry point within 4096 bytes and each language module within 8192 bytes, with corresponding step IDs. Edit sources before regenerating derived material.
2. Update VERSION, CHANGELOG.md and README version text, and review dependency descriptions in `delivery.json`. Add runtime files to the installer's `RUNTIME_FILES` when needed. Preserve the previous release's provenance digest and exact file set in `PREVIOUS_PROVENANCE_RUNTIME_FILES` for upgrade recognition.
3. Run the commands below from the repository root. `--write` refreshes the bundled LICENSE, delivery version and inventory, provenance hashes, installer and documentation pins, and `llms-full.txt`. The default command checks consistency. This is a maintainer release-preparation tool.

```bash
python scripts/build_release.py --write
python scripts/build_release.py
python -I -m unittest discover -s tests -p 'test_*.py'
git diff --check
```

4. Perform recipient acceptance on affected hosts and record the platform, model, task, artifacts and untested scope in VALIDATION.md. Keep historical replays attributed to their original version; choose new behavioral cases according to the change.
5. Review the diff, version and license, commit, then push and create version tags within repository permissions. Recipients can pin a commit or tag and use the matching INSTALL.md checksum. Commit generated manifests and pins with their sources.

For additional hosts, begin with verified locations and integration instructions. Change the installer when an actual need exceeds its existing custom-destination interface.

## Upgrade and roll back

Keep an ordinary copy of the previous version outside discovery roots, for example in a separate `skill-backups` directory. Compare provenance and personal edits; the installer rejects unknown or modified existing runtime packages. Resolve conflicts before upgrading. Backups are an explicit maintenance step; temporary installer staging is not a long-term backup.

For rollback, preserve the current installation outside discovery, restore the saved version to the original location, check its files and start a new session. Repeat the same representative task. Follow the dedicated [INSTALL.md](../../INSTALL.md) procedure when migrating from the LB623 identity.

## Downstream maintenance

An unchanged copy of this maintained release retains its identity and integrity data. A downstream project publishing its own changes under a new source updates package identity and repository in the installer and provenance, plus documentation links. Retain MIT and LB623 attribution, and record the downstream version and validation. Treat a new identity as an explicit source migration.

[llms.txt](../../llms.txt) indexes the documentation; [llms-full.txt](../../llms-full.txt) is the generated reading copy. Edit the bilingual rules and guides, then rebuild the full bundle.
