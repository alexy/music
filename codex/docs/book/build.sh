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
stable_mobi="docs/book/dist/$title_stem.mobi"
versioned_pdf="docs/book/dist/$manual_name.pdf"
versioned_epub="docs/book/dist/$manual_name.epub"
versioned_mobi="docs/book/dist/$manual_name.mobi"

{
  printf 'manual_name: %s\n' "$manual_name"
  printf 'built_at: %s\n' "$pubdate"
  printf 'pdf_file: %s.pdf\n' "$title_stem"
  printf 'epub_file: %s.epub\n' "$title_stem"
  printf 'mobi_file: %s.mobi\n' "$title_stem"
  printf 'versioned_pdf: %s.pdf\n' "$manual_name"
  printf 'versioned_epub: %s.epub\n' "$manual_name"
  printf 'versioned_mobi: %s.mobi\n' "$manual_name"
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

ebook_convert="$(
  if command -v ebook-convert >/dev/null 2>&1; then
    command -v ebook-convert
  elif [[ -x /Applications/calibre.app/Contents/MacOS/ebook-convert ]]; then
    printf '%s\n' /Applications/calibre.app/Contents/MacOS/ebook-convert
  fi
)"

if [[ -z "$ebook_convert" ]]; then
  echo "could not find ebook-convert for MOBI generation" >&2
  exit 1
fi

"$ebook_convert" "$stable_epub" "$stable_mobi"

copy_artifact() {
  local src="$1"
  local dst="$2"

  if [[ "$src" -ef "$dst" ]]; then
    return 0
  fi

  cp "$src" "$dst"
}

copy_artifact "$stable_pdf" "$versioned_pdf"
copy_artifact "$stable_epub" "$versioned_epub"
copy_artifact "$stable_mobi" "$versioned_mobi"

printf 'Built %s, %s, and %s\n' "$versioned_pdf" "$versioned_epub" "$versioned_mobi"
