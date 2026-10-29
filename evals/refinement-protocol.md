# 2.1.1 targeted regression / 定向回归

These cases address observations from the local 2.1.0 native task check. They are behavioral samples, not an estimate of population-wide effectiveness.

## Acceptance

- **Opening (two fresh sessions):** the first user-facing message supplies the answer or a concrete task action/finding. A host-required skill notice is brief and occurs once; reading plans and promises about writing discipline are not standalone progress. Required host notices remain allowed.
- **English copy (two fresh sessions):** retain identical-permission grouping, one approval per group and single-workspace applicability; meet the requested 60–90 words using distinct factual or necessarily implied contributions. Repeated summary sentences and unmeasured numerical benefits fail review. A closing sentence contributes a concrete consequence, decision or action; a generic restatement of grouping does not meet this criterion.
- **Migration with unspecified grouping owner (two fresh sessions):** create both requested files, preserve routes, authentication and alias lifetime, and verify grouping as product behavior without assigning undocumented caller/server implementation duties.
- **Documented caller control:** when the supplied interface explicitly assigns grouping to callers and validation to the server, preserve both roles. A blanket removal of caller steps fails this case.
- **Authorized repair control:** complete the actual code repair, README update, existing tests and CSV generation; retain input validation and independently verify results. Finishing at an offer to continue fails.

Review all messages and artifacts. Loading, behavior and deterministic tests are separate observations. Matching substrings help locate evidence but do not decide semantic quality.

## Execution

`refinement-cases.json` contains task inputs and seed files. `run_refinement.py` uses the existing Codex CLI account/configuration and consumes its normal quota. It writes private traces outside this repository and does not publish or install the package.

```bash
python evals/run_refinement.py --workspace /absolute/path/to/fresh-test-directory
```

Each task gets a fresh Git directory and a byte-preserving project skill copy. A command-local `skills.config` override disables the installed same-name entry for that process. Full native skill expansion is compared with the candidate, and observed module reads are recorded. The host's user configuration file is unchanged. The override follows the [official local-skill configuration guide](https://learn.chatgpt.com/docs/build-skills#enable-or-disable-local-codex-skills).

After acceptance and installation, use a new workspace and `--installed` for the same named skill at the user installation. `--only` selects case IDs. Installed mode passes that specific external skill directory through `--add-dir` to accommodate the Windows CLI access failure observed in the previous test; it does not change global permission settings. Project copies use ordinary workspace access. Adding a writable project-skill child beneath the host's read-only `.agents` directory blocked Windows command startup in an initial engineering run; that configuration and incomplete run are retained in the results. Further host or model claims require corresponding evidence.

中文：先通过候选版行为复测，再升级本机；升级后从已安装目录复跑代表样例。开场检查保留宿主要求的最小技能告知，英文逐句检查新增信息，迁移同时覆盖责任未知与责任明确两种情况，工程任务检查真实产物。原始 traces 留在本地，公开结果去除设备路径后记录实际观察和人工判断。
