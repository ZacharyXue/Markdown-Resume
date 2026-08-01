# AGENTS.md

## 隐私设计

- **公开仓库**：只含脚本、样式、模板（`Resume.example.md`），**不含任何真实个人信息**。
- **真实简历**：存放在 `dist/Resume.md`（gitignored，不提交到公开仓库），日常编辑直接改这个文件。
- **版本备份**：`~/.local/resume/` 是独立私有 git 仓库，手动同步 `dist/Resume.md` 过去做版本管理。
- **构建产物**：输出到 `dist/`（gitignored，不提交）。

## 内容源

| 优先级 | 路径 | 用途 |
|--------|------|------|
| 1 | `dist/Resume.md` | **日常编辑目标**（gitignored，在项目目录里方便编辑） |
| 2 | `~/.local/resume/Resume.md` | git 版本备份（首次运行自动复制到 dist/） |
| 3 | `Resume.example.md` | 公开脱敏模板（fallback，供参考和测试） |

`RESUME_PATH` 环境变量可覆盖以上所有自动检测。

## 工作流

```bash
# 1. 编辑简历（日常操作）
vim dist/Resume.md

# 2. 构建 HTML
python scripts/generate_resume.py
# → 输出 dist/Resume.html

# 3. 版本管理（可选，定期备份）
cp dist/Resume.md ~/.local/resume/Resume.md
cd ~/.local/resume && git commit -am "update resume"
```

## 构建

需要 `markdown` Python 包（`pip install markdown`）。

```bash
python scripts/generate_resume.py
# 输出: dist/Resume.html
```

## 架构

- `Resume.example.md` — 脱敏模板（公开）
- `resume.css` — Typora 兼容样式表
- `assets/` — Markdown 中通过 `<img>` 标签引用的 SVG 图标
- `scripts/generate_resume.py` — Markdown → HTML 转换
- `dist/` — 构建产物 + 真实简历源文件（gitignored）
- `~/.local/resume/` — 真实简历的 git 版本备份（不公开）

## 首次设置

```bash
# 如果已有 ~/.local/resume/Resume.md
python scripts/generate_resume.py
# → 自动复制到 dist/Resume.md，之后直接编辑 dist/Resume.md

# 如果从零开始
cp Resume.example.md dist/Resume.md
vim dist/Resume.md    # 替换为真实信息
```

## 工具链注意事项

- Python 构建时，`resume.css` 中的 `@include-when-export` 指令会被过滤掉（Typora 专用）。
- Python 脚本会将 2 空格嵌套列表缩进规范化为 4 空格，以符合标准 Markdown。

## 技能

- OpenCode 技能从 `Paramchoudhary/ResumeSkills` 安装，并在 `skills-lock.json` 中追踪。
- `skills-lock.json` 和 `.agents/` 均已加入 `.gitignore`。
