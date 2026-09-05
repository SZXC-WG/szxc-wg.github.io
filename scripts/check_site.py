#!/usr/bin/env python3
"""Check a Hugo build without network access or third-party dependencies.

Usage: python scripts/check_site.py public --base-url https://szxc-wg.github.io/
Checks local links, HTML anchors, referenced assets, duplicate IDs, document
language, and reciprocal English/Chinese alternate links. Hugo alias pages are
checked for broken links but do not need language alternates.
"""
from __future__ import annotations

import argparse
import json
import posixpath
import re
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit


class Page(HTMLParser):
    def __init__(self, source: str) -> None:
        super().__init__(convert_charrefs=True)
        self.source = source
        self.ids: set[str] = set()
        self.duplicates: set[str] = set()
        self.links: list[tuple[str, str]] = []
        self.alternates: dict[str, str] = {}
        self.lang = ""
        self.redirect = False

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        if tag == "html":
            self.lang = values.get("lang") or ""
        if tag == "meta" and (values.get("http-equiv") or "").lower() == "refresh":
            self.redirect = True
        identifier = values.get("id") or (values.get("name") if tag == "a" else None)
        if identifier:
            if identifier in self.ids:
                self.duplicates.add(identifier)
            self.ids.add(identifier)
        for attr in ("href", "src", "poster"):
            if values.get(attr):
                self.links.append((values[attr], f"{tag}[{attr}]"))
        # Data URLs may contain commas; they are self-contained and need no check.
        srcset = values.get("srcset") or ""
        if srcset and "data:" not in srcset:
            for candidate in srcset.split(","):
                parts = candidate.strip().split()
                if parts:
                    self.links.append((parts[0], f"{tag}[srcset]"))
        if tag == "link" and "alternate" in (values.get("rel") or "").split():
            lang = values.get("hreflang")
            href = values.get("href")
            if lang and href and lang != "x-default":
                self.alternates[lang.lower().split("-")[0]] = href

    handle_startendtag = handle_starttag


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("directory", nargs="?", default="public", type=Path)
    parser.add_argument("--base-url", default="https://szxc-wg.github.io/")
    parser.add_argument("--languages", nargs="+", default=["en", "zh"])
    args = parser.parse_args()
    root = args.directory.resolve()
    if not root.is_dir():
        parser.error(f"build directory does not exist: {root}")
    base_url = args.base_url.rstrip("/") + "/"
    base = urlsplit(base_url)
    prefix = base.path.rstrip("/")
    files = {path.relative_to(root).as_posix(): path for path in root.rglob("*") if path.is_file()}
    pages: dict[str, Page] = {}
    errors: set[str] = set()
    checked = 0
    for name, path in files.items():
        if name.endswith(".html"):
            page = Page(name)
            page.feed(path.read_text(encoding="utf-8"))
            pages[name] = page
    if not pages:
        parser.error(f"no HTML pages found in {root}")

    def document_url(source: str) -> str:
        route = source[:-10] if source.endswith("index.html") else source
        return urljoin(base_url, route)

    def resolve(source: str, target: str) -> tuple[str | None, str]:
        parsed = urlsplit(urljoin(document_url(source), target))
        if parsed.scheme not in ("http", "https") or parsed.netloc.lower() != base.netloc.lower():
            return None, ""
        path = unquote(parsed.path)
        if prefix:
            if path != prefix and not path.startswith(prefix + "/"):
                return "<outside base URL>" + path, ""
            path = path[len(prefix):]
        relative = posixpath.normpath(path).lstrip("/")
        if relative == ".":
            relative = ""
        # Match exact names even on Windows, where Path.exists is case-insensitive.
        if relative not in files:
            relative = posixpath.join(relative, "index.html")
        fragment = unquote(parsed.fragment.split(":~:", 1)[0])
        return relative, fragment

    def check_link(source: str, target: str, context: str) -> None:
        nonlocal checked
        destination, fragment = resolve(source, target)
        if destination is None:
            return
        checked += 1
        if destination not in files:
            errors.add(f"{source}: missing {context} {target!r} -> {destination}")
        elif fragment and fragment != "top" and destination in pages and fragment not in pages[destination].ids:
            errors.add(f"{source}: missing anchor {target!r} in {destination}")

    for source, page in pages.items():
        for identifier in page.duplicates:
            errors.add(f"{source}: duplicate id {identifier!r}")
        for target, context in page.links:
            check_link(source, target, context)
        if page.redirect or source.endswith("404.html"):
            continue
        own_lang = page.lang.lower().split("-")[0]
        if own_lang not in args.languages:
            errors.add(f"{source}: expected document lang in {args.languages}, got {page.lang!r}")
        for lang in args.languages:
            if lang not in page.alternates:
                errors.add(f"{source}: missing {lang} alternate link")
                continue
            target, _ = resolve(source, page.alternates[lang])
            if target not in pages:
                errors.add(f"{source}: {lang} alternate does not point to a local HTML page")
                continue
            alternate = pages[target]
            actual_lang = alternate.lang.lower().split("-")[0]
            if actual_lang != lang:
                errors.add(f"{source}: {lang} alternate {target} has lang {alternate.lang!r}")
            if own_lang in alternate.alternates:
                reciprocal, _ = resolve(target, alternate.alternates[own_lang])
                if reciprocal != source:
                    errors.add(f"{source}: {lang} alternate {target} does not link back")
            else:
                errors.add(f"{source}: {lang} alternate {target} lacks reciprocal {own_lang} link")

    css_urls = re.compile(r"url\(\s*(['\"]?)(.*?)\1\s*\)", re.IGNORECASE)
    for source, path in files.items():
        if source.endswith(".css"):
            css = re.sub(r"/\*.*?\*/", "", path.read_text(encoding="utf-8"), flags=re.DOTALL)
            for _, target in css_urls.findall(css):
                if target and not target.startswith("#"):
                    check_link(source, target, "CSS resource")
        elif source.endswith(".webmanifest"):
            try:
                manifest = json.loads(path.read_text(encoding="utf-8"))
                for icon in manifest.get("icons", []):
                    if icon.get("src"):
                        check_link(source, icon["src"], "manifest icon")
            except (json.JSONDecodeError, AttributeError) as exc:
                errors.add(f"{source}: invalid webmanifest: {exc}")

    for error in sorted(errors):
        print(f"ERROR {error}")
    if errors:
        print(f"FAILED: {len(errors)} issue(s) across {len(pages)} HTML pages; {checked} local references checked.")
        return 1
    print(f"OK: {len(pages)} HTML pages, {checked} local references, reciprocal {'/'.join(args.languages)} translations.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
