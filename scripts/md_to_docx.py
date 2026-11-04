"""Convert a pipeline page (.md) into a .docx with real Heading 1/2/3 styles.

Usage: python3 scripts/md_to_docx.py clients/<slug>/pages/<page>.md
Writes the .docx next to the .md file, same name.
"""
import re
import sys
from pathlib import Path

from docx import Document
from docx.shared import Pt
from docx.opc.constants import RELATIONSHIP_TYPE as RT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn


INLINE = re.compile(r"\*\*(.+?)\*\*|\[(.+?)\]\((\S+?)\)")


def add_link(paragraph, text, url):
    """Append a live, blue, underlined hyperlink run."""
    r_id = paragraph.part.relate_to(url, RT.HYPERLINK, is_external=True)
    link = OxmlElement("w:hyperlink")
    link.set(qn("r:id"), r_id)
    run = OxmlElement("w:r")
    props = OxmlElement("w:rPr")
    color = OxmlElement("w:color")
    color.set(qn("w:val"), "0563C1")
    underline = OxmlElement("w:u")
    underline.set(qn("w:val"), "single")
    props.extend([color, underline])
    run.append(props)
    t = OxmlElement("w:t")
    t.text = text
    t.set(qn("xml:space"), "preserve")
    run.append(t)
    link.append(run)
    paragraph._p.append(link)


def add_inline(paragraph, text):
    """Add text, rendering **bold** and [text](url) links."""
    pos = 0
    for m in INLINE.finditer(text):
        if m.start() > pos:
            paragraph.add_run(text[pos:m.start()])
        if m.group(1):
            paragraph.add_run(m.group(1)).bold = True
        else:
            add_link(paragraph, m.group(2), m.group(3))
        pos = m.end()
    if pos < len(text):
        paragraph.add_run(text[pos:])


def convert(md_path: Path) -> Path:
    text = md_path.read_text(encoding="utf-8")
    doc = Document()
    # Page heading sizes (house standard): H1 18 pt, H2 16 pt, H3 14 pt.
    for name, size in (("Heading 1", 18), ("Heading 2", 16), ("Heading 3", 14)):
        doc.styles[name].font.size = Pt(size)

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
            h = doc.add_heading(level=len(m.group(1)))
            add_inline(h, m.group(2))
        elif line.startswith("- "):
            add_inline(doc.add_paragraph(style="List Bullet"), line[2:])
        else:
            add_inline(doc.add_paragraph(), line)

    out = md_path.with_suffix(".docx")
    doc.save(out)
    return out


if __name__ == "__main__":
    for arg in sys.argv[1:]:
        print(convert(Path(arg)))
