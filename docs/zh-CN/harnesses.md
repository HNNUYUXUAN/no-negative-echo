# 接入 agent harness

[English](../en/harnesses.md) · [使用说明](usage.md) · [安装器](../../INSTALL.md)

核心是可读取的 `SKILL.md` 与中英文规则模块。宿主负责发现技能、选择模型、提供工具和管理权限；技能负责指导表达与交付。日常使用只需读取文本。可选扫描器和仓库安装器使用 Python 3.10+ 标准库。

## 选择接入方式

以下路径来自宿主公开文档或本仓库既有 Codex 接入记录，核对日期为 2026-10-29。表中路径是技能根，安装后应包含 `no-negative-echo/SKILL.md`。这些是本地接入路径；云端或临时工作区按对应产品的项目配置加载。

| 宿主 | 用户级技能根 | 本仓库接入方式 | 验证依据 |
|---|---|---|---|
| Codex | `~/.agents/skills` | `--agent codex` | 已有 Windows Codex 文本回放与新会话调用记录；加载证据范围见[验证记录](../../VALIDATION.md) |
| Claude Code | `~/.claude/skills` | `--agent claude` | [官方目录与调用说明](https://code.claude.com/docs/en/skills)；本机原生行为待测 |
| Cursor | `~/.cursor/skills` | `--agent cursor` | [官方技能说明](https://cursor.com/docs/skills)；本机原生行为待测 |
| Gemini CLI | `~/.gemini/skills` | `--agent gemini` | [官方技能说明](https://geminicli.com/docs/cli/skills/)；本机原生行为待测 |
| GitHub Copilot CLI | `~/.copilot/skills` | `--agent copilot` | [官方技能说明](https://docs.github.com/en/copilot/concepts/customizations/agent-skills)；本机原生行为待测 |
| OpenCode | `~/.config/opencode/skills` | 下方自定义目录命令 | [官方技能说明](https://opencode.ai/docs/skills/)；本机原生行为待测 |
| WorkBuddy、自定义 harness | 以当前宿主配置为准 | 本地文件读取或文本注入 | 待接收者验证 |

安装命令与版本校验值见 [INSTALL.md](../../INSTALL.md)。只选择一个适用位置。部分宿主也读取 `.agents/skills` 或 `.claude/skills`；已有共享安装时先确认它是否被当前宿主识别，保留单一生效来源。

OpenCode 的项目级接入示例：先切换到目标项目，在 Bash 中将 `SOURCE` 设置为本仓库克隆的绝对路径，将 `PIN` 设置为该版本 INSTALL.md 中的 SHA-256。两者都是本地发布信息。

```bash
SOURCE=/absolute/path/to/no-negative-echo
PIN=REPLACE_WITH_SHA256_FROM_INSTALL_MD
python -I -B "$SOURCE/scripts/install_skill.py" \
  --expected-provenance-sha256 "$PIN" \
  --skills-dir "$PWD/.opencode/skills" \
  --discovery-root "$PWD/.opencode/skills"
```

若相关项目或用户目录已有同名技能，把实际参与发现的根目录一并传入 `--discovery-root`。Windows PowerShell 用户使用绝对路径和单行命令，路径示例为 `C:/Projects/demo/.opencode/skills`。

## 原生技能、项目说明与纯文本

**原生技能。** 安装完整 `no-negative-echo/` 目录，保留 references、LICENSE 和来源清单。Codex 可用 `$no-negative-echo`；Claude Code 可用 `/no-negative-echo`。其他宿主使用其技能选择器或明确要求“使用 no-negative-echo 完成此任务”。`agents/openai.yaml` 提供 Codex 界面元数据，其他宿主可依据标准入口读取规则。

**只有项目说明入口。** 将完整技能放入项目中选定的普通目录，例如 `vendor/no-negative-echo/`。在已有项目说明文件中按宿主规则合并以下段落；路径随实际位置调整：

```text
本项目在回答、协作、对外成稿和修复任务中使用 no-negative-echo。
开始相关任务时，读取 vendor/no-negative-echo/SKILL.md，
再按语言和任务读取其中链接的模块；遵循当前宿主权限与用户授权。
```

合并位置可能是宿主支持的 AGENTS.md、CLAUDE.md 或其他说明文件，须先确认该宿主实际读取的入口。保留项目已有约定。

**没有文件工具。** 从 [llms-full.txt](../../llms-full.txt) 选取 `SKILL.md` 和本次语言的相关模块正文，放入宿主允许的任务上下文；需要高保证收尾时再附对应章节。保存版本号和选取的源章节，便于复现。llms 文件提供阅读资料，宿主仍需显式注入或加载这些内容。

## 接收端验收

依次记录三个状态：`files_installed`（文件一致）、`skill_loaded`（宿主可观察加载）、`task_passed`（实际任务达标）。仅能观察到输出时，将加载状态记为 unknown，并单独评价输出。

使用[使用说明中的样例](usage.md)完成一轮实际任务，再运行自己的代表性任务。记录宿主/模型版本、操作系统、安装范围、调用方式、模块、输出或 diff 和实际检查结果。分享问题时附最小输入和有问题的片段，并移除敏感内容。

扩展新宿主时先核对其官方目录、加载和权限规则，完成本地接入验证，再更新此表与验证记录。[Agent Skills 规范](https://agentskills.io/specification)提供可复用的入口格式。
