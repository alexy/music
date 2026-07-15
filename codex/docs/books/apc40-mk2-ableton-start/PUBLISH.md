# APC40 MK2 Ableton Book Publishing Runbook

This is the source-owned build for `apc40-mk2-ableton-start`. The manuscript,
metadata, 21 generated SVG plates, interactive tutorial, version, and canonical
artifacts live in this repository. FirstPair owns public catalog and delivery.

## Build

The canonical configuration is the repository-root `book.build.json`. From the
repository root, or from any directory through the wrapper, run:

```sh
codex/docs/books/apc40-mk2-ableton-start/build.sh
```

The wrapper invokes FirstPair's pinned shared builder. It regenerates the SVG
plates, builds and verifies Typst PDF, EPUB3, MOBI, single-file HTML, and split
HTML readers, copies the tracked interactive tutorial into `dist/`, and writes
stable and version-stamped artifact links plus `VERSION.md`.

The version comes from `VERSION`; the build stamp is
`<version>-<8-character-source-commit>`. The native Pandoc, Typst, Calibre,
Poppler, Ghostscript, and related tools are checked against FirstPair's
Homebrew-backed toolchain lock before the build begins.

The reader-facing portrait cover and wide library headboard live under
`assets/`. `book.build.json` registers the portrait PNG as the PDF/EPUB cover
and the 16:9 PNG as `headboardImage`; FirstPair uses those same files for the
library card and detail-page hero. Their source art, exact First Pair Press
publisher mask, prompt record, and deterministic renderer are documented in
`assets/COVER_ART.md`.

Resolve configuration without building:

```sh
codex/docs/books/apc40-mk2-ableton-start/build.sh --print-plan
```

## Outputs

The publish-complete directory is:

```text
codex/docs/books/apc40-mk2-ableton-start/dist/
```

It contains stable PDF, EPUB, MOBI, HTML, chapter HTML, the interactive Learn
tutorial, versioned links, and `VERSION.md`. The build does not upload, deploy,
or copy anything to iCloud.

## Verification

Verification is mandatory and runs as part of the shared build. It checks PDF
geometry and rendered pages, EPUB metadata/content/resources, HTML content and
resources, chapter packaging, version markers, and stable/versioned links.

Useful manual probes after a build:

```sh
pdfinfo 'codex/docs/books/apc40-mk2-ableton-start/dist/apc40-mk2-ableton-start.pdf'
pdftotext 'codex/docs/books/apc40-mk2-ableton-start/dist/apc40-mk2-ableton-start.pdf' - | rg "APC Only|Oh Long Johnson|Don't Cry Tonight|Link, Tempo"
unzip -p 'codex/docs/books/apc40-mk2-ableton-start/dist/apc40-mk2-ableton-start.epub' EPUB/package.opf | rg 'APC40 MK2 Ableton Live 12 Getting Started'
```

For a non-mutating FirstPair integration probe:

```sh
cd "$HOME/src/firstpair"
npm run library:publish -- "$HOME/src/music" \
  --slug apc40-mk2-ableton-start \
  --dry-run --no-build --no-smoke --no-deploy --no-icloud
```

Publishing is a separate outward-facing action governed by FirstPair's
`AGENTS.md`; a successful source build never implies publication.
