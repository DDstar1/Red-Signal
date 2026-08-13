"""
build.py — compile landing.template.html → landing.html

Placeholder syntax in the template:
  {{ASSET:filename}}        — inline as data URI (images) or raw SVG tag
  {{ASSET_URI:filename}}    — always data URI (even for SVGs), for use in src/url()

SVGs get special treatment:
  - {{ASSET:icon.svg}}      → raw <svg>...</svg> so CSS variables can reach inside
  - {{ASSET_URI:icon.svg}}  → data:image/svg+xml;base64,... for use in <img src> or CSS url()

Supported formats: jpg/jpeg, png, gif, webp → data URI  |  svg → inline or data URI
"""

import base64, mimetypes, pathlib, re, sys

ASSETS = pathlib.Path("assets")
TEMPLATE = pathlib.Path("landing.template.html")
OUTPUT = pathlib.Path("landing.html")


def data_uri(path: pathlib.Path) -> str:
    mime = mimetypes.guess_type(path)[0] or "application/octet-stream"
    b64 = base64.b64encode(path.read_bytes()).decode()
    return f"data:{mime};base64,{b64}"


def inline_svg(path: pathlib.Path) -> str:
    return path.read_text(encoding="utf-8").strip()


def resolve(match: re.Match) -> str:
    kind = match.group(1)   # "ASSET" or "ASSET_URI"
    name = match.group(2).strip()
    path = ASSETS / name

    if not path.exists():
        print(f"  WARNING: asset not found → {path}", file=sys.stderr)
        return match.group(0)  # leave placeholder as-is

    ext = path.suffix.lower()

    if kind == "ASSET" and ext == ".svg":
        print(f"  inline SVG  : {name}")
        return inline_svg(path)
    else:
        print(f"  data URI    : {name}")
        return data_uri(path)


def build():
    if not TEMPLATE.exists():
        sys.exit(f"ERROR: {TEMPLATE} not found")

    template = TEMPLATE.read_text(encoding="utf-8")
    pattern = re.compile(r"\{\{(ASSET(?:_URI)?):([^}]+)\}\}")
    result = pattern.sub(resolve, template)

    OUTPUT.write_text(result, encoding="utf-8")
    print(f"\nOK {OUTPUT}  ({len(result):,} chars)")


if __name__ == "__main__":
    build()
