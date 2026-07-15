# Ableton cover and headboard

The portrait cover and wide First Pair headboard are derived from the performance
screenshot supplied for the July 2026 edition. The generated source art is kept
under `cover-source/`; the final reader-facing PNGs are rendered by
`render-cover-assets.py` so title, author, and imprint typography remain exact.

The exact First Pair publisher engraving is copied from
`~/src/firstpair/logo/firstpair-publisher-mask.png`. In the grayscale mask,
white is logo ink and black is transparent paper. The renderer tints the mask
warm ivory, scales it to 28 percent of the cover width, and superimposes it at
the bottom center without a backplate or shadow.

Run the renderer with a Python environment that provides Pillow:

```sh
/Users/alexy/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 \
  codex/docs/books/apc40-mk2-ableton-start/assets/render-cover-assets.py
```

Final assets:

- `apc40-mk2-ableton-start-cover.png` — 1800 x 2880 (5:8), used by PDF,
  EPUB, the First Pair library card, and the stable cover route.
- `apc40-mk2-ableton-start-headboard.png` — 2400 x 1350 (16:9), used by
  the First Pair book-detail hero. The left side stays dark for site text.

## Image-generation prompts

The cover source asked for a 5:8 cinematic editorial transformation preserving
the three performers and instruments, with the morin khuur player as the
vertical anchor, the two controller players at lower left and right, calm navy
space above for typography, no UI chrome, no added text, and no watermark.

The headboard source asked for a unified 16:9 scene with the performers across
the center-right two thirds, a calm navy-to-teal left third for site copy,
realistic people and instruments, subtle independent-press grain, no UI chrome,
no added text, and no watermark.
