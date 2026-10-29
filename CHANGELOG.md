# Changelog / 版本记录

## 2.1.1 — 2026-10-29

- 开场规则前置到核心入口；必要技能告知与具体任务动作合并，过程消息提供实际任务信息。Entry-level opening guidance combines required skill notices with concrete task information.
- 中英文表达与成稿规则逐句检查信息增量；结尾须提供具体后果、决策或行动。Sentence-level contribution checks consolidate repeated explanations; closing sentences contribute a concrete consequence, decision or action.
- 迁移步骤依据明确的主体与责任；缺少责任归属时使用结果验收，保留已确认的调用方操作。Migration steps follow established responsibility, using outcome checks for unspecified actors and preserving documented caller actions.
- 保留 2.1.0 升级识别，重新生成发布清单与 llms 全文。Retains v2.1.0 upgrade recognition and refreshes release metadata and the agent bundle.

## 2.1.0 — 2026-10-29

- 宿主中立的 Agent Skills 入口；保留四组双语规则与 Codex 界面元数据。Host-neutral entry with the four bilingual rule groups and Codex UI metadata.
- 提供六种本地 harness 的接入路径、通用项目说明和文本注入指南；原生行为证据按宿主记录。Integration paths for six local harnesses, project-instruction and text-injection guides, with host-specific evidence.
- 新增 llms 索引、可离线阅读的完整资料及双语使用/维护说明。Agent index, offline full reading bundle and bilingual usage/continuity guides.
- 运行包携带 MIT 许可；发布工具统一生成清单、摘要与阅读副本。Runtime license and deterministic metadata/bundle generation.
- 安装器保留 v2.0.0 来源识别；升级前保存用户改动和独立备份，更新后重新加载技能。Installer recognizes v2.0.0; preserve edits and an external backup, then reload after upgrade.

## 2.0.0 — 2026-10-29

首个维护版：自然表达、持续协作、对外成稿、根因修复四组模块；保留上游安装器和扫描器。Codex 回放与验证范围见 [VALIDATION.md](VALIDATION.md)。

First maintained release: four modular behavior groups, retaining the upstream installer and scanner. Codex replay evidence is scoped in [VALIDATION.md](VALIDATION.md).

## Upstream baseline

Based on LB623/no-negative-echo at `eba9f1d2`; original MIT attribution is retained. Git history preserves the inherited source.
