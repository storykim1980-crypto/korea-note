#!/usr/bin/env python3
"""Build a clean, allow-listed static deployment folder and archives."""
from __future__ import annotations

import argparse
import shutil
import zipfile
from pathlib import Path

SOURCE = Path(__file__).resolve().parent
WORKSPACE = SOURCE.parent
DEFAULT_PUBLIC = WORKSPACE / "seoul-note-public"
DEFAULT_SITE_ZIP = WORKSPACE / "seoul-note-site.zip"
DEFAULT_PROJECT_ZIP = WORKSPACE / "seoul-note-project.zip"

PUBLIC_PATHS = (
    Path("index.html"),
    Path("en/index.html"),
    Path("contact.html"),
    Path("en/contact.html"),
    Path("guides/climate-card.html"),
    Path("en/guides/climate-card.html"),
    Path("guides/hangul-signs.html"),
    Path("en/guides/hangul-signs.html"),
    Path("guides/kbeauty-labels.html"),
    Path("en/guides/kbeauty-labels.html"),
    Path("guides/kimjang.html"),
    Path("en/guides/kimjang.html"),
    Path("guides/korea-arrival.html"),
    Path("en/guides/korea-arrival.html"),
    Path("guides/korean-holidays.html"),
    Path("en/guides/korean-holidays.html"),
    Path("guides/korean-meal-culture.html"),
    Path("en/guides/korean-meal-culture.html"),
    Path("guides/seoul-neighborhoods.html"),
    Path("en/guides/seoul-neighborhoods.html"),
    Path("guides/tax-refund.html"),
    Path("en/guides/tax-refund.html"),
    Path("favicon.svg"),
    Path("404.html"),
    Path("robots.txt"),
    Path("sitemap.xml"),
)


def add_file(zf: zipfile.ZipFile, path: Path, base: Path, prefix: str = "") -> None:
    if path.is_file():
        name = Path(prefix) / path.relative_to(base)
        zf.write(path, name.as_posix())


def build_public(public_dir: Path, site_zip: Path) -> None:
    public_dir = public_dir.resolve()
    if public_dir == SOURCE or SOURCE in public_dir.parents:
        raise SystemExit("Refusing to put generated public output inside the source tree.")
    if public_dir.exists():
        shutil.rmtree(public_dir)
    public_dir.mkdir(parents=True)

    for relative in PUBLIC_PATHS:
        source_path = SOURCE / relative
        if not source_path.is_file():
            raise SystemExit(f"Missing required public file: {source_path}")
        target = public_dir / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source_path, target)

    assets_source = SOURCE / "assets"
    if not assets_source.is_dir():
        raise SystemExit(f"Missing public assets directory: {assets_source}")
    shutil.copytree(assets_source, public_dir / "assets")

    site_zip.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(site_zip, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
        for path in sorted(public_dir.rglob("*")):
            if path.is_file():
                zf.write(path, path.relative_to(public_dir).as_posix())
    with zipfile.ZipFile(site_zip) as zf:
        bad = zf.testzip()
        if bad:
            raise SystemExit(f"Archive CRC test failed at: {bad}")
        expected = {p.relative_to(public_dir).as_posix() for p in public_dir.rglob("*") if p.is_file()}
        actual = set(zf.namelist())
        if expected != actual:
            raise SystemExit(f"Deployment ZIP does not match the allow-list build. Missing={expected-actual}; extra={actual-expected}")


def build_project_archive(project_zip: Path) -> None:
    project_zip.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(project_zip, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
        for path in sorted(SOURCE.rglob("*")):
            if not path.is_file():
                continue
            if any(part.startswith(".") for part in path.relative_to(SOURCE).parts):
                continue
            zf.write(path, (Path(SOURCE.name) / path.relative_to(SOURCE)).as_posix())
    with zipfile.ZipFile(project_zip) as zf:
        bad = zf.testzip()
        if bad:
            raise SystemExit(f"Project archive CRC test failed at: {bad}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--public-dir", type=Path, default=DEFAULT_PUBLIC)
    parser.add_argument("--site-zip", type=Path, default=DEFAULT_SITE_ZIP)
    parser.add_argument("--project-zip", type=Path, default=DEFAULT_PROJECT_ZIP)
    args = parser.parse_args()

    build_public(args.public_dir, args.site_zip)
    build_project_archive(args.project_zip)

    with zipfile.ZipFile(args.site_zip) as zf:
        print(f"Public deployment: {args.public_dir} ({len(zf.namelist())} files, ZIP {args.site_zip.stat().st_size:,} bytes)")
        print("Entries:")
        for name in zf.namelist():
            print(f"  {name}")
    print(f"Full source/research archive: {args.project_zip} ({args.project_zip.stat().st_size:,} bytes). Do not deploy this archive.")


if __name__ == "__main__":
    main()
