# AGENTS.md

## 内容源

- **`Resume.md`** 是唯一应编辑的内容文件。
- `Resume.html` 由 `Resume.md` **生成**——不要直接编辑它。

## 构建

```
python scripts/generate_resume.py
```

需要 `markdown` Python 包（pip install markdown）。该脚本读取 `Resume.md` + `resume.css`，生成 `Resume.html`。

## 架构

- `Resume.md` — Markdown 简历（中文，个人模板）
- `resume.css` — Typora 兼容样式表，Typora 和 Python 脚本均会使用
- `Resume.html` — 生成的 HTML 输出（随源文件一起提交）
- `Resume.pdf`、`Resume.png` — 渲染快照（已提交）
- `assets/` — Markdown 中通过 `<img>` 标签引用的 SVG 图标
- `scripts/generate_resume.py` — Markdown 转 HTML 转换器，使用 Python-Markdown 的 `extra` 和 `sane_lists` 扩展
- `docs/BRIDGE.md` — Agent 工作流指南，描述从 MD 到 HTML 的完整转换流程

## 工具链注意事项

- 该仓库**没有 CI、没有测试、没有 lint、没有包管理器**。
- 原始工作流使用 **Typora** 导出 HTML/PDF；Python 脚本提供了程序化替代方案。
- Python 构建时，`resume.css` 中的 `@include-when-export` 指令会被过滤掉，因为它们是 Typora 专用的。
- Python 脚本会将 2 空格嵌套列表缩进规范化为 4 空格，以符合标准 Markdown。

## 技能

- OpenCode 技能从 `Paramchoudhary/ResumeSkills` 安装，并在 `skills-lock.json` 中追踪。
- `skills-lock.json` 和 `.agents/` 均已加入 `.gitignore`。
