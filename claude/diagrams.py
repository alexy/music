"""Diagram-drawing helpers for the MPK Mini manual, built with reportlab.graphics.shapes.
Each function returns a Drawing flowable that can be appended directly to a platypus story.
"""
from reportlab.graphics.shapes import (
    Drawing, Rect, Circle, Line, String, Polygon, Group
)
from reportlab.lib import colors

INK = colors.HexColor("#1a1a2e")
ACCENT = colors.HexColor("#3a3a6e")
LIGHT = colors.HexColor("#eef0fb")
LIGHT2 = colors.HexColor("#dfe3f7")
WHITE = colors.white
GREY = colors.HexColor("#888888")
GOOD = colors.HexColor("#2e7d32")


def _label(d, x, y, text, size=7.5, color=INK, anchor="middle", bold=False):
    # Several call sites pass embedded "\n" to lay out a label on multiple
    # lines. A reportlab String can't render a literal newline character
    # (it shows up as a missing-glyph box), so split here and stack the
    # lines vertically, centered on the requested y.
    lines = text.split("\n")
    line_h = size * 1.25
    for i, ln in enumerate(lines):
        yy = y + (len(lines) - 1) * line_h / 2 - i * line_h
        d.add(String(x, yy, ln, fontSize=size, fillColor=color,
                      textAnchor=anchor, fontName="Helvetica-Bold" if bold else "Helvetica"))


def mpk_mini_diagram():
    """Top-down labeled diagram of the Akai MPK Mini control surface."""
    w, h = 480, 300
    d = Drawing(w, h)

    bx0, by0, bx1, by1 = 40, 40, 440, 230
    d.add(Rect(bx0, by0, bx1 - bx0, by1 - by0, rx=10, ry=10,
                fillColor=colors.HexColor("#22223a"), strokeColor=INK, strokeWidth=1.5))

    # Joystick (top-left)
    jx, jy = 75, 195
    d.add(Circle(jx, jy, 16, fillColor=colors.HexColor("#444466"), strokeColor=WHITE, strokeWidth=1))
    d.add(Circle(jx, jy, 6, fillColor=colors.HexColor("#cccccc"), strokeColor=None))
    _label(d, jx, by1 + 14, "1. Joystick", 8, WHITE if False else INK, bold=True)
    d.add(Line(jx, by1, jx, by1 + 8, strokeColor=GREY))

    # Knobs row (top, 4 knobs)
    knob_y = 195
    knob_xs = [150, 195, 240, 285]
    for i, kx in enumerate(knob_xs):
        d.add(Circle(kx, knob_y, 13, fillColor=colors.HexColor("#555577"), strokeColor=WHITE, strokeWidth=1))
        d.add(Line(kx, knob_y, kx + 8, knob_y + 9, strokeColor=colors.HexColor("#cccccc"), strokeWidth=1.5))
    _label(d, (knob_xs[0] + knob_xs[-1]) / 2, by1 + 14, "2. Knobs K1–K4 (turn to send MIDI CC)", 8, INK, bold=True)
    d.add(Line((knob_xs[0] + knob_xs[-1]) / 2, by1, (knob_xs[0] + knob_xs[-1]) / 2, by1 + 8, strokeColor=GREY))

    # Transport buttons (top right)
    tb_y = 195
    tb_xs = [340, 365, 390, 415]
    tb_labels = ["◀◀", "▶", "■", "●"]
    for tx, lab in zip(tb_xs, tb_labels):
        d.add(Rect(tx - 9, tb_y - 9, 18, 18, rx=3, ry=3, fillColor=colors.HexColor("#444466"), strokeColor=WHITE))
        _label(d, tx, tb_y - 3, lab, 7, WHITE)
    _label(d, (tb_xs[0] + tb_xs[-1]) / 2, by1 + 24, "3. Transport / Record", 8, INK, bold=True)
    d.add(Line((tb_xs[0] + tb_xs[-1]) / 2, by1, (tb_xs[0] + tb_xs[-1]) / 2, by1 + 18, strokeColor=GREY))

    # Pads grid (2 rows x 4 cols = 8 visible, representing Bank A/B of 16)
    pad_w, pad_h = 28, 26
    pad_gap = 8
    grid_x0 = 330
    grid_y0 = 100
    for row in range(2):
        for col in range(4):
            px = grid_x0 + col * (pad_w + pad_gap)
            py = grid_y0 + row * (pad_h + pad_gap)
            shade = colors.HexColor("#6a6ad0") if (row + col) % 2 == 0 else colors.HexColor("#5757b0")
            d.add(Rect(px, py, pad_w, pad_h, rx=4, ry=4, fillColor=shade, strokeColor=WHITE, strokeWidth=1))
            num = row * 4 + col + 1
            _label(d, px + pad_w / 2, py + pad_h / 2 - 3, str(num), 8, WHITE)
    _label(d, grid_x0 + (4 * (pad_w + pad_gap)) / 2 - pad_gap / 2, by1 + 14, "4. Pads 1–8 (Bank A/B = 16 total)", 8, INK, bold=True)
    d.add(Line(grid_x0 + 70, by1, grid_x0 + 70, by1 + 8, strokeColor=GREY))

    # Keybed (bottom) — fills the same left/right margin as the device
    # outline (bx0+20 .. bx1-20) so the keys reach the right side of the
    # control surface instead of stopping well short of it.
    key_y0 = 50
    key_h = 40
    n_white = 16
    kx0 = bx0 + 20
    kx1 = bx1 - 20
    key_w = (kx1 - kx0) / n_white
    for i in range(n_white):
        d.add(Rect(kx0 + i * key_w, key_y0, key_w - 1, key_h, fillColor=WHITE, strokeColor=colors.HexColor("#333333")))
    # black keys (skip pattern)
    pattern = [1, 1, 0, 1, 1, 1, 0] * 3
    bk_w = key_w * 0.6
    bi = 0
    for i, has_black in enumerate(pattern[:n_white - 1]):
        if has_black:
            bx = kx0 + (i + 1) * key_w - bk_w / 2
            d.add(Rect(bx, key_y0 + key_h * 0.4, bk_w, key_h * 0.6, fillColor=colors.HexColor("#111111")))
    _label(d, kx0 + (n_white * key_w) / 2, by0 - 14, "5. Keybed – 25 mini keys (velocity-sensitive)", 8, INK, bold=True)
    d.add(Line(kx0 + (n_white * key_w) / 2, by0, kx0 + (n_white * key_w) / 2, by0 - 6, strokeColor=GREY))

    # USB port (back, drawn as a small tab on the right edge). Labels are
    # right-aligned to the canvas edge so they grow leftward and never run
    # off the right side of the drawing.
    d.add(Rect(bx1 - 4, by1 - 60, 14, 10, fillColor=colors.HexColor("#cccccc"), strokeColor=INK))
    _label(d, w - 4, by1 - 55, "6. USB-B port\n(rear)", 7.5, INK, anchor="end")
    _label(d, w - 4, by1 - 65, "(connects to Mac)", 7, GREY, anchor="end")

    # Title
    _label(d, w / 2, h - 14, "Akai MPK Mini — Top View (mkII / mkIII / MK4 layout is similar)", 10, INK, bold=True)

    return d


def midi_signal_flow_diagram():
    """MPK Mini -> Mac -> DAW -> Instrument -> Audio out."""
    w, h = 480, 175
    d = Drawing(w, h)
    boxes = [
        ("MPK Mini\n(MIDI controller)", 10),
        ("Mac\n(USB MIDI driver)", 110),
        ("DAW\n(Logic / Live / GarageBand)", 220),
        ("Software\nInstrument", 335),
        ("Speakers /\nHeadphones", 415),
    ]
    bw, bh = 90, 60
    y = 60
    centers = []
    for label, x in boxes:
        bw_use = 90 if x != 415 else 60
        d.add(Rect(x, y, bw_use, bh, rx=8, ry=8, fillColor=LIGHT, strokeColor=ACCENT, strokeWidth=1.3))
        lines = label.split("\n")
        for i, ln in enumerate(lines):
            _label(d, x + bw_use / 2, y + bh / 2 + 8 - i * 11, ln, 8, INK)
        centers.append((x, x + bw_use, y + bh / 2))

    for i in range(len(centers) - 1):
        x1 = centers[i][1]
        x2 = centers[i + 1][0]
        yy = centers[i][2]
        d.add(Line(x1, yy, x2 - 4, yy, strokeColor=ACCENT, strokeWidth=1.5))
        d.add(Polygon(points=[x2 - 4, yy - 4, x2 - 4, yy + 4, x2, yy], fillColor=ACCENT, strokeColor=ACCENT))

    _label(d, (centers[0][1] + centers[1][0]) / 2, y + bh + 14, "USB cable", 7.5, GREY)
    _label(d, (centers[2][1] + centers[3][0]) / 2, y + bh + 14, "MIDI notes\n+ CC", 7.5, GREY)
    _label(d, (centers[3][1] + centers[4][0]) / 2, y + bh + 14, "Audio", 7.5, GREY)
    _label(d, w / 2, h - 12, "How a Key/Pad Press Becomes Sound", 10, INK, bold=True)
    return d


def audio_signal_chain_diagram():
    """Mic/Source -> Interface -> DAW track -> EQ/Comp -> Fader -> Master -> Speakers."""
    w, h = 480, 160
    d = Drawing(w, h)
    stages = ["Mic / Sample\nSource", "Audio\nInterface", "DAW Track\n(recorded audio)", "EQ +\nCompressor", "Fader\n(level)", "Master\nBus"]
    n = len(stages)
    bw = 68
    gap = (w - 20 - n * bw) / (n - 1)
    y = 70
    bh = 55
    xs = [10 + i * (bw + gap) for i in range(n)]
    for x, label in zip(xs, stages):
        d.add(Rect(x, y, bw, bh, rx=7, ry=7, fillColor=LIGHT2, strokeColor=ACCENT, strokeWidth=1.2))
        lines = label.split("\n")
        for i, ln in enumerate(lines):
            _label(d, x + bw / 2, y + bh / 2 + 6 - i * 10, ln, 7.3, INK)
    for i in range(n - 1):
        x1 = xs[i] + bw
        x2 = xs[i + 1]
        yy = y + bh / 2
        d.add(Line(x1, yy, x2 - 4, yy, strokeColor=ACCENT, strokeWidth=1.5))
        d.add(Polygon(points=[x2 - 4, yy - 4, x2 - 4, yy + 4, x2, yy], fillColor=ACCENT, strokeColor=ACCENT))
    _label(d, w / 2, h - 14, "Audio Signal Path: Source to Speakers", 10, INK, bold=True)
    _label(d, w / 2, 20, "Every recorded sound (vocal sample, mic, line-in) follows this same path.", 7.5, GREY)
    return d


def knob_cc_mapping_diagram():
    """Knob -> CC number -> MIDI Learn -> DAW parameter."""
    w, h = 480, 150
    d = Drawing(w, h)
    # Knob icon
    kx, ky = 50, 90
    d.add(Circle(kx, ky, 24, fillColor=colors.HexColor("#555577"), strokeColor=WHITE, strokeWidth=1.5))
    d.add(Line(kx, ky, kx + 15, ky + 16, strokeColor=colors.HexColor("#dddddd"), strokeWidth=2))
    _label(d, kx, ky - 38, "Physical knob\non MPK Mini", 8, INK)

    d.add(Line(kx + 30, ky, 150, ky, strokeColor=ACCENT, strokeWidth=1.5))
    d.add(Polygon(points=[146, ky - 4, 146, ky + 4, 150, ky], fillColor=ACCENT))

    d.add(Rect(150, ky - 25, 90, 50, rx=8, ry=8, fillColor=LIGHT, strokeColor=ACCENT))
    _label(d, 195, ky + 6, "Sends MIDI", 7.5, INK)
    _label(d, 195, ky - 6, "CC #1–#119", 8.5, INK, bold=True)

    d.add(Line(240, ky, 290, ky, strokeColor=ACCENT, strokeWidth=1.5))
    d.add(Polygon(points=[286, ky - 4, 286, ky + 4, 290, ky], fillColor=ACCENT))

    d.add(Rect(290, ky - 25, 90, 50, rx=8, ry=8, fillColor=LIGHT, strokeColor=ACCENT))
    _label(d, 335, ky + 6, "DAW “MIDI", 7.5, INK)
    _label(d, 335, ky - 6, "Learn / Map”", 8.5, INK, bold=True)

    d.add(Line(380, ky, 430, ky, strokeColor=ACCENT, strokeWidth=1.5))
    d.add(Polygon(points=[426, ky - 4, 426, ky + 4, 430, ky], fillColor=ACCENT))

    d.add(Rect(430, ky - 25, 45, 50, rx=8, ry=8, fillColor=colors.HexColor("#d7f7da"), strokeColor=GOOD))
    _label(d, 452, ky + 8, "Filter /", 7, INK)
    _label(d, 452, ky - 2, "Volume /", 7, INK)
    _label(d, 452, ky - 12, "Send", 7, INK)

    _label(d, w / 2, h - 14, "Turning a Knob into a Live Mix Control", 10, INK, bold=True)
    return d


def eq_curve_diagram():
    """Simple frequency response curve showing a cut and a boost."""
    w, h = 480, 170
    d = Drawing(w, h)
    x0, y0, x1, y1 = 50, 30, 440, 140
    d.add(Line(x0, y0, x1, y0, strokeColor=GREY))
    d.add(Line(x0, y0, x0, y1, strokeColor=GREY))
    _label(d, (x0 + x1) / 2, 10, "Frequency (Hz) — low to high, left to right", 8, GREY)
    d.add(String(15, (y0 + y1) / 2, "Volume", fontSize=8, fillColor=GREY))

    mid = y0 + (y1 - y0) * 0.55
    pts = []
    import math
    n = 60
    for i in range(n + 1):
        t = i / n
        x = x0 + t * (x1 - x0)
        # baseline with a dip around 30% (low-mid cut) and a bump around 70% (presence boost)
        dip = -22 * math.exp(-((t - 0.28) ** 2) / (2 * 0.025))
        bump = 16 * math.exp(-((t - 0.72) ** 2) / (2 * 0.02))
        y = mid + dip + bump
        pts.extend([x, y])
    from reportlab.graphics.shapes import PolyLine
    d.add(PolyLine(pts, strokeColor=ACCENT, strokeWidth=2.2))
    d.add(Line(x0, mid, x1, mid, strokeColor=colors.HexColor("#cccccc"), strokeWidth=0.8))

    cut_x = x0 + 0.28 * (x1 - x0)
    boost_x = x0 + 0.72 * (x1 - x0)
    _label(d, cut_x, y1 + 8, "Cut\n(e.g. 300–500 Hz,\nclear room for vocal)", 7, INK)
    _label(d, boost_x, y1 + 8, "Gentle boost\n(e.g. presence\naround 3–5 kHz)", 7, INK)

    _label(d, w / 2, h - 14, "Reading an EQ Curve", 10, INK, bold=True)
    return d


def video_sync_diagram():
    """Clap/marker syncing camera audio and DAW audio on a timeline."""
    w, h = 170 * 1 + 0, 170
    w = 480
    d = Drawing(w, h)
    track_h = 26
    y_cam = 100
    y_daw = 60
    x0 = 60
    x1 = 430
    d.add(Rect(x0, y_cam, x1 - x0, track_h, fillColor=colors.HexColor("#ffe9c6"), strokeColor=colors.HexColor("#b9852f")))
    _label(d, 38, y_cam + track_h / 2, "Camera\naudio", 7.5, INK, anchor="end")
    d.add(Rect(x0, y_daw, x1 - x0, track_h, fillColor=LIGHT2, strokeColor=ACCENT))
    _label(d, 38, y_daw + track_h / 2, "DAW\nrecording", 7.5, INK, anchor="end")

    clap_x = x0 + 35
    d.add(Line(clap_x, y_cam, clap_x, y_daw + track_h, strokeColor=colors.HexColor("#c62828"), strokeWidth=1.5, strokeDashArray=[3, 2]))
    _label(d, clap_x, y_cam + track_h + 10, "Clap / marker\n(spike in both waveforms)", 7.2, colors.HexColor("#c62828"))

    # fake waveforms
    import random
    random.seed(3)
    for trackY, col in [(y_cam, colors.HexColor("#b9852f")), (y_daw, ACCENT)]:
        prev = trackY + track_h / 2
        xpos = x0 + 4
        while xpos < x1 - 4:
            amp = 10 if abs(xpos - clap_x) > 6 else 11
            yy = trackY + track_h / 2 + random.uniform(-amp, amp) * (1 if abs(xpos - clap_x) > 6 else 1.0)
            d.add(Line(xpos, trackY + track_h / 2, xpos, yy, strokeColor=col, strokeWidth=0.8))
            xpos += 3

    _label(d, w / 2, h - 14, "Lining Up Camera Audio with Your DAW Recording", 10, INK, bold=True)
    _label(d, w / 2, 18, "Align both tracks at the spike, then your video editor stays in sync for the whole take.", 7.3, GREY)
    return d


def pad_bank_diagram():
    """16-pad grid (Bank A + Bank B) with sample-role labels."""
    w, h = 540, 230
    d = Drawing(w, h)
    labels_a = ["Vocal\nchop 1", "Vocal\nchop 2", "Vocal\nchop 3", "Vocal\nchop 4",
                "Kick\nloop", "Clap/Snare\nloop", "Hi-hat\nloop", "Perc\nloop"]
    labels_b = ["Bass\nstart", "Bass\nstop", "Riser\nFX", "Sweep\nFX",
                "Drop\nimpact", "Crash", "Ad-lib 1", "Ad-lib 2"]

    def grid(x0, y0, labels, bank_name, color):
        _label(d, x0 + 1.5 * 60, y0 + 110, bank_name, 9, INK, bold=True)
        for i, lab in enumerate(labels):
            row = i // 4
            col = i % 4
            px = x0 + col * 62
            py = y0 + (1 - row) * 46
            d.add(Rect(px, py, 56, 40, rx=5, ry=5, fillColor=color, strokeColor=WHITE, strokeWidth=1))
            lines = lab.split("\n")
            for li, ln in enumerate(lines):
                _label(d, px + 28, py + 22 - li * 10, ln, 7, WHITE)
            _label(d, px + 6, py + 33, str(i + 1), 7, colors.HexColor("#dddddd"), anchor="start")

    grid(20, 30, labels_a, "Bank A", colors.HexColor("#5757b0"))
    grid(270, 30, labels_b, "Bank B", colors.HexColor("#3a3a6e"))

    _label(d, w / 2, h - 14, "Example 16-Pad Layout for a Remix Build", 10, INK, bold=True)
    return d


def motu_m4_routing_diagram():
    """Two signal paths into the MOTU M4: UT87 -> Pre-73 -> Line In 2, and Shure 55 -> Mic In 1 direct."""
    w, h = 560, 230
    d = Drawing(w, h)

    def box(x, y, bw, bh, label, fill=LIGHT, textcol=INK, fsize=8):
        d.add(Rect(x, y, bw, bh, rx=7, ry=7, fillColor=fill, strokeColor=ACCENT, strokeWidth=1.2))
        lines = label.split("\n")
        for i, ln in enumerate(lines):
            _label(d, x + bw / 2, y + bh / 2 + (len(lines) - 1) * 5 - i * 10, ln, fsize, textcol)

    def arrow(x1, y1, x2, y2, label=None, dy_label=10):
        d.add(Line(x1, y1, x2 - 4, y2, strokeColor=ACCENT, strokeWidth=1.5))
        d.add(Polygon(points=[x2 - 4, y2 - 4, x2 - 4, y2 + 4, x2, y2], fillColor=ACCENT, strokeColor=ACCENT))
        if label:
            _label(d, (x1 + x2) / 2, y2 + dy_label, label, 7, GREY)

    # --- Top path: UT87 -> Pre-73 -> M4 Line In 2 ---
    y_top = 165
    box(15, y_top - 22, 70, 44, "UT87\nmicrophone", LIGHT2)
    arrow(85, y_top, 130, y_top, "XLR")
    box(130, y_top - 22, 90, 44, "Pre-73\npreamp\n(line/DI out)", LIGHT2)
    arrow(220, y_top, 290, y_top, "1/4\" line\nor XLR")

    # --- Bottom path: Shure 55 -> M4 Mic In 1 direct ---
    y_bot = 70
    box(15, y_bot - 22, 70, 44, "Shure 55\nmicrophone", colors.HexColor("#ffe9c6"))
    arrow(85, y_bot, 290, y_bot, "XLR, direct")

    # --- MOTU M4 ---
    mx, my, mw, mh = 290, 35, 150, 160
    d.add(Rect(mx, my, mw, mh, rx=10, ry=10, fillColor=colors.HexColor("#22223a"), strokeColor=INK, strokeWidth=1.5))
    _label(d, mx + mw / 2, my + mh - 16, "MOTU M4", 10, WHITE, bold=True)
    d.add(Rect(mx + 15, y_top - 14, 26, 28, rx=4, ry=4, fillColor=colors.HexColor("#5757b0"), strokeColor=WHITE))
    _label(d, mx + 28, y_top - 2, "In 2\n(Line,\ngain knob)", 6.3, WHITE)
    d.add(Rect(mx + 15, y_bot - 14, 26, 28, rx=4, ry=4, fillColor=colors.HexColor("#5757b0"), strokeColor=WHITE))
    _label(d, mx + 28, y_bot - 2, "In 1\n(Mic/Combo,\n+48V off)", 6.3, WHITE)
    arrow(mx + 50, y_top, mx + 50, y_top, None)  # placeholder no-op to keep structure simple
    d.add(Line(mx + 60, (y_top + y_bot) / 2 + 50, mx + 110, (y_top + y_bot) / 2 + 50, strokeColor=colors.HexColor("#888899"), strokeWidth=1))
    _label(d, mx + mw / 2, my + 28, "USB-C to Mac", 8, colors.HexColor("#cccccc"))
    d.add(Rect(mx + mw - 16, my + mh / 2 - 6, 14, 12, fillColor=colors.HexColor("#cccccc"), strokeColor=INK))
    arrow(mx + mw, my + mh / 2, 480, my + mh / 2, None)
    _label(d, 483, my + mh / 2 + 14, "to Mac\n(USB-C)", 7, GREY, anchor="start")

    _label(d, w / 2, h - 14, "Two Mic Paths Into the MOTU M4", 10, INK, bold=True)
    _label(d, w / 2, 14, "UT87 → Pre-73 (sets the tone/gain) → M4 Line In; Shure 55 → M4 Mic In directly, no preamp needed.", 7.3, GREY)
    return d


def build_arrangement_timeline_diagram():
    """Intro -> Build -> Drop -> Breakdown -> Drop2 -> Outro timeline."""
    w, h = 480, 130
    d = Drawing(w, h)
    sections = [("Intro", colors.HexColor("#c9d6f5")), ("Build", colors.HexColor("#9fb4ec")),
                ("Drop", colors.HexColor("#3a3a6e")), ("Breakdown", colors.HexColor("#c9d6f5")),
                ("Drop 2", colors.HexColor("#3a3a6e")), ("Outro", colors.HexColor("#9fb4ec"))]
    widths = [50, 60, 80, 60, 80, 50]
    x = 20
    y = 50
    bh = 40
    for (name, col), bw in zip(sections, widths):
        textcol = WHITE if col == colors.HexColor("#3a3a6e") else INK
        d.add(Rect(x, y, bw - 2, bh, fillColor=col, strokeColor=INK, strokeWidth=0.8))
        _label(d, x + bw / 2, y + bh / 2 - 3, name, 8, textcol, bold=True)
        x += bw
    _label(d, w / 2, h - 14, "Typical Arrangement Shape for a Club/Dance Remix", 10, INK, bold=True)
    _label(d, w / 2, 18, "Pads trigger new layers at each boundary; knobs sweep filters across the transitions.", 7.3, GREY)
    return d
