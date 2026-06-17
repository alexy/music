#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/../.."

mkdir -p docs/book/dist docs/book/build

tmpdir="$(mktemp -d)"
trap 'rm -rf "$tmpdir"' EXIT

version="$(tr -d '[:space:]' < docs/book/VERSION)"
if [[ -z "$version" ]]; then
  echo "could not read docs/book/VERSION" >&2
  exit 1
fi

pubdate="$(date -u +%F)"
title_stem="$(
  awk -F: '
    $1 ~ /^[[:space:]]*title_stem[[:space:]]*$/ {
      value = $2
      sub(/^[[:space:]]*/, "", value)
      sub(/[[:space:]]*$/, "", value)
      gsub(/^["'\''"]|["'\''"]$/, "", value)
      print value
      exit
    }
  ' docs/book/metadata.yaml
)"

if [[ -z "$title_stem" ]]; then
  title_stem="kiffness-mpk-mini-manual"
fi

manual_name="$title_stem ($version)"
stable_pdf="docs/book/dist/$title_stem.pdf"
stable_epub="docs/book/dist/$title_stem.epub"

{
  printf 'manual_name: %s\n' "$manual_name"
  printf 'built_at: %s\n' "$pubdate"
  printf 'pdf_file: %s.pdf\n' "$title_stem"
  printf 'epub_file: %s.epub\n' "$title_stem"
} > docs/book/dist/VERSION.md

sed "s/{{MANUAL_NAME}}/$manual_name/g" docs/book/cover.md > "$tmpdir/cover.md"

pandoc "$tmpdir/cover.md" \
  -o "$tmpdir/cover.pdf" \
  --pdf-engine=typst

pandoc docs/book/manual.md \
  -o "$tmpdir/body.pdf" \
  --pdf-engine=typst \
  --toc \
  --number-sections \
  --metadata-file docs/book/metadata.yaml \
  --metadata date="$pubdate"

pdfunite "$tmpdir/cover.pdf" "$tmpdir/body.pdf" "$stable_pdf"

pandoc "$tmpdir/cover.md" docs/book/manual.md \
  -o "$stable_epub" \
  --toc \
  --number-sections \
  --metadata-file docs/book/metadata.yaml \
  --metadata date="$pubdate" \
  --css docs/book/epub.css \
  --epub-title-page=false

printf 'Built %s and %s\n' "$stable_pdf" "$stable_epub"
