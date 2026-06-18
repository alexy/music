manual_name: Akai MPK Mini Mixing Manual (0.2.1)
version: 0.2.1
built_at: 2026-06-18
source_files: build_manual.py, diagrams.py, build_epub.py
pdf_file: Akai_MPK_Mini_Mixing_Manual.pdf
epub_file: Akai_MPK_Mini_Mixing_Manual.epub
versioned_epub: Akai_MPK_Mini_Mixing_Manual (0.2.1).epub
pages: 31
chapters: 19
figures: 9
changelog:
  - 0.1.0: Initial short manual covering MPK Mini basics and mixing.
  - 0.2.0: Expanded to chapter-per-topic format with custom diagrams; added
      Chapter 9 covering MOTU M4 + Pre-73 + UT87 + Shure 55 signal chain,
      with GarageBand and FL Studio setup instructions.
  - 0.2.1: EPUB is now built natively (build_epub.py) from the same
      content events as the PDF instead of a PDF->EPUB conversion, so all
      9 diagrams appear as real embedded images. Fixed a diagram bug where
      multi-line labels rendered literal newline characters as
      missing-glyph boxes, and widened/repositioned several diagrams
      (MPK Mini overview, MIDI signal flow, 16-pad layout, MOTU M4
      routing) that were clipped at the right edge of the canvas.
