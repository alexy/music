# FirstPair Library Contract

slug: professional-podcast-audio
shelf: music
default_edition: full

## Ownership

This is a separate title inside the Git repository at `/Users/alexy/src/music`.
Its title root is `books/professional-podcast-audio`; this directory is not a
separate Git repository. The repository-root contract continues to identify
`apc40-mk2-ableton-start`. Never publish this book by passing the music
repository root or by changing that existing title's slug.

The title root owns the manuscript, illustrations, configuration, metadata,
version, tutorial, and source-specific vault adapter. The authoritative
implementation and operational rules remain in `~/src/firstpair/AGENTS.md`
and `~/src/firstpair/publishing/PUBLISH.md`.

## Build

From this directory, run `./build.sh book`. The wrapper delegates to the unified
FirstPair builder with this title root as `--repo-root`. All paths in
`book.build.json` are relative to this directory. PDF, EPUB, single-file HTML,
chapter HTML, and the standalone interactive tutorial appear in `dist/`.
The book uses a 7 by 10 inch color layout and has no MOBI edition.

Run `./build.sh prepare-vault` after editing the manuscript. It projects the
chapter records into ignored build inputs and updates the reader order in
`vault.build.json`. Commit the finished sources and this configuration before
running `./build.sh vault`. The shared vault builder requires the complete
music Git worktree to be clean, checks that Obsidian is fully closed, and
refuses to overwrite an existing output. It uses the shared Reader plugin and
composed guide, with a source-owned adapter for chapter links and image assets.
The generated vault is `dist-obsidian/Professional Podcast Audio/`.

`build/`, `dist/`, and `dist-obsidian/` are local derived artifacts. A future
remote publication that consumes committed build artifacts must explicitly
include the finished package in its clean source handoff.

## Handoff

Building is not publication. Only a non-writing publisher plan is authorized
as an automatic handoff. From `~/src/firstpair`, pass this title root:

```sh
npm run library:publish -- /Users/alexy/src/music/books/professional-podcast-audio \
  --dry-run --no-build --no-smoke --no-deploy --no-icloud
```

When the vault has been built, add its absolute directory with `--vault-dir`
and its root `Guide.md` with `--vault-guide`. Confirm the plan resolves this
title's slug, music shelf, full edition, PDF, EPUB, HTML, chapters, tutorial,
cover, and headboard. The tutorial's eventual route is
`/learn/professional-podcast-audio/`.

Follow the centralized publication procedure only after explicit public
release authorization. Do not upload, copy to iCloud, alter the public catalog,
or deploy as part of a local build. Do not duplicate the central procedure here.
