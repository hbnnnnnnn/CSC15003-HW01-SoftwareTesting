#!/usr/bin/env python3
"""Convert markdown files to PDF using Google Chrome headless, with inline images."""

import subprocess
import os
import tempfile
import base64
import re

# Files to export
FILES = [
    "HW01_Report.md",
    "AI-02_AI_Audit_Report.md",
    "AI-03_AI_Disclosure_Form.md",
    "AI-05_AI_Privacy_Checklist.md",
    "AI-06_AI_Student_Acknowledgement.md",
    "prompt_log.md",
    "QA_QC_Mindmap.md",
]

BASE_DIR = "/Users/hbn/Documents/CSC15003-HW01-SoftwareTesting"
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"


def inline_images(html_content, md_dir):
    """Replace relative <img> src with base64 data URIs."""

    def replace_src(match):
        src = match.group(1)
        # Skip external URLs
        if src.startswith("http"):
            return match.group(0)

        # Resolve absolute path
        img_path = os.path.normpath(os.path.join(md_dir, src))
        if not os.path.exists(img_path):
            return f'<img src="" alt="(image not found: {src})" style="max-width:100%;height:auto;border:2px solid red;">'

        with open(img_path, "rb") as f:
            data = f.read()

        ext = os.path.splitext(img_path)[1].lower()
        mime = {
            ".png": "image/png",
            ".jpg": "image/jpeg",
            ".jpeg": "image/jpeg",
            ".gif": "image/gif",
            ".webp": "image/webp",
        }.get(ext, "image/png")

        b64 = base64.b64encode(data).decode("ascii")
        # Only prompt_log screenshots get the red border; all others are plain
        is_prompt_log = "screenshots/prompt_log" in src
        style = "max-width:100%;height:auto;" + ("border:2px solid red;" if is_prompt_log else "")
        return f'<img src="data:{mime};base64,{b64}" style="{style}">'

    # Match <img ... src="..." ...>
    return re.sub(r'<img\s+[^>]*src="([^"]+)"[^>]*>', replace_src, html_content)


def md_to_html(md_path):
    """Convert markdown to basic HTML, inlining local images."""
    import markdown

    with open(md_path, "r", encoding="utf-8") as f:
        md_content = f.read()

    md_dir = os.path.dirname(md_path) or "."

    html_content = markdown.markdown(
        md_content,
        extensions=["tables", "fenced_code", "nl2br"],
    )

    # Inline images as base64
    html_content = inline_images(html_content, md_dir)

    title = os.path.basename(md_path).replace(".md", "")

    template = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>{title}</title>
<style>
  body {{
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
    font-size: 11pt;
    line-height: 1.6;
    max-width: 900px;
    margin: 2cm auto;
    padding: 0 1cm;
    color: #222;
  }}
  h1 {{ font-size: 20pt; border-bottom: 2px solid #333; padding-bottom: 8px; margin-top: 24px; }}
  h2 {{ font-size: 16pt; border-bottom: 1px solid #aaa; padding-bottom: 4px; margin-top: 20px; }}
  h3 {{ font-size: 13pt; margin-top: 16px; }}
  h4 {{ font-size: 11pt; margin-top: 14px; }}
  table {{ border-collapse: collapse; width: 100%; margin: 12px 0; font-size: 10pt; }}
  th, td {{ border: 1px solid #aaa; padding: 6px 8px; text-align: left; }}
  th {{ background: #f0f0f0; font-weight: bold; }}
  tr:nth-child(even) {{ background: #fafafa; }}
  code {{ background: #f5f5f5; padding: 1px 4px; border-radius: 3px; font-size: 9pt; }}
  pre {{ background: #f5f5f5; padding: 12px; border-radius: 4px; overflow-x: auto; font-size: 9pt; }}
  img {{ max-width: 100%; height: auto; }}
  blockquote {{ border-left: 3px solid #ccc; margin-left: 0; padding-left: 12px; color: #555; }}
  a {{ color: #0066cc; }}
  hr {{ border: none; border-top: 1px solid #ccc; margin: 20px 0; }}
  .mermaid {{ background: #fff; }}
</style>
</head>
<body>
{html_content}
</body>
</html>"""

    return template


def export_to_pdf(html_path, pdf_path):
    """Export HTML to PDF using Chrome headless."""
    cmd = [
        CHROME,
        "--headless=new",
        "--no-sandbox",
        f"--print-to-pdf={pdf_path}",
        "--print-to-pdf-no-header",
        f"--margins-top=15",
        f"--margins-bottom=15",
        f"--margins-left=15",
        f"--margins-right=15",
        f"file://{html_path}",
    ]
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
    return result.returncode == 0


def main():
    os.makedirs(os.path.join(BASE_DIR, "pdf_exports"), exist_ok=True)

    for md_file in FILES:
        md_path = os.path.join(BASE_DIR, md_file)
        if not os.path.exists(md_path):
            print(f"  SKIP  {md_file} — not found")
            continue

        html = md_to_html(md_path)
        with tempfile.NamedTemporaryFile(
            suffix=".html", delete=False, mode="w", encoding="utf-8"
        ) as f:
            f.write(html)
            tmp_html = f.name

        pdf_name = md_file.replace(".md", ".pdf")
        pdf_path = os.path.join(BASE_DIR, "pdf_exports", pdf_name)

        print(f"  Exporting {md_file} → {pdf_name} ...", end=" ", flush=True)
        ok = export_to_pdf(tmp_html, pdf_path)
        os.unlink(tmp_html)

        if ok:
            print("OK")
        else:
            print("FAILED")

    print("\nDone. PDFs saved to pdf_exports/")


if __name__ == "__main__":
    main()