# AGENTS.md

## 隐私设计

- **公开仓库**：只含脚本、样式、模板（`Resume.example.md`），**不含任何真实个人信息**。
- **真实简历**：存放在 `~/.local/resume/Resume.md`（独立私有 git 仓库管理版本）。
- **构建产物**：输出到 `dist/`（gitignored，不提交）。

## 内容源

- **`Resume.example.md`** — 脱敏模板，供参考和本地测试，是仓库中唯一的简历文件。
- **`~/.local/resume/Resume.md`** — 真实简历（私有不公开），`generate_resume.py` 优先读取。
- `Resume.html`、`Resume.pdf`、`Resume.png` — 不应出现在仓库中，由脚本生成到 `dist/`。

## 构建

```bash
# 确保 ~/.local/resume/Resume.md 存在（或设置 RESUME_PATH 环境变量）
python scripts/generate_resume.py

# 输出到 dist/Resume.html + dist/Resume.md
```

需要 `markdown` Python 包（`pip install markdown`）。

## 架构

- `Resume.example.md` — 脱敏模板（公开）
- `resume.css` — Typora 兼容样式表
- `assets/` — Markdown 中通过 `<img>` 标签引用的 SVG 图标
- `scripts/generate_resume.py` — Markdown → HTML 转换
- `dist/` — 构建产物输出目录（gitignored）
- `~/.local/resume/` — 真实简历仓库（私有 git，不公开）

## 设置真实简历

```bash
mkdir -p ~/.local/resume
cd ~/.local/resume
git init
# 编辑 Resume.md 写入真实内容
cp /path/to/Markdown-Resume/Resume.example.md Resume.md  # 用模板起步
git add Resume.md && git commit -m "init"
```

## 工具链注意事项

- Python 构建时，`resume.css` 中的 `@include-when-export` 指令会被过滤掉（Typora 专用）。
- Python 脚本会将 2 空格嵌套列表缩进规范化为 4 空格，以符合标准 Markdown。

## 技能

- OpenCode 技能从 `Paramchoudhary/ResumeSkills` 安装，并在 `skills-lock.json` 中追踪。
- `skills-lock.json` 和 `.agents/` 均已加入 `.gitignore`。
