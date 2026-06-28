#!/usr/bin/env python3
"""Convert Resume.md to Resume.html with built-in PDF export functionality."""

import re
import sys
from pathlib import Path
from markdown import markdown


PROJECT_DIR = Path(__file__).resolve().parent.parent
RESUME_MD = PROJECT_DIR / "Resume.md"
RESUME_HTML = PROJECT_DIR / "Resume.html"
CSS_FILE = PROJECT_DIR / "resume.css"

PDF_BUTTON_JS = r"""
function exportPDF() {
    window.print();
}
"""

PDF_BUTTON_CSS = r"""
.pdf-export-btn {
    position: fixed;
    bottom: 24px;
    right: 24px;
    z-index: 9999;
    padding: 10px 20px;
    background: #1a73e8;
    color: #ffffff;
    border: none;
    border-radius: 6px;
    font-size: 15px;
    font-family: "Open Sans", "Helvetica Neue", Helvetica, Arial, sans-serif;
    cursor: pointer;
    box-shadow: 0 2px 8px rgba(0,0,0,0.2);
    transition: background 0.2s, box-shadow 0.2s;
}
.pdf-export-btn:hover {
    background: #1557b0;
    box-shadow: 0 4px 12px rgba(0,0,0,0.3);
}
@media print {
    .pdf-export-btn {
        display: none !important;
    }
}
"""

TEMPLATE = """<!doctype html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Resume</title>
{fonts}
<style>
{base_css}
</style>
<style>
{resume_css}
</style>
<style>
{pdf_btn_css}
</style>
</head>
<body class="typora-export os-windows">
<button class="pdf-export-btn" onclick="exportPDF()">导出 PDF</button>
<script>
{pdf_btn_js}
</script>
<div id="write" class="is-node">
{content}
</div>
</body>
</html>
"""


def load_css(css_path: Path) -> str:
    """Load resume.css and strip Typora-specific directives."""
    css = css_path.read_text(encoding="utf-8")
    lines = []
    for line in css.splitlines():
        if "@include-when-export" in line:
            continue
        lines.append(line)
    return "\n".join(lines)


def preprocess_md(text: str) -> str:
    """Normalize markdown for Python-Markdown library.

    Handles:
    1. <center> → <div style="text-align:center"> (avoids <p> wrapping)
    2. 2-space nested lists → 4-space (standard markdown nesting)
    3. Inserts blank lines before sub-lists that follow paragraph text
    """
    text = text.replace("<center>", '<div style="text-align:center">')
    text = text.replace("</center>", "</div>")

    lines = text.splitlines()
    result = []

    for i, line in enumerate(lines):
        stripped = line.lstrip()
        indent = len(line) - len(stripped)

        # Track list context: a line starting with "- " or indented "- "
        is_list_item = bool(re.match(r"^\s*-\s", line)) and stripped.startswith("- ")

        # Convert 2-space indented list items (not starting at column 0) to 4-space
        if is_list_item and 0 < indent < 4:
            line = "    " + stripped

        # Insert blank line before sub-list that follows non-list text
        # Pattern: previous non-empty line is indented text (not list),
        # current line is an indented list item
        if is_list_item and indent >= 4 and result:
            prev_line = result[-1]
            # If previous line is not blank and not a list item, add blank line
            if prev_line.strip() and not re.match(r"^\s*(?:-|\d+\.)\s", prev_line) and prev_line.strip():
                result.append("")

        result.append(line)

    return "\n".join(result)


def generate() -> None:
    """Read Resume.md, convert to HTML, and write Resume.html."""

    if not RESUME_MD.exists():
        sys.exit(f"ERROR: {RESUME_MD} not found.")

    md_content = RESUME_MD.read_text(encoding="utf-8")
    md_content = preprocess_md(md_content)

    html_body = markdown(
        md_content,
        extensions=["extra", "sane_lists"],
        output_format="html5",
    )

    resume_css = load_css(CSS_FILE) if CSS_FILE.exists() else ""

    google_fonts = (
        '<link href="https://fonts.loli.net/css'
        '?family=Open+Sans:400italic,700italic,700,400'
        '&subset=latin,latin-ext" rel="stylesheet" type="text/css">'
    )

    base_css = """html {
    overflow-x: initial !important;
}
html {
    font-size: 16px;
}
body {
    font-family: "Open Sans", "Clear Sans", "Helvetica Neue", Helvetica, Arial, sans-serif;
    color: #333333;
    line-height: 1.6;
    margin: 0;
    padding: 0;
}
#write {
    max-width: 860px;
    margin: 0 auto;
    padding: 30px 30px 100px;
}
p {
    margin: 0.8em 0;
}
ul, ol {
    padding-left: 30px;
}
@media print {
    html {
        font-size: 13px;
    }
    table, pre {
        page-break-inside: avoid;
    }
    pre {
        word-wrap: break-word;
    }
    @page {
        margin: 20mm 0;
    }
}"""

    output = TEMPLATE.format(
        fonts=google_fonts,
        base_css=base_css,
        resume_css=resume_css,
        pdf_btn_css=PDF_BUTTON_CSS,
        pdf_btn_js=PDF_BUTTON_JS,
        content=html_body,
    )

    RESUME_HTML.write_text(output, encoding="utf-8")
    print(f"Generated {RESUME_HTML}")


if __name__ == "__main__":
    generate()
