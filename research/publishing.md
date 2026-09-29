# Professional Podcat Audio: publishing integration

Research and implementation inspection: 29 September 2026. The actual source
Git root is `/Users/alexy/src/music`. No `~/src/First Press` directory exists;
the established source contract points to `/Users/alexy/src/firstpair`.

## Preserve the two title identities

The root `FIRSTPAIR.md` and `book.build.json` identify the existing
`apc40-mk2-ableton-start` title. They must not be replaced with the podcast
book's identity. The added title package is
`books/professional-podcat-audio/`, with its own contract/configuration and
`slug: professional-podcat-audio`, `shelf: music`, `default_edition: full`.

This nested title root is supported by the actual shared implementation:

- `build-library-book.mjs` resolves `--repo-root` directly and resolves the
  default `book.build.json` and all configured paths relative to that input.
  It also supports `--config <file>`, but the publisher does not expose the
  same alternate-config switch. Using one nested title root for both avoids
  incompatible path bases.
- `publish-book-to-library.mjs:firstPairContract()` reads the contract in the
  supplied input directory. `configuredDistCandidates()` reads that input's
  `book.build.json`. Cover/headboard and metadata discovery also use that
  directory. Its source-URL and publication-preflight functions separately
  discover the real Git root, so no nested Git repository is necessary.
- The tutorial is a standalone HTML artifact, copied into the dist directory
  by the shared builder. `VERSION.md` records `tutorial_file`; the publisher
  exposes it at `/learn/professional-podcat-audio/` after a separately
  authorized publication.

## Local book build

```sh
cd /Users/alexy/src/music/books/professional-podcat-audio
./build.sh book
```

This delegates to the shared builder. The PDF uses Typst, a 7 × 10 inch cover
and body, an 11 point body, colored headings, and `assets/cover.png`. The
headboard is `assets/headboard.png`; EPUB uses the same canonical cover and
suppresses a duplicate rendered cover. MOBI is disabled. PDF, EPUB, standalone
HTML, chapter HTML, tutorial, and `VERSION.md` go into ignored `dist/`.

The builder owns the toolchain, metadata, versioned artifact links, PDF raster
and geometry checks, and EPUB/HTML package validation. On 29 September,
`publishing/scripts/verify-toolchain.mjs --quiet` passed against the shared
lock. Pandoc, Typst, Poppler, Node, Python, and uv are available locally.

The builder's `--print-plan` is **not** fully read-only when hooks exist:
it verifies the toolchain and executes `hooks.prebuild` before printing the
plan. The publisher `--dry-run` is the safe non-writing delivery plan.

## Vault contract and adapter

The shared configuration requires `schemaVersion`, `slug`, `title`, `profile`,
`sourceCommit`, nonempty `reader`, and `products`. `repoRoot` is resolved
relative to the config's own directory. Reader/evidence source paths must be
relative, regular files within that root. Output must also remain within it.

The `history` profile is the closest currently supported profile for a manual
with visual and documentary evidence; the profile name does not describe the
subject matter of the book. A title-owned `nativeDriver` preserves chapter
navigation, illustration links, worksheets, and the publisher-compatible
`professional-podcat-audio/_data/units.jsonl` ledger. FirstPair composes the
complete guide and deterministic first-open workspace and seals the finished
file inventory. The title adapter copies the canonical FirstPair Reader
plugin byte-for-byte and leaves it disabled.

Why use the native adapter: the basic shared projection copies each Reader
source verbatim and does not rewrite manuscript-relative image paths; it also
produces a `VAULT-MANIFEST.json` layout that the current publisher's
`isProperVault()` does not recognize by itself. The native output includes
both the expected chapter ledger and `FIRSTPAIR-VAULT-MANIFEST.json`, allowing
the shared validator to verify the sealed package during publisher dry-runs.

```sh
cd /Users/alexy/src/music/books/professional-podcat-audio
./build.sh prepare-vault
./build.sh plan-vault
# Commit the complete source tree when ready; fully quit Obsidian.
./build.sh vault
./build.sh check-vault
```

`prepare-vault` touches only source configuration and ignored build inputs,
not a vault. It projects `#` chapters from the manuscript into
`build/reader-source/` and records their canonical order in `vault.build.json`.
The native builder checks those inputs against the canonical manuscript,
rewrites local asset links, and emits chapter line ranges, hashes, indices,
static navigation, cover, source/visual notes, and a reusable session log.
It includes only referenced illustration assets and the standalone tutorial;
downloaded manufacturer manuals are not bundled.

## Exact gates

FirstPair's `AGENTS.md` requires a read-only process check before touching any
vault. The sandboxed `pgrep -x Obsidian` could not inspect processes. An
escalated read-only check succeeded and found Obsidian running (PID 73992) at
the initial check; the main task requested that the user quit it. Repeat the
check immediately before generation. Do not infer that elapsed time means it
closed. The shared builder itself repeats this process gate.

The local shared vault builder calls `require_clean_worktree()`, which runs
`git status --porcelain` against the entire source worktree. It requires clean
and committed sources, including user-supplied `gear/` and all book inputs,
but **does not require a remote push**. `sourceCommit: HEAD` resolves to the
real music repository commit. Generated build/dist/vault output is ignored so
it does not dirty that committed source state. The builder refuses to replace
an existing output directory. Preserve or rename an earlier release before
building a new candidate; do not delete a reader's personal edits.

Live publication has a stronger gate: both the music and FirstPair worktrees
must be clean and exactly at their configured remote upstreams. This is
enforced by `git_publish_preflight.py`; a local ahead commit is insufficient.
The non-writing publisher dry-run is exempt and can inspect a local build.

## Reviewable delivery plan

From `/Users/alexy/src/firstpair`:

```sh
npm run library:publish -- /Users/alexy/src/music/books/professional-podcat-audio \
  --dry-run --no-build --no-smoke --no-deploy --no-icloud
```

After a successful vault build add:

```sh
--vault-dir '/Users/alexy/src/music/books/professional-podcat-audio/dist-obsidian/Professional Podcat Audio' \
--vault-guide '/Users/alexy/src/music/books/professional-podcat-audio/dist-obsidian/Professional Podcat Audio/Guide.md'
```

The present request authorizes building the book and tutorial using the
FirstPair workflow; it does not explicitly authorize making them public.
Finish the local artifacts and dry-run before any publication request. The
root source contract says: “Only run the live command … when the user has
explicitly asked to publish.” No uploads, public catalog changes, iCloud
copies, deployment, or FirstPair mutations were made for this integration.

## Authoritative local references

- `/Users/alexy/src/music/FIRSTPAIR.md`
- `/Users/alexy/src/firstpair/AGENTS.md`
- `/Users/alexy/src/firstpair/publishing/PUBLISH.md`
- `/Users/alexy/src/firstpair/publishing/book.build.schema.json`
- `/Users/alexy/src/firstpair/publishing/scripts/build-library-book.mjs`
- `/Users/alexy/src/firstpair/scripts/publish-book-to-library.mjs`
- `/Users/alexy/src/firstpair/publishing/VAULT-CONSTRUCTION.md`
- `/Users/alexy/src/firstpair/publishing/vault/schema/vault.build.schema.json`
- `/Users/alexy/src/firstpair/publishing/vault/firstpair_vault/{builder,native,revisions,verify}.py`
