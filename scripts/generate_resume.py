#!/usr/bin/env python3
"""Convert Resume.md to Resume.html with composable project selection.

Architecture (new split mode):
  dist/resume-base.md       ← header, personal info, summary, education, work, skills
  dist/projects/*.md         ← individual project entries (one file per project)
  dist/Resume.html           ← generated output

Backward compatible: if dist/resume-base.md doesn't exist, falls back to the
old single-file dist/Resume.md (or ~/.local/resume/Resume.md).

Usage:
  python scripts/generate_resume.py                           # all projects
  python scripts/generate_resume.py --list-projects           # list available projects
  python scripts/generate_resume.py --projects gitlab-ci,chip # selected projects only
"""

import argparse
import os
import re
import sys
from pathlib import Path
from markdown import markdown

PROJECT_DIR = Path(__file__).resolve().parent.parent
DIST_DIR = PROJECT_DIR / "dist"
PROJECTS_DIR = DIST_DIR / "projects"

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
    """Normalize markdown for Python-Markdown library."""
    text = text.replace("<center>", '<div style="text-align:center">')
    text = text.replace("</center>", "</div>")

    lines = text.splitlines()
    result = []

    for i, line in enumerate(lines):
        stripped = line.lstrip()
        indent = len(line) - len(stripped)
        is_list_item = bool(re.match(r"^\s*-\s", line)) and stripped.startswith("- ")

        if is_list_item and 0 < indent < 4:
            line = "    " + stripped

        if is_list_item and indent >= 4 and result:
            prev_line = result[-1]
            if prev_line.strip() and not re.match(r"^\s*(?:-|\d+\.)\s", prev_line) and prev_line.strip():
                result.append("")

        result.append(line)

    return "\n".join(result)


def list_projects() -> list[Path]:
    """Return sorted list of available project .md files (recursive)."""
    if not PROJECTS_DIR.exists():
        return []
    return sorted(PROJECTS_DIR.glob("**/*.md"))


def get_project_title(project_path: Path) -> str:
    """Extract project title from the first line of a project .md file."""
    first_line = project_path.read_text(encoding="utf-8").splitlines()[0].strip()
    # Strip leading "- **" and trailing "**（...）"
    match = re.match(r"^- \*\*(.+?)\*\*", first_line)
    if match:
        return match.group(1)
    return first_line


def assemble_resume(base_path: Path, project_slugs: list[str]) -> str:
    """Assemble full resume from base + selected projects."""
    base_content = base_path.read_text(encoding="utf-8")

    # Build slug → path map (slug = relative path from PROJECTS_DIR, no .md)
    available = {}
    for p in list_projects():
        rel = p.relative_to(PROJECTS_DIR)
        available[str(rel.with_suffix(""))] = p

    project_section = []
    for slug in project_slugs:
        proj_path = available.get(slug)
        if proj_path:
            project_section.append(proj_path.read_text(encoding="utf-8").rstrip())

    assembled = base_content.replace("<!-- PROJECTS -->", "\n\n".join(project_section))

    return assembled


def locate_base_md() -> Path | None:
    """Locate the base resume markdown file.

    Priority:
      1. RESUME_PATH env var (for old-style single file)
      2. dist/resume-base.md (new split mode)
      3. dist/Resume.md (old single-file mode, backward compat)
      4. ~/.local/resume/Resume.md (old backup mode)
      5. Resume.example.md (fallback)
    """
    env_path = os.environ.get("RESUME_PATH")
    if env_path:
        return Path(env_path)

    # New split mode
    base = DIST_DIR / "resume-base.md"
    if base.exists():
        return base

    # Old single-file mode
    old = DIST_DIR / "Resume.md"
    if old.exists():
        return old

    # Old backup mode
    local = Path.home() / ".local" / "resume" / "Resume.md"
    if local.exists():
        DIST_DIR.mkdir(exist_ok=True)
        old.write_text(local.read_text(encoding="utf-8"))
        print(f"Bootstrapped dist/Resume.md from ~/.local/resume/")
        return old

    # Fallback
    example = PROJECT_DIR / "Resume.example.md"
    if example.exists():
        return example

    return None


def is_split_mode(base_path: Path) -> bool:
    """Check if we're using the new split mode (resume-base.md + projects/)."""
    return base_path.name == "resume-base.md" and "<!-- PROJECTS -->" in base_path.read_text(encoding="utf-8")


def generate(project_slugs: list[str] | None = None) -> None:
    """Generate Resume.html from base + selected projects."""
    base_path = locate_base_md()

    if not base_path or not base_path.exists():
        print("ERROR: No resume source found.")
        print("Options:")
        print("  1. Create dist/resume-base.md + dist/projects/ for split mode")
        print("  2. Create ~/.local/resume/Resume.md for old single-file mode")
        print("  3. Set RESUME_PATH=/path/to/your/Resume.md")
        sys.exit(1)

    css_path = PROJECT_DIR / "resume.css"

    print(f"Source: {base_path}")

    if is_split_mode(base_path):
        # Build slug → path map
        available_slugs = {}
        for p in list_projects():
            rel = p.relative_to(PROJECTS_DIR)
            available_slugs[str(rel.with_suffix(""))] = p

        if project_slugs is None:
            project_slugs = list(available_slugs.keys())

        for slug in project_slugs:
            if slug not in available_slugs:
                print(f"WARNING: Project '{slug}' not found. Available: {', '.join(available_slugs.keys())}")

        valid_slugs = [s for s in project_slugs if s in available_slugs]

        if not valid_slugs:
            print("ERROR: No valid projects selected.")
            sys.exit(1)

        print(f"Projects: {', '.join(valid_slugs)}")

        md_content = assemble_resume(base_path, valid_slugs)
    else:
        # Old single-file mode
        if project_slugs is not None:
            print("WARNING: --projects is ignored in single-file mode. Use split mode (dist/resume-base.md).")
        md_content = base_path.read_text(encoding="utf-8")

    md_content = preprocess_md(md_content)

    html_body = markdown(
        md_content,
        extensions=["extra", "sane_lists"],
        output_format="html5",
    )

    resume_css = load_css(css_path) if css_path.exists() else ""

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
        fonts="",
        base_css=base_css,
        resume_css=resume_css,
        content=html_body,
    )

    DIST_DIR.mkdir(exist_ok=True)
    resume_html = DIST_DIR / "Resume.html"
    resume_html.write_text(output, encoding="utf-8")
    print(f"Generated {resume_html}")


def cmd_list_projects() -> None:
    """List available project files with their titles and subdirectories."""
    projects = list_projects()
    if not projects:
        print("No projects found in dist/projects/")
        print("Add .md files under dist/projects/ — one per project.")
        print("Use subdirectories to organize by company or category.")
        return

    print(f"Available projects ({len(projects)}):")
    for p in projects:
        rel = p.relative_to(PROJECTS_DIR)
        slug = str(rel.with_suffix(""))
        title = get_project_title(p)
        print(f"  {slug:40s} → {title}")


def main():
    parser = argparse.ArgumentParser(description="Generate resume HTML from Markdown source.")
    parser.add_argument(
        "--projects", "-p",
        type=str,
        default=None,
        help="Comma-separated project slugs to include (e.g., 'gitlab-ci,chip-review'). "
             "Omit to include all projects.",
    )
    parser.add_argument(
        "--list-projects", "-l",
        action="store_true",
        help="List available project files and exit.",
    )
    args = parser.parse_args()

    if args.list_projects:
        cmd_list_projects()
        return

    slugs = None
    if args.projects:
        slugs = [s.strip() for s in args.projects.split(",") if s.strip()]

    generate(slugs)


if __name__ == "__main__":
    main()
