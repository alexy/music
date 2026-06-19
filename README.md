# Music Learning Manuals

This repository is an experiment in bespoke, AI-aligned learning textbooks:
small, practical books and interactive guides built around one learner's actual
gear, goals, references, taste, and next practice session.

![MPK and GarageBand learning rig](codex/docs/assets/mpk-garageband-learning.svg)

## Deliverables

- [Latest PDF manual](codex/docs/book/dist/kiffness-mpk-mini-manual%20(0.2.1).pdf)
- [Latest EPUB manual](codex/docs/book/dist/kiffness-mpk-mini-manual%20(0.2.1).epub)
- [Latest MOBI manual](codex/docs/book/dist/kiffness-mpk-mini-manual%20(0.2.1).mobi)
- [What Is Love GarageBand animated tutorial](codex/docs/what-is-love-garageband-animated.html)
- [Don't Cry Tonight GarageBand animated tutorial](codex/docs/dont-cry-tonight-garageband-animated.html)
- [What Is Love figure-by-figure settings guide](codex/docs/WhatIsLoveGarageBandFigures.md)
- [Don't Cry Tonight figure-by-figure settings guide](codex/docs/DontCryTonightGarageBandFigures.md)
- [Changelog](codex/CHANGELOG.md)

## What This Is

The current book is an Akai MPK mini remix manual for learning how to build
Kiffness-style and 1980s/synthwave-inspired remix videos on a Mac. It covers
MIDI, DAW setup, source-clip preparation, MPK mapping, drum programming, bass
and chord parts, arrangement, mixing, video sync, export settings, and practical
case studies.

The interactive tutorials are intentionally GarageBand-only. The book itself
also keeps Ableton Live and FL Studio as separate DAW paths, with each DAW
getting its own setup checklist, audio-interface checklist, starter layout, and
workflow notes. That keeps the manual easy to extend without turning every
table into a fragile multi-column comparison.

## Bespoke AI-Aligned Textbooks

This project follows the learning approach described in Alexy Khrabrov's Chief
Scientist post, [Learn Rust from Bespoke Books](https://chiefscientist.org/learn-rust-from-bespoke-books-69e1d853dbca).
The idea is that a book can be coauthored around a learner's real context
instead of delivered as a generic static curriculum.

For this music manual, that means the material is aligned to:

- the actual controller: Akai MPK mini IV;
- the actual beginner DAW path: GarageBand;
- the learner's musical references, including Kiffness-style remix videos,
  MunomaMusic's "What Is Love" live-loop cover, and the Savage / John E.S
  "Don't Cry Tonight" remix;
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

- `codex/docs/book/manual.md` - main manuscript.
- `codex/docs/book/build.sh` - PDF/EPUB/MOBI build script.
- `codex/docs/book/dist/` - versioned release artifacts.
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

## Rights

This repository is for personal learning and study. The manual references
public videos and official product documentation, but it does not include copied
lyrics, transcripts, copyrighted video frames, or source audio in the published
manual artifacts. Use your own recordings, licensed material, public-domain
sources, or material you have permission to remix.
