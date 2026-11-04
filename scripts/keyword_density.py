"""Check keyword density on a pipeline page (.md). Every term must stay under 1%.

Usage: python3 scripts/keyword_density.py clients/<slug>/pages/<page>.md [more.md ...]
Counts every occurrence, including headings, the meta description, and the
business name (e.g., "Show Me Tree Service" counts as "tree service").

The location name is checked too. It is read from the H1 (the text after the
last " in "), split on commas, with the state abbreviation dropped. So
"Tree Service in Hillcrest, Jacksonville, FL" checks "Hillcrest" and
"Jacksonville" separately. Pass --place "Name" to check another name instead.
"""
import re
import sys

TERMS = {
    "tree service": r"tree services?\b",
    "arborist": r"arborists?\b",
    "tree care": r"tree care\b",
    "expert": r"experts?\b",
}


def places_from_h1(text):
    m = re.search(r"^# (.+)$", text, re.M)
    if not m or " in " not in m.group(1):
        return []
    parts = [p.strip() for p in m.group(1).rsplit(" in ", 1)[1].split(",")]
    return [p for p in parts if p and not re.fullmatch(r"[A-Z]{2}", p)]


def check(path, places=None):
    text = open(path, encoding="utf-8").read()
    terms = dict(TERMS)
    for place in places or places_from_h1(text):
        terms[place] = re.escape(place.lower()) + r"\b"
    text = re.sub(r"^---\nmeta_description:\s*", "", text)
    clean = re.sub(r"[#*\[\]()_`>-]", " ", text).lower()
    words = len(re.findall(r"[a-z0-9$][\w'$,.]*", clean))
    ok = True
    print(f"{path}  ({words} words)")
    for term, pattern in terms.items():
        n = len(re.findall(pattern, clean))
        pct = 100 * n / words if words else 0
        flag = "OVER" if pct >= 1 else "ok"
        ok &= pct < 1
        print(f"  {term:<22} {n:>3}  {pct:5.2f}%  {flag}")
    return ok


if __name__ == "__main__":
    args = sys.argv[1:]
    places = []
    while "--place" in args:
        i = args.index("--place")
        places.append(args[i + 1])
        del args[i:i + 2]
    results = [check(p, places) for p in args]
    sys.exit(0 if all(results) else 1)
