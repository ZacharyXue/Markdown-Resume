# 工作流程指南

本文档用于引导 Agent 完成从 Markdown 到 HTML 的简历生成。

## 架构概览

```
Resume.md ──(scripts/generate_resume.py)──> Resume.html
                  │
           resume.css (样式)
           assets/   (SVG 图标)
```

## Agent 工作流

### 1. 理解源文件

- **`Resume.md`** — 唯一需要编辑的内容文件。使用 Markdown 撰写，包含中文简历内容。
- **`resume.css`** — 简历专用样式表，兼容 Typora 和 Python 脚本。
- **`assets/`** — Markdown 中通过 `<img>` 标签引用的 SVG 图标。

### 2. 编辑内容

直接修改 `Resume.md`，遵循以下约定：
- 使用 `<center>` 包裹头部信息（姓名、联系方式）
- 二级标题搭配 SVG 图标引入各段落
- 嵌套列表使用 4 空格缩进
- 技能清单使用 ★ 评级

### 3. 构建 HTML

```bash
python scripts/generate_resume.py
```

**依赖：** `markdown` Python 包（`pip install markdown`）

**脚本做了什么：**
1. 读取 `Resume.md` 并预处理（标准化列表缩进、处理 `<center>` 标签）
2. 使用 `markdown` 库（extensions: `extra`, `sane_lists`）转换为 HTML
3. 读取 `resume.css`，过滤 `@include-when-export` 指令
4. 组合内联样式、Google Fonts 和 HTML 内容，写入 `Resume.html`

### 4. 验证

构建完成后，可以用浏览器打开 `Resume.html` 检查效果。

### 5. 导出 PDF（浏览器打印）

浏览器原生支持 HTML 转 PDF：
- 用浏览器打开 `Resume.html`
- `Ctrl+P` (或 `Cmd+P`) 打开打印对话框
- 目标选择"另存为 PDF"
- 建议去除页眉页脚，边距设为"无"

## 关键约定

- **不要直接编辑 `Resume.html`** — 它由 `Resume.md` 生成。
- **不要通过工具的方式生成 PDF** — 浏览器打印已足够。
- 每次修改 `Resume.md` 后，运行构建脚本更新 `Resume.html`。
