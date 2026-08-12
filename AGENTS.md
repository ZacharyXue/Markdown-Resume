# AGENTS.md

## 隐私设计

- **公开仓库**：只含脚本、样式、模板（`Resume.example.md`），**不含任何真实个人信息**。
- **真实简历**：存放在 `dist/`（父仓库 gitignored）。
- **版本管理**：`dist/` 本身是一个独立的私有 git 仓库，不推送到远程，无远端连接。
- **构建产物**：输出到 `dist/`（gitignored，不提交）。

## 内容源（拆分模式）

| 优先级 | 路径 | 用途 |
|--------|------|------|
| 1 | `dist/resume-base.md` | **基本信息**（头/教育/工作/技能），`<!-- PROJECTS -->` 为项目注入点 |
| 2 | `dist/projects/` | **项目经历**，按公司分目录，一个项目一个 `.md` |
| 3 | `Resume.example.md` | 公开脱敏模板（fallback） |

`RESUME_PATH` 环境变量可强制指定源文件（兼容旧单文件模式）。

## 工作流

```bash
# 1. 编辑基本信息
vim dist/resume-base.md

# 2. 编辑/新增项目
vim dist/projects/bytedance/my-project.md

# 3. 查看可用项目
python scripts/generate_resume.py --list-projects

# 4. 构建 HTML
python scripts/generate_resume.py -p bytedance/gitlab-ci-platform,bytedance/model-testing-deployment

# 5. 版本管理（dist/ 是独立 git 仓库，本地私有）
cd dist && git add -A && git commit -m "update: xxx"
```

## 项目文件格式

```markdown
- **项目名称**（开始时间~结束时间/至今）

    *技术栈1, 技术栈2*

    项目简述。主要工作：
    - 要点一（动词 + 做了什么 + 量化结果）
    - 要点二
```

要点开头动词示例：主导、搭建、开发、引入、推动、缩短、支撑、设计、带领

## 构建

需要 `markdown` Python 包（`pip install markdown`）。

```bash
python scripts/generate_resume.py             # 全部项目
python scripts/generate_resume.py -p a,b      # 指定项目
python scripts/generate_resume.py -l          # 列出可用项目
```

## 架构

- `dist/resume-base.md` — 基本信息（gitignored）
- `dist/projects/` — 项目经历，一个 `.md` 一个项目（gitignored）
- `dist/Resume.html` — 构建产物（gitignored）
- `Resume.example.md` — 脱敏模板（公开）
- `resume.css` — Typora 兼容样式表
- `assets/` — SVG 图标
- `scripts/generate_resume.py` — Markdown → HTML 转换，支持项目选择

## Hermes 技能

- `resume-builder` — 润色原始描述为简历语言 + 管理项目文件 + 生成 HTML
- `resume-workflow` — 旧版流程参考
- `markdown-resume` — PDF 导出与格式陷阱

## 工具链注意事项

- Python 构建时，`resume.css` 中的 `@include-when-export` 指令会被过滤掉。
- Python 脚本会将 2 空格嵌套列表缩进规范化为 4 空格。
- `skills-lock.json` 和 `.agents/` 均已加入 `.gitignore`。
