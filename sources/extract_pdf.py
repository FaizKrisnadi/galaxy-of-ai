#!/usr/bin/env python3
"""Page-numbered text extraction from downloaded PDFs. Run with -I; PDF paths as args.
Writes <name>.txt with '=== p.N ===' markers; prints a quality summary (chars/page, empty pages)."""
import sys, pathlib
from pypdf import PdfReader

for pdf_path in sys.argv[1:]:
    p = pathlib.Path(pdf_path)
    out = p.with_suffix(".txt")
    r = PdfReader(str(p))
    n = len(r.pages)
    parts, empty, chars_total = [], 0, 0
    for i, page in enumerate(r.pages, start=1):
        try:
            t = page.extract_text() or ""
        except Exception as e:
            t = f"[EXTRACTION ERROR page {i}: {e}]"
        t = t.strip()
        t = t.encode("utf-8", "replace").decode("utf-8")  # sanitise surrogates from broken font mappings
        chars_total += len(t)
        if len(t) < 20: empty += 1
        parts.append(f"=== p.{i} ===\n{t}")
    out.write_text("\n\n".join(parts), encoding="utf-8")
    print(f"{p.name}: {n} pages, {chars_total} chars ({chars_total//max(n,1)} avg/page), {empty} near-empty pages -> {out.name}")
