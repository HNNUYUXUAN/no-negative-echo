# No Negative Echo

面向 Codex 的自然表达、持续协作、对外成稿与根因修复技能。版本 **2.0.0**。

技能围绕当前目标组织回答和实现，通过按需读取的中英文模块，帮助代码、文档及交付说明一致表达已确认的成果。

## 能力

| 场景 | 行为 |
|---|---|
| 自然表达 | 先回答问题，按读者需要展开，纠正落实到后续输出 |
| 持续协作 | 推进已授权工作，报告实质发现，按实际使用路径验证 |
| 对外成稿 | 成果介绍写清能力、机制与收益，适用条件准确明确 |
| 根因修复 | 修正产生错误的抽象、数据流、接口或状态，使实现自洽 |

成果介绍集中表达成果与收益。问题分析、历史比较、风险评审与迁移说明按各自目的组织内容。Commit 和 PR 描述当前行为，并保留读者需要的触发条件、兼容影响及验证事实。

## 安装与调用

```bash
git clone https://github.com/HNNUYUXUAN/no-negative-echo.git
cd no-negative-echo
python -I -B scripts/install_skill.py --expected-provenance-sha256 41e324f77249235fc34c61388ceba3dd9230938bf19b14eb1af21c4f1eaddf4f --agent codex
```

从上游安装迁移时，先按 [INSTALL.md](INSTALL.md) 的来源迁移步骤保存旧版本。调用方式：

```text
使用 $no-negative-echo 完成本次任务。
```

日常规则由 Codex 执行。Python 3.10+ 用于安装、可选扫描和开发测试。技能被列出、原生加载、行为改善是分别验证的状态；更新后开启新会话加载新版。

## 开发与证据

- [验证记录](VALIDATION.md)
- [研究来源](research.md)
- [12 个对照回放任务](evals/fork-prompts.jsonl)
- [回放结果](evals/replay-results.json)
- [上游评测协议](evals/evaluation-protocol.md)

```bash
python -I -m unittest discover -s tests -p 'test_*.py'
python evals/run_fork_replay.py
```

回放脚本使用本机 Codex CLI 和当前账号额度，启动 40 次独立文本任务，将中间记录保存到仓库外的工作目录。语义回放、确定性测试和原生激活分别记录，结果仅覆盖记录中的环境与用例。

本 fork 由 HNNUYUXUAN 维护，基于 [LB623/no-negative-echo](https://github.com/LB623/no-negative-echo) 的提交 `eba9f1d2`，保留原作者署名与 [MIT License](LICENSE)。[English](README_EN.md)
