#!/usr/bin/env python3
"""Render the APC40 book cover and First Pair library headboard.

The source art is AI-derived from the user-supplied performance screenshot.
Typography and the First Pair Press publisher mask are applied here so the
reader-facing title, author, and imprint remain exact and reproducible.
"""

from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont, ImageOps


ASSET_DIR = Path(__file__).resolve().parent
SOURCE_DIR = ASSET_DIR / "cover-source"

COVER_SOURCE = SOURCE_DIR / "ableton-cover-art.png"
HEADBOARD_SOURCE = SOURCE_DIR / "ableton-headboard-art.png"
PUBLISHER_MASK = SOURCE_DIR / "firstpair-publisher-mask.png"

COVER_OUTPUT = ASSET_DIR / "apc40-mk2-ableton-start-cover.png"
HEADBOARD_OUTPUT = ASSET_DIR / "apc40-mk2-ableton-start-headboard.png"

COVER_SIZE = (1800, 2880)
HEADBOARD_SIZE = (2400, 1350)

FONT_PATH = "/System/Library/Fonts/Avenir Next Condensed.ttc"
FONT_HEAVY_INDEX = 8
FONT_DEMI_INDEX = 2
FONT_REGULAR_INDEX = 7


def font(size: int, index: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(FONT_PATH, size=size, index=index)


def add_vertical_gradient(
    image: Image.Image,
    *,
    top_alpha: int,
    end_y: int,
    color: tuple[int, int, int] = (5, 20, 34),
) -> None:
    overlay = Image.new("RGBA", image.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    for y in range(min(end_y, image.height)):
        alpha = round(top_alpha * (1 - y / end_y))
        draw.line((0, y, image.width, y), fill=(*color, alpha))
    image.alpha_composite(overlay)


def add_left_gradient(image: Image.Image, *, start_alpha: int, end_x: int) -> None:
    overlay = Image.new("RGBA", image.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    for x in range(min(end_x, image.width)):
        alpha = round(start_alpha * (1 - x / end_x))
        draw.line((x, 0, x, image.height), fill=(3, 18, 31, alpha))
    image.alpha_composite(overlay)


def draw_text(
    draw: ImageDraw.ImageDraw,
    xy: tuple[int, int],
    text: str,
    typeface: ImageFont.FreeTypeFont,
    *,
    fill: str,
    stroke_width: int = 0,
    stroke_fill: str | None = None,
) -> None:
    draw.text(
        xy,
        text,
        font=typeface,
        fill=fill,
        stroke_width=stroke_width,
        stroke_fill=stroke_fill or fill,
    )


def publisher_mark(width: int) -> Image.Image:
    mask = Image.open(PUBLISHER_MASK).convert("L")
    height = round(mask.height * width / mask.width)
    mask = mask.resize((width, height), Image.Resampling.LANCZOS)
    # The grayscale mask is the exact publisher engraving: white is ink and
    # black is transparent paper. Tint it warm ivory without a backplate.
    alpha = mask.point(lambda value: round(value * 0.64))
    mark = Image.new("RGBA", mask.size, (226, 213, 178, 0))
    mark.putalpha(alpha)
    return mark


def render_cover() -> None:
    cover = ImageOps.fit(
        Image.open(COVER_SOURCE).convert("RGB"),
        COVER_SIZE,
        method=Image.Resampling.LANCZOS,
        centering=(0.5, 0.5),
    ).convert("RGBA")
    add_vertical_gradient(cover, top_alpha=108, end_y=1160)

    draw = ImageDraw.Draw(cover)
    left = 138
    ivory = "#f2efe8"
    cool = "#c7d5df"
    green = "#9bc47d"
    shadow = "#07131f"

    draw.rounded_rectangle((left, 144, left + 290, 157), radius=7, fill=green)
    draw.rounded_rectangle((left, 175, left + 142, 181), radius=3, fill=ivory)

    draw_text(
        draw,
        (left, 224),
        "APC40 MK2",
        font(170, FONT_HEAVY_INDEX),
        fill=ivory,
        stroke_width=4,
        stroke_fill=shadow,
    )
    draw_text(
        draw,
        (left, 390),
        "ABLETON LIVE 12",
        font(132, FONT_HEAVY_INDEX),
        fill=ivory,
        stroke_width=4,
        stroke_fill=shadow,
    )
    draw_text(
        draw,
        (left, 528),
        "GETTING STARTED",
        font(112, FONT_DEMI_INDEX),
        fill=cool,
        stroke_width=3,
        stroke_fill=shadow,
    )
    draw_text(
        draw,
        (left, 684),
        "APC-ONLY  /  ZERO-TO-ONE  /  LIVE LOOPING",
        font(47, FONT_DEMI_INDEX),
        fill=green,
        stroke_width=2,
        stroke_fill=shadow,
    )
    draw_text(
        draw,
        (left, 786),
        "ALEXY KHRABROV",
        font(58, FONT_REGULAR_INDEX),
        fill=ivory,
        stroke_width=2,
        stroke_fill=shadow,
    )

    mark = publisher_mark(round(COVER_SIZE[0] * 0.28))
    cover.alpha_composite(
        mark,
        ((COVER_SIZE[0] - mark.width) // 2, COVER_SIZE[1] - mark.height - 26),
    )

    cover.convert("RGB").save(COVER_OUTPUT, optimize=True)


def render_headboard() -> None:
    headboard = ImageOps.fit(
        Image.open(HEADBOARD_SOURCE).convert("RGB"),
        HEADBOARD_SIZE,
        method=Image.Resampling.LANCZOS,
        centering=(0.5, 0.5),
    ).convert("RGBA")
    # First Pair overlays catalog text on the left side of this image.
    add_left_gradient(headboard, start_alpha=62, end_x=1120)
    headboard.convert("RGB").save(HEADBOARD_OUTPUT, optimize=True)


def main() -> None:
    render_cover()
    render_headboard()
    print(f"Rendered {COVER_OUTPUT}")
    print(f"Rendered {HEADBOARD_OUTPUT}")


if __name__ == "__main__":
    main()
