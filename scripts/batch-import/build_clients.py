#!/usr/bin/env python3
"""Build client folders (about.md, customer-persona.md, pipeline-notes.md) from Turnkey source files.
Usage: python3 build_clients.py <turnkey_dir> <repo_clients_dir> [--write]
"""
import os, re, sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
exec(open(os.path.join(HERE, "clients_map.py")).read())

SRC, OUT = sys.argv[1], sys.argv[2]
WRITE = "--write" in sys.argv

def rd(p):
    b = open(os.path.join(SRC, p), "rb").read()
    if b[:2] in (b"\xff\xfe", b"\xfe\xff"):
        return b.decode("utf-16")
    return b.decode("utf-8-sig", errors="replace")

BULLET = re.compile(r"^(\s*)(?:[*\-•–]\s*)+(.*)$")
HMARK = re.compile(r"^\[(h[1-4])\]\s*(.*)$", re.I)

def convert(text, title):
    out = [f"# {title}", ""]
    in_list = False
    for raw in text.replace("\r", "").split("\n"):
        line = raw.replace(" ", " ").rstrip()
        st = line.strip()
        if not st or re.fullmatch(r"[_\-=]{4,}", st):
            if in_list:
                out.append(""); in_list = False
            continue
        m = HMARK.match(st)
        if m:
            lvl = {"h1": "##", "h2": "###", "h3": "####", "h4": "####"}[m.group(1).lower()]
            out += ["", f"{lvl} {m.group(2)}", ""]; in_list = False; continue
        if st.startswith("#"):
            if st.startswith("# "):
                st = "#" + st
            out += ["", st, ""]; in_list = False; continue
        b = BULLET.match(line)
        if b and b.group(2).strip():
            ind = len(b.group(1).expandtabs(4))
            if not in_list:
                out.append("")
            out.append(("   " if ind > 0 and in_list else "") + "* " + b.group(2).strip())
            in_list = True; continue
        if b:  # empty bullet marker
            continue
        n = re.match(r"^(\d+)[.)]\s+(.*)$", st)
        if n:
            if not in_list:
                out.append("")
            out.append(f"{n.group(1)}. {n.group(2)}"); in_list = True; continue
        lv = re.match(r"^([A-Za-z][\w &'/()\-]{1,40}):\s+(\S.*)$", st)
        if lv and len(st) < 160:
            if not in_list:
                out.append("")
            out.append(f"* {st}"); in_list = True; continue
        if in_list:
            out.append(""); in_list = False
        if st.endswith(":") and len(st) <= 80:
            out += [f"### {st[:-1].strip()}", ""]; continue
        if len(st) <= 70 and not re.search(r"[.!?\"”]$", st):
            out += [f"## {st}", ""]; continue
        out += [st, ""]
    txt = "\n".join(out)
    txt = re.sub(r"\n{3,}", "\n\n", txt).strip() + "\n"
    return txt

WORD = re.compile(r"[^\W_]+", re.U)
def missing_words(src, dst):
    a, b = Counter(WORD.findall(src.lower())), Counter(WORD.findall(dst.lower()))
    return {k: v - b.get(k, 0) for k, v in a.items() if v > b.get(k, 0) and k not in ("h1", "h2", "h3", "h4")}

def bullets(t):
    return sum(1 for l in t.splitlines() if BULLET.match(l) and BULLET.match(l).group(2).strip())

# ---------- field extraction for pipeline-notes ----------
PHONE = re.compile(r"\+?1?\s*\(?\b\d{3}\)?[\s.\-‑]?\d{3}[\s.\-‑]\d{4}\b|\b\d{10}\b")
URL = re.compile(r"https?://\S+|\b[\w-]+\.(?:com|org|net|ai|co)\b/?")
EMAIL = re.compile(r"[\w.+-]+@[\w-]+\.[\w.]+")
def label(t, *names):
    lines = t.replace("\r", "").split("\n")
    for n in names:
        for i, l in enumerate(lines):
            m = re.match(r"(?i)^\W*(?:" + n + r")\s*:?\s*(.*)$", l.strip())
            if not m:
                continue
            v = m.group(1).strip().strip('"')
            if not v:
                for l2 in lines[i + 1:i + 4]:
                    if l2.strip():
                        v = l2.strip().lstrip("*-• ").strip(); break
            if v:
                return v
    return ""

def section(t, header_re):
    lines = t.replace("\r", "").split("\n")
    items = []
    for i, l in enumerate(lines):
        s = l.strip().lstrip("*-• ").strip()
        if re.match(r"(?i)^(?:" + header_re + r")\s*:?\s*(.*)$", s):
            inline = re.match(r"(?i)^(?:" + header_re + r")\s*:?\s*(.*)$", s).group(1)
            if inline:
                items += [x.strip() for x in re.split(r",(?![^()]*\))", inline) if x.strip()]
            for l2 in lines[i + 1:]:
                if not l2.strip():
                    if items: break
                    continue
                b = BULLET.match(l2)
                if not b:
                    break
                v = b.group(2).strip()
                if re.match(r"(?i)^(?:main services|our services|services|usps?|company usps|service areas?|other service areas|primary service area)\s*:?$", v):
                    break
                if v and not re.match(r"(?i)^(?:our services include|main services)\s*:?$", v):
                    items += [x.strip() for x in v.split(",") if x.strip()] if v.count(",") >= 1 and len(v) < 90 and "(" not in v else [v]
            if items:
                return items
    return items

BANNED = ("amplify adaptive assist augment automate bespoke bold boost commend contextual craft crafting curate curated captivate catalyze comprehensive cutting-edge daunting delve disrupt discover deploy efficiently elevate embark empower endeavor enhance ensure entrust esteemed foster future game-changer groundbreaking heart harness intricate landscape master merely meticulous navigate optimize passionate persistent precise precision prompt proven realm relentless revolutionize rigorous robust savvy seasoned seek sharp skilled skyrocket smart straightforward swift streamline tailored tapestry top-tier transform underpins underscore unlock unparalleled unveil uncover utmost best top number leading greatest deserve premier").split()
SUPER = re.compile(r"(?i)\b(best|top[- ]?(?:notch|rated|tier|quality)?|#1|no\.\s?1|number one|leading|premier|unparalleled|most trusted|greatest)\b")

def flags_for(about, usps):
    f = []
    hits = sorted(set(m.group(0) for m in SUPER.finditer(about + "\n" + "\n".join(usps))))
    if hits:
        f.append("Superlatives in the source text (never use on pages): " + ", ".join(f'"{h}"' for h in hits) + ".")
    bw = sorted(set(w for w in BANNED if re.search(r"(?i)\b" + re.escape(w) + r"\w*\b", "\n".join(usps))))
    if bw:
        f.append("USPs contain banned words (reword before using as headings): " + ", ".join(f'"{w}"' for w in bw) + ".")
    if re.search(r"(?i)certif", about):
        f.append('"Certified" is allowed: about.md mentions certification. Use only the exact certification it names.')
    else:
        f.append('"Certified" is not allowed: about.md mentions no certification. "Arborist" alone is fine.')
    return f

def notes(slug, name, ind, about, persona, extra, ovr={}):
    phone = (PHONE.findall(about) or [""])[0].strip()
    email = (EMAIL.findall(about) or [""])[0]
    web = next((u for u in URL.findall(about) if "@" not in u), "")
    est = label(about, r"established", r"business open date", r"founded")
    addr = label(about, r"address", r"located", r"location")
    if not addr:
        m = re.search(r"(?m)^\W*(\d+\s+[^\n]*,\s*[^\n]*\b[A-Z]{2}\b[^\n]*)$", about)
        addr = m.group(1).strip() if m else ""
    city = label(about, r"main target city", r"target city", r"target area", r"target location", r"target service location", r"primary service location", r"primary service area", r"primary location", r"main service area", r"main service location")
    if not city and addr:
        m = re.search(r",\s*([A-Za-z .]+),?\s+([A-Z]{2})\b", addr)
        city = f"{m.group(1).strip()}, {m.group(2)}" if m else ""
    services = section(about, r"(?:main |our )?services(?: we offer)?|main services")
    usps = section(about, r"(?:company )?usps?|ups?s")
    areas = section(about, r"(?:other )?service areas?|areas we serve|we also serve|service locations")
    city = ovr.get("city", city); services = ovr.get("services", services); usps = ovr.get("usps", usps); areas = ovr.get("areas", areas)
    tree = ind == "tree"
    city_note = city or "UNCONFIRMED (not stated in about.md)"
    L = ["---", f"business_name: {name}", f"industry: {'Tree Service' if tree else ind.title() + ' (NOT tree service)'}"]
    if phone: L.append(f'phone: "{phone}"')
    if email: L.append(f"email: {email}")
    if web: L.append(f"website: {web}")
    L.append(f"address: {addr or 'Not provided'}")
    if est: L.append(f"established: {est}")
    L += [f"main_targeted_city: {city_note}", "---", "", f"# Pipeline Notes: {name}", "",
          "This file holds only what `about.md` and `customer-persona.md` do not already cover: tracking data the content pipeline needs to keep pages varied and consistent.", "",
          "**Auto-drafted from the source files in a batch import.** Fields below were extracted by script. Review them, especially the main city, services, USPs, and process steps, before writing the first page.", ""]
    if not tree:
        L += [f"**Different industry.** This business is {ind}, not tree service. The page templates in `templates/` are written for tree service (tree-specific H1, Service Definitions, required terms like \"arborist\" and \"tree surgeons\"). Those parts do not apply. Decide on an industry-specific template before writing pages.", ""]
    L += ["## Page Types", "",
          f"1. **Main Targeted City: {city_note}**",
          "   - General location page: `templates/location-page-template.md`" if tree else "   - Template: TBD for this industry",
          "   - Per-service pages: `templates/service-location-page-template.md`" if tree else "",
          "2. **Nearby Cities:** `templates/location-page-template.md` with population-tier word counts" if tree else "2. **Nearby Cities:** template TBD for this industry",
          "3. **Neighborhood Pages:** template TBD", ""]
    L += ["## Service Area (reference only, not a fixed content queue)", ""]
    L += [f"- {a}" for a in areas] if areas else ["- Not listed in about.md. See customer-persona.md."]
    L += ["", "## Services", ""]
    L += [f"- {s}" for s in services] if services else ["- Not clearly listed in about.md. Confirm."]
    if tree:
        L += ["", "Tree Removal means section by section, and Tree Cutting means felling in one piece (Service Definitions in tone-and-qa-rules.md). Offer Tree Cutting only if it is listed above."]
    L += ["", "## USPs", "", "From about.md. On service pages, tie each one to the service (see service-location-page-template.md).", ""]
    L += [f"- {u}" for u in usps] if usps else ["- Not listed in about.md. Build from customer-persona.md and confirm."]
    L += ["", "## Working Process Steps", "", "Not drafted yet. Build 4 or 6 genuine job steps from customer-persona.md (\"What to Expect\" or similar) before the first page. No USPs as steps.", "",
          "## Pricing Reference (for FAQ cost answers)", "",
          "Check customer-persona.md for price ranges. If it has none, research a real local or regional range per page and present it as a typical area range, not the company's own price.", "",
          "## Client-Specific Banned Words", "(In addition to the global list in tone-and-qa-rules.md)", "- None identified yet", "",
          "## Client-Specific Notes", ""]
    for f in flags_for(about, usps) + extra:
        L.append(f"- {f}")
    if not persona:
        L.append("- No customer persona file (fine for this client). Pages rely on about.md and city research.")
    L += ["", "## Pattern and Angle Tracker", "Updated after every page. Choose a pattern or angle not used in the client's last 3 to 5 pages (per column).", "",
          "| City, State | Page Type | H1 Pattern | Heading Angle | Services Angle | Why-Choose-Us Angle | Process Angle | FAQ Topics |",
          "|---|---|---|---|---|---|---|---|", "",
          "## Heading Pool: Customized Local H2", "| Heading Used | City, State | Notes |", "|---|---|---|", "",
          "## Pages Written", "| City, State | Date | File |", "|---|---|---|", ""]
    txt = "\n".join(l for l in L if l is not None)
    return txt, dict(city=city, phone=phone, addr=addr, services=len(services), usps=len(usps), areas=len(areas))

EXTRA = {}
OVR = {}
extra_path = os.path.join(HERE, "client_extra_notes.py")
if os.path.exists(extra_path):
    exec(open(extra_path).read())

problems = 0
for slug, name, ab, pe, ind in B:
    about_src = "\n\n".join(rd(p) for p in ab)
    pers_src = "\n\n".join(rd(p) for p in pe)
    about_md = convert(about_src, f"About: {name}") if ab else f"# About: {name}\n\nNo about file was provided. See customer-persona.md.\n"
    pers_md = convert(pers_src, f"{name} Customer Profile") if pe else ""
    mw = {}
    if ab: mw.update(missing_words(about_src, about_md))
    if pe: mw.update(missing_words(pers_src, pers_md))
    bok = (bullets(about_md) >= bullets(about_src)) and (not pe or bullets(pers_md) >= bullets(pers_src))
    nt, info = notes(slug, name, ind, about_src, pers_src, EXTRA.get(slug, []), OVR.get(slug, {}))
    ok = not mw and bok
    if not ok: problems += 1
    print(f"{'OK ' if ok else 'BAD'} {slug:44} city={info['city'][:28]:28} svc={info['services']:2} usp={info['usps']:2} areas={info['areas']:2} phone={'y' if info['phone'] else 'n'} addr={'y' if info['addr'] else 'n'}" + (f" missing={list(mw.items())[:5]}" if mw else "") + ("" if bok else " BULLETS-MISMATCH"))
    if WRITE:
        d = os.path.join(OUT, slug)
        os.makedirs(d, exist_ok=True)
        open(os.path.join(d, "about.md"), "w").write(about_md)
        if pe:
            open(os.path.join(d, "customer-persona.md"), "w").write(pers_md)
        open(os.path.join(d, "pipeline-notes.md"), "w").write(nt)
print("problems:", problems)
