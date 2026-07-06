# APC40 MK2 Ableton Book Publishing Runbook

This book is separate from the MPK/APC combination manual. It lives under
`docs/books/apc40-mk2-ableton-start/` and is focused on APC40 MK2 only.

## Build

From `kiffness/codex`:

```sh
docs/books/apc40-mk2-ableton-start/build.sh
```

The build script:

1. Regenerates the original SVG figure plates in `assets/`.
2. Reads the version from `VERSION` and stamps it with the short git hash of
   HEAD (`<version>-<short-git-hash>`, e.g. `0.2.0-dd45fa`), following the
   unified publishing workflow convention. Override with `BOOK_VERSION_STAMP`.
3. Reads `title_stem` from `metadata.yaml`.
4. Writes `dist/VERSION.md` including the `version_stamp` field.
5. Builds PDF, EPUB, and MOBI stable artifacts.
6. Copies stable artifacts to versioned names such as
   `apc40-mk2-ableton-start (0.2.0-dd45fa).pdf`.

## Validation

After building, verify:

```sh
pdfinfo docs/books/apc40-mk2-ableton-start/dist/apc40-mk2-ableton-start.pdf
pdftotext docs/books/apc40-mk2-ableton-start/dist/apc40-mk2-ableton-start.pdf - | rg "APC Only|Oh Long Johnson|Don't Cry Tonight|Link, Tempo"
pdftoppm -png -f 1 -l 12 docs/books/apc40-mk2-ableton-start/dist/apc40-mk2-ableton-start.pdf docs/books/apc40-mk2-ableton-start/build/page
```

The visual plates are original diagrams and recreated setup panels. They are
not copied YouTube frames, Ableton screenshots, or Akai product art.
