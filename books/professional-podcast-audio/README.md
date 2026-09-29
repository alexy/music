# Professional Podcast Audio

A 15-chapter color field manual for the owner's BeesNeez B67-269, United Studio Technologies UT Twin87, photographed PRE-73 **Premier**, COMP-54 and MOTU M4, with GarageBand for Mac and Ableton Live 12 Lite.

## Read and practice

- [PDF desk edition](dist/professional-podcast-audio.pdf)
- [EPUB](dist/professional-podcast-audio.epub)
- [Interactive tutorial](tutorial.html) — portable, offline, mic → known mode → recipe → DAW, ten steps, complete control cards, local progress, comparison log, CSV export and print.
- [Single-page HTML reader](dist/professional-podcast-audio.html)
- [Chapter reader](dist/professional-podcast-audio-chapters/index.html)
- [Comparison log CSV](comparison-log.csv) and [36 control sweeps](control-sweeps.csv)
- [Obsidian guide](vault-guide.md); generated vault and archive are in `dist-obsidian/` after the closed-app gate and clean-source build.

All recipes are **unmeasured starting points**. The actual gain/threshold/makeup values must be calibrated to the speaker. The BeesNeez default is its internal state **as found**. Optional internal profiles require its manufacturer's verified handling procedure. Twin87 phantom is provided by the PRE-73; BeesNeez phantom stays off. The main route uses rear M4 mono Input 3 with centered software monitoring.

## Source ownership

`chapters/` and `presets.json` are source content. `scripts/make-presets.py` owns the canonical recipe data; `scripts/assemble-book.py` assembles the manuscript and worksheets; `scripts/generate-assets.py` draws original plates and places the user's unchanged photos; `scripts/build-tutorial.py` creates the portable tutorial. The generated `manuscript.md`, photos, plates and tutorial are retained for reproducible publication.

Manufacturer manuals are linked in the book, not included in distributable artifacts. The two source HEIC files remain in the repository's `gear/` folder. Exact software point releases may differ; the manuscript records its reference date and version limitations.

## Build

First read [FIRSTPAIR.md](FIRSTPAIR.md). The shared build implementation is in `~/src/firstpair`; no public upload occurs during this local build.

From this directory, using a Python with Pillow installed (on this Mac use the bundled runtime below):

```sh
podcast_python="$HOME/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3"
"$podcast_python" scripts/make-presets.py
"$podcast_python" scripts/generate-assets.py
"$podcast_python" scripts/assemble-book.py
"$podcast_python" scripts/build-tutorial.py
./build.sh prepare-vault
./build.sh book
"$podcast_python" scripts/validate-package.py
```

The desktop bundled Python is suitable for the image scripts. PDF QA additionally needs `pypdf` and `pypdfium2`; `scripts/qa-pdf.py` renders every page and contact sheets under ignored `build/qa/` for visual review. FirstPair's unified builder runs the pinned toolchain, PDF layout and artifact/version checks.

For the **final release**, commit completed source, then rebuild the book so its `VERSION.md` names that source revision. Obsidian must be fully closed before any vault generation/packaging. A clean committed source is also required by the shared vault builder:

```sh
./build.sh vault
./build.sh check-vault
```

Do not modify a generated vault while Obsidian is running. Copy the generated vault for personal session notes; rebuilding source editions must not overwrite the reader's observations. The optional FirstPair plugin ships disabled. Local vault build does not require a push; public publishing requires clean/pushed source and FirstPair repos plus the publishing authorization in FIRSTPAIR.md.

The original APC40 book's top-level config and catalog slug are preserved. This title has its own nested config/contract, title slug `professional-podcast-audio`, shelf `music`.
