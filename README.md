## 快速开始

```bash
# 1. 复制模板
cp Resume.example.md dist/resume-base.md

# 2. 编辑基本信息
vim dist/resume-base.md

# 3. 生成 HTML
python scripts/generate_resume.py
# → 输出 dist/Resume.html
```

依赖：`pip install markdown`

## 拆分模式（推荐）

简历分为 **基本信息** 和 **项目经历** 两部分，支持按需组合：

```
dist/
├── resume-base.md          ← 头/教育/工作/技能（编辑这个）
├── projects/               ← 项目经历，一个项目一个 .md
│   ├── project-a.md
│   └── project-b.md
└── Resume.html             ← 生成产物
```

```bash
# 列出可用项目
python scripts/generate_resume.py -l

# 全部项目
python scripts/generate_resume.py

# 指定项目
python scripts/generate_resume.py -p project-a,project-b
```

### 项目文件格式

```markdown
- **项目名称**（开始时间~结束时间）

    *技术栈1, 技术栈2*

    项目简述。主要工作：
    - 要点一（动词 + 做了什么 + 量化结果）
    - 要点二
```

## 导出 PDF

```bash
# weasyprint（简单）
python3 -c "import weasyprint; weasyprint.HTML('dist/Resume.html').write_pdf('dist/Resume.pdf')"

# Chrome headless（加粗效果更好）
# 详见 docs/BRIDGE.md
```

## Typora 用户（传统方式）

（1）将 resume.css 复制到 Typora 的主题文件夹

![](assets/1.png)

（2）主题文件夹可以在"文件->偏好设置->主题文件夹"中打开

![](assets/2.png)
![](assets/3.png)

（3）重启 Typora，在主题中选择 Resume

![](assets/4.png)

（4）导出：文件 -> 导出 -> HTML

![](assets/5.png)

（5）浏览器打开 HTML，Ctrl+P 打印，去除页眉页脚

![](assets/6.png)

## 简历格式检查

https://cyc2018.github.io/Text-Typesetting/

![](assets/check-resume.png)

## 关于图标

因为有些 Markdown 编辑器不支持 HTML 语法（例如 Typora），无法导入 fontawesome 样式表。无奈之下只能将本简历模版需要使用到的图标单独下载，放入 assets 目录下，并且在简历中以 `<img>` 标签来引用。

## License

- [fontawesome](https://fontawesome.com/license)
