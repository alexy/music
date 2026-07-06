# Changelog

All notable changes to the music learning manuals are recorded here.

## [apc40-mk2-ableton-start 0.2.0] - 2026-07-06

### Added

- Added a "Meet Ableton Live 12" chapter for complete newcomers: DAW basics,
  Session vs Arrangement View, the six zones of the Live window, and a
  glossary of the words the book uses constantly.
- Added a "How To Use This Book" section with chunked sittings, checkpoints,
  and a practice photo-journal habit.
- Added per-chapter "Watch first" video-segment boxes and a segment-to-chapter
  map, so source videos are watched in chunks right before the matching
  hands-on work.
- Added a complete "Build Every Clip, Step By Step" walkthrough to the Don't
  Cry Tonight chapter: tempo/metronome/count-in, loading a 909-style kit,
  drawing kick/clap/hat patterns, the octave bass, chords and pad voicings,
  the lead hook, the FX column, and a copy-edit table that fills all eight
  scenes.
- Added a "Listen Like A Remixer" worksheet section for studying the John E.S
  mix by ear with personal timestamps.
- Added "The 64-Bar Performance Score" one-page performance plate and an
  "Export Your Take" section covering Export Audio/Video settings.
- Added ten original visual plates (12-21): Live 12 first look, browser
  loading, MIDI clip creation, drum step patterns, bass/chord piano roll,
  tempo/warp settings, APC scene-window navigation, the 64-bar performance
  score, the video segment map, and audio export.
- Added an animated APC40 Don't Cry Tonight Ableton browser tutorial for the
  GitHub Pages site, mirroring the book's build and performance path.

### Fixed

- Corrected the scene 6-8 navigation instructions: the Session ring moves one
  scene per Down-arrow press, so reaching scenes 6-8 takes three presses, not
  one.

### Changed

- Versioned artifacts now carry the unified publishing version stamp
  `<version>-<short-git-hash>`, and `dist/VERSION.md` records `version_stamp`,
  matching the querygraph publishing workflow convention.

### Built

- Rebuilt stable PDF, EPUB, and MOBI outputs.
- Added versioned `0.2.0` hash-stamped PDF, EPUB, and MOBI outputs.

## [apc40-mk2-ableton-start 0.1.1] - 2026-07-06

### Added

- Added an APC40 MK2 and Ableton Live chapter for rebuilding the feel of Savage
  & John E.S, "Don t cry tonight (The official remix)" as a legal practice set.
- Added an eight-track/eight-scene Ableton Session View map for the remix study,
  covering kick, clap, hats, bass, chords, lead/vocal, pad, and FX tracks.
- Added APC performance passes for scene launching, faders, mutes, sends,
  device macros, and Arrangement recording.
- Added an original visual plate for the Don't Cry Tonight APC40 remix map.

### Built

- Rebuilt stable PDF, EPUB, and MOBI outputs.
- Added versioned `0.1.1` PDF, EPUB, and MOBI outputs.

## [apc40-mk2-ableton-start 0.1.0] - 2026-07-06

### Added

- Added a separate APC40 MK2 Ableton Live 12 getting-started book under
  `docs/books/apc40-mk2-ableton-start/`.
- Added source-video research for APC40 MK2 zero-to-one setup, including the
  29-minute Meta Mind Music walkthrough, Akai's official APC40 mkII operation
  video, APC workflow videos, and Ableton 12 Session View references.
- Added original SVG visual plates for Ableton MIDI settings, APC surface
  zones, Session View setup, clip launch states, mixer/fader moves, device/send
  controls, Arrangement recording, troubleshooting, and the Kiffness practice
  set.
- Picked `Oh Long Johnson x The Kiffness` as the APC-only practice track because
  its layer inventory exercises scenes, clips, faders, mutes, sends, device
  controls, and transitions.

### Built

- Built stable PDF, EPUB, and MOBI outputs.
- Added versioned `0.1.0` PDF, EPUB, and MOBI outputs.

## [0.3.2] - 2026-07-05

### Changed

- Expanded the guide from MPK-only to MPK mini MK3 plus APC40 MK2 workflows.
- Added three controller-combination sections: APC only, MPK only, and both
  together.
- Added APC40 MK2 identification, Ableton setup notes, clip-grid workflow,
  fader/device-control roles, updated practice plan, and three final-project
  variants.

### Built

- Rebuilt stable PDF, EPUB, and MOBI outputs.
- Added versioned `0.3.2` PDF, EPUB, and MOBI outputs.

## [0.2.1] - 2026-06-19

### Changed

- Reworked the multi-DAW material so each DAW is a separate subsection instead
  of another column in a wide comparison table.
- Added the scalable DAW model for GarageBand, Ableton Live, and FL Studio:
  setup checklist, audio-interface checklist, starter layout, and workflow
  notes per DAW.
- Reworked the 16-bar workflow into separate GarageBand, Ableton Live, and FL
  Studio subsections.
- Clarified that the interactive tutorials are GarageBand-only.

### Built

- Rebuilt stable PDF, EPUB, and MOBI outputs.
- Added versioned `0.2.1` PDF, EPUB, and MOBI outputs.

## [0.2.0] - 2026-06-19

### Added

- Added a Kiffness lessons chapter built from visible MPK-style layer captions
  and effect/layer studies.
- Added `docs/KiffnessEffects.md` as the source inventory for Kiffness videos
  with on-screen layer or effect captions.
- Added a GarageBand/MPK mini IV case study for MunomaMusic's "Haddaway - What
  Is Love (Live Loop Cover) | Minilab 3".
- Added a figure-by-figure GarageBand settings guide for the What Is Love live
  loop study.
- Added an animated GarageBand-only HTML tutorial for the What Is Love live loop
  study.
- Added a GarageBand/MPK mini IV case study for Savage & John.E.S, "Don t cry
  tonight (The official remix)".
- Added a figure-by-figure GarageBand settings guide for the Don't Cry Tonight
  remix study.
- Added an animated GarageBand-only HTML tutorial for the Don't Cry Tonight
  remix study.
- Added MPK-centric reference material for the Don't Cry Tonight study,
  including MPK/GarageBand and 1980s/synthwave controller-cover examples.
- Added local reference captures under `references/` for review and analysis.

### Changed

- Expanded the manual from a beginner MPK remix guide into a larger practice
  manual with case studies, production workflows, video planning, and hardware
  setup guidance.
- Updated title/metadata/cover language around the expanded Ableton-oriented
  manual frame while preserving GarageBand-specific interactive tutorials.
- Updated the build script to avoid copying an artifact onto itself when stable
  and versioned outputs resolve to the same file.

### Built

- Rebuilt stable PDF, EPUB, and MOBI outputs.
- Added versioned `0.2.0` PDF, EPUB, and MOBI outputs.

## [0.1.0] - 2026-06-18

### Added

- Added the initial Codex MPK remix manual source tree.
- Added the publishing runbook, cover source, metadata, EPUB stylesheet, and
  build script.
- Added the first manuscript covering MPK basics, MIDI/audio concepts, Mac
  setup, source preparation, DAW basics, remix workflow, mixing, video sync,
  export settings, practice projects, troubleshooting, and source references.

### Built

- Added versioned `0.1.0` PDF, EPUB, and MOBI outputs.
