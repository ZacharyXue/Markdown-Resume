#!/usr/bin/env python3
"""Convert Resume.md to Resume.html.

Reads real resume from ~/.local/resume/Resume.md by default.
Set RESUME_PATH env var to override.
Outputs to dist/ directory.
"""

import os
import re
import sys
from pathlib import Path
from markdown import markdown


PROJECT_DIR = Path(__file__).resolve().parent.parent
DIST_DIR = PROJECT_DIR / "dist"

# --- Locate the real resume ---
RESUME_PATH = os.environ.get("RESUME_PATH")
if RESUME_PATH:
    RESUME_MD = Path(RESUME_PATH)
else:
    local_resume = Path.home() / ".local" / "resume" / "Resume.md"
    if local_resume.exists():
        RESUME_MD = local_resume
    else:
        # Fallback to project root (for development with example)
        RESUME_MD = PROJECT_DIR / "Resume.md"

CSS_FILE = PROJECT_DIR / "resume.css"

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
</head>
<body class="typora-export os-windows">
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
        if is_list_item and indent >= 4 and result:
            prev_line = result[-1]
            if prev_line.strip() and not re.match(r"^\s*(?:-|\d+\.)\s", prev_line) and prev_line.strip():
                result.append("")

        result.append(line)

    return "\n".join(result)


def generate() -> None:
    """Read Resume.md, convert to HTML, and write to dist/Resume.html."""

    if not RESUME_MD.exists():
        print(f"ERROR: Resume not found at {RESUME_MD}")
        print("Options:")
        print("  1. Create ~/.local/resume/Resume.md with your real resume")
        print("  2. Set RESUME_PATH=/path/to/your/Resume.md")
        print("  3. Copy Resume.example.md to Resume.md for testing")
        sys.exit(1)

    print(f"Using resume: {RESUME_MD}")

    md_content = RESUME_MD.read_text(encoding="utf-8")
    md_content = preprocess_md(md_content)

    html_body = markdown(
        md_content,
        extensions=["extra", "sane_lists"],
        output_format="html5",
    )

    resume_css = load_css(CSS_FILE) if CSS_FILE.exists() else ""

    google_fonts = ""

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
        content=html_body,
    )

    DIST_DIR.mkdir(exist_ok=True)
    resume_html = DIST_DIR / "Resume.html"
    resume_html.write_text(output, encoding="utf-8")

    # Also copy the source markdown to dist for reference
    resume_md_copy = DIST_DIR / "Resume.md"
    resume_md_copy.write_text(RESUME_MD.read_text(encoding="utf-8"))

    print(f"✓ Generated {resume_html}")
    print(f"✓ Copied source to {resume_md_copy}")


if __name__ == "__main__":
    generate()
