#!/usr/bin/env python3
"""Build the full beginner-friendly Akai MPK Mini manual, with one chapter per topic
and diagrams, as a PDF."""

from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle,
    ListFlowable, ListItem, HRFlowable, KeepTogether
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER

import diagrams as dg

OUT = "/sessions/upbeat-gifted-hamilton/mnt/com~apple~CloudDocs/music/kiffness/claude/Akai_MPK_Mini_Mixing_Manual.pdf"

styles = getSampleStyleSheet()

title_style = ParagraphStyle("TitleBig", parent=styles["Title"], fontSize=25, leading=29, textColor=colors.HexColor("#1a1a2e"))
subtitle_style = ParagraphStyle("Subtitle", parent=styles["Normal"], fontSize=12.5, leading=17, textColor=colors.HexColor("#555577"), alignment=TA_CENTER, spaceAfter=6)
chapter_label_style = ParagraphStyle("ChapterLabel", parent=styles["Normal"], fontSize=11, leading=13, textColor=colors.HexColor("#8888aa"), spaceBefore=0, spaceAfter=2)
h1 = ParagraphStyle("H1", parent=styles["Heading1"], fontSize=19, leading=23, textColor=colors.HexColor("#1a1a2e"), spaceBefore=0, spaceAfter=10)
h2 = ParagraphStyle("H2", parent=styles["Heading2"], fontSize=13, leading=16, textColor=colors.HexColor("#3a3a6e"), spaceBefore=12, spaceAfter=6)
body = ParagraphStyle("Body", parent=styles["Normal"], fontSize=10.3, leading=14.5, spaceAfter=8)
bullet = ParagraphStyle("Bullet", parent=body, leftIndent=14, spaceAfter=4)
note_style = ParagraphStyle("Note", parent=body, backColor=colors.HexColor("#f0f0fa"), borderPadding=8, leftIndent=4, rightIndent=4, spaceAfter=10)
warn_style = ParagraphStyle("Warn", parent=body, backColor=colors.HexColor("#fff3e0"), borderPadding=8, leftIndent=4, rightIndent=4, spaceAfter=10)
caption = ParagraphStyle("Caption", parent=styles["Normal"], fontSize=8.5, leading=11, textColor=colors.HexColor("#777"), alignment=TA_CENTER, spaceAfter=10)
toc_style = ParagraphStyle("Toc", parent=body, fontSize=10.5, leading=18)

story = []
CH_NUM = [0]


def add_chapter_break(num, title):
    story.append(PageBreak())
    story.append(Paragraph(f"CHAPTER {num}", chapter_label_style))
    story.append(Paragraph(title, h1))
    story.append(HRFlowable(width="100%", thickness=0.75, color=colors.HexColor("#cccccc")))
    story.append(Spacer(1, 8))


def add_h2(text):
    story.append(Paragraph(text, h2))


def add_p(text):
    story.append(Paragraph(text, body))


def add_bullets(items, numbered=False):
    story.append(ListFlowable(
        [ListItem(Paragraph(i, bullet), leftIndent=14) for i in items],
        bulletType="1" if numbered else "bullet", start="1" if numbered else "circle", leftIndent=10
    ))
    story.append(Spacer(1, 6))


def add_note(text):
    story.append(Paragraph("<b>Tip:</b> " + text, note_style))


def add_warn(text):
    story.append(Paragraph("<b>Watch out:</b> " + text, warn_style))


def add_figure(drawing, cap_text):
    story.append(Spacer(1, 6))
    story.append(drawing)
    story.append(Paragraph(cap_text, caption))


def add_table(data, col_widths, header=True):
    t = Table(data, colWidths=col_widths)
    style = [
        ("FONTSIZE", (0, 0), (-1, -1), 9.3),
        ("GRID", (0, 0), (-1, -1), 0.4, colors.HexColor("#cccccc")),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("ROWBACKGROUNDS", (0, 1 if header else 0), (-1, -1), [colors.white, colors.HexColor("#f4f4fb")]),
    ]
    if header:
        style += [
            ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#3a3a6e")),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ]
    t.setStyle(TableStyle(style))
    story.append(t)
    story.append(Spacer(1, 10))


# ============================================================ COVER
story.append(Spacer(1, 1.3 * inch))
story.append(Paragraph("Akai MPK Mini Mixing, Recording &amp; Video-Sync Manual", title_style))
story.append(Spacer(1, 0.12 * inch))
story.append(Paragraph(
    "A complete beginner's guide — MIDI, your Mac, the MPK Mini, recording, mixing, and "
    "syncing to video — for building layered remix videos in the style of The Kiffness",
    subtitle_style
))
story.append(Spacer(1, 0.4 * inch))
story.append(HRFlowable(width="60%", thickness=1, color=colors.HexColor("#cccccc"), hAlign="CENTER"))
story.append(Spacer(1, 0.3 * inch))
ref_table_data = [
    ["Reference videos studied for this guide"],
    ["The Shira Choir x The Kiffness – Im Hashem Lo Yivneh Bayis (Psalm 127 Dance Remix)"],
    ["The Kiffness – Ievan Polkka ft. Bilal Göregen (Club Remix)"],
    ["The Kiffness x Ognjen & Sinisa – Insomnia (Balkan Club Remix)"],
]
t = Table(ref_table_data, colWidths=[4.6 * inch])
t.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#1a1a2e")),
    ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
    ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
    ("FONTSIZE", (0, 0), (-1, -1), 9.5),
    ("BACKGROUND", (0, 1), (-1, -1), colors.HexColor("#f4f4fb")),
    ("BOX", (0, 0), (-1, -1), 0.5, colors.HexColor("#cccccc")),
    ("INNERGRID", (0, 0), (-1, -1), 0.5, colors.white),
    ("TOPPADDING", (0, 0), (-1, -1), 7),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
    ("LEFTPADDING", (0, 0), (-1, -1), 10),
    ("ALIGN", (0, 0), (-1, -1), "CENTER"),
]))
story.append(t)
story.append(Spacer(1, 0.5 * inch))
story.append(Paragraph(
    "This guide assumes no prior experience with MIDI, music software, audio recording, or the MPK Mini. "
    "Every chapter builds on the last — read in order the first time through.",
    caption
))

# ============================================================ TABLE OF CONTENTS
story.append(PageBreak())
story.append(Paragraph("Table of Contents", h1))
story.append(Spacer(1, 6))
toc_items = [
    "1. What You're Going to Build",
    "2. What Is MIDI? (The Idea Behind Everything)",
    "3. What Is a DAW, and Setting Up Your Mac",
    "4. Meet Your Akai MPK Mini",
    "5. Connecting the MPK Mini to Your Mac",
    "6. Installing and Configuring Your Software",
    "7. Keys, Pads, Knobs and Joystick — What Each One Actually Does",
    "8. Recording Your First MIDI Instrument",
    "9. Connecting Your Audio Interface: MOTU M4, Pre-73, and Your Microphones",
    "10. Recording Audio: Vocals, Samples, and Real Instruments",
    "11. Mapping Pads to Trigger Samples and Loops",
    "12. Mapping Knobs for Live Mixing",
    "13. Mixing Fundamentals for Complete Beginners",
    "14. Building a Layered Remix, Start to Finish",
    "15. Live-Looping Performance Technique",
    "16. Syncing Your Performance to Video",
    "17. Exporting and Finishing Your Track and Video",
    "18. Troubleshooting Common Problems",
    "19. Practice Plan and Quick-Reference Cheat Sheets",
]
for item in toc_items:
    story.append(Paragraph(item, toc_style))

# ============================================================ CHAPTER 1
add_chapter_break(1, "What You're Going to Build")
add_p(
    "Before touching any gear, it helps to know exactly what the finished result looks and sounds "
    "like, because every chapter after this one is building one piece of it."
)
add_p(
    "The three reference videos for this manual are all the same kind of project: someone finds a "
    "striking vocal or instrumental recording (a choir, a viral clip, a folk tune), and turns it into "
    "a club/dance remix by adding a beat, bass, and energy underneath it — and a lot of that adding-in "
    "happens live, on camera, by hand, using pads and knobs on a small controller like the Akai MPK Mini."
)
add_h2("The end result has three layers")
add_bullets([
    "<b>A finished piece of music</b> — an arrangement with an intro, a build, a drop, a breakdown, and an outro, mixed so it sounds good on headphones or speakers.",
    "<b>A video</b> — footage of you performing the remix live, synced precisely to the audio.",
    "<b>A repeatable workflow</b> — once you've done it once, you can apply the same steps to a new sample next time.",
])
add_h2("What you'll learn, chapter by chapter")
add_p(
    "Chapters 2–6 get your computer, software, and controller talking to each other — this is setup, "
    "done once. Chapters 7–11 teach you what every button on the MPK Mini does and how to make it "
    "trigger sounds and control your mix. Chapter 13 is a crash course in mixing, written for someone "
    "who has never mixed audio before. Chapters 13–16 walk through the actual remix-building and "
    "video-recording process end to end. Chapters 17–18 are for troubleshooting and quick lookup once "
    "you're working independently."
)
add_note(
    "You do not need to already own music software or know how to read sheet music. The only "
    "things you need are a Mac, an Akai MPK Mini, and (eventually) a way to record video, such as "
    "your phone or your Mac's built-in camera."
)

# ============================================================ CHAPTER 2
add_chapter_break(2, "What Is MIDI? (The Idea Behind Everything)")
add_p(
    "MIDI (Musical Instrument Digital Interface) is the single most important concept to understand "
    "before using the MPK Mini, so it's worth slowing down here."
)
add_h2("MIDI is not audio")
add_p(
    "When you press a key on the MPK Mini, it does <b>not</b> send any sound. There is no speaker, no "
    "audio circuitry, and no recorded tone inside it. Instead, it sends a tiny digital message — "
    "essentially a note saying “key number 60 was just pressed, at this loudness” or “key number 60 "
    "was just released.” That message travels over a USB cable into your computer."
)
add_p(
    "Your software (the DAW, covered in the next chapter) receives that message and decides what to "
    "do with it — usually, play a note on whatever virtual instrument (piano, synth, drum kit) is "
    "loaded on that track. The actual sound is generated entirely inside the computer. This is why "
    "the MPK Mini is called a <b>MIDI controller</b>, not an instrument by itself: it's a remote control "
    "for sounds that live in your software."
)
add_figure(dg.midi_signal_flow_diagram(), "Figure 2.1 — A key or pad press becomes a MIDI message, which your Mac and DAW turn into sound.")
add_h2("Two kinds of MIDI messages you'll use constantly")
add_bullets([
    "<b>Notes</b> — sent by the keys and pads. Each has a note number (which pitch/sample) and a velocity (how hard you pressed it, 0–127).",
    "<b>Control Change (CC) messages</b> — sent by the knobs and joystick. Each has a CC number and a value from 0–127, used for continuous changes like a filter sweep or volume fade rather than on/off notes.",
])
add_h2("Why this matters for mixing")
add_p(
    "Because MIDI carries no sound of its own, the exact same knob turn can mean “make it louder,” "
    "“open the filter,” or “add more reverb” — depending entirely on what you've told your software "
    "to do with that message. This is what makes the MPK Mini flexible: you're not limited to factory "
    "functions, you assign each control yourself (covered in Chapters 10–11)."
)
add_note(
    "If a pad or key seems to “do nothing,” it's almost never broken — it's far more likely that no "
    "instrument is loaded on the track it's pointed at, or the MIDI routing isn't set up yet. Chapters "
    "5–6 fix exactly this.",
)

# ============================================================ CHAPTER 3
add_chapter_break(3, "What Is a DAW, and Setting Up Your Mac")
add_h2("What a DAW is")
add_p(
    "A DAW (Digital Audio Workstation) is the software where everything actually happens: recording, "
    "arranging, mixing, and exporting. Think of it as a multi-track tape recorder crossed with a mixing "
    "desk crossed with a collection of virtual instruments, all running on your Mac."
)
add_h2("Which DAW to use")
add_bullets([
    "<b>GarageBand</b> — free, already installed on most Macs, and a genuinely good starting point. Use this if you want to start today with zero cost.",
    "<b>Logic Pro</b> — a one-time paid upgrade from GarageBand made by Apple, with deeper mixing tools and a proper live-loop grid (“Live Loops”) well suited to this project.",
    "<b>Ableton Live</b> — the DAW most associated with this exact style of live-looped remix performance, thanks to its Session View (a grid of loop clips you trigger by hand). Has a free trial.",
    "<b>FL Studio</b> — Windows-native but fully supported on Mac, with a Channel Rack and Playlist that work well for pad-triggered loops, and very mature audio-interface/ASIO-style handling carried over from its Windows roots. Has a free trial (“FL Studio Fruity Edition demo”).",
]
)
add_p(
    "This manual's instructions are written so the underlying ideas apply to any of the four; where "
    "steps differ, Ableton Live is used as the main example because its Session View maps most directly "
    "onto the “trigger loops with pads” workflow in the reference videos, with GarageBand and FL Studio "
    "specifics called out wherever the steps diverge — especially in Chapter 9, where the three differ "
    "most in how they handle audio interfaces."
)
add_h2("Setting up your Mac before you start")
add_bullets([
    "<b>Update macOS</b> — open System Settings → General → Software Update, and install any pending updates so your DAW and the MPK Mini drivers behave correctly.",
    "<b>Check available storage</b> — audio and video projects use a lot of disk space; aim for at least 10–20 GB free before a project.",
    "<b>Turn on “Do Not Disturb”</b> while recording, so notifications don't make sound or pop up on screen during a take (Control Center → Focus).",
    "<b>Plug in headphones or studio monitors</b> — built-in MacBook speakers are fine for early practice, but for any real mixing decision (Chapter 13) you'll want headphones at minimum, because laptop speakers hide bass problems.",
])
add_note(
    "GarageBand is pre-installed — open Launchpad and search “GarageBand” to confirm. If you "
    "don't see it, it's a free download from the Mac App Store."
)

# ============================================================ CHAPTER 4
add_chapter_break(4, "Meet Your Akai MPK Mini")
add_p(
    "The MPK Mini comes in a few hardware generations (mkII, mkIII, MK4) with slightly different "
    "knobs and screens, but the core layout below is the same across all of them."
)
add_figure(dg.mpk_mini_diagram(), "Figure 4.1 — The Akai MPK Mini's main controls, viewed from above.")
add_h2("The six things you need to know")
add_bullets([
    "<b>1. Joystick</b> — push left/right for pitch bend (bends a note's pitch up or down while held), push up/down for modulation (often adds vibrato or filter movement, instrument-dependent).",
    "<b>2. Knobs (K1–K4 or K1–K8 depending on model)</b> — turn to send a continuous MIDI CC value; you decide what each one controls (Chapter 12).",
    "<b>3. Transport / Record buttons</b> — control playback in your DAW remotely, so you don't need to reach for the trackpad while playing: rewind, play, stop, and record.",
    "<b>4. Pads (8 physical, 2 banks = 16 total)</b> — press to trigger a note, sample, or loop; backlit and pressure-sensitive.",
    "<b>5. Keybed</b> — 25 mini, velocity-sensitive keys spanning roughly two octaves; use the Octave Up/Down buttons to reach higher or lower notes.",
    "<b>6. USB-B port (rear)</b> — the only cable you need; it carries both MIDI data and power to the unit.",
])
add_h2("Other controls worth knowing")
add_bullets([
    "<b>Arpeggiator (ARP) button</b> — automatically plays the notes you hold in a repeating pattern; useful for instant motion under a sample.",
    "<b>Note Repeat</b> — holds a pad down and automatically repeats it in time, great for hi-hat rolls.",
    "<b>Octave Up/Down</b> — shifts the entire keybed up or down in 12-note (one octave) steps.",
    "<b>Sustain pedal input</b> — on the back of most models, lets you add a foot pedal for sustained notes, freeing both hands for pads and knobs.",
])

# ============================================================ CHAPTER 5
add_chapter_break(5, "Connecting the MPK Mini to Your Mac")
add_h2("Step by step")
add_bullets([
    "Connect the MPK Mini to your Mac using a USB-A-to-USB-B (or USB-C, depending on cable/model) cable — directly into the Mac, not through an unpowered hub if you can avoid it.",
    "The pads should light up briefly; this confirms it's receiving power over USB.",
    "Open <b>Audio MIDI Setup</b> (search for it in Spotlight, the magnifying glass top-right of your screen) and choose Window → Show MIDI Studio. You should see “MPK Mini” listed as a connected device.",
    "If it isn't listed, unplug and replug the cable, then try a different USB port.",
], numbered=True)
add_warn(
    "The MPK Mini is class-compliant, meaning macOS recognizes it natively — you do not need to "
    "install a driver just to see it appear in Audio MIDI Setup. You only need Akai's MPK Mini Editor "
    "software (next chapter) for advanced custom pad/knob mapping, not basic connection."
)
add_h2("Confirming it's actually sending MIDI")
add_p(
    "Still inside Audio MIDI Setup, double-click the MPK Mini icon in MIDI Studio — you should see an "
    "input and output port. Pressing a key on the MPK Mini won't visibly animate anything here, but "
    "this confirms macOS sees both directions of communication, which your DAW will rely on."
)

# ============================================================ CHAPTER 6
add_chapter_break(6, "Installing and Configuring Your Software")
add_h2("6.1 Install the MPK Mini Editor")
add_p(
    "Download the free “MPK Mini MIDI Editor” (or “MPC Beats,” which bundles it) from akaipro.com. "
    "This is the app where you build and save <b>programs</b> — named presets that define what each pad "
    "and knob sends, so you can switch instantly between a “drum triggers” layout and a “mixing knobs” "
    "layout without re-mapping by hand every session."
)
add_h2("6.2 Install and open your DAW")
add_p(
    "Open GarageBand, Logic Pro, or Ableton Live (whichever you chose in Chapter 3). Create a new, "
    "empty project."
)
add_h2("6.3 Tell your DAW about the MPK Mini")
add_bullets([
    "<b>GarageBand / Logic Pro:</b> these usually detect class-compliant MIDI keyboards automatically — open Preferences → MIDI to confirm the MPK Mini is listed as an input.",
    "<b>Ableton Live:</b> open Live → Settings (or Preferences) → Link/MIDI tab. Find “MPK Mini” in the input list and switch both <b>Track</b> and <b>Remote</b> to On.",
])
add_h2("6.4 Create one MIDI track and test it")
add_bullets([
    "Add a new Software Instrument (or MIDI) track.",
    "Make sure the track is record-enabled / “armed” (a red circle or similar icon).",
    "Press a key on the MPK Mini — you should hear a default piano or synth sound.",
], numbered=True)
add_note(
    "If you hear nothing: check that your Mac's output volume isn't muted, that headphones/speakers "
    "are selected as the output device in System Settings → Sound, and that the new track is armed "
    "for input, not just selected."
)
add_h2("6.5 Save two MPK Mini programs for later")
add_p(
    "In the MPK Mini Editor, create and save: (1) a program named something like “Pads-Triggers” with "
    "pads in Note Mode for Chapter 11, and (2) a program named “Knobs-Mixer” with knobs set to CC "
    "numbers for Chapter 12. You'll switch between them with the PGM button while working."
)

# ============================================================ CHAPTER 7
add_chapter_break(7, "Keys, Pads, Knobs and Joystick — What Each One Actually Does")
add_p(
    "This chapter goes one level deeper than Chapter 4: the practical behavior of each control, and "
    "the settings that change how it feels."
)
add_h2("7.1 Keys")
add_p(
    "Velocity-sensitive means how hard you press changes the recorded loudness — useful for "
    "expressive bass lines or chords, less useful when you want every hit to sound identical."
)
add_h2("7.2 Pads")
add_bullets([
    "<b>Note Mode</b> — each pad sends a single fixed MIDI note; this is what you want for triggering one-shot samples, drum hits, or starting/stopping loop clips.",
    "<b>Velocity curve / Full Level</b> — in the Editor, you can force pads to always send maximum velocity (127) regardless of how hard you hit them. Use this for sample triggers and loop launches, where you want consistent volume; leave normal velocity for expressive drum programming.",
    "<b>Banks A and B</b> — double the 8 physical pads to 16 addressable triggers; switch banks with the dedicated Bank button.",
])
add_h2("7.3 Knobs")
add_p(
    "Each knob sends one continuous CC value as you turn it, from 0 (fully counter-clockwise) to 127 "
    "(fully clockwise). They have no physical limit/end-stop tied to the software parameter — the "
    "knob's physical position and the on-screen control's position will drift apart over time unless "
    "you reset both to a known point occasionally (a “pickup” style sync, which most modern DAWs handle for you)."
)
add_h2("7.4 Joystick")
add_bullets([
    "<b>Left/right</b> — pitch bend, springs back to center when released.",
    "<b>Up/down</b> — modulation, often does <i>not</i> spring back, so reset it manually after using it or you may leave an effect “stuck on.”",
])
add_figure(dg.knob_cc_mapping_diagram(), "Figure 7.1 — How a single knob turn becomes a usable mixing control.")
add_warn(
    "A common beginner mistake: pushing the joystick up for vibrato, then forgetting to push it back "
    "down — leaving every subsequent note wobbly. Get in the habit of recentering it after each use."
)

# ============================================================ CHAPTER 8
add_chapter_break(8, "Recording Your First MIDI Instrument")
add_p(
    "This is your first hands-on recording, before any samples or mixing are involved — the goal is "
    "comfort with the basic record/playback loop in your DAW."
)
add_bullets([
    "Pick a simple software instrument (a piano or a synth bass preset) on your armed MIDI track.",
    "Set a tempo you're comfortable with (most DAWs default to 120 BPM — beats per minute).",
    "Turn on the metronome / click track.",
    "Press the DAW's Record button (or the Record transport button on the MPK Mini itself, once mapped).",
    "Play a simple 4–8 note pattern in time with the click.",
    "Press Stop, then press Play from the beginning to listen back.",
], numbered=True)
add_h2("If it didn't sound right")
add_bullets([
    "<b>Notes are late/early</b> — normal at first; most DAWs have a quantize function that snaps recorded notes to the nearest beat after the fact. Don't worry about perfect timing yet.",
    "<b>Wrong notes</b> — undo (Cmd+Z) and try again; recording is non-destructive, you can always redo a take.",
    "<b>No sound at all</b> — revisit Chapter 6.4's checklist.",
])
add_note(
    "Get comfortable with Cmd+Z (undo) and the Loop/Cycle button in your DAW — looping a short section "
    "and recording over it repeatedly until a take feels right is exactly the muscle-memory habit you'll "
    "rely on in Chapters 13–14."
)

# ============================================================ CHAPTER 9
add_chapter_break(9, "Connecting Your Audio Interface: MOTU M4, Pre-73, and Your Microphones")
add_p(
    "If you're recording real vocals or instruments rather than only using software instruments and "
    "found samples, you'll route everything through an audio interface first. This chapter covers your "
    "specific setup: a MOTU M4 with a UT87 microphone going through a Pre-73 preamp on one channel, and "
    "a Shure 55 microphone going directly into the M4 on another."
)
add_h2("9.1 What each piece of gear does")
add_bullets([
    "<b>MOTU M4</b> — your audio interface: it converts microphone/instrument signals into digital audio your Mac can record, and converts the DAW's output back into sound for your speakers/headphones. It has 2 combo mic/line/instrument inputs on the front, plus 2 more line inputs on the back.",
    "<b>UT87</b> — a large-diaphragm condenser microphone (a U87-style design). Condenser mics need either phantom power or, as in your chain, a preamp that supplies it, and they're sensitive — good for capturing vocal detail.",
    "<b>Pre-73</b> — an outboard microphone preamp (a 1073-style design) that sits between the UT87 and the M4. It supplies the phantom power the condenser mic needs, boosts its signal to a usable level, and adds its own characteristic tone (often described as warm, slightly forward) before the signal ever reaches the interface.",
    "<b>Shure 55</b> — a dynamic microphone (the classic Elvis-style body). Dynamic mics don't need phantom power and have a built-in tolerance for loud sources; they're commonly plugged straight into an interface's mic input with no outboard preamp required.",
])
add_figure(dg.motu_m4_routing_diagram(), "Figure 9.1 — UT87 through the Pre-73 into the M4's line input, and the Shure 55 plugged directly into the M4's mic input.")
add_h2("9.2 Wiring it up")
add_bullets([
    "<b>UT87 → Pre-73:</b> connect the UT87 to the Pre-73's mic input (XLR). Turn on the Pre-73's phantom power (+48V) switch — the UT87 needs this to operate; the Shure 55 path does not.",
    "<b>Pre-73 → MOTU M4:</b> run the Pre-73's output (its 1/4\" line/DI output, or its XLR output if it has one) into one of the M4's <b>line</b> inputs — typically input 2 on the front, or one of the rear line inputs. Because the Pre-73 has already brought the signal up to line level and shaped its tone, you don't engage the M4's own mic preamp or phantom power on this channel.",
    "<b>Shure 55 → MOTU M4:</b> connect the Shure 55 directly into the M4's other combo input (e.g., input 1) using a standard XLR cable. Leave phantom power <b>off</b> for this input — dynamic mics like the Shure 55 don't use it, and some vintage-style dynamic mics can be damaged by phantom power over time.",
    "<b>MOTU M4 → Mac:</b> connect the M4 to your Mac with the included USB-C cable.",
], numbered=True)
add_warn(
    "Double-check which M4 input has phantom power enabled before plugging anything in. Turn the M4's "
    "physical gain knobs all the way down first, connect your mics, then bring gain up slowly while "
    "talking/singing at normal performance level — this avoids a loud pop reaching your ears or speakers."
)
add_h2("9.3 Setting gain on each channel")
add_bullets([
    "For the <b>UT87/Pre-73 channel</b>, do most of the gain work on the Pre-73 itself (it has its own input/output gain controls), then use the M4's line input trim only for fine adjustment — you're aiming for the M4's meter to read comfortably without hitting red.",
    "For the <b>Shure 55 channel</b>, since dynamic mics output a much weaker signal than condensers, you'll typically need to turn the M4's mic gain knob up noticeably further than you might expect — this is normal and not a sign anything is wrong.",
    "In both cases, watch the M4's own input meters (and your DAW's input meter) while doing a normal-volume test take, adjusting until the loudest moments sit comfortably below clipping.",
])
add_h2("9.4 Telling your Mac and DAW about the M4")
add_bullets([
    "Open System Settings → Sound, and confirm “MOTU M4” is available as both an input and output device (you can leave your Mac's system sound on its built-in output if you prefer monitoring through the M4 only inside your DAW).",
    "The M4 is class-compliant on macOS — no separate driver install is required, though installing MOTU's free “MOTU Pro Audio Installer” gives you the M4's onscreen mixer (CueMix) for routing and headphone monitoring control.",
])
add_h2("9.5 GarageBand setup with the M4")
add_bullets([
    "Open GarageBand → Settings (or Preferences) → Audio/MIDI, and set both the Input Device and Output Device to “MOTU M4.”",
    "Create a new Audio track, and in the track's input selector choose Input 1 (Shure 55) or Input 2 (UT87/Pre-73) as needed.",
    "Turn on “Monitor” (sometimes shown as a small speaker icon) on the armed track so you can hear yourself while recording, or rely on the M4's own direct hardware monitoring via CueMix if you'd rather not add any software monitoring latency.",
])
add_h2("9.6 FL Studio setup with the M4")
add_bullets([
    "Open FL Studio → Options → Audio Settings. Under Input/Output, choose “MOTU M4” as the device (on Mac, FL Studio uses Core Audio rather than ASIO, so you won't see an ASIO panel the way you would on Windows).",
    "Set the buffer size here too — start around 256–512 samples; lower values reduce monitoring latency but demand more from your Mac, higher values are more stable but you'll hear a slight delay while recording.",
    "Create an Audio Track in the Playlist, click its input selector, and choose the M4's Input 1 or Input 2 to match whichever microphone path you're recording.",
    "Enable the track's monitoring/“record arm” button before hitting record, the same way you would in GarageBand.",
])
add_note(
    "Keep a single, written-down “session template” once you've got both mic paths configured correctly "
    "in your DAW of choice — save it as a starting project so you never have to rebuild this routing from "
    "scratch."
)

# ============================================================ CHAPTER 10
add_chapter_break(10, "Recording Audio: Vocals, Samples, and Real Instruments")
add_p(
    "MIDI tracks (Chapter 8) record performance data, not sound. To get an actual vocal, a sampled "
    "video's audio, or a real instrument into your project, you record <b>audio</b> instead — a "
    "different kind of track that captures actual sound waves."
)
add_figure(dg.audio_signal_chain_diagram(), "Figure 10.1 — The path any recorded sound takes from source to speakers.")
add_h2("10.1 Getting sound into your Mac")
add_bullets([
    "<b>Built-in microphone</b> — fine for early experiments and for quick scratch vocals, but picks up room noise and is not great quality.",
    "<b>USB microphone</b> — a big, cheap upgrade; plugs directly into the Mac and is selectable as an input in System Settings → Sound and in your DAW.",
    "<b>Audio interface + XLR microphone</b> — best quality, needed once you're serious about vocal recording; the interface converts the microphone's analog signal into something your Mac can record and also lets you plug in real instruments (guitar, keyboard line-out).",
    "<b>Importing existing audio (e.g., the source clip you're remixing)</b> — no recording needed; just drag the audio file into your DAW's track area.",
])
add_h2("10.2 Recording an audio track")
add_bullets([
    "Create a new Audio track (not a Software Instrument/MIDI track).",
    "Select your input device (built-in mic, USB mic, or interface) for that track.",
    "Arm the track for recording, put on headphones (to avoid the mic picking up your speakers — this feedback loop is called “monitoring spill”), and press Record.",
    "Speak or play at a normal level and check the track's level meter — it should move comfortably without constantly hitting the red “clipping” zone at the top.",
], numbered=True)
add_warn(
    "If the meter pins red and you hear crackling, your input gain is too high — turn it down on the "
    "interface or in System Settings → Sound → Input before recording again. Clipped audio cannot be "
    "fixed after the fact."
)
add_h2("10.3 Working with a found sample (vocal/choir clip, viral video audio)")
add_p(
    "If your source material is an existing recording rather than something you perform yourself "
    "(as in all three reference videos), simply import the audio file into a track. From here it's "
    "treated exactly like anything you recorded — you can trim it, slice it, and assign pieces to pads, "
    "which is exactly what Chapter 11 covers."
)
add_note(
    "Only use audio you have the rights to use, or that's licensed for remixing — this matters both "
    "legally and, on platforms like YouTube, for whether your finished video can stay monetized or "
    "even stay up."
)

# ============================================================ CHAPTER 10
add_chapter_break(11, "Mapping Pads to Trigger Samples and Loops")
add_p(
    "This is the technique that turns a single imported recording into sixteen playable pieces — the "
    "core trick behind the reference videos' vocal-chop sound."
)
add_h2("11.1 Slice the source")
add_bullets([
    "Import your source sample as an audio clip (Chapter 10.3).",
    "Use your DAW's slicing tool (in Ableton: right-click → “Slice to New MIDI Track”; in Logic: the Audio-to-MIDI / Flex tools; GarageBand: manually split at each phrase with Cmd+T) to break it into individual words or phrases.",
    "Each slice becomes its own short clip or sample.",
], numbered=True)
add_h2("11.2 Lay clips out so pads can reach them")
add_p(
    "Arrange your project on a handful of stacked tracks — for example “Vocal Chops,” “Drums,” "
    "“Bass,” and “FX/Risers” — with one short loop or one-shot sample sitting in a clip slot on each "
    "track. In Ableton's Session View this is literally a grid; in Logic's Live Loops it's the same "
    "idea; in GarageBand you'll trigger regions on the timeline instead, which is more limited but "
    "workable for practice."
)
add_h2("11.3 Point pads at the clips")
add_bullets([
    "Switch the MPK Mini to your “Pads-Triggers” program (Chapter 6.5), with pads in Note Mode.",
    "In the DAW, enable MIDI-mapping for clip launching (Ableton: right-click a clip → “Show Clip in Detail View,” then use the MIDI map button just like Chapter 12's knob mapping, but click a clip slot instead of a knob).",
    "Press each pad once to confirm it triggers the correct clip, working through Bank A then Bank B.",
])
add_figure(dg.pad_bank_diagram(), "Figure 11.1 — A practical starting layout: vocal chops and drums on Bank A, bass and FX on Bank B.")
add_h2("11.4 Set pad sensitivity for consistent triggers")
add_p(
    "In the MPK Mini Editor, set these pads' velocity response to <b>Full Level</b> so a light tap "
    "still plays back at full, consistent volume — you want every vocal chop and drum hit to land at "
    "the same loudness regardless of exactly how hard you tapped the pad."
)
add_note(
    "Practice triggering pads 1→8 in order, slowly, until you can do it without looking — this is "
    "the single most useful physical skill for the live-performance chapters later."
)

# ============================================================ CHAPTER 11
add_chapter_break(12, "Mapping Knobs for Live Mixing")
add_p(
    "Knobs are what make a performance look (and sound) live: sweeping a filter into a drop, easing "
    "a reverb in on a build, or pulling a fader down for a breakdown, all while the track keeps playing."
)
add_h2("12.1 Default CC numbers (MPK Mini mkII/mkIII factory program)")
add_table(
    [
        ["Knob", "Default CC", "Recommended mix assignment"],
        ["K1", "CC 1 (Mod Wheel)", "Master low-pass filter cutoff — the classic “sweep into the drop”"],
        ["K2", "CC 2", "Vocal/sample track volume — ride it against the beat"],
        ["K3", "CC 3", "Reverb or delay send on vocal chops — add space on builds"],
        ["K4", "CC 4", "High-pass filter on drums — thin the beat out in breakdowns"],
    ],
    [0.7 * inch, 1.3 * inch, 3.5 * inch]
)
add_h2("12.2 How to map a knob, step by step (Ableton Live example)")
add_bullets([
    "Click the MIDI map button in the top-right corner of the Live window (the screen border turns blue/purple).",
    "Click the on-screen control you want it to control — for example, an Auto Filter device's Frequency knob.",
    "Turn the physical MPK Mini knob; Live links the two automatically and shows the mapping in a panel on the left.",
    "Repeat for each knob you want active, then click the MIDI map button again to exit mapping mode.",
    "Save the project as a template so this mapping is ready every time you start a new remix.",
], numbered=True)
add_h2("12.3 The same idea in GarageBand or Logic")
add_p(
    "Both support “Learn MIDI Assignment” (Logic: Control-click a knob on screen → “Learn Assignment,” "
    "then move the MPK Mini knob) for mapping a physical knob to a software control such as a Smart "
    "Control or plugin parameter."
)
add_note(
    "If a knob feels reversed or jumps unevenly, check its range and curve in the MPK Mini Editor — "
    "set it to the full 0–127 range with a linear curve to avoid dead zones at either end of the sweep."
)

# ============================================================ CHAPTER 12
add_chapter_break(13, "Mixing Fundamentals for Complete Beginners")
add_p(
    "“Mixing” means adjusting the relative volume, tone, and space of each track so the whole thing "
    "sounds clear and intentional rather than muddy. This chapter introduces the four tools you'll use "
    "constantly: volume, EQ, compression, and reverb/delay sends."
)
add_h2("13.1 Volume and gain staging")
add_p(
    "Before reaching for any effect, get relative volumes right first. Keep individual track peaks "
    "around −6 dB (decibels) on the meter so there's headroom before anything distorts, and only add a "
    "limiter to the master bus at the very end, to catch occasional peaks — not to make the track "
    "“loud.”"
)
add_h2("13.2 EQ (equalization)")
add_p(
    "An EQ boosts or cuts specific frequency ranges — bass, midrange, treble — on a track. The two "
    "moves you'll use most: cutting frequencies where two tracks compete (so they don't fight for the "
    "same space) and gently boosting a frequency that helps a sound cut through."
)
add_figure(dg.eq_curve_diagram(), "Figure 13.1 — A simple EQ move: cut around 300–500 Hz to make room for a vocal, then a gentle presence boost around 3–5 kHz.")
add_bullets([
    "EQ-cut your new drums/bass around 300 Hz–3 kHz, where vocal samples usually live, so the original hook stays clear.",
    "High-pass (cut everything below) non-bass elements — drums, FX, vocal chops — around 80–100 Hz, keeping low end clean for just the bass and kick.",
])
add_h2("13.3 Compression")
add_p(
    "A compressor automatically turns down a sound when it gets loud, then lets it back up — it "
    "evens out a performance and, used on multiple tracks together (“sidechain” compression), can make "
    "a bass duck slightly every time the kick hits, which is the “pumping” feeling in most club remixes."
)
add_h2("13.4 Reverb and delay (sends)")
add_p(
    "Reverb simulates a room or space; delay repeats a sound like an echo. Both are usually used as a "
    "<b>send</b> — a shared effect that multiple tracks can dial in different amounts of, rather than a "
    "separate copy on every track — which is exactly why Chapter 12 maps a knob to a reverb send rather "
    "than a literal reverb amount per track."
)
add_h2("13.5 A practical beginner checklist, in order")
add_bullets([
    "Set rough volume balance first — bass and drums roughly even, vocal/sample clearly audible on top.",
    "EQ to remove clashes (Section 12.2) before reaching for anything fancier.",
    "Add sidechain compression on the bass against the kick for the drop sections.",
    "Add a touch of reverb/delay to glue the dry original sample into the new backing track.",
    "Recheck overall volume on headphones <i>and</i> on a phone speaker or laptop speakers — the mix should still make sense on a small speaker.",
], numbered=True)
add_note(
    "Mix at a moderate volume, not loud. Loud mixes trick your ears into thinking bass and treble are "
    "balanced when they aren't — turn it down to roughly conversational level for the most reliable "
    "mixing decisions."
)

# ============================================================ CHAPTER 13
add_chapter_break(14, "Building a Layered Remix, Start to Finish")
add_p("This chapter ties Chapters 8–12 together into the actual recipe behind all three reference videos.")
add_figure(dg.build_arrangement_timeline_diagram(), "Figure 14.1 — The typical shape of a club/dance remix arrangement.")
add_bullets([
    "<b>Find and clean the source.</b> Isolate the vocal/instrumental hook (Chapter 10.3); trim silence and normalize its level.",
    "<b>Set the tempo and key.</b> Time-stretch or pitch the source to a round tempo — 124–128 BPM is typical for club remixes — and a key that suits a simple bassline.",
    "<b>Lay the foundation loop.</b> Program or play a kick/bass/clap loop on the keys and Bank A pads (Chapter 8); record it into a loop clip.",
    "<b>Chop and place the hook.</b> Slice the vocal and assign pieces to pads (Chapter 11), then record yourself triggering them in time over the foundation loop.",
    "<b>Add movement.</b> Layer in hi-hats, percussion, and a riser/FX pad for transitions between sections (intro → build → drop → breakdown → outro).",
    "<b>Perform the mix live.</b> With knobs mapped per Chapter 12, record a pass where you ride the filter into the drop and pull levels down for the breakdown — this live-mixed take is often what ends up in the final video.",
    "<b>Mix properly.</b> Apply Chapter 13's checklist to the full arrangement.",
    "<b>Bounce.</b> Render (“export” or “bounce”) the finished arrangement to a single audio file before moving to video (Chapters 15–16).",
], numbered=True)
add_note(
    "Build the arrangement across several short sessions rather than one long sitting — fresh ears "
    "catch balance problems that tired ears stop noticing."
)

# ============================================================ CHAPTER 14
add_chapter_break(15, "Live-Looping Performance Technique")
add_p(
    "The on-camera “magic” in these videos is mostly a live performance over a mostly pre-built "
    "arrangement, captured in as few takes as possible."
)
add_bullets([
    "Build the full arrangement first (Chapter 14) so you're not creating from nothing on camera — you're performing a piece you already know works.",
    "Mute or empty out the specific clips you want to trigger live on camera, leaving the rest of the arrangement playing in the background, so your live pad presses are the visible/audible “performance” layer.",
    "Rehearse the pad sequence on its own, with no recording running, until it's muscle memory — you should be able to trigger the right pad without looking down.",
    "Use the joystick for small pitch bends or filter wiggles (Chapter 7.4) to add visible, audible character to the performance — but remember to recenter it afterward.",
    "Do several full run-throughs before recording “for real” — the best take is usually the one where the live mixing (Chapter 12) lands tightest with the beat, which only comes with repetition.",
])
add_note(
    "It's normal for the first 5–10 takes of a live-looped section to feel clumsy. This is rehearsal, "
    "not failure — the reference videos represent the one take out of many that worked."
)

# ============================================================ CHAPTER 15
add_chapter_break(16, "Syncing Your Performance to Video")
add_p(
    "Once you can perform the remix cleanly, the next step is capturing that performance on camera "
    "and lining the video up exactly with the audio — this is the technical part that makes a "
    "performance video look polished rather than amateur."
)
add_h2("16.1 What you need")
add_bullets([
    "A camera — your phone, a webcam, or your Mac's built-in camera all work for a first attempt.",
    "A way to record your DAW's audio output at the same time as the video (most simply: just record video with the camera's own microphone pointed near your speakers, or run a cable from your interface to the camera's mic input for cleaner sound).",
    "A video editor — iMovie (free, pre-installed on Mac) is enough for this project.",
])
add_h2("16.2 The clap-sync method")
add_p(
    "Professional sets use a clapperboard for exactly this reason: a single sharp sound creates a "
    "visible spike on an audio waveform and a visible motion on video, giving you one unmistakable "
    "point to line both up against."
)
add_bullets([
    "Start your camera recording first.",
    "Start your DAW recording.",
    "Clap once, in view of the camera, right after both are rolling.",
    "Perform your remix (Chapter 15).",
    "Stop both recordings.",
], numbered=True)
add_figure(dg.video_sync_diagram(), "Figure 16.1 — Lining up the clap spike in both the camera audio and the DAW recording.")
add_h2("16.3 Lining them up in iMovie")
add_bullets([
    "Import both the video clip and your final DAW audio bounce (Chapter 14, step 8) into iMovie.",
    "Place the video clip on the timeline, then place the audio clip on the track below it.",
    "Zoom into both waveforms at the clap and drag the audio clip left/right until the clap spikes line up exactly.",
    "Once aligned, mute or delete the camera's own scratch audio track and keep only your clean DAW audio — the camera audio was only ever a sync reference.",
], numbered=True)
add_note(
    "If you don't have a clean way to record camera + DAW audio simultaneously, you can instead "
    "play your finished, bounced track out loud through speakers while filming yourself performing "
    "along to it — then in editing, simply replace the camera's audio entirely with your clean bounce, "
    "synced by ear to your own movements."
)

# ============================================================ CHAPTER 16
add_chapter_break(17, "Exporting and Finishing Your Track and Video")
add_h2("17.1 Bouncing the final audio")
add_bullets([
    "In your DAW, select the full arrangement from the very start to the very end (including a second or two of silence at the tail so reverb tails aren't cut off).",
    "Export/Bounce as a WAV or AIFF file at the highest quality your DAW offers (44.1kHz/24-bit is a safe standard) for editing, and an MP3 copy if you need a smaller file to share quickly.",
])
add_h2("17.2 Finishing the video in iMovie")
add_bullets([
    "Trim the start/end so the video begins right as the music starts (after removing the clap reference, Chapter 16.3).",
    "Add a simple title card if you like — keep it short, it's not the focus.",
    "Export via File → Share → File, choosing 1080p (or your camera's native resolution) at the highest quality setting.",
])
add_h2("17.3 Before you publish")
add_bullets([
    "Watch the full export back once, start to finish, on the device you're most likely to view it on later (phone, if that's where most viewers will be).",
    "Double-check audio and video are still in sync at both the very start and the very end — drift can creep in on longer videos if the export frame rate doesn't match the original footage.",
    "Confirm you have the rights to use your source sample (Chapter 10.3) before uploading anywhere public.",
])

# ============================================================ CHAPTER 17
add_chapter_break(18, "Troubleshooting Common Problems")
add_table(
    [
        ["Problem", "Likely cause", "Fix"],
        ["MPK Mini not detected by Mac", "Loose cable / USB hub", "Plug directly into a Mac USB port; try a different cable"],
        ["Pressing a key makes no sound", "Track not armed, or no instrument loaded", "Arm the track for input; confirm a software instrument is loaded (Ch. 6.4)"],
        ["Knob does nothing in the DAW", "Not yet MIDI-mapped", "Re-do the MIDI map steps in Ch. 12.2"],
        ["Knob “jumps” when turned", "Non-linear curve / wrong range in Editor", "Set knob range to 0–127, linear curve, in MPK Mini Editor"],
        ["Recorded audio is distorted/crackling", "Input gain too high (clipping)", "Lower input gain before recording again (Ch. 10.2) — can't be fixed after"],
        ["Pads trigger the wrong clip", "Bank A/B mismatch, or note numbers changed", "Confirm current bank with the Bank button; re-check program in Editor"],
        ["Video and audio drift out of sync over time", "Mismatched frame rate on export", "Re-export at the same frame rate as the original camera footage"],
        ["Joystick leaves a “stuck” effect on", "Modulation (up/down) doesn't auto-recenter", "Manually push the joystick back to center after use (Ch. 7.4)"],
    ],
    [1.7 * inch, 1.5 * inch, 2.3 * inch]
)

# ============================================================ CHAPTER 18
add_chapter_break(19, "Practice Plan and Quick-Reference Cheat Sheets")
add_h2("19.1 A four-week practice plan")
add_bullets([
    "<b>Week 1 — Foundations:</b> complete setup (Ch. 2–6); record a simple MIDI melody (Ch. 8); record one audio take of your own voice (Ch. 10).",
    "<b>Week 2 — Triggers and mixing controls:</b> chop a sample and map it across 8–16 pads (Ch. 11); map all four knobs to mixer functions (Ch. 12); read through Chapter 13 once fully.",
    "<b>Week 3 — Build a remix:</b> work through the full Chapter 14 recipe with a short (60–90 second) idea, start to finish, including a basic mix pass.",
    "<b>Week 4 — Perform and film:</b> rehearse a live-looped pass (Ch. 15), film and sync it (Ch. 16), and export a finished video (Ch. 17).",
])
add_h2("19.2 Cheat sheet — default knob CC assignments")
add_table(
    [
        ["Knob", "Default CC", "Suggested use"],
        ["K1", "CC 1", "Master filter sweep"],
        ["K2", "CC 2", "Vocal/sample volume"],
        ["K3", "CC 3", "Reverb/delay send"],
        ["K4", "CC 4", "Drum high-pass filter"],
    ],
    [0.7 * inch, 1.1 * inch, 3.7 * inch]
)
add_h2("19.3 Cheat sheet — suggested 16-pad layout")
add_table(
    [
        ["Pad", "Bank A", "Pad", "Bank B"],
        ["1–4", "Vocal/sample chops", "1–2", "Bass loop start/stop"],
        ["5–6", "Kick + clap/snare loop", "3–4", "Riser / sweep FX"],
        ["7–8", "Hi-hat / percussion loop", "5–6", "Drop impact / crash"],
        ["", "", "7–8", "Alternate vocal ad-libs"],
    ],
    [0.6 * inch, 1.9 * inch, 0.6 * inch, 1.9 * inch]
)
add_h2("19.4 Cheat sheet — beginner mixing order")
add_bullets([
    "1. Rough volume balance  →  2. EQ to remove clashes  →  3. Sidechain compression on the drop  →  4. Reverb/delay glue  →  5. Recheck on a small speaker",
])

story.append(Spacer(1, 14))
story.append(HRFlowable(width="100%", thickness=0.5, color=colors.HexColor("#cccccc")))
story.append(Spacer(1, 6))
story.append(Paragraph(
    "Reference videos: “The Shira Choir x The Kiffness – Im Hashem Lo Yivneh Bayis (Psalm 127 Dance Remix)” "
    "(youtube.com/watch?v=EGmXAu8geVg), “The Kiffness – Ievan Polkka ft. Bilal Göregen (Club Remix)” "
    "(youtube.com/watch?v=CAyWN9ba9J8), and “The Kiffness x Ognjen & Sinisa – Insomnia (Balkan Club Remix)” "
    "(youtube.com/watch?v=hVJtPuuQK_s). This guide describes general production technique inspired by the "
    "style of these videos; it is not affiliated with or endorsed by The Kiffness.",
    caption
))


def make_canvas_factory():
    from reportlab.pdfgen import canvas as _canvas

    class NumberedCanvas(_canvas.Canvas):
        def showPage(self):
            self.setFont("Helvetica", 8)
            self.setFillColor(colors.HexColor("#999999"))
            self.drawRightString(560, 25, str(self._pageNumber))
            _canvas.Canvas.showPage(self)

    return NumberedCanvas


doc = SimpleDocTemplate(
    OUT, pagesize=letter,
    topMargin=0.75 * inch, bottomMargin=0.7 * inch,
    leftMargin=0.85 * inch, rightMargin=0.85 * inch,
    title="Akai MPK Mini Mixing, Recording & Video-Sync Manual",
    author="Generated for Alexy",
)
doc.build(story, canvasmaker=make_canvas_factory())
print("done, pages built")
