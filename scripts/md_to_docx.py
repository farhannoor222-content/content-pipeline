"""Convert a pipeline page (.md) into a .docx with real Heading 1/2/3 styles.

Usage: python3 scripts/md_to_docx.py clients/<slug>/pages/<page>.md
Writes the .docx next to the .md file, same name.
"""
import re
import sys
from pathlib import Path

from docx import Document


def convert(md_path: Path) -> Path:
    text = md_path.read_text(encoding="utf-8")
    doc = Document()

    # Front matter: show the meta description as a labeled paragraph.
    fm = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if fm:
        text = text[fm.end():]
        meta = re.search(r'meta_description:\s*"?(.*?)"?\s*$', fm.group(1), re.M)
        if meta:
            p = doc.add_paragraph()
            p.add_run("Meta Description: ").bold = True
            p.add_run(meta.group(1))

    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue
        m = re.match(r"^(#{1,3})\s+(.*)$", line)
        if m:
            doc.add_heading(m.group(2), level=len(m.group(1)))
        elif line.startswith("- "):
            doc.add_paragraph(line[2:], style="List Bullet")
        else:
            doc.add_paragraph(line)

    out = md_path.with_suffix(".docx")
    doc.save(out)
    return out


if __name__ == "__main__":
    for arg in sys.argv[1:]:
        print(convert(Path(arg)))
