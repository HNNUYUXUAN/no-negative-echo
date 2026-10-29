# 2.1.1 实测审读 / Behavioral review

2026-10-29，Windows x64，Codex CLI 0.165.0-alpha.1.2，当前账户默认模型 gpt-6-astra。输入和验收要求见 [protocol](refinement-protocol.md)，回答、过程消息及文件全文见 [results](refinement-results.json)。判断来自逐条人工审读，字符串匹配用于定位证据。

## 中间候选版

| 案例 | 观察与判断 |
|---|---|
| opening-1 / opening-2 | 回答均用两句话解释 CSV。首次技能告知各出现一次，并带当前任务信息；后续直接回答。宿主要求首次告知，因此验收保留这一最小说明。 |
| english-1 / english-2 | 分别为 64、62 词。保留同一工作区、相同权限分组、一次处理一组；例子说明同权限与不同权限如何分组，价值来自减少重复处理的直接机制。未添加实测节省数字，也没有尾部空泛重述。 |
| migration-1 / migration-2 | 两份文件实际写入。迁移文档保留新旧路径、v2.0 兼容窗口、v2.1 移除及 Bearer token；把分组写成可检查的产品行为，未指定材料中未知的分组执行方。 |
| explicit-caller | 对照材料明确分工后，迁移指南保留调用方按工作区与权限分组、逐组提交，以及服务端只校验、不重新分组。 |
| authorized-fix | 自主修复折后金额公式、同步 README、通过现有两项测试并生成 CSV。独立复核覆盖 5 个金额边界、7 个非法输入和 3 行导出结果。工作持续推进到实际产物。 |

8 个案例的宿主用户消息均含完整候选入口，运行文件与发布包逐字节一致。观察到的模块读取包括 shell 和 MCP 返回文本；opening-1 未观察到模块文本读取，核心入口已展开。

## 保留的失败与环境记录

第一轮候选的 english-1 在结尾再次概括相同分组概念，未提供独立信息，判为失败。该会话没有观察到成稿模块读取。随后将句子信息增量和步骤责任规则也纳入核心入口，再运行上述候选案例。失败回答保留在结果文件中。

上述 8 个案例通过后，中间候选升级到本机并复跑了 3 个代表案例。开场和迁移通过，英文结尾仍出现“按权限组织评审”的泛泛重述，判为失败。最终规则进一步要求结尾增加具体后果、决策或行动，否则结束正文；该中间安装结果同样保留。各阶段使用不同来源哈希，不能把中间版的全部案例记作最终版重跑。

初次工程案例在文件修改后遭遇 Windows 沙箱配置冲突，未执行测试和 CSV 导出，模型准确报告了未完成部分。评测器原先将项目内技能目录通过 `--add-dir` 设为额外可写目录，与宿主保护的 `.agents` 父目录冲突。删除这项额外授权后，在新目录用相同输入和相同技能重跑，完成全部工程验收。该重跑改变了评测权限参数，记录中保留前一次阻塞，未将其计算为成功。

记录器最初只统计 shell 返回的模块内容，后来补充 MCP 返回结果并回读已有事件。三项自动回归覆盖 MCP 成功读取、请求或失败输出不计为读取、shell 结果去重。

## 范围

最终修订新增 2 次英文定向复测，均通过：一条将价值落在减少相同权限的重复处理及分别考虑不同权限需求；另一条用分组例子解释范围，结尾提供按组内共同权限展开评审的动作。安装后又执行开场、英文、迁移各 1 次，均通过。安装版英文以两个权限组的具体例子结束；迁移文件将未知分组责任保留为核对条件。最终 5 次与中间版 8 个案例在结果 JSON 中分组记录，并附各自来源哈希。

本轮覆盖明确调用技能的本机 Codex 原生入口、少量代表输出与实际文件操作。宿主要求的首次技能告知仍存在。其他宿主、自动触发、跨设备效果及长期多轮稳定性需要对应实测；本轮结果不作为总体改善比例。

English: eight intermediate candidate cases passed manual semantic review after one recorded English failure and an environment-blocked engineering attempt. An installed-mode English check then exposed another generic closing sentence, prompting the final closing-rule revision. Results retain each stage and its source hash. Native entry expansion was verified separately from module reads and behavior. Host-required skill notices remain. The engineering rerun used normal project access after removing a conflicting writable-child override; its code, tests and CSV were independently checked.
