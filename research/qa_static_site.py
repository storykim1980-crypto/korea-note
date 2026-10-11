#!/usr/bin/env python3
"""Static structural QA for the current bilingual site; no network or deployment."""
from __future__ import annotations

import re
import subprocess
import tempfile
import xml.etree.ElementTree as ET
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse, unquote

ROOT = Path(__file__).resolve().parents[1]
PAGES = [ROOT / "index.html", ROOT / "en/index.html", ROOT / "contact.html", ROOT / "en/contact.html"] + sorted((ROOT / "guides").glob("*.html")) + sorted((ROOT / "en/guides").glob("*.html"))
OWN_HOSTS = {"seoul-note.com", "www.seoul-note.com"}
REF_ATTRS = ("aria-labelledby", "aria-describedby", "aria-controls", "aria-owns", "aria-activedescendant")


class Scan(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.ids: list[str] = []
        self.refs: list[tuple[str, str]] = []
        self.hrefs: list[tuple[str, dict[str, str]]] = []
        self.resources: list[tuple[str, str]] = []
        self.images: list[dict[str, str]] = []
        self.scripts: list[str] = []
        self._script_depth = False
        self._active_script: list[str] = []
        self.h1_count = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        d = {k: (v or "") for k, v in attrs}
        if "id" in d:
            self.ids.append(d["id"])
        if tag == "h1":
            self.h1_count += 1
        for attr in REF_ATTRS:
            if d.get(attr):
                self.refs.extend((attr, token) for token in d[attr].split())
        if tag == "label" and d.get("for"):
            self.refs.append(("for", d["for"]))
        if tag == "a" and d.get("href"):
            self.hrefs.append((d["href"], d))
        if tag in {"img", "script", "link", "source", "video", "audio"}:
            attr = "src" if tag in {"img", "script", "source", "video", "audio"} else "href"
            if d.get(attr):
                self.resources.append((tag, d[attr]))
        if tag == "img":
            self.images.append(d)
        if tag == "script" and d.get("type", "").lower() not in {"application/ld+json", "application/json"}:
            self._script_depth = True
            self._active_script = []

    def handle_data(self, data: str) -> None:
        if self._script_depth:
            self._active_script.append(data)

    def handle_endtag(self, tag: str) -> None:
        if tag == "script" and self._script_depth:
            self.scripts.append("".join(self._active_script))
            self._script_depth = False
            self._active_script = []


def local_file(current: Path, url_path: str) -> Path:
    decoded = unquote(url_path)
    if not decoded:
        return current.resolve()
    if decoded.endswith("/"):
        decoded += "index.html"
    relative = Path(decoded.lstrip("/")) if decoded.startswith("/") else (current.parent / decoded).relative_to(ROOT)
    return (ROOT / relative).resolve()


def check_sitemap(errors: list[str]) -> int:
    sitemap_path = ROOT / "sitemap.xml"
    sitemap_ns = "{http://www.sitemaps.org/schemas/sitemap/0.9}"
    xhtml_ns = "{http://www.w3.org/1999/xhtml}"
    pairs = [("/", "/en/"), ("/contact.html", "/en/contact.html")]
    pairs.extend((f"/guides/{page.name}", f"/en/guides/{page.name}") for page in sorted((ROOT / "guides").glob("*.html")))
    expected: dict[str, dict[str, str]] = {}
    for ja_path, en_path in pairs:
        ja_url = f"https://seoul-note.com{ja_path}"
        en_url = f"https://seoul-note.com{en_path}"
        alternates = {"ja-JP": ja_url, "en": en_url, "x-default": ja_url}
        expected[ja_url] = alternates
        expected[en_url] = alternates
    try:
        root = ET.parse(sitemap_path).getroot()
    except (OSError, ET.ParseError) as exc:
        errors.append(f"sitemap.xml: could not parse XML: {exc}")
        return 0
    found: dict[str, dict[str, str]] = {}
    for entry in root.findall(f"{sitemap_ns}url"):
        loc = (entry.findtext(f"{sitemap_ns}loc") or "").strip()
        if not loc:
            errors.append("sitemap.xml: url entry is missing loc")
            continue
        if loc in found:
            errors.append(f"sitemap.xml: duplicate URL {loc}")
        alternates = {
            link.attrib.get("hreflang", ""): link.attrib.get("href", "")
            for link in entry.findall(f"{xhtml_ns}link")
            if link.attrib.get("rel") == "alternate"
        }
        found[loc] = alternates
        parsed = urlparse(loc)
        if parsed.scheme != "https" or parsed.netloc != "seoul-note.com":
            errors.append(f"sitemap.xml: unexpected canonical URL {loc}")
        elif not local_file(ROOT / "index.html", parsed.path).is_file():
            errors.append(f"sitemap.xml: URL target does not exist: {loc}")
        if loc in expected and alternates != expected[loc]:
            errors.append(f"sitemap.xml: incorrect language alternates for {loc}: {alternates}")
        lastmod = (entry.findtext(f"{sitemap_ns}lastmod") or "").strip()
        if lastmod and not re.fullmatch(r"\d{4}-\d{2}-\d{2}", lastmod):
            errors.append(f"sitemap.xml: invalid lastmod date for {loc}: {lastmod}")
    for missing in sorted(set(expected) - set(found)):
        errors.append(f"sitemap.xml: missing expected URL {missing}")
    for extra in sorted(set(found) - set(expected)):
        errors.append(f"sitemap.xml: unexpected URL {extra}")
    return len(found)


def main() -> int:
    errors: list[str] = []
    totals = Counter()
    own_base = "https://seoul-note.com/"

    home_image_sets: dict[str, set[str]] = {}
    for page in PAGES:
        rel = page.relative_to(ROOT).as_posix()
        parser = Scan()
        raw = page.read_text(encoding="utf-8")
        parser.feed(raw)
        image_sources = [image.get("src", "") for image in parser.images]
        duplicates = [src for src, count in Counter(image_sources).items() if src and count > 1]
        if duplicates:
            errors.append(f"{rel}: repeated image source(s): {', '.join(duplicates)}")
        if rel in {"index.html", "en/index.html"}:
            if len(image_sources) != 12:
                errors.append(f"{rel}: expected 12 editorial image placements, found {len(image_sources)}")
            home_image_sets[rel] = {Path(urlparse(src).path).name for src in image_sources if src}
        totals["pages"] += 1
        if parser.h1_count != 1:
            errors.append(f"{rel}: expected one h1, found {parser.h1_count}")
        duplicated = [ident for ident, count in Counter(parser.ids).items() if count > 1]
        if duplicated:
            errors.append(f"{rel}: duplicate id(s): {', '.join(duplicated)}")
        id_set = set(parser.ids)
        for attr, ref in parser.refs:
            if ref not in id_set:
                errors.append(f"{rel}: {attr} references missing id #{ref}")
        for image in parser.images:
            if "alt" not in image:
                errors.append(f"{rel}: image missing alt: {image.get('src','')}")
            if not image.get("src", "").lower().startswith("data:"):
                target = local_file(page, image.get("src", ""))
                if not target.exists():
                    errors.append(f"{rel}: missing image {image.get('src')} -> {target}")
                else:
                    totals["images"] += 1
        for href, attrs in parser.hrefs:
            parsed = urlparse(href)
            if parsed.scheme in {"mailto", "tel", "javascript", "data"}:
                continue
            if parsed.netloc and parsed.netloc not in OWN_HOSTS:
                totals["external_links"] += 1
                if attrs.get("target", "").lower() == "_blank":
                    rel_tokens = set(attrs.get("rel", "").lower().split())
                    if not {"noopener", "noreferrer"}.issubset(rel_tokens):
                        errors.append(f"{rel}: _blank link missing noopener noreferrer: {href}")
                continue
            if parsed.netloc in OWN_HOSTS:
                path = parsed.path
                fragment = parsed.fragment
            else:
                path = parsed.path
                fragment = parsed.fragment
            target = local_file(page, path)
            if not target.exists():
                errors.append(f"{rel}: missing internal link {href} -> {target}")
                continue
            totals["internal_links"] += 1
            if fragment and target.suffix.lower() in {".html", ".htm"}:
                other = Scan()
                other.feed(target.read_text(encoding="utf-8"))
                if unquote(fragment) not in set(other.ids):
                    errors.append(f"{rel}: fragment #{fragment} missing in {target.relative_to(ROOT)}")
        for tag, src in parser.resources:
            if tag == "script" and src.lower().startswith(("http:", "https:", "data:")):
                continue
            if tag == "link" and src.lower().startswith(("http:", "https:", "data:")):
                continue
            if tag not in {"script", "link", "source", "video", "audio"}:
                continue
            if src.lower().startswith("data:"):
                continue
            if urlparse(src).netloc and urlparse(src).netloc not in OWN_HOSTS:
                continue
            target = local_file(page, urlparse(src).path)
            if not target.exists():
                errors.append(f"{rel}: missing {tag} resource {src} -> {target}")

        for idx, script in enumerate(parser.scripts):
            if not script.strip():
                continue
            with tempfile.NamedTemporaryFile("w", suffix=".js", encoding="utf-8", delete=False) as tmp:
                tmp.write(script)
                temp_name = tmp.name
            result = subprocess.run(["node", "--check", temp_name], capture_output=True, text=True)
            Path(temp_name).unlink(missing_ok=True)
            if result.returncode:
                errors.append(f"{rel}: JS syntax error in script {idx + 1}: {result.stderr.strip()[:500]}")
            else:
                totals["scripts"] += 1

    ja_images = home_image_sets.get("index.html", set())
    en_images = home_image_sets.get("en/index.html", set())
    if ja_images != en_images:
        errors.append("homepages: Japanese and English editions do not use the same topic-image set")
    unique_home_images = len(ja_images)
    sitemap_count = check_sitemap(errors)
    print(f"Pages: {totals['pages']}; local image references: {totals['images']}; unique homepage image assets: {unique_home_images}; inline scripts syntax-checked: {totals['scripts']}; internal links: {totals['internal_links']}; external links checked for rel: {totals['external_links']}; sitemap URLs: {sitemap_count}")
    if errors:
        print(f"FAIL: {len(errors)} issue(s)")
        for error in errors:
            print(" -", error)
        return 1
    print("PASS: no duplicate IDs, missing ARIA/label references, missing local files, missing image alt text, or JavaScript syntax errors.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
