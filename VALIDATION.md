# 验证记录 / Validation

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
