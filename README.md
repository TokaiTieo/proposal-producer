# Proposal Producer

基于 Proposal 制作 SOP v1.10 的试用 Skill，版本 **0.4.0-trial**。

可从本仓库安装，或把完整 `install.py` 发给其他 agent 执行；安装器自带完整 Skill，安装时核对版本与文件哈希。

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
| contracts/presentation-quality.json、assets/presentation-plan.json | 参考方法、页级问题、场景、机制、价值与费用对价 |
| assets/calibration.json、schemas/quality-review.schema.json | 关键页内部校准及最终质量评审结构 |
| assets/visual-kit/、assets/visual-profile.json、assets/render-policy.json | 通用视觉资源、任务风格和渲染路线 |
| contracts/fact-policy.json、scripts/facts.py、render_adapter.py | 共用事实、交付派生、实际导出与页面核对 |
| schemas/*.schema.json、schemas/templates/* | 字段、枚举、结构及取值约束 |
| scripts/proposal.py、contracts.py、gates.py | 计算、状态绑定、校验及放行门禁 |
| hooks/claude_stop.py | Claude Code 停止事件适配器 |
| scripts/test_*.py、evals/contracts.json | 正反例、回归及评测数据 |
| agents/openai.yaml、SKILL.md frontmatter | 宿主规定的技能元数据格式 |

机器规则使用 JSON；Markdown 不再维护字段表、数值阈值或检查清单。仓库使用内嵌 ZIP 分发，安装后展开为上述文件。

在任务所用 Python 环境中准备 requirements.txt 的组件后校验：

```sh
python3 ~/.agents/skills/proposal-producer/scripts/proposal.py validate --workdir /path/to/work
python3 -m pip install -r ~/.agents/skills/proposal-producer/requirements-test.txt
python3 -m unittest discover -s ~/.agents/skills/proposal-producer/scripts -p 'test_*.py' -v
```

安装后调用：

> 用 $proposal-producer，基于我提供的资料制作方案报价型提案。先提交内容确认，确认后制作所选 PPTX、SOW 和对应 PDF。

需要宿主刷新技能列表时，重新开启会话。制作依赖宿主可用的演示文稿、文档、PDF、导出渲染工具和中文字体。本轮三类均有本地合成候选的真实导出验证，方案报价型还验证了 SOW 及对应 PDF。完整真实项目的业务与展示质量仍按当前候选评价。

0.2 版加入本地 release 门禁：检查当前确认、独立复核、适用项证据和测量阈值后生成放行记录。Claude Code 可通过 hook-config 命令生成项目设置片段，具体接入见安装后 references/enforcement.md。该适配器的协议已做模拟测试，未在实际 Claude Code 会话中验证。当前 Codex 会话使用命令门禁；宿主 hook 不会因安装自动启用。

0.3 版将参考页分析纳入实际制作输入。填写 presentation-plan.json，先渲染并校准关键解释页，再运行 production-check，沿用既有内容确认后连续制作全稿。页计划明确每页的决策问题、具体场景、机制关系、价值依据及费用对价。

成品沿用本次独立检查者，通过 quality-init 创建 quality-review.json，分别记录技术、业务论证和展示质量。展示目标未达到时，技术通过不能代替论证或展示通过；用户明确选用审阅稿时保留实际质量结论。普通视觉校准不新增用户审批节点。

evals/presentation-cases.json 的真实同 brief 旧新稿配对评测当前留空。新增自动测试验证输入关联、校准、状态与结论门禁，未以合成样例宣称真实成品质量已提高。

本地 Schema 校验已接入命令；模型生成时的 constrained decoding 需要宿主另行传入 Schema。检查证据的真实性和语义结论仍由真实检查负责。脚本不代发客户文件。

旧版项目保留原件，按当前 Schema 补齐迁移字段并重新生成确认与复核记录；原始人类 SOP 及历史试用证据保持原版本。

GitHub Actions 使用只读仓库权限，运行安装校验、Schema 校验和行为测试。手动检查安装器：

```sh
python3 test_install.py
```

安装器内 RELEASE 记录当前版本、ZIP 哈希及文件哈希。仓库不包含客户 ref、账号凭据、Office 引擎或字体。

0.4 版增加同族 SVG 图标与构图索引、任务 visual-profile、可选择的原生／混合／整页图像适配器，以及实际对象、连线端点、图像区域和字面核对。`doctor` 可在初始化前检测环境；`build`、`export` 和 `render-check` 保存实际候选、PDF、字体与渲染证据。整页图像使用已有明确选择，生成服务通过可选 JSON 适配器接入，本轮未调用收费服务。

共用底稿增加日期、版本、覆盖期、需求优先级、工作包、SOW 稳定章节和里程碑。支持税率未知的含税总包价，保留未知税额与未税额，金额触发核算独立于提案类型。只读取已登记的任务 JSON，运行日志不作为底稿。

目标缺陷、后续约定和适用限制分开登记，影响目标的缺口始终反映到实际结论。自动测试验证合同、计算、对应关系与门禁；本地真实导出和独立正向试用另有原始记录。真实客户旧新版本的同 brief 配对评测继续留空。CI 覆盖安装、Schema 与合成回归，执行结果见仓库 Actions。
