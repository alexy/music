---
title: Akai MPK Mini MK3 and APC40 MK2 Loop Lab
subtitle: Controller workflows for MPK-only, APC-only, and combined GarageBand/Ableton rigs
---

# Start Here

This book is for learning the Akai MPK mini MK3 and Akai APC40 MK2 as practical
performance controllers, not as mysterious USB accessories. The goal is simple:
plug them into a Mac, understand what each surface is good at, and use either
one, or both together, to make short loops in GarageBand and Ableton Live.

The guide is grounded in these study references:

- Smith's Covers, "Gorillaz - Clint Eastwood (Akai MPK Mini MK3 Cover)":
  <https://www.youtube.com/shorts/d_VK75O173w>
- inMusic Brands Support, "Akai Pro MPK Mini Play MK3 | Onboard Features &
  Standalone Use": <https://www.youtube.com/watch?v=QTLGsW9tlw4>
- IxStage, "50 Cent - In Da Club / AKAI MPK MINI MK3 COVER":
  <https://youtu.be/awnLq-c5N8M>
- Dezavi Productions, "AKAI MPK mini MK3 Tutorial Beginners":
  <https://youtu.be/sM6RY5s4e8o>
- Autumn Gard, "AKAI MPK MINI PLAY MK3 TUTORIAL WITH ABLETON LIVE":
  <https://youtu.be/ckAbhrpB89w>
- Matthew Stratton, "AKAI MPK MINI MK3 Complete Setup":
  <https://youtu.be/FqU2F31dJiw>
- Matthew Stratton, "AKAI MPK MINI MK3 - Ableton Live Setup Tutorial":
  <https://youtu.be/mQBsBtT1CHY>

Those videos teach three different things. The cover videos show what the MPK
looks like when someone has already mapped it and can perform confidently. The
beginner videos explain the controls: pads, banks, note repeat, arpeggiator,
octaves, knobs, and software setup. The Ableton tutorial shows the same hardware
inside a clip-based DAW, where pads and knobs become a live-looping surface. The
APC40 MK2 extends that idea: it is less of a piano-style instrument and more of
a dedicated Ableton session, clip, mixer, and performance surface.

This book does not copy the source music, video frames, or transcripts. It turns
the observed techniques into original practice routines you can do with your own
sounds.

# The Mental Model

The MPK mini and APC40 both send MIDI. MIDI is not audio. When you press a key,
tap a pad, move a joystick, launch a clip, move a fader, or turn a knob, the
controller sends a message such as "note C2 on," "controller 74 moved," "clip
launch pressed," or "pitch bend up." GarageBand or Ableton receives that message
and decides what sound or command it should control.

Think of the MPK mini as four instruments in one:

| Surface | What it feels like | What it sends | Typical job |
|---|---|---|---|
| Keys | tiny keyboard | MIDI notes with velocity | bass, chords, lead, melody |
| Pads | finger drums | MIDI notes, CC, or program changes | drums, samples, clip launch |
| Knobs | eight rotary controls | MIDI CC values | filter, volume, pan, sends, effects |
| Buttons/joystick | performance controls | transport, octave, arp, bend, mod | range, timing, expression |

Think of the APC40 MK2 as four Ableton performance zones:

| Surface | What it feels like | What it sends | Typical job |
|---|---|---|---|
| Clip grid | live-loop board | clip/scene launch and status feedback | start, stop, record, and combine clips |
| Faders | small mixer | MIDI CC values | track volume, sends, and performance fades |
| Device knobs | macro controls | MIDI CC values | filter, reverb, delay, effect macros |
| Transport/crossfader | DJ/live set controls | DAW control messages | play, stop, record, cue, transition |

The important beginner lesson is that the same physical pad can do different
things in different modes. In Drum or Notes mode it sends a note. In CC mode it
sends a control-change message. In Program Change mode it changes presets or
patches. In Ableton or GarageBand scripts on newer models, pads can also select
tracks, arm tracks, mute, solo, launch clips, or stop clips.

The second beginner lesson is role separation. The MPK is better when you need
to play notes, finger-drum, use note repeat, or shape a synth part from the same
small keyboard. The APC40 MK2 is better when you need to launch clips, mix
tracks, arm/stop parts, and move through an Ableton session without staring at
the computer.

# Identifying Your MPK Mini

Your photo shows the familiar MPK mini layout: 25 mini keys, eight MPC-style
pads, eight knobs, octave buttons, arpeggiator, note repeat, full level, and a
small display/joystick area depending on generation. You believe it is an MK3,
so the examples below use MK3 language. If a label on your physical unit differs
from a tutorial video, use this translation:

| If the video says | On your controller look for | Meaning |
|---|---|---|
| Bank A/B | Bank A/B, Pads A/B, or Pad Bank | Switch pads from notes 1-8 to 9-16 |
| Full Level | Full Level | Pads always send velocity 127 |
| Note Repeat | Note Repeat | Held pads repeat in time |
| Arp | Arpeggiator or ARP On/Off | Held keys become rhythmic patterns |
| Tap Tempo | Tap Tempo | Sets internal arp/note-repeat tempo |
| Prog Select | Program Select or Program | Recall saved controller mappings |
| CC | CC or Control Change | Pads send control messages instead of notes |
| Prog Change | Program Change | Pads send patch-change messages |
| Joystick/X-Y | X-Y controller, joystick, pitch/mod | Pitch bend and modulation/expression |

MK3 and MPK Mini Play MK3 tutorials overlap, but the Play model has internal
sounds and a speaker. A plain MK3 relies on the Mac for sound. When a tutorial
says "internal sound," translate that to "software instrument in GarageBand or
Ableton" unless your unit is the Play version.

# Identifying Your APC40 MK2

The APC40 MK2 is designed around Ableton Live. Its main surface is the clip grid:
five rows by eight columns for launching clips and scenes, with track controls,
faders, knobs, transport buttons, and a crossfader around it. Unlike the MPK, it
does not have piano keys and is not the obvious first choice for playing a bass
line or melody from scratch.

Use this translation when moving between generic Ableton tutorials and the
APC40 MK2:

| If the tutorial says | On the APC40 MK2 look for | Meaning |
|---|---|---|
| Clip slot | 5x8 clip grid button | Launch or record one clip |
| Scene launch | right-side scene buttons | Launch a whole row of clips |
| Track volume | vertical fader | Mix one track louder or softer |
| Track activator | track on/off button | Mute or unmute the track |
| Solo/Cue | Solo/Cue buttons | Isolate or monitor a track |
| Device controls | eight device control knobs | Move macros or device parameters |
| Sends | send control mode/knobs | Add delay, reverb, or other return effects |
| Crossfader | bottom horizontal fader | Blend between A/B-assigned tracks |

GarageBand does not have Ableton's clip-launching model, so the APC40 MK2 is
much less natural there. You may be able to map some controls as generic MIDI,
but the APC's main value appears in Ableton Live.

# Controller Combinations

Use one of these three rigs depending on what you are trying to practice. Do not
try to make both controllers do everything. A clean division of jobs is easier
to learn and easier to film.

## APC Only

Use APC-only when you already have loops, samples, or MIDI clips prepared and
you want to practice arranging, mixing, muting, launching, and performing.

Best in Ableton Live:

| APC control | Job |
|---|---|
| Clip grid | launch drums, bass, chords, lead, and FX clips |
| Scene buttons | move between intro, groove, break, drop, and ending |
| Faders | balance track volumes while the loop plays |
| Device knobs | open filters, increase reverb, or move effect macros |
| Track stop/activator | create breaks and dropouts |
| Crossfader | blend between two groups of tracks |

APC-only starter set:

1. Create eight Ableton tracks: drums, percussion, bass, chords, lead, vocal
   chop, FX, and master resample.
2. Put one to five clips on each track.
3. Name the scenes Intro, Groove, Break, Drop, and End.
4. Use the APC grid to launch scenes first.
5. Then launch individual clips to make variations.
6. Use faders for volume moves before mapping any fancy effects.

APC-only is not ideal in GarageBand. If GarageBand is the DAW, treat the APC as
an optional MIDI control surface for a few mapped parameters, not as the center
of the workflow.

## MPK Only

Use MPK-only when you need to write or record the musical material yourself:
drums, bass, chords, melodies, arpeggios, note repeat parts, and simple knob
automation.

Best in GarageBand or Ableton:

| MPK control | Job |
|---|---|
| Keys | bass lines, chords, lead hooks |
| Pads | drums, samples, clip launches, or one-shot FX |
| Knobs | filter, reverb, delay, volume, pan, or macros |
| Note Repeat | hats, rolls, and rhythmic fills |
| Arpeggiator | pluck patterns and repeating chord textures |
| Joystick | pitch bends and modulation gestures |

MPK-only starter loop:

1. Record drums with pads.
2. Record bass on the lower keys.
3. Record chords in the middle octave.
4. Record a hook in the upper octave.
5. Map K1 to filter cutoff and K8 to reverb or delay.
6. Film the performance from above so pads, keys, and knobs are visible.

MPK-only is the best first setup for GarageBand because GarageBand understands
notes and software instruments more naturally than it understands clip-launch
hardware.

## Both

Use both controllers when you want the MPK to create or perform parts and the
APC40 MK2 to arrange, launch, and mix those parts. This is the most powerful
Ableton setup because each controller keeps its natural job.

Recommended division:

| Job | Use the MPK mini MK3 | Use the APC40 MK2 |
|---|---|---|
| Drums | finger-drum or note-repeat hats | launch saved drum clips |
| Bass/chords/lead | play notes and record clips | launch, stop, and arrange clips |
| Effects | quick knob gestures | macro banks, sends, fades, crossfader |
| Song form | perform fills and hooks | launch scenes and create transitions |
| Mixing | emergency knob mapping | faders, mutes, solo/cue, track balance |

Combined Ableton starter workflow:

1. Connect both controllers before opening Ableton Live.
2. In Preferences > Link/Tempo/MIDI, enable Track for the MPK input.
3. Enable Remote for the MPK input if you want manual knob or pad mapping.
4. Select the APC40 MK2 as an Ableton control surface if Live does not auto-detect it.
5. Use the MPK to record drums, bass, chords, and lead into clips.
6. Use the APC grid to launch those clips and scenes.
7. Use APC faders for track volume and APC device knobs for macro changes.
8. Keep the MPK pads free for drums/fills instead of duplicating the APC clip grid.

Combined GarageBand workflow is possible but limited. Use the MPK as the main
GarageBand instrument, and only map APC controls if a specific GarageBand Smart
Control or mixer move is worth the setup time.

# The Keys

The 25 keys are velocity-sensitive. Press softly and the DAW receives a softer
note. Press harder and the DAW receives a louder/brighter note if the instrument
responds to velocity.

The keys are small, so use them deliberately:

| Job | Good beginner range | Practice pattern |
|---|---|---|
| Bass | lower octave | root, fifth, octave |
| Chords | middle octave | two-note shells or triads |
| Lead | upper octave | short repeated hook |
| Arpeggio | any held chord | hold three notes with ARP on |

## Octave Buttons

The Octave Down and Octave Up buttons shift the keyboard range. If the bass is
too high, press Octave Down once. If the lead is buried, press Octave Up once.
Press both octave buttons together on many MPK models to return to center.

Beginner rule: record bass one octave down, chords at center, and lead one
octave up. Do not chase every octave while recording. Choose the range first,
then play.

## Key Exercise: One-Bar Bass

Set a GarageBand or Ableton software instrument to a simple synth bass.

1. Set tempo to 92 BPM.
2. Press Octave Down once.
3. Play C, G, C, rest.
4. Record one bar.
5. Quantize to 1/8 notes.
6. Loop it for four bars.

Now change only the sound. Try synth bass, electric bass, organ bass, and
sub-bass. The MIDI notes stay the same while the instrument changes.

# The Pads

The eight pads are the fastest way to feel the MPK as an MPC-style performance
surface. They are usually velocity-sensitive. A soft tap sends a lower velocity;
a hard hit sends a higher velocity.

## Pad Banks

Bank A gives eight pads. Bank B gives eight more. Together they act like a
sixteen-pad grid.

| Bank | Beginner mapping |
|---|---|
| A Pad 1 | Kick |
| A Pad 2 | Snare or clap |
| A Pad 3 | Closed hat |
| A Pad 4 | Open hat or percussion |
| A Pad 5 | Vocal chop or sample stab |
| A Pad 6 | Extra percussion |
| A Pad 7 | Riser or transition |
| A Pad 8 | Stop, mute, or crash |
| B Pads 1-8 | alternate samples, fills, or second drum kit row |

## Full Level

Full Level makes every pad hit send maximum velocity. Use it when you want even
drums and are tired of weak snare hits. Turn it off when you want expressive
finger drumming.

Practice:

1. Choose a drum kit.
2. Turn Full Level off and play kick-snare-hat.
3. Turn Full Level on and repeat.
4. Decide which version feels better for the loop.

For beginner loops, use Full Level while learning timing, then turn it off when
you want musical dynamics.

## Note Repeat

Note Repeat retriggers a held pad at the current tempo and division. It is for
hi-hats, rolls, tambourines, and trap-style repeated hits. In the beginner MK3
tutorials, this is usually demonstrated with pads, not keys.

Practice:

1. Put closed hat on Pad 3.
2. Turn Note Repeat on.
3. Hold Pad 3 while the project plays.
4. Try 1/8, 1/16, and 1/16 triplet divisions.
5. Record the one that grooves.

If Note Repeat is late or drifting, check whether the MPK is using internal
clock or external clock from the DAW. For tight DAW loops, external sync is
usually the cleanest path when your model/software supports it.

# The Knobs

The eight knobs are assignable MIDI controls. In tutorials they are often called
Q-Link knobs or assignable encoders. They do not make sound by themselves. They
move a parameter inside the current instrument, effect, mixer, or DAW script.

Use this default learning map:

| Knob | GarageBand Smart Control | Ableton Device/Mixer job | What you hear |
|---|---|---|---|
| K1 | cutoff or tone | filter cutoff | darker to brighter |
| K2 | resonance | filter resonance | sharper filter peak |
| K3 | attack | envelope attack | pluck to swell |
| K4 | release | envelope release | short to long tail |
| K5 | track volume | mixer volume | quiet to loud |
| K6 | pan | mixer pan | left to right |
| K7 | echo/delay send | delay send | dry to echo |
| K8 | reverb send | reverb send | close to spacious |

## GarageBand Knob Reality

GarageBand does not give the older MK3 the same deep control-script behavior
that newer MPK mini IV guides describe. With a plain MK3, you usually use MIDI
Learn or Smart Controls when available. The practical workflow is:

1. Select a software instrument track.
2. Open Smart Controls.
3. Choose the control you want to move.
4. Use MIDI Learn if GarageBand exposes it for that control.
5. Turn the MPK knob.
6. Test that the on-screen knob moves.

If the knob does not map, do not panic. Record the MIDI notes first, then use
GarageBand's on-screen automation for the sound change. The musical idea matters
more than proving every knob works on day one.

## Ableton Knob Reality

Ableton is friendlier for manual mapping:

1. Open Preferences > Link/Tempo/MIDI.
2. Enable Track and Remote for the MPK input.
3. Click MIDI Map Mode.
4. Click the Ableton parameter.
5. Turn the MPK knob.
6. Exit MIDI Map Mode.

Start with K1 mapped to Auto Filter frequency and K8 mapped to Reverb dry/wet.
That gives you the two most obvious performance moves: open the sound and push
it into space.

# Arpeggiator

The arpeggiator belongs to the keys. Hold a chord and the MPK turns it into a
pattern. It can run up, down, in order, randomly, or across multiple octaves
depending on settings.

Beginner settings:

| Parameter | Starting value | Why |
|---|---|---|
| Tempo/clock | DAW sync or 92 BPM internal | keeps loops in time |
| Division | 1/8 | clear enough to hear |
| Mode | Up | predictable |
| Octave | 1 | avoids chaos |
| Latch | Off at first | stops when you release |
| Swing | 50% | straight grid |

Exercise:

1. Choose a pluck or bell sound.
2. Turn ARP on.
3. Hold C minor: C, Eb, G.
4. Record two bars.
5. Change only the division to 1/16.
6. Record a second pass and compare.

Use ARP for texture. Do not let it become a substitute for learning the hook.

# Joystick, Pitch, and Modulation

The MK3 joystick is usually pitch bend on one axis and modulation on another.
Pitch bend changes note pitch temporarily. Modulation often adds vibrato,
filter movement, or another instrument-specific effect.

Practice:

1. Load a lead synth.
2. Hold one note.
3. Move the joystick left/right slowly for pitch bend.
4. Move it up/down for modulation.
5. Record a short lead phrase with one bend at the end.

Use the joystick like punctuation. One bend can sound expressive. Constant bend
movement often sounds accidental.

# Programs and Presets

A program is a saved controller mapping: which MIDI notes pads send, what CC
numbers knobs send, what channel the keys use, and how the performance controls
behave. The Matthew Stratton setup video is useful because it emphasizes the
registration/software-manager path: install the supporting software, download
bundled instruments, and understand where the MPK editor or software manager
fits.

For this book, use three beginner programs:

| Program | Purpose |
|---|---|
| Program 1: Loop Lab | keys, pads, knobs all on one normal MIDI channel |
| Program 2: Drum Practice | pads mapped for a 16-pad drum rack |
| Program 3: Performance | pads for samples, keys for lead/bass, knobs for filter/effects |

If you are unsure, stay on Program 1. Most beginner frustration comes from
accidentally changing programs or modes and then wondering why the DAW no longer
responds the same way.

# GarageBand Loop Lab

GarageBand is the simplest place to start because it opens quickly and has
friendly built-in sounds.

## Setup

1. Connect the MPK by USB.
2. Open GarageBand.
3. Create an Empty Project.
4. Add a Software Instrument track.
5. Play the keys. You should hear the default instrument.
6. Open Musical Typing only if you need a comparison; the MPK should be the real
   input.

If GarageBand does not hear the MPK, open GarageBand > Settings > Audio/MIDI and
reset MIDI drivers. On macOS you can also remove and reconnect the device in
Audio MIDI Setup.

## Four-Track Starter Loop

Set tempo to 92 BPM and make a four-bar cycle.

| Track | GarageBand patch | MPK control | Part |
|---|---|---|---|
| 1 | Drum Kit or Beat Machine | Pads 1-4 | kick, snare, hat |
| 2 | Synth Bass | lower keys | root/fifth bass |
| 3 | Classic Electric Piano | middle keys | two-note chords |
| 4 | Lead Synth or Organ | upper keys + joystick | short hook |

### Track 1: Drums

1. Select the drum track.
2. Turn Full Level on.
3. Record Pad 1 on beats 1 and 3.
4. Record Pad 2 on beats 2 and 4.
5. Add Pad 3 as eighth-note hats.
6. Quantize to 1/16 if needed.

### Track 2: Bass

1. Select a bass patch.
2. Press Octave Down once.
3. Record C, G, C, rest.
4. Keep the bass shorter than the drum loop.

### Track 3: Chords

1. Select an electric piano or pad.
2. Return octave to center.
3. Record C minor for two beats, Ab major for two beats.
4. Use only two or three notes per chord.

### Track 4: Hook

1. Select a lead or organ sound.
2. Press Octave Up once.
3. Record a five-note hook.
4. Use the joystick on the last note only.

## GarageBand Loops and Cycle

GarageBand's cycle region lets you loop a section while recording. Turn cycle on,
drag the yellow cycle bar over four bars, and record multiple passes until the
take feels right.

Beginner loop rules:

1. Record only one job per track.
2. Fix timing with quantize after the take.
3. Duplicate good regions instead of replaying everything.
4. Use automation after the musical parts are stable.

# Ableton Live Loop Lab

Ableton Live is built for clips, scenes, and looping. The MPK feels more like a
performance controller here because Ableton can map pads and knobs directly.

## Setup

1. Connect the MPK by USB. If you are using the APC40 MK2 too, connect it
   before opening Ableton.
2. Open Ableton Live or Live Lite.
3. Open Preferences > Link/Tempo/MIDI.
4. In MIDI Ports, enable Track for the MPK mini input. This lets pads and keys
   play instruments.
5. Enable Remote for the MPK mini input if you want knobs or pads to control
   Ableton parameters through MIDI mapping.
6. If Live offers MPK mini MK3 in Control Surface, select it, then choose the
   MPK mini input and output. If Live fills those in automatically, leave them.
7. On the controller, use Program Select to choose the Ableton Live program if
   your MPK already has one loaded.
8. Enable Sync on the MPK output if you want Ableton to send clock for
   arpeggiator or note repeat.
9. If Live does not auto-detect the APC40 MK2, choose it in Control Surface and
   set the APC input and output ports. Its clip grid, faders, and device
   controls should follow the selected Ableton session area.

If you are using a newer MPK mini IV, Akai's Ableton guide describes selecting
the MPK mini IV control surface and DAW port. For MK3, the reliable beginner
path is simpler: Track on for notes, Remote on for mapping, Sync on only when
you need tempo sync.

Matthew Stratton's MK3 Ableton setup video is the most directly relevant
Ableton reference for this book because it shows the exact MK3 checklist:
confirm pads and keys first, map an encoder to a device parameter, open
Link/MIDI preferences when something does not respond, turn on Track for notes,
turn on Remote for encoder mapping, select the MPK mini MK3 control surface when
available, and use Sync only when you want tempo-locked Note Repeat.

## Four-Clip Starter Set

Create four MIDI tracks for MPK-only practice:

| Track | Ableton device | MPK control | Clip length |
|---|---|---|---|
| Drums | Drum Rack | Pads | 1 or 2 bars |
| Bass | Analog, Drift, or Wavetable bass | keys | 2 bars |
| Chords | Electric, Piano, or Pad | keys | 4 bars |
| Lead | synth lead | keys + joystick | 4 bars |

For APC-only or combined practice, keep those four tracks and add four more:

| Track | Ableton device/audio | APC job | Clip role |
|---|---|---|---|
| Percussion | Drum Rack or audio loops | clip launch + fader | extra groove |
| Vocal Chop | Simpler or audio clips | clip launch | hook/stab |
| FX | risers, impacts, noise | scene transitions | build and release |
| Return/Master | delay, reverb, filter macros | knobs/crossfader | performance movement |

## Drum Rack Mapping

1. Load Drum Rack.
2. Drop Kick, Snare, Closed Hat, and Open Hat into the first four cells.
3. Tap Pad 1. If it does not hit the kick, move the sample to the pad's incoming
   note or remap the pad with the MPK editor.
4. Record a one-bar clip.
5. Turn on overdub and add hats.

## Knob Mapping

1. Put Auto Filter after the lead instrument.
2. Enter MIDI Map Mode.
3. Click Auto Filter Frequency.
4. Turn K1.
5. Click Auto Filter Resonance.
6. Turn K2.
7. Exit MIDI Map Mode.
8. Record automation while the clip plays.

If the encoders do not move anything, re-open Preferences > Link/Tempo/MIDI and
check Remote on the MPK input. Track lets notes play instruments; Remote lets
controls map to Ableton parameters.

## Clip Launch With Pads

Older MK3 units do not automatically become an Ableton clip grid unless you use
a script or manual mapping. You can still make a useful setup:

1. Enter MIDI Map Mode.
2. Click the first drum clip launch button.
3. Tap Pad 5.
4. Click the bass clip launch button.
5. Tap Pad 6.
6. Click the chord clip launch button.
7. Tap Pad 7.
8. Click Stop All Clips or a track stop button.
9. Tap Pad 8.

Now Pads 1-4 can stay drums, while Pads 5-8 launch or stop clips.

## Sync Note Repeat to Live

To make Note Repeat follow Ableton's tempo:

1. In Ableton Preferences > Link/Tempo/MIDI, turn Sync on for the MPK output.
2. On the MPK, open the Note Repeat or clock setting.
3. Set the clock source to external if your program exposes that option.
4. Start Live playback.
5. Hold a hat pad with Note Repeat on.

If repeat only works when Live is playing, that is expected with external sync.
The MPK is waiting for Live's clock.

# Performance Studies

## Clint Eastwood-Style Hook

The Smith's Covers Short shows the MPK as a miniature performance station:
simple lead phrase, low anchor notes, and a middle pad section.

Practice version:

1. Use an organ, melodica, or nasal synth lead.
2. Map drums to Pads 1-4.
3. Map a vocal/sample stab or effect to Pad 5.
4. Play the hook in one octave.
5. Move to the pads for a short fill.
6. Return to the hook.

Do not start with the full song. Start with one hook, one pad fill, and one
ending.

## In Da Club-Style Cover

The IxStage performance reference is useful because it treats the MPK as a
cover instrument: keys carry the riff and pads can handle drums or samples.

Practice version:

1. Find the lowest note of the riff.
2. Put that note under your left hand.
3. Put the answer notes under your right hand.
4. Use Pad 1 for kick and Pad 2 for clap.
5. Record the riff first, then drums.

## Beginner MK3 Control Study

The Dezavi Productions tutorial is the core beginner-control study: pads,
pressure, bank switching, full level, note repeat, octave shifting, arpeggiator,
and knobs.

Practice checklist:

1. Play all eight pads softly and loudly.
2. Turn Full Level on and repeat.
3. Switch Bank A/B and repeat.
4. Turn Note Repeat on and hold a hat pad.
5. Turn ARP on and hold a triad on the keys.
6. Move every knob while watching the DAW.
7. Move the joystick while holding a lead note.

# Troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| Keys play but pads do nothing | drum kit expects different MIDI notes | move samples, change pad notes, or use Drum Rack learn |
| Pads play but velocity is uneven | Full Level off | turn Full Level on while practicing |
| Note Repeat is not in time | internal clock differs from DAW tempo | use external sync or tap tempo carefully |
| Knobs do not move anything | not mapped | use MIDI Learn or Ableton MIDI Map Mode |
| GarageBand hears no MIDI | MIDI driver/session stale | reset MIDI drivers or reconnect in Audio MIDI Setup |
| Ableton records notes but mapping fails | Remote disabled | enable Remote for the MPK input |
| Arpeggiator keeps playing | latch on | turn latch off or stop the arpeggiator |
| Wrong octave | octave shifted | press both octave buttons or return to center |

# Thirty-Day Practice Plan

| Days | Focus | Result |
|---|---|---|
| 1-3 | Keys and octaves | one bass loop |
| 4-6 | Pads and Full Level | one drum loop |
| 7-9 | Note Repeat | hats and rolls in time |
| 10-12 | Knobs | filter and reverb automation |
| 13-15 | Arpeggiator | one pluck pattern |
| 16-18 | GarageBand four-track loop | drums, bass, chords, hook |
| 19-21 | Ableton four-clip set | clips and Drum Rack |
| 22-24 | APC-only launching | scenes, clip grid, faders, and mutes |
| 25-27 | Combined MPK + APC performance | MPK records parts, APC launches and mixes |
| 28-30 | Film and revise | one shareable top-down MPK video |

# Final Project

Make a 60-second loop video in one of the three controller combinations.

APC-only version:

1. Start with an Ableton set that already has clips prepared.
2. Launch the intro scene.
3. Bring in drums, bass, chords, lead, and FX from the APC grid.
4. Use faders for the main volume moves.
5. Use device knobs or sends for one filter/reverb build.
6. End by launching an ending scene or stopping tracks cleanly.

MPK-only version:

1. Start with the controller visible.
2. Record drums with pads.
3. Add bass with lower keys.
4. Add chords with middle keys.
5. Add a hook with upper keys.
6. Turn K1 for a filter opening.
7. Use K8 for reverb on the final phrase.
8. End with Pad 8 as a crash, mute, or stop.

Combined version:

1. Start with both controllers visible.
2. Use the MPK to record or perform drums, bass, chords, and hook clips.
3. Use the APC to launch scenes and stop tracks.
4. Use APC faders for the big mix moves.
5. Use MPK note repeat or joystick for a visible performance moment.
6. Use APC device knobs or sends for the final transition.
7. End with the APC scene/stop controls, not a mouse click.

The finished video should prove that you know what every surface does. It does
not need to be complicated. A clean four-track loop is better than a crowded
arrangement where the controller work is hidden.
