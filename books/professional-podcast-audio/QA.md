# Interactive tutorial QA

Verified 2026-09-29 against the generated book-local `tutorial.html` in an isolated Chromium context. The browser did not interact with the user's open applications or physical audio hardware.

## Reproduce

From `/Users/alexy/src/music`, run:

```sh
env \
  PODCAST_PLAYWRIGHT_MODULE=/Users/alexy/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright \
  PODCAST_BROWSER_PATH=/Users/alexy/Library/Caches/ms-playwright/chromium_headless_shell-1228/chrome-headless-shell-mac-arm64/chrome-headless-shell \
  PODCAST_QA_DIR=/private/tmp \
  /Users/alexy/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/bin/node \
  books/professional-podcast-audio/scripts/test-tutorial.cjs
```

The module/browser paths are this machine's installed dependencies; use the corresponding local paths elsewhere. The test opens `../tutorial.html` relative to its own `scripts/` directory. On macOS, launching isolated Chromium may require permission outside the filesystem sandbox.

## Result

Exit code 0:

```json
{
  "passed": true,
  "combinations": 42,
  "jsErrors": [],
  "csvBytes": 3906
}
```

The 42 cases cover five B67-269 mode selections (including as found), two Twin87 modes, three recipes and two DAWs. Every case has ten steps and complete recall settings. Tests also verify the different phantom-power instructions, checkbox persistence after reload, separate progress for each microphone, reset preserving saved observations, observation persistence, the loudness-match calculation, and CSV export with real CRLF separators, UTF-8 BOM, quoted commas/newlines and protection against a formula-like take name.

At a 390 x 844 viewport, all ten steps pass the horizontal-overflow check. Desktop and mobile screenshots were visually reviewed. Full-step printing produced 13 A4 pages: three recall pages followed by ten step pages. Rendered pages were inspected; print spacing was adjusted to keep the preamp and compressor checkpoints with their respective steps. No clipped settings, overlapping text or orphan-checkpoint pages remained.

The test writes these temporary QA artifacts:

- `/private/tmp/podcast-desktop.png`
- `/private/tmp/podcast-mobile.png`
- `/private/tmp/podcast-tutorial-print.pdf`

The printable PDF is a QA sample, not a separate book edition. Native DAW operation, measured microphone sound, physical gain calibration and recordings were not tested; their instructions were researched from the cited manufacturer documents. The tutorial is a recall/checklist application and does not connect to or set the hardware.

## Book and package verification

The final layout contains 53 pages, 15 chapters, 13,269 words and 13 numbered figures (two supplied photos and eleven original plates), plus the illustrated cover. Every PDF page was rasterized and visually reviewed through full-page renders/contact sheets; the six chain recipes each begin on a separate page. Captions, tables, page numbering and the source register were checked.

The shared FirstPair build passed its pinned toolchain, PDF layout, library artifact and VERSION.md contracts. The source-owned `validate-package.py` passed EPUB XML/resource integrity (37 archive files, cover-image manifest entry), all manuscript images, tutorial/source equality, 58 comparison-log fields and 36 control sweeps. A non-writing publisher plan resolved the nested `professional-podcast-audio` title on the Music shelf, full edition, with PDF/EPUB/HTML/chapters/tutorial/cover/headboard. No public upload, deployment or iCloud copy was performed.

The Obsidian source adapter, 15 chapter records and validation code are prepared. Generation and archive validation remain pending until the user closes Obsidian, as required by FirstPair's process gate. No generated vault is claimed as tested yet.
