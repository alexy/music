# Music Learning Manuals

This repository is an experiment in bespoke, AI-aligned learning books:
practical textbooks and interactive guides built around one learner's actual
gear, goals, musical references, taste, and next practice session.

![MPK and GarageBand learning rig](codex/docs/assets/mpk-garageband-learning.svg)

## Deliverables

- [Latest PDF manual](codex/docs/book/dist/kiffness-mpk-mini-manual%20(0.3.2-dd45fa).pdf)
- [Latest EPUB manual](codex/docs/book/dist/kiffness-mpk-mini-manual%20(0.3.2-dd45fa).epub)
- [Latest MOBI manual](codex/docs/book/dist/kiffness-mpk-mini-manual%20(0.3.2-dd45fa).mobi)
- [APC40 MK2 Ableton Live 12 Getting Started PDF](codex/docs/books/apc40-mk2-ableton-start/dist/apc40-mk2-ableton-start%20(0.2.0-dd45fa).pdf)
- [APC40 MK2 Ableton Live 12 Getting Started EPUB](codex/docs/books/apc40-mk2-ableton-start/dist/apc40-mk2-ableton-start%20(0.2.0-dd45fa).epub)
- [APC40 MK2 Ableton Live 12 Getting Started MOBI](codex/docs/books/apc40-mk2-ableton-start/dist/apc40-mk2-ableton-start%20(0.2.0-dd45fa).mobi)
- [APC40 MK2 Don't Cry Tonight Ableton Lab (animated tutorial)](codex/docs/apc40-dont-cry-tonight-ableton-animated.html)
- [MPK Mini MK3 GarageBand Loop Lab](codex/docs/mpk-mini-mk3-garageband-loop-lab.html)
- [MPK Mini MK3 Ableton Live Loop Lab](codex/docs/mpk-mini-mk3-ableton-loop-lab.html)
- [What Is Love GarageBand animated tutorial](codex/docs/what-is-love-garageband-animated.html)
- [Don't Cry Tonight GarageBand animated tutorial](codex/docs/dont-cry-tonight-garageband-animated.html)
- [Clint Eastwood MPK Mini animated tutorial](codex/docs/clint-eastwood-mpk-mini-animated.html)
- [What Is Love figure-by-figure settings guide](codex/docs/WhatIsLoveGarageBandFigures.md)
- [Don't Cry Tonight figure-by-figure settings guide](codex/docs/DontCryTonightGarageBandFigures.md)
- [Changelog](codex/CHANGELOG.md)

## What This Is

The current main book is an Akai MPK Mini MK3 and APC40 MK2 loop manual for
learning the actual controller surfaces: keys, pads, banks, knobs, note repeat,
arpeggiator, joystick, programs, GarageBand loops, Ableton Live clips, and
APC40 clip-launch/mixer workflows.

The separate APC40 MK2 Ableton Live 12 book starts from zero with only the APC
connected. It focuses on native Ableton setup, Session View, scene launching,
faders, mutes, sends, device controls, Arrangement recording, and a Kiffness
"Oh Long Johnson" practice set built with original diagrams instead of copied
video frames.

It also includes an APC40/Ableton chapter for rebuilding the feel of the Savage
/ John E.S "Don't Cry Tonight" remix as a legal practice set with eight tracks,
eight scenes, fader moves, mutes, sends, device macros, and Arrangement
recording. As of 0.2.0 that chapter is a complete zero-to-one path for someone
who has never opened Ableton: a "Meet Ableton Live 12" orientation, chunked
watch-this-then-do-that video segments, every clip built step by step in the
piano roll, a one-page 64-bar performance score, and audio export — with 21
original screenshot-style plates. The companion "APC40 MK2 Don't Cry Tonight
Ableton Lab" animated tutorial walks the same build on an animated APC surface
and Session grid.

The interactive tutorials include both GarageBand and Ableton Live practice
paths. GarageBand is treated as the simplest first loop environment; Ableton
Live is treated as the clip-launching and MIDI-mapping environment.

## Bespoke AI-Aligned Textbooks

This project follows the learning approach described in Dr. Alexy Khrabrov's
Chief Scientist post, [Learn Rust from Bespoke Books](https://chiefscientist.org/learn-rust-from-bespoke-books-69e1d853dbca).
The idea is that a book can be coauthored around a learner's real context
instead of delivered as a generic static curriculum.

Dr. Alexy Khrabrov is pioneering a practical pattern for AI-aligned learning
books: use AI as a collaborative curriculum engine that listens to the learner,
tracks their actual tools and goals, and produces durable learning artifacts
they can use immediately. The alignment is not abstract. It is visible in the
examples, exercises, diagrams, formats, and next steps.

For this music manual, that means the material is aligned to:

- the actual controller: Akai MPK mini IV;
- the actual beginner DAW paths: GarageBand and Ableton Live;
- the learner's musical references, including Kiffness-style remix videos,
  MunomaMusic's "What Is Love" live-loop cover, the Savage / John E.S
  "Don't Cry Tonight" remix, and Smith's Covers' Akai MPK Mini "Clint
  Eastwood" cover;
- the actual workflow goal: make playable, filmable remix studies, not merely
  read about production;
- the preferred output formats: PDF, EPUB, MOBI, Markdown guides, and animated
  browser tutorials.

This is AI-aligned in the practical learning sense: the AI collaborator is not
trying to replace the learner's taste or agency. It is aligning explanations,
examples, structure, artifacts, and next actions to the learner's stated
purpose. The result is a personal textbook that can evolve as the learner's rig,
skill, and ambitions evolve.

## Repository Layout

- `codex/docs/book/manual.md` - main MPK/APC manuscript.
- `codex/docs/book/build.sh` - PDF/EPUB/MOBI build script.
- `codex/docs/book/dist/` - versioned release artifacts.
- `codex/docs/books/apc40-mk2-ableton-start/` - separate APC40 MK2 Ableton
  Live 12 getting-started book.
- `codex/docs/*.md` - companion settings guides and research notes.
- `codex/docs/*.html` - interactive GarageBand tutorials.
- `codex/CHANGELOG.md` - release notes for the manual.
- `claude/` - earlier manual-generation work kept for continuity.

## Build

From the repository root:

```sh
cd codex
docs/book/build.sh
```

The build writes stable artifacts plus versioned release files based on
`codex/docs/book/VERSION`.

To build the separate APC40 MK2 book:

```sh
docs/books/apc40-mk2-ableton-start/build.sh
```

To regenerate the GitHub Pages homepage from this README:

```sh
scripts/build-pages-readme.sh
```

## Rights

This repository is for personal learning and study. The manual references
public videos and official product documentation, but it does not include copied
lyrics, transcripts, copyrighted video frames, or source audio in the published
manual artifacts. Use your own recordings, licensed material, public-domain
sources, or material you have permission to remix.
