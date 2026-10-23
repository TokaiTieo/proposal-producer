# Proposal Producer

基于 Proposal 制作 SOP v1.10 的试用 Skill，版本 **0.2.0-trial**。

把下面这段话发给具有文件及命令执行能力的 agent：

> 请从 https://github.com/TokaiTieo/proposal-producer 克隆仓库，读取 README.md 和 AGENTS.md，使用可用的 Python 3 运行 install.py，将 proposal-producer 安装到我的用户级技能目录。完成后核对版本和文件，按 requirements.txt 检查校验组件，再检查本机 PPTX、DOCX、PDF 制作与渲染工具。

```sh
git clone https://github.com/TokaiTieo/proposal-producer.git
cd proposal-producer
python3 install.py
```

安装器内含完整 Skill ZIP 和逐文件哈希，使用 Python 标准库解码、校验、解压并安装。没有 Git 时可下载完整 install.py 运行。默认位置为 `~/.agents/skills/proposal-producer`；其他宿主可指定技能目录：

```sh
python3 install.py --project /path/to/project
python3 install.py --dest /path/to/skills
python3 install.py --dry-run
python3 install.py --update
```

相同内容重复安装返回 unchanged；更新使用 --update，旧版保存在技能发现目录外。安装器不修改全局 Python 包、宿主权限或 hook 设置。

安装后的文件按职责分开：

| 文件 | 职责 |
|---|---|
| SKILL.md、references/*.md | 意图、背景、操作与工具说明 |
| contracts/policy.json | 类型、默认值、阈值、流程条件和执行边界 |
| contracts/fields.json、checks.json | 底稿字段、内容任务、检查项及映射 |
| contracts/sop-catalog.json、governance.json | SOP 结构化规则、可选治理 |
| assets/project.json、assets/templates/*.json | 项目和七份模板数据 |
| schemas/*.schema.json、schemas/templates/* | 字段、枚举、结构及取值约束 |
| scripts/proposal.py、contracts.py、gates.py | 计算、状态绑定、校验及放行门禁 |
| hooks/claude_stop.py | Claude Code 停止事件适配器 |
| scripts/test_*.py、evals/contracts.json | 正反例、回归及评测数据 |
| agents/openai.yaml、SKILL.md frontmatter | 宿主规定的技能元数据格式 |

机器规则使用 JSON；Markdown 不再维护字段表、数值阈值或检查清单。仓库使用内嵌 ZIP 分发，安装后展开为上述文件。

在任务所用 Python 环境中准备 requirements.txt 的组件后校验：

```sh
python3 ~/.agents/skills/proposal-producer/scripts/proposal.py validate --workdir /path/to/work
python3 -m unittest discover -s ~/.agents/skills/proposal-producer/scripts -p 'test_*.py' -v
```

安装后调用：

> 用 $proposal-producer，基于我提供的资料制作方案报价型提案。先提交内容确认，确认后制作所选 PPTX、SOW 和对应 PDF。

需要宿主刷新技能列表时，重新开启会话。制作依赖宿主可用的演示文稿、文档、PDF、导出渲染工具和中文字体。方案报价型已有四文件试用；其余已确认类型保留结构，尚未整稿验证。

0.2 版新增本地 release 门禁：检查当前确认、独立复核、适用项证据和测量阈值后生成放行记录。Claude Code 可通过 hook-config 命令生成项目设置片段，具体接入见安装后 references/enforcement.md。该适配器的协议已做模拟测试，未在实际 Claude Code 会话中验证。当前 Codex 会话使用命令门禁；宿主 hook 不会因安装自动启用。

本地 Schema 校验已接入命令；模型生成时的 constrained decoding 需要宿主另行传入 Schema。检查证据的真实性和语义结论仍由真实检查负责。脚本不代发客户文件。

旧版项目保留原件，按当前 Schema 补齐迁移字段并重新生成确认与复核记录；原始人类 SOP 及历史试用证据保持原版本。

GitHub Actions 使用只读仓库权限，运行安装校验、Schema 校验和行为测试。手动检查安装器：

```sh
python3 test_install.py
```

安装器内 RELEASE 记录当前版本、ZIP 哈希及文件哈希。仓库不包含客户 ref、账号凭据、Office 引擎或字体。
