#!/usr/bin/env python3
"""Build the EPUB edition of the manual directly from the same EVENTS log that
drives the PDF (see build_manual.py), so every figure is rendered as a real
embedded PNG instead of relying on a PDF->EPUB conversion (which dropped the
vector-drawn diagrams entirely).
"""
import os
import re
import shutil
import tempfile

from reportlab.graphics import renderPM
from ebooklib import epub

import build_manual as bm

OUT_DIR = "/sessions/upbeat-gifted-hamilton/mnt/com~apple~CloudDocs/music/kiffness/claude"
VERSION = "0.2.2"
BASENAME = "Akai_MPK_Mini_Mixing_Manual"
OUT_PLAIN = os.path.join(OUT_DIR, f"{BASENAME}.epub")
OUT_VERSIONED = os.path.join(OUT_DIR, f"{BASENAME} ({VERSION}).epub")

_AMP_RE = re.compile(r"&(?!amp;|lt;|gt;|quot;|#)")


def esc(text):
    """Escape stray bare ampersands so the string is valid XHTML, while
    leaving the small set of inline tags (<b>, <i>, etc.) already used in
    the manual's source text untouched."""
    return _AMP_RE.sub("&amp;", text)


CSS = """
body { font-family: -apple-system, Georgia, serif; line-height: 1.45; }
h1.chapter-title { font-size: 1.5em; color: #1a1a2e; border-bottom: 2px solid #cccccc; padding-bottom: 0.2em; }
h1.book-title { font-size: 1.6em; color: #1a1a2e; text-align: center; }
p.subtitle { color: #555577; text-align: center; font-size: 0.95em; }
h2 { font-size: 1.15em; color: #3a3a6e; margin-top: 1.3em; }
p { font-size: 1em; }
ul, ol { margin-left: 0.4em; }
li { margin-bottom: 0.4em; }
div.note, div.warn { padding: 0.6em 0.8em; margin: 0.8em 0; border-radius: 4px; }
div.note { background: #f0f0fa; }
div.warn { background: #fff3e0; }
figure { text-align: center; margin: 1em 0; }
figure img { max-width: 100%; }
figcaption { font-size: 0.8em; color: #777777; margin-top: 0.3em; }
table { border-collapse: collapse; width: 100%; margin: 0.8em 0; font-size: 0.9em; }
table th, table td { border: 1px solid #cccccc; padding: 0.35em 0.5em; }
table th { background: #3a3a6e; color: white; }
table tr:nth-child(even) td { background: #f4f4fb; }
.ref-box { background: #1a1a2e; color: white; padding: 0.6em; text-align: center; font-weight: bold; }
.ref-list { background: #f4f4fb; padding: 0.6em; text-align: center; }
.footer-note { font-size: 0.8em; color: #777777; text-align: center; margin-top: 2em; }
"""


def render_figures(events, tmpdir):
    """Render every Drawing in EVENTS to a PNG file, return {id(drawing): filename}."""
    mapping = {}
    n = 0
    for ev in events:
        if ev[0] == "figure":
            n += 1
            drawing = ev[1]
            fname = f"fig_{n:02d}.png"
            path = os.path.join(tmpdir, fname)
            renderPM.drawToFile(drawing, path, fmt="PNG", dpi=150)
            mapping[id(drawing)] = fname
    return mapping


def bullets_html(items, numbered):
    tag = "ol" if numbered else "ul"
    lis = "\n".join(f"<li>{esc(i)}</li>" for i in items)
    return f"<{tag}>\n{lis}\n</{tag}>"


def table_html(data, header):
    rows_html = []
    for i, row in enumerate(data):
        cell_tag = "th" if (header and i == 0) else "td"
        cells = "".join(f"<{cell_tag}>{esc(c)}</{cell_tag}>" for c in row)
        rows_html.append(f"<tr>{cells}</tr>")
    return "<table>\n" + "\n".join(rows_html) + "\n</table>"


def build():
    events = bm.EVENTS
    tmpdir = tempfile.mkdtemp(prefix="mpk_epub_")
    fig_files = render_figures(events, tmpdir)

    book = epub.EpubBook()
    book.set_identifier(f"akai-mpk-mini-mixing-manual-{VERSION}")
    book.set_title("Akai MPK Mini Mixing, Recording & Video-Sync Manual")
    book.set_language("en")
    book.add_author("Generated for Alexy")

    css_item = epub.EpubItem(uid="style", file_name="style/main.css", media_type="text/css", content=CSS)
    book.add_item(css_item)

    image_items = {}
    for fname in fig_files.values():
        with open(os.path.join(tmpdir, fname), "rb") as f:
            data = f.read()
        item = epub.EpubItem(uid=fname, file_name=f"images/{fname}", media_type="image/png", content=data)
        book.add_item(item)
        image_items[fname] = item

    chapters = []
    spine = ["nav"]

    # --- Cover / intro page, built from the single "cover" event ---
    cover_html_parts = []
    chapter_num = None
    chapter_title = None
    body_parts = []

    def flush_chapter():
        nonlocal chapter_num, chapter_title, body_parts
        if chapter_title is None:
            return
        c = epub.EpubHtml(
            title=f"{chapter_num}. {chapter_title}" if chapter_num else chapter_title,
            file_name=f"chap_{chapter_num or 0:02d}.xhtml",
            lang="en",
        )
        heading = f'<h1 class="chapter-title">Chapter {chapter_num}<br/>{esc(chapter_title)}</h1>' if chapter_num else f'<h1 class="chapter-title">{esc(chapter_title)}</h1>'
        c.content = f"<html><body>{heading}{''.join(body_parts)}</body></html>"
        c.add_item(css_item)
        book.add_item(c)
        chapters.append(c)
        spine.append(c)
        body_parts = []

    for ev in events:
        kind = ev[0]
        if kind == "cover":
            _, title, subtitle, ref_videos = ev
            ref_rows = "".join(f'<div class="ref-list">{esc(v)}</div>' for v in ref_videos)
            cover_html = (
                f'<h1 class="book-title">{title}</h1>'
                f'<p class="subtitle">{esc(subtitle)}</p>'
                f'<div class="ref-box">Reference videos studied for this guide</div>'
                f'{ref_rows}'
                f'<p class="subtitle">This guide assumes no prior experience with MIDI, music software, '
                f'audio recording, or the MPK Mini. Every chapter builds on the last — read in order the '
                f'first time through.</p>'
            )
            cover_page = epub.EpubHtml(title="Akai MPK Mini Mixing Manual", file_name="cover.xhtml", lang="en")
            cover_page.content = f"<html><body>{cover_html}</body></html>"
            cover_page.add_item(css_item)
            book.add_item(cover_page)
            chapters.append(cover_page)
            spine.append(cover_page)
        elif kind == "chapter":
            flush_chapter()
            _, chapter_num, chapter_title = ev
        elif kind == "h2":
            body_parts.append(f"<h2>{esc(ev[1])}</h2>")
        elif kind == "p":
            body_parts.append(f"<p>{esc(ev[1])}</p>")
        elif kind == "bullets":
            body_parts.append(bullets_html(ev[1], ev[2]))
        elif kind == "note":
            body_parts.append(f'<div class="note"><b>Tip:</b> {esc(ev[1])}</div>')
        elif kind == "warn":
            body_parts.append(f'<div class="warn"><b>Watch out:</b> {esc(ev[1])}</div>')
        elif kind == "table":
            body_parts.append(table_html(ev[1], ev[2]))
        elif kind == "figure":
            _, drawing, cap_text = ev
            fname = fig_files[id(drawing)]
            body_parts.append(
                f'<figure><img src="images/{fname}" alt="{esc(cap_text)}"/>'
                f'<figcaption>{esc(cap_text)}</figcaption></figure>'
            )
        elif kind == "footer":
            body_parts.append(f'<p class="footer-note">{esc(ev[1])}</p>')

    flush_chapter()

    book.toc = tuple(chapters)
    book.add_item(epub.EpubNcx())
    book.add_item(epub.EpubNav())
    book.spine = spine

    epub.write_epub(OUT_PLAIN, book)
    shutil.copyfile(OUT_PLAIN, OUT_VERSIONED)
    shutil.rmtree(tmpdir, ignore_errors=True)
    print(f"done, wrote {OUT_PLAIN} and {OUT_VERSIONED} with {len(fig_files)} embedded figures")


if __name__ == "__main__":
    build()
