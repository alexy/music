#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/../../.."

book_dir="docs/books/apc40-mk2-ableton-start"
mkdir -p "$book_dir/dist" "$book_dir/build"

node "$book_dir/assets/generate-assets.mjs"

tmpdir="$(mktemp -d)"
trap 'rm -rf "$tmpdir"' EXIT

version="$(tr -d '[:space:]' < "$book_dir/VERSION")"
if [[ -z "$version" ]]; then
  echo "could not read $book_dir/VERSION" >&2
  exit 1
fi

githash="$(git rev-parse --short=6 HEAD 2>/dev/null || echo nogit)"
version_stamp="${BOOK_VERSION_STAMP:-$version-$githash}"
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
  ' "$book_dir/metadata.yaml"
)"

if [[ -z "$title_stem" ]]; then
  title_stem="apc40-mk2-ableton-start"
fi

manual_name="$title_stem ($version_stamp)"
stable_pdf="$book_dir/dist/$title_stem.pdf"
stable_epub="$book_dir/dist/$title_stem.epub"
stable_mobi="$book_dir/dist/$title_stem.mobi"
versioned_pdf="$book_dir/dist/$manual_name.pdf"
versioned_epub="$book_dir/dist/$manual_name.epub"
versioned_mobi="$book_dir/dist/$manual_name.mobi"

{
  printf 'manual_name: %s\n' "$manual_name"
  printf 'version_stamp: %s\n' "$version_stamp"
  printf 'built_at: %s\n' "$pubdate"
  printf 'pdf_file: %s.pdf\n' "$title_stem"
  printf 'epub_file: %s.epub\n' "$title_stem"
  printf 'mobi_file: %s.mobi\n' "$title_stem"
  printf 'versioned_pdf: %s.pdf\n' "$manual_name"
  printf 'versioned_epub: %s.epub\n' "$manual_name"
  printf 'versioned_mobi: %s.mobi\n' "$manual_name"
} > "$book_dir/dist/VERSION.md"

sed "s/{{MANUAL_NAME}}/$manual_name/g" "$book_dir/cover.md" > "$tmpdir/cover.md"

resource_path="$book_dir:$book_dir/assets"

pandoc "$tmpdir/cover.md" \
  -o "$tmpdir/cover.pdf" \
  --pdf-engine=typst \
  --resource-path="$resource_path"

pandoc "$book_dir/manual.md" \
  -o "$tmpdir/body.pdf" \
  --pdf-engine=typst \
  --toc \
  --number-sections \
  --metadata-file "$book_dir/metadata.yaml" \
  --metadata date="$pubdate" \
  --resource-path="$resource_path"

pdfunite "$tmpdir/cover.pdf" "$tmpdir/body.pdf" "$stable_pdf"

pandoc "$tmpdir/cover.md" "$book_dir/manual.md" \
  -o "$stable_epub" \
  --toc \
  --number-sections \
  --metadata-file "$book_dir/metadata.yaml" \
  --metadata date="$pubdate" \
  --css "$book_dir/epub.css" \
  --epub-title-page=false \
  --resource-path="$resource_path"

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
