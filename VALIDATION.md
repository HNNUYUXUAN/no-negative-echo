# 验证记录 / Validation

## 2.1.1 — opening, English copy and migration / 开场、英文与迁移

2026-10-29，Windows x64，Python 3.12.14，Codex CLI 0.165.0-alpha.1.2，默认模型 gpt-6-astra。

- 最终版本执行 123 项测试：115 通过、8 按平台条件跳过。覆盖安装、清单、扫描器、评分器及新增的三项 shell/MCP 模块读取证据回归。
- 最终修订完成 2 次英文定向实测，安装后完成开场、英文和迁移各 1 次实测，5 次均通过人工审读。均从宿主展开的用户消息核对完整技能入口，来源哈希与最终发布包一致。
- 前一候选执行 8 个通过案例，覆盖两次开场、两次英文、两次责任未知的迁移、一次责任明确的对照和一次自主工程修复。工程产物另经独立验证：现有两项测试、5 个金额边界、7 个非法输入及 3 行实际 CSV 通过。最终结尾规则调整后只重跑受影响的英文及安装代表案例，未将上述 8 个案例全部记作最终版本重跑。
- 两次英文失败记录和一次工程环境阻塞均保留。工程初次因项目 `.agents` 只读父目录下的额外可写目录配置而未完成命令执行；删除评测器多余权限后重跑成功。模型当时准确报告未完成部分。
- portable-skill-creator 结构检查通过。入口 4079 字节，双语模块均在 8192 字节内；发布生成器、补丁格式及更新文档本地链接检查通过。
- 本机安装最终 2.1.1，18 个运行文件与发布包逐字节一致；2.1.0 和中间候选均保留在技能发现目录之外。未发现本地运行文件修改冲突。
- 宿主要求的首次技能告知仍保留一次，并与任务信息合并。实测显式调用技能，未测试自动触发、其他宿主或跨设备效果。样例数量不足以推断长期稳定性或总体改善比例。

输入、逐条判断和分阶段输出见 [protocol](evals/refinement-protocol.md)、[review](evals/refinement-review.md)、[results](evals/refinement-results.json)；工程独立复核见 [engineering check](evals/refinement-engineering-check.json)。公开记录包含实际回答与产物，原始会话事件留在本地。

English: 123 tests ran (115 passed, 8 platform skips). Five final-revision native Codex checks passed manual review: two targeted English tasks and three installed-mode checks. Eight earlier candidate cases and their engineering evidence retain their original source hash. Two English failures and a sandbox-blocked engineering attempt remain recorded. All 18 installed runtime files match the final release; previous installations are preserved outside discovery directories. Required host notices remain, and automatic activation or other hosts were not tested.

## 2.1.0 — portability and documentation / 接入与文档

2026-10-29，Windows x64，Python 3.12.14，Codex CLI 0.165.0-alpha.1.2。

- 120 项测试：112 通过、8 按平台条件跳过。覆盖既有安装器、扫描器、评测器，以及新增的发布元数据一致性、离线重定位安装和历史清单形状检查。
- 从提交 `26127e86f9c75dd86a84bb54487978631ed0b591` 恢复 v2.0.0 运行包，在独立目录升级到 v2.1.0，全部运行文件与新发布包逐字节一致。安装器保留了旧版备份。
- 离线安装测试将运行包移至含空格和中文的目录，并阻止 socket 创建；安装和随包 LICENSE 校验通过。该测试覆盖本地文件路径，不代表所有操作系统或宿主均已验收。
- portable-skill-creator 结构检查通过；SKILL.md 为 3869 字节，各语言模块在 8192 字节内。依赖扫描未发现额外项；人工检查确认日常规则使用宿主文本读取，可选脚本使用 Python 标准库，安装过程无需上游网络访问。
- 中英文各执行 1 个 Codex 单轮成稿样例，均读取注入的新版入口与对应模块文本；输出保留给定能力和适用范围，未添加无依据的量化收益。输入、输出和源文件哈希见 [portability-smoke.json](evals/portability-smoke.json)。这验证文本注入路径，原生技能加载状态未测。
- 六种本地 harness 的目录或接入方式有对应文档依据。除 Codex 文本样例外，其余宿主原生行为和跨设备运行均待接收者验证，见[接入矩阵](docs/zh-CN/harnesses.md)。
- README 静态检查无 error/warning；新增使用、接入、维护与 llms 文档的本地链接均可解析。双语内容与实际代码人工核对。发布生成器检查通过。
- 本机 Codex 安装已更新至 2.1.0，运行文件逐字节核对通过，安装器将 2.0.0 备份保存在技能发现目录之外。新会话需按宿主方式重新加载。
- Chrome 页面检查覆盖普通桌面与手机宽度的浅色 README；按实测将场景表格改为段落，将图示交付为双语 SVG，并优化小屏字形。深色渲染检查受浏览器调试接口限制，本次未完成。GitHub Actions 本次未返回运行记录，以上测试结果来自本机。

English: 120 tests ran (112 passed, 8 platform skips). A relocated v2.0.0 installation upgraded byte-for-byte to v2.1.0. A socket-blocked runtime relocation test retained all files and the license. Two single-turn Codex text-injection writing samples passed manual review. Other hosts' native loading and behavior, other devices, and operating systems were not exercised locally. Historical v2.0.0 results below retain their original scope.

## 2.0.0 — original behavioral baseline / 原行为基线

日期：2026-10-29。版本：2.0.0。宿主：Windows x64，Codex CLI 0.165.0-alpha.1.2，Python 3.12.14。

## 已观察的检查 / Observed checks

- 单元测试117项：109项通过，8项按平台条件跳过。包含原安装器、扫描器、评分器测试以及新增包清单/语言模块检查。
- portable-skill-creator结构校验通过；入口与模块满足4096/8192字节限制，中英文步骤ID对应。依赖扫描结果为启发式记录；人工确认日常指令依赖Codex宿主，可选脚本使用Python标准库。
- 12个代表任务，上游与fork两条件，共40次回放，全部收到有效结构化输出。其中4个含对话历史的场景各重复3次。原16个上游用例保留。
- 独立审读40条结果：上游迁移样例1条存在未经依据的路径结构假设；fork样例未发现实质任务错误。此结果不构成普遍效果提升的统计证明。
- 8份返回代码经人工查看后执行断言：折扣公式边界和输入校验、单一状态及start/stop行为均通过。代码由收集器落盘，不能据此宣称代理自主编辑仓库验收通过。
- 本地安装完成逐文件回读，旧版已保存至技能发现目录之外。当前安装来源为HNNUYUXUAN fork。

## 方法与范围 / Method and limits

回放采用相同CLI参数、全新工作目录、手工注入对应技能文本，允许共享宿主技能目录；模型使用CLI默认值，事件未给出模型标识，记为unknown。对话历史以合成提示回放，未执行真实多轮持久会话。它与原生激活以及自主工程端到端任务分别记录。

本轮没有执行上游协议规定的完整四条件、双盲评分或独立holdout，也没有测量跨设备/其他宿主效果。发布范围为本机Codex开发版。

创建器bootstrap将WindowsApps路径统一视为不可用；本轮直接验证并使用官方捆绑Python 3.12.14执行创建器检查，未安装额外解释器。

Raw replay prompts and CLI events remain local working evidence. Published JSON includes task text, outputs and hashes; credentials and machine-specific working paths are excluded.

## 新会话调用 / Fresh-session invocation

安装后在新CLI会话显式调用技能，获得符合成果介绍要求的中文输出。事件只包含消息，未提供技能读取/激活的独立记录，因此原生激活状态记为unobserved；不能由输出措辞推定已加载。随后统一为LF并逐文件核对安装副本与发布包。
