#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$repo_root"

# Version stamps follow the unified publishing convention:
# <version>-<short-git-hash>, read from each book's dist/VERSION.md
# (written by the book build scripts). Falls back to the bare VERSION
# file for dists built before hash stamping existed.
read_stamp() {
  local marker="$1"
  local fallback="$2"
  local stamp=""
  if [[ -f "$marker" ]]; then
    stamp="$(awk -F': ' '$1 == "version_stamp" { print $2; exit }' "$marker")"
  fi
  if [[ -z "$stamp" ]]; then
    stamp="$(tr -d '[:space:]' < "$fallback")"
  fi
  printf '%s\n' "$stamp"
}

version="$(read_stamp codex/docs/book/dist/VERSION.md codex/docs/book/VERSION)"
apc_book_dir="codex/docs/books/apc40-mk2-ableton-start"
apc_version="$(read_stamp "$apc_book_dir/dist/VERSION.md" "$apc_book_dir/VERSION")"
tmpdir="$(mktemp -d)"
trap 'rm -rf "$tmpdir"' EXIT

mkdir -p docs/assets docs/downloads docs/tutorials

cp codex/docs/assets/mpk-garageband-learning.svg docs/assets/mpk-garageband-learning.svg
cp "codex/docs/book/dist/kiffness-mpk-mini-manual (${version}).pdf" \
  "docs/downloads/kiffness-mpk-mini-manual-${version}.pdf"
cp "codex/docs/book/dist/kiffness-mpk-mini-manual (${version}).epub" \
  "docs/downloads/kiffness-mpk-mini-manual-${version}.epub"
cp "codex/docs/book/dist/kiffness-mpk-mini-manual (${version}).mobi" \
  "docs/downloads/kiffness-mpk-mini-manual-${version}.mobi"
cp "$apc_book_dir/dist/apc40-mk2-ableton-start (${apc_version}).pdf" \
  "docs/downloads/apc40-mk2-ableton-start-${apc_version}.pdf"
cp "$apc_book_dir/dist/apc40-mk2-ableton-start (${apc_version}).epub" \
  "docs/downloads/apc40-mk2-ableton-start-${apc_version}.epub"
cp "$apc_book_dir/dist/apc40-mk2-ableton-start (${apc_version}).mobi" \
  "docs/downloads/apc40-mk2-ableton-start-${apc_version}.mobi"
cp codex/docs/what-is-love-garageband-animated.html \
  docs/tutorials/what-is-love-garageband-animated.html
cp codex/docs/dont-cry-tonight-garageband-animated.html \
  docs/tutorials/dont-cry-tonight-garageband-animated.html
cp codex/docs/clint-eastwood-mpk-mini-animated.html \
  docs/tutorials/clint-eastwood-mpk-mini-animated.html
cp codex/docs/mpk-mini-mk3-garageband-loop-lab.html \
  docs/tutorials/mpk-mini-mk3-garageband-loop-lab.html
cp codex/docs/mpk-mini-mk3-ableton-loop-lab.html \
  docs/tutorials/mpk-mini-mk3-ableton-loop-lab.html
cp codex/docs/apc40-dont-cry-tonight-ableton-animated.html \
  docs/tutorials/apc40-dont-cry-tonight-ableton-animated.html

python3 - "$version" "$apc_version" > "$tmpdir/pages-readme.md" <<'PY'
from pathlib import Path
import re
import sys

version = sys.argv[1]
apc_version = sys.argv[2]
text = Path("README.md").read_text()

replacements = {
    "codex/docs/assets/mpk-garageband-learning.svg": "assets/mpk-garageband-learning.svg",
    f"codex/docs/book/dist/kiffness-mpk-mini-manual%20({version}).pdf": f"downloads/kiffness-mpk-mini-manual-{version}.pdf",
    f"codex/docs/book/dist/kiffness-mpk-mini-manual%20({version}).epub": f"downloads/kiffness-mpk-mini-manual-{version}.epub",
    f"codex/docs/book/dist/kiffness-mpk-mini-manual%20({version}).mobi": f"downloads/kiffness-mpk-mini-manual-{version}.mobi",
    f"codex/docs/books/apc40-mk2-ableton-start/dist/apc40-mk2-ableton-start%20({apc_version}).pdf": f"downloads/apc40-mk2-ableton-start-{apc_version}.pdf",
    f"codex/docs/books/apc40-mk2-ableton-start/dist/apc40-mk2-ableton-start%20({apc_version}).epub": f"downloads/apc40-mk2-ableton-start-{apc_version}.epub",
    f"codex/docs/books/apc40-mk2-ableton-start/dist/apc40-mk2-ableton-start%20({apc_version}).mobi": f"downloads/apc40-mk2-ableton-start-{apc_version}.mobi",
    "codex/docs/what-is-love-garageband-animated.html": "tutorials/what-is-love-garageband-animated.html",
    "codex/docs/dont-cry-tonight-garageband-animated.html": "tutorials/dont-cry-tonight-garageband-animated.html",
    "codex/docs/clint-eastwood-mpk-mini-animated.html": "tutorials/clint-eastwood-mpk-mini-animated.html",
    "codex/docs/mpk-mini-mk3-garageband-loop-lab.html": "tutorials/mpk-mini-mk3-garageband-loop-lab.html",
    "codex/docs/mpk-mini-mk3-ableton-loop-lab.html": "tutorials/mpk-mini-mk3-ableton-loop-lab.html",
    "codex/docs/apc40-dont-cry-tonight-ableton-animated.html": "tutorials/apc40-dont-cry-tonight-ableton-animated.html",
    "codex/docs/WhatIsLoveGarageBandFigures.md": "https://github.com/alexy/music/blob/master/codex/docs/WhatIsLoveGarageBandFigures.md",
    "codex/docs/DontCryTonightGarageBandFigures.md": "https://github.com/alexy/music/blob/master/codex/docs/DontCryTonightGarageBandFigures.md",
    "codex/CHANGELOG.md": "https://github.com/alexy/music/blob/master/codex/CHANGELOG.md",
}

for old, new in replacements.items():
    text = text.replace(old, new)

text = re.sub(r"## Repository Layout.*?## Build", "## Build", text, flags=re.S)
print(text)
PY

cat > "$tmpdir/pages.css" <<'CSS'
:root {
  --ink: #17202a;
  --muted: #5d6876;
  --paper: #f7f3ea;
  --panel: #ffffff;
  --line: #d8d0c2;
  --teal: #246a73;
}
* { box-sizing: border-box; }
body {
  margin: 0;
  font: 17px/1.55 -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  color: var(--ink);
  background: var(--paper);
}
main {
  max-width: 960px;
  margin: 0 auto;
  padding: 34px 18px 56px;
}
h1 {
  margin: 0 0 10px;
  font-size: clamp(34px, 6vw, 62px);
  line-height: 1;
  letter-spacing: 0;
}
h2 {
  margin-top: 34px;
  padding-top: 8px;
  border-top: 1px solid var(--line);
}
p, li { max-width: 820px; }
a { color: var(--teal); font-weight: 650; }
img {
  display: block;
  width: 100%;
  max-width: 960px;
  margin: 22px 0 26px;
  border-radius: 8px;
  background: #18202a;
}
ul {
  padding-left: 1.2rem;
}
li {
  margin: 0.35rem 0;
}
code {
  padding: 0.08rem 0.28rem;
  border-radius: 4px;
  background: #eee7dc;
}
pre {
  padding: 14px;
  overflow-x: auto;
  border-radius: 8px;
  background: #18202a;
  color: white;
}
body > main > ul:first-of-type {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 12px;
  padding-left: 0;
  list-style: none;
}
body > main > ul:first-of-type li {
  margin: 0;
  padding: 14px 16px;
  min-height: 84px;
  border: 1px solid var(--line);
  border-radius: 8px;
  background: var(--panel);
}
CSS

pandoc "$tmpdir/pages-readme.md" -t html -o "$tmpdir/body.html"

cat > docs/index.html <<TPL
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Music Learning Manuals</title>
  <style>
$(cat "$tmpdir/pages.css")
  </style>
</head>
<body>
  <main>
$(cat "$tmpdir/body.html")
  </main>
</body>
</html>
TPL

touch docs/.nojekyll
