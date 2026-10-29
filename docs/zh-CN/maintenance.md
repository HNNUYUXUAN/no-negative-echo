# 维护与接续

[English](../en/maintenance.md) · [接入宿主](harnesses.md) · [版本记录](../../CHANGELOG.md)

本项目的维护源为 `HNNUYUXUAN/no-negative-echo`。完整克隆包含运行包、安装器、规则源文档、测试和评测资料；安装器使用本地文件，日常规则通过宿主读取。LB623 上游保留在项目来源和历史记录中。上游的在线可用性不参与技能加载、安装校验或本地测试。

## 保留可维护副本

保留普通目录形式的完整 Git 克隆，并记录使用的提交：

```bash
git clone https://github.com/HNNUYUXUAN/no-negative-echo.git
cd no-negative-echo
git rev-parse HEAD
git fsck --full
```

完整克隆中的 `.git` 保存提交历史；离线分发完整仓库时保留该目录和许可证。仅分享运行包时，交付完整 `no-negative-echo/` 目录，其中的 LICENSE、模块和来源清单随包保存。发布目录之外的个人记录、凭据和配置由各自所有者管理。

需要在另一服务接续时，先创建自己有权限的新空仓库，再从保留的克隆添加新的 remote，推送所需分支与标签。保留维护源与历史来源的区分；需要复制全部引用时参考 [GitHub 仓库复制说明](https://docs.github.com/en/repositories/creating-and-managing-repositories/duplicating-a-repository)，核对目标内容后再执行镜像写入。仓库托管元数据、议题和附件需单独迁移，Git 历史覆盖源码与提交。

## 修改与发布

1. 在独立工作副本中修改。核心入口最多 4096 字节，各语言模块最多 8192 字节；两种语言保留对应的步骤 ID。先完善源文件，再生成派生资料。
2. 更新 VERSION、CHANGELOG.md 与 README 的版本说明；调整 `delivery.json` 中的依赖说明。新增运行文件时同步安装器的 `RUNTIME_FILES`。保留前一发布的来源摘要及准确文件集合到 `PREVIOUS_PROVENANCE_RUNTIME_FILES`，以便识别升级来源。
3. 从仓库根运行下方命令。`--write` 根据明确的文件清单更新随包 LICENSE、delivery 版本和清单、来源哈希、安装器与文档校验值，以及 `llms-full.txt`；默认命令只检查是否一致。该工具用于维护者准备发布。

```bash
python scripts/build_release.py --write
python scripts/build_release.py
python -I -m unittest discover -s tests -p 'test_*.py'
git diff --check
```

4. 对变更涉及的宿主完成接收端验收，在 VALIDATION.md 记录平台、模型、任务、产物与未测范围。旧版回放作为旧版证据保留；按变更风险选择新的行为用例。
5. 审阅 diff、版本与许可后提交；按仓库维护权限推送并创建版本标签。接收者可固定到提交或标签，并使用同版本 INSTALL.md 的校验值。发布前生成的清单和校验值应随源码一起提交。

新增宿主优先补充已核对的目录和接入说明；只有出现现有自定义目录接口无法表达的真实需求时，再改安装器。

## 升级与回滚

保留上个版本的普通目录副本到技能发现范围之外，例如单独的 `skill-backups` 目录。对比来源清单并检查个人改动；安装器会拒绝不认识或被修改的已有运行包。先解决冲突，再执行升级。备份是显式维护步骤，安装器的临时 staging 不作为长期备份。

回滚时，将当前安装移到发现范围之外供检查，把保存的上一版本放回原位置，核对文件并启动新会话。使用同一个代表性任务检查恢复结果。跨 LB623 来源迁移按 [INSTALL.md](../../INSTALL.md) 的专门步骤处理。

## 下游重新维护

继续发布此维护源的原样副本时，保留其包身份和校验信息。下游若自行修改并以新维护源发布，更新安装器与来源标记中的包身份、来源仓库以及文档链接，保留 MIT 许可和 LB623 署名；记录自己的版本和验证结果。新身份按显式来源迁移处理。

维护者可从 [llms.txt](../../llms.txt) 定位文档；[llms-full.txt](../../llms-full.txt) 是自动生成的阅读副本。双语规则与使用说明是编辑源，完整阅读副本由脚本重建。
