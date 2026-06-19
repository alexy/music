# MPK Remix Manual Publishing Runbook

This folder mirrors the Pandoc/Typst publishing shape used by
`/Users/alexy/src/typesec/docs/book`, adapted for this standalone music manual.

## Source Layout

- Manuscript: `docs/book/manual.md`
- Cover source: `docs/book/cover.md`
- Metadata: `docs/book/metadata.yaml`
- Build script: `docs/book/build.sh`
- EPUB stylesheet: `docs/book/epub.css`
- Changelog: `CHANGELOG.md`
- Final artifacts: `docs/book/dist/`

## Build

From the workspace root:

```sh
docs/book/build.sh
```

The build script:

1. Reads the manual version from `docs/book/VERSION`.
2. Reads `title_stem` from `docs/book/metadata.yaml`.
3. Computes a versioned manual name such as `kiffness-mpk-mini-manual (0.1.0)`.
4. Writes `docs/book/dist/VERSION.md`.
5. Renders `docs/book/cover.md` through Pandoc and Typst.
6. Renders the manuscript body through Pandoc and Typst with a table of contents
   and numbered sections.
7. Merges cover and body into `docs/book/dist/kiffness-mpk-mini-manual.pdf`.
8. Builds `docs/book/dist/kiffness-mpk-mini-manual.epub`.
9. Converts the EPUB to `docs/book/dist/kiffness-mpk-mini-manual.mobi`.
10. Copies stable artifacts to versioned release files such as:
   - `docs/book/dist/kiffness-mpk-mini-manual (0.1.0).pdf`
   - `docs/book/dist/kiffness-mpk-mini-manual (0.1.0).epub`
   - `docs/book/dist/kiffness-mpk-mini-manual (0.1.0).mobi`

## Version Bumps

When bumping `docs/book/VERSION`, update `CHANGELOG.md` in the same change.
Keep entries retroactive when needed so the versioned artifacts in
`docs/book/dist/` have matching release notes.

Use this order:

1. Update `CHANGELOG.md` with the new version, date, changes, and built
   artifacts.
2. Update `docs/book/VERSION`.
3. Run `docs/book/build.sh`.
4. Verify `docs/book/dist/VERSION.md` names the same version.
5. Verify the versioned PDF, EPUB, and MOBI exist.

## Validation

After building, inspect the generated PDF:

```sh
pdfinfo docs/book/dist/kiffness-mpk-mini-manual.pdf
pdftotext -f 1 -l 1 docs/book/dist/kiffness-mpk-mini-manual.pdf -
pdftotext -f 2 -l 2 docs/book/dist/kiffness-mpk-mini-manual.pdf -
pdftoppm -png -f 1 -l 6 docs/book/dist/kiffness-mpk-mini-manual.pdf docs/book/build/page
ls -lh docs/book/dist/kiffness-mpk-mini-manual\ \(0.1.0\).{pdf,epub,mobi}
```

Expected:

- Page 1 is the unnumbered cover.
- Page 2 contains the table of contents/body start.
- Rendered PNG pages are legible, with no obvious overlap or clipping.
- Versioned PDF, EPUB, and MOBI files exist in `docs/book/dist/` and are
  intended to be checked into Git.
- Stable nonversioned PDF, EPUB, and MOBI files are local build products and
  are ignored by Git.
- `CHANGELOG.md` has an entry for the version in `docs/book/VERSION`.

## Notes

This manual references public YouTube pages and official Akai setup/support
material. It does not copy video frames, lyrics, transcripts, audio, or other
copyrighted media from the referenced works.
