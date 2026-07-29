# 工作流程指南

本文档用于引导 Agent 完成从 Markdown 到 HTML/PDF 的简历生成。

## 架构概览

```
Resume.md ──(scripts/generate_resume.py)──> Resume.html
                  │                              │
           resume.css (样式)              ┌──────┴──────┐
           assets/   (SVG 图标)           │  两种 PDF 导出 │
                                          │ weasyprint   │
                                          │ Chrome/Chromium│
                                          └─────────────┘
```

## Agent 工作流

### 1. 编辑内容

直接修改 `Resume.md`。遵循以下约定：
- 使用 `<center>` 包裹头部信息
- 二级标题搭配 SVG 图标：`## <img src="assets/xxx.svg" width="30px"> 标题`
- 加粗使用 Markdown 语法 `**文字**`
- 嵌套列表使用 4 空格缩进

### 2. 构建 HTML

```bash
python scripts/generate_resume.py
```

依赖：`pip install markdown`

### 3. 导出 PDF

**方案一（推荐）：Chrome/Chromium 无头模式** — 加粗渲染正常，CJK 字体完整

```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import base64

svc = Service(executable_path='/home/xzh/chromedriver/chromedriver')
opts = Options()
opts.add_argument('--headless=new')
opts.add_argument('--no-sandbox')
drv = webdriver.Chrome(service=svc, options=opts)
drv.get('file:///home/xzh/Markdown-Resume/Resume.html')
pdf = drv.execute_cdp_cmd('Page.printToPDF', {
    'printBackground': True,
    'paperWidth': 8.27, 'paperHeight': 11.69,
    'marginTop': 0.4, 'marginBottom': 0.4,
})
with open('Resume.pdf', 'wb') as f:
    f.write(base64.b64decode(pdf['data']))
drv.quit()
```

需要：`chromedriver`（已安装在 `/home/xzh/chromedriver/`）+ `pip install selenium`

**方案二：weasyprint** — 简单但 CJK 加粗渲染有问题

```bash
pip install weasyprint
python -c "import weasyprint; weasyprint.HTML('Resume.html').write_pdf('Resume.pdf')"
```

**问题**：系统缺少 CJK 粗体字体（如 WQY Zen Hei 只有 Regular），中文加粗不显示。

## PDF 渲染排坑记录

| 问题 | 原因 | 解决 |
|------|------|------|
| 图标过大 | 仅 `h2 img` 有 CSS 限制，其他上下文图标未约束 | 为 `h1/h2/h3/p/div img` 统一加 `width` 限制 |
| 中文加粗无效 | weasyprint + 系统无 CJK Bold 字体 | ① 换 Chrome 导出；② 或 `text-shadow` 模拟 |
| 字体缺失报错 | `@font-face` 引用的 `./github/*.woff` 不存在 | 删除无效 `@font-face` 和 Google Fonts 链接 |
| Chrome 未安装 | WSL2 snap 限制 | 用系统已有的 `/home/xzh/chromedriver/chromedriver` |

## 关键约定

- **不要直接编辑 `Resume.html`** — 它由脚本生成
- 修改 MD 后重新构建 HTML + PDF
- 修改只 commit 不 push，确认后手动推送分支
- `<center>` 标签会被脚本转为 `<div style="text-align:center">`
- CSS 中 `@include-when-export` 会被脚本自动过滤
