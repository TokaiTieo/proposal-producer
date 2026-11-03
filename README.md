# Proposal Producer

通用 Proposal 制作 Skill，**0.8.1-trial / SOP v1.13**，可供 agent 自动下载安装的分发仓库。

制作顺序：先生成实际 SOW，再用用户指定的 business-case-and-proposal 方法写 A4 Proposal DOCX 和对应 PDF；用户选择后，从实际 Proposal 提炼并制作 PPT。默认客户交付仍是书面 Proposal；sow_required 仅选择是否一并交付上游 SOW。

把下面这句话发给其他 agent，即可让它下载并安装：

> 请从 https://github.com/TokaiTieo/proposal-producer 克隆仓库，读取 README.md 和 AGENTS.md，用可用的 Python 3 运行 install.py；已安装旧版时加 --update。按当前宿主选择技能目录，完成后核对版本及文件哈希，并读取安装后的 SKILL.md。

```sh
git clone https://github.com/TokaiTieo/proposal-producer.git
cd proposal-producer
python3 install.py --dry-run
python3 install.py
python3 install.py --dest /path/to/skills
python3 install.py --update
```

安装器包含完整 Skill，校验 ZIP 和逐文件哈希。升级保留旧版备份；不自动启用 hooks 或修改全局依赖。安装后读取 SKILL.md，在任务 Python 环境安装 requirements.txt；选择 PPT 时另准备 requirements-presentation.txt。

新任务从 init、sow-build、proposal-brief 开始。读取真实 SOW 和交接指向的方法原文，应用方法完成共同论证与章节计划后，运行 proposal-record。完成 production-check 及原有内容确认，再 build、export 书面稿。用户需要 PPT 时，运行 presentation-brief、presentation-record，内部校准后用 presentation-build 制作汇报版。具体参数见包内 references/data-and-commands.md。

business-case-and-proposal 已完整集成为包内方法模块。所有机器直接使用本包内的方法文件，无需另装或查找 Hermes；来源、版本及 CC0-1.0 许可证保留在方法原文和契约中。运行时校验包内方法版本，制作与复核流程保持不变。

新任务使用 schema 7；旧任务原件与评价保留；在新版重建 schema 7 的 PPT 时需补齐内置方法交接与图像制作记录。默认输出 proposal_docx 与 proposal_pdf，--sow-required 选择 SOW 客户交付，--presentation-requested 选择汇报版。原有有效授权继续沿用，普通写作排版内部连续完成。

```sh
python3 /path/to/skill/scripts/proposal.py doctor --workdir /path/to/task
python3 /path/to/skill/scripts/proposal.py validate --workdir /path/to/task
python3 -m unittest discover -s /path/to/skill/scripts -p 'test_*.py' -v
python3 test_install.py
```

测试使用 requirements-test.txt。实际导出需要宿主提供可用 Office 引擎、Poppler 和字体，doctor 检查实际能力。文件通过技术校验不代表商业批准或客户接受。包内没有客户原件、账号或工具缓存。

本版使用 client-2：编写前区分内部制作、过度防御和必要商务内容，独立检查者对实际文件分别完成六项编辑检查并逐项处置疑点。已判违规必须修改；必要商务内容的误报需逐项说明原文、决策关系、位置及每处用途。放行要求已确认违规和待判定疑点零残留，证据绑定当前文件及真实截图。旧 client-1 记录需要重新复核，不自动转换为分项通过。client-content-check 负责程序检查，关键词及重复仅为疑点。图表只生成一次题注，可选文内引用仅显示编号。固定总价可用 coverage_period 描述真实期间，未知月数保留 null。方法及字段说明见 references/client-content.md。

选配 PPT 已集成 ppt-image-render 2.4.1 的完整入口原文、配套脚本、参考和资源。无需全局安装；presentation-brief 提供包内路径，presentation-image-prepare 实际选路和生成提示词，审计及晋级后才可构建。PPT 采用整页图像，支持整图替换。样式使用当前项目配置，授权沿用既有规则。源文件及工具依赖分别检查；图像模型、Office、OCR 引擎和字体仍由宿主提供。包内来源保留 internal-use 标记，不改授为 CC0。
