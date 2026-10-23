# Proposal Producer

基于 Proposal 制作 SOP v1.10 的 Skill，版本 **0.1.0-trial**。

## 让 agent 自动下载安装

把下面这段话发给具有本地文件及命令执行能力的 agent：

> 请从 https://github.com/TokaiTieo/proposal-producer 克隆仓库，读取 README.md 和 AGENTS.md，使用可用的 Python 3 运行 install.py，将 proposal-producer 安装到我的用户级技能目录。完成后核对版本和文件，并检查 PPTX、DOCX、PDF 制作与渲染工具是否齐备。

```sh
git clone https://github.com/TokaiTieo/proposal-producer.git
cd proposal-producer
python3 install.py
```

`install.py` 是单文件安装器，内含完整原始Skill ZIP与18份文件的哈希清单，使用Python标准库自动解码、校验、解压并安装。没有Git时，下载本仓库的 install.py，保留完整文件后运行即可。

默认安装位置为 `~/.agents/skills/proposal-producer`。其他选项：

```sh
python3 install.py --project /path/to/project
python3 install.py --dest /path/to/skills
python3 install.py --dry-run
python3 install.py --update
```

相同内容重复安装返回 unchanged；不同版本更新需要 --update，旧版保存在技能发现目录之外。目录中完整保留SKILL.md、七份模板、SOP快照、references、scripts和agents。安装器不修改全局Python包或文稿工具。

## 使用

安装后在下一轮输入：

> 用 $proposal-producer，基于我提供的资料制作方案报价型提案。先整理方案与报价并提交内容确认，确认后生成 PPTX、SOW 和对应 PDF。

Codex未刷新列表时重启。用户级／项目级技能位置及调用方式依据 [OpenAI官方文档](https://learn.chatgpt.com/docs/build-skills)。其他宿主按其规范使用 --dest 并适配工具。

## 能力与环境

优先完整支持方案报价型：共用底稿、报价和回报计算、一次内容确认、所选源稿与PDF制作、跨文件检查及独立复核。商机／合作沟通、产品定义／立项保留已确认结构，尚未完成整稿验证。

辅助脚本使用Python标准库；PDF读取检查需要pypdf。实际制作需要宿主可用的演示文稿、文档及PDF能力、源稿导出／逐页渲染工具和中文字体。本版macOS试用使用过LibreOffice和Poppler。安装文件成功与本机文稿链可用分别检查。

原试用以虚构客户生成8页中文PPTX、SOW DOCX及双PDF，做过独立重算、编辑保存重开和视觉返修。未测试真实客户交付及其他操作系统，复杂报价和现金回报模型尚未验证。没有复核方时可制作候选，保留待复核状态。

仓库未包含客户ref、账号凭据、Office引擎或字体。当前是小范围试用版，未发布为插件商店产品。

## 验证

```sh
python3 test_install.py
python3 ~/.agents/skills/proposal-producer/scripts/test_proposal.py
```

安装测试不写用户全局目录；Skill中原生PPTX测试需要当前Python环境有python-pptx。安装器内的RELEASE字段列出版本、ZIP及每个文件哈希，ARCHIVE_BASE64保存原ZIP。安装时验证所有18份文件后再写入目标。
