#!/usr/bin/env python3
"""Static build for onojk123.com (stdlib only).

Reads data/*.json and rewrites the HTML between marker comments in source pages:

    <!-- BUILD:name -->  ...generated...  <!-- /BUILD:name -->

Everything outside the markers is left alone, and the output depends only on the
data files (and, for time-dependent blocks, the build date), so running it twice
in a row produces identical files.

Usage:
    python3 scripts/build.py           # validate data, rewrite pages
    python3 scripts/build.py --check   # validate, exit 1 if any page is stale
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
TODO = "TODO"

# Pages that may contain BUILD markers. Kept explicit so the build never touches
# files it wasn't meant to (e.g. backups, vendored HTML).
PAGES = ["index.html"]

MARKER = re.compile(
    r"(?P<open><!-- BUILD:(?P<name>[a-z0-9-]+) -->)(?P<body>.*?)(?P<close><!-- /BUILD:(?P=name) -->)",
    re.S,
)

STATUSES = {"live", "coming", TODO}
FORMAT_TYPES = {"kindle", "paperback", "audiobook", "youtube-readalong"}
VIDEO_KINDS = {"readalong", "music-video", "demo"}
ASIN_RE = re.compile(r"^[A-Z0-9]{10}$")
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


# --------------------------------------------------------------------------- data

class DataError(Exception):
    pass


def load(name):
    path = DATA / name
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        raise DataError(f"missing {path.relative_to(ROOT)}")
    except json.JSONDecodeError as e:
        raise DataError(f"{path.relative_to(ROOT)}: invalid JSON: {e}")


def known(v):
    """True if a data value is filled in (not empty, not TODO)."""
    return v not in (None, "", TODO)


def validate(books, videos, giveaways):
    errs = []
    ids = set()
    for i, b in enumerate(books.get("books", [])):
        where = f"books[{i}] ({b.get('id', '?')})"
        for f in ("id", "title", "subtitle", "series", "series_number", "status",
                  "formats", "date", "blurb", "cover", "readalong_urls"):
            if f not in b:
                errs.append(f"{where}: missing field '{f}'")
        if b.get("id") in ids:
            errs.append(f"{where}: duplicate id")
        ids.add(b.get("id"))
        if b.get("status") not in STATUSES:
            errs.append(f"{where}: status must be one of {sorted(STATUSES)}")
        if known(b.get("date")) and not DATE_RE.match(b["date"]):
            errs.append(f"{where}: date must be YYYY-MM-DD or TODO")
        for j, fm in enumerate(b.get("formats", [])):
            if fm.get("type") not in FORMAT_TYPES:
                errs.append(f"{where}: formats[{j}].type '{fm.get('type')}' not in {sorted(FORMAT_TYPES)}")
            if known(fm.get("asin")) and not ASIN_RE.match(fm["asin"]):
                errs.append(f"{where}: formats[{j}].asin '{fm['asin']}' is not a 10-character ASIN")
            if known(fm.get("url")) and not fm["url"].startswith("https://"):
                errs.append(f"{where}: formats[{j}].url must be https")
        for j, r in enumerate(b.get("readalong_urls", [])):
            if not str(r.get("url", "")).startswith("https://"):
                errs.append(f"{where}: readalong_urls[{j}].url must be https")
        cover = b.get("cover")
        if known(cover) and not (ROOT / cover.lstrip("/")).is_file():
            errs.append(f"{where}: cover file not found: {cover}")
    for i, v in enumerate(videos.get("videos", [])):
        where = f"videos[{i}]"
        if v.get("kind") not in VIDEO_KINDS:
            errs.append(f"{where}: kind must be one of {sorted(VIDEO_KINDS)}")
        if v.get("book_id") is not None and v["book_id"] not in ids:
            errs.append(f"{where}: unknown book_id '{v['book_id']}'")
        if not str(v.get("url", "")).startswith("https://"):
            errs.append(f"{where}: url must be https")
    if not isinstance(giveaways, list):
        errs.append("giveaways.json must be a JSON array")
    else:
        for i, g in enumerate(giveaways):
            if g.get("book_id") not in ids:
                errs.append(f"giveaways[{i}]: unknown book_id '{g.get('book_id')}'")
            for k in ("start", "end"):
                if not DATE_RE.match(str(g.get(k, ""))):
                    errs.append(f"giveaways[{i}].{k} must be YYYY-MM-DD (America/Los_Angeles)")
    if errs:
        raise DataError("\n  ".join(["data validation failed:"] + errs))


# ---------------------------------------------------------------------- renderers
# Each renderer takes the loaded data dict and returns the HTML that goes between
# its markers. Registered by marker name. Stages add renderers here.

RENDERERS = {}


def renderer(name):
    def deco(fn):
        RENDERERS[name] = fn
        return fn
    return deco


# --------------------------------------------------------------------------- core

def render_page(text, data, page):
    seen = []

    def sub(m):
        name = m.group("name")
        seen.append(name)
        fn = RENDERERS.get(name)
        if fn is None:
            raise DataError(f"{page}: no renderer for marker BUILD:{name}")
        body = fn(data).strip("\n")
        return f"{m.group('open')}\n{body}\n{m.group('close')}"

    out = MARKER.sub(sub, text)
    stray = re.findall(r"<!-- /?BUILD:[^>]*-->", MARKER.sub("", text))
    if stray:
        raise DataError(f"{page}: unmatched marker(s): {stray}")
    return out, seen


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--check", action="store_true", help="exit 1 if any page would change")
    args = ap.parse_args(argv)

    try:
        books = load("books.json")
        videos = load("videos.json")
        giveaways = load("giveaways.json")
        validate(books, videos, giveaways)
        data = {"books": books, "videos": videos, "giveaways": giveaways}

        stale = []
        for page in PAGES:
            path = ROOT / page
            old = path.read_text(encoding="utf-8")
            new, seen = render_page(old, data, page)
            status = "unchanged" if new == old else ("stale" if args.check else "updated")
            print(f"{page}: {len(seen)} block(s) [{', '.join(seen) or '-'}] {status}")
            if new != old:
                stale.append(page)
                if not args.check:
                    path.write_text(new, encoding="utf-8")
    except DataError as e:
        print(f"build: {e}", file=sys.stderr)
        return 2
    if args.check and stale:
        print("build --check: run `make build`", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
