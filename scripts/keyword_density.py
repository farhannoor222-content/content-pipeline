"""Check keyword density on a pipeline page (.md). Every term must stay under 1%.

Usage: python3 scripts/keyword_density.py clients/<slug>/pages/<page>.md [more.md ...]
Counts every occurrence, including headings, the meta description, and the
business name (e.g., "Show Me Tree Service" counts as "tree service").
"""
import re
import sys

TERMS = {
    "tree service": r"tree services?\b",
    "arborist": r"arborists?\b",
    "tree care": r"tree care\b",
    "expert": r"experts?\b",
}


def check(path):
    text = open(path, encoding="utf-8").read()
    text = re.sub(r"^---\nmeta_description:\s*", "", text)
    clean = re.sub(r"[#*\[\]()_`>-]", " ", text).lower()
    words = len(re.findall(r"[a-z0-9$][\w'$,.]*", clean))
    ok = True
    print(f"{path}  ({words} words)")
    for term, pattern in TERMS.items():
        n = len(re.findall(pattern, clean))
        pct = 100 * n / words if words else 0
        flag = "OVER" if pct >= 1 else "ok"
        ok &= pct < 1
        print(f"  {term:<13} {n:>3}  {pct:5.2f}%  {flag}")
    return ok


if __name__ == "__main__":
    results = [check(p) for p in sys.argv[1:]]
    sys.exit(0 if all(results) else 1)
