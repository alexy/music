---
title: Make Remix Videos With an Akai MPK mini
subtitle: A beginner manual for Kiffness-style video remixes on Mac
---

# Start Here: What You Are Learning

You want to make videos in the spirit of The Kiffness: take a memorable source
clip, find the musical hook inside it, and build a funny, tight, danceable
arrangement around it. The Akai MPK mini is a good controller for learning this
because it gives you keys, pads, knobs, and simple performance controls in one
small desk instrument.

This manual assumes you are new to the MPK, MIDI, Mac audio, recording,
mixing, syncing to video, and DAW workflow. It explains the pieces from zero
and then turns them into a practice system.

The three reference videos for study are:

- The Shira Choir x The Kiffness - Im Hashem Lo Yivneh Bayis (Psalm 127 DANCE REMIX):
  <https://www.youtube.com/watch?v=EGmXAu8geVg>
- The Kiffness - Ievan Polkka ft. Bilal Goregen (Club Remix):
  <https://www.youtube.com/watch?v=CAyWN9ba9J8>
- The Kiffness x Ognjen & Sinisa - Insomnia (Balkan Club Remix):
  <https://www.youtube.com/watch?v=hVJtPuuQK_s>

Respect copyright and permission. Use your own recordings, licensed samples,
public-domain material, collaboration footage, or source clips you are allowed
to remix. Learn the method, not unauthorized copying.

# The Kiffness Method

The method is not "put a beat under a video." It is closer to a musical reply.
The source clip stays the star. Your job is to reveal the song hiding inside
the clip.

```{=typst}
#figure(
  rect(width: 100%, inset: 10pt, radius: 6pt, stroke: rgb("#D8D2C4"), fill: rgb("#FFFDF8"))[
    #text(weight: "bold")[Remix workflow]\
    #v(0.6em)
    #grid(columns: (1fr, 1fr, 1fr, 1fr, 1fr), gutter: 7pt,
      rect(fill: rgb("#246A73"), radius: 4pt, inset: 7pt)[#align(center)[#text(fill: white, weight: "bold")[Find hook]]],
      rect(fill: rgb("#51A3A3"), radius: 4pt, inset: 7pt)[#align(center)[#text(fill: white, weight: "bold")[Lock tempo]]],
      rect(fill: rgb("#2A9D8F"), radius: 4pt, inset: 7pt)[#align(center)[#text(fill: white, weight: "bold")[Add groove]]],
      rect(fill: rgb("#E76F51"), radius: 4pt, inset: 7pt)[#align(center)[#text(fill: white, weight: "bold")[Arrange]]],
      rect(fill: rgb("#E9C46A"), radius: 4pt, inset: 7pt)[#align(center)[#text(fill: black, weight: "bold")[Mix/export]]],
    )
  ],
  caption: [A source clip becomes a remix by moving from hook to tempo to groove to arrangement.]
)
```

Watch the reference videos for these ingredients:

| Ingredient | What to notice |
|---|---|
| Source hook | A voice, phrase, rhythm, or visual moment that is immediately recognizable. |
| Groove translation | Drums and bass make the source feel like a track. |
| Call and response | The source says something; the music answers. |
| Build and payoff | Layers enter in a way the viewer can follow. |
| Performance evidence | Hands, face, instruments, or DAW moments show the remix being made. |

Your beginner goal is not to imitate every detail. Your goal is to finish short
studies: 15 seconds, 30 seconds, then one minute.

# What the MPK mini Is

The MPK mini is a MIDI controller. It usually does not make finished sound by
itself. It sends instructions to software on your Mac: note on, note off,
velocity, pad hit, knob movement, pitch bend, modulation, and timing features.

```{=typst}
#figure(
  rect(width: 100%, inset: 10pt, radius: 7pt, fill: rgb("#293241"))[
    #text(fill: white, weight: "bold")[MPK mini control map]\
    #v(0.6em)
    #grid(columns: (1.1fr, 1fr, 1.1fr), gutter: 10pt,
      rect(fill: rgb("#E76F51"), radius: 5pt, inset: 8pt)[#text(fill: white, weight: "bold")[Pads]#linebreak()#text(fill: white, size: 8pt)[drums, samples, mutes, chops]],
      rect(fill: rgb("#51A3A3"), radius: 5pt, inset: 8pt)[#text(fill: white, weight: "bold")[Knobs]#linebreak()#text(fill: white, size: 8pt)[levels, filters, sends, macros]],
      rect(fill: rgb("#2A9D8F"), radius: 5pt, inset: 8pt)[#text(fill: white, weight: "bold")[Joystick/wheels]#linebreak()#text(fill: white, size: 8pt)[pitch, modulation, expression]],
    )
    #v(0.7em)
    #rect(fill: white, radius: 4pt, inset: 8pt)[
      #text(weight: "bold")[25 keys] #h(1em)
      bass lines, chords, leads, pads, one-finger sketches
    ]
    #v(0.5em)
    #grid(columns: (1fr, 1fr), gutter: 10pt,
      rect(fill: rgb("#246A73"), radius: 5pt, inset: 8pt)[#text(fill: white, weight: "bold")[Arpeggiator]#linebreak()#text(fill: white, size: 8pt)[tempo-locked patterns]],
      rect(fill: rgb("#E9C46A"), radius: 5pt, inset: 8pt)[#text(weight: "bold")[Note Repeat]#linebreak()#text(size: 8pt)[fast hats, rolls, stutters]],
    )
  ],
  caption: [Treat the MPK as a performance surface for the DAW, not as the whole studio.]
)
```

| MPK part | What to use it for |
|---|---|
| Keys | Bass, chords, synth lines, piano parts, pads, and hooks. |
| Pads | Kick, snare, hats, percussion, samples, source chops, and transitions. |
| Knobs | Track volume, filter cutoff, reverb send, delay send, panning, and effect macros. |
| Joystick or wheels | Pitch bend, vibrato, filter movement, and expressive synth moments. |
| Arpeggiator | Rhythmic note patterns from held notes or chords. |
| Note Repeat | Repeated pad hits in time with the project tempo. |

The most important beginner distinction: the MPK sends MIDI, while your DAW
and plugins create audio.

# MIDI and Audio Without Confusion

MIDI is control information. Audio is sound.

```{=typst}
#figure(
  rect(width: 100%, inset: 10pt, radius: 6pt, stroke: rgb("#D8D2C4"), fill: rgb("#FFFDF8"))[
    #text(weight: "bold")[Signal flow]\
    #v(0.6em)
    #grid(columns: (1fr, 1fr, 1fr, 1fr, 1fr), gutter: 6pt,
      rect(fill: rgb("#246A73"), radius: 4pt, inset: 6pt)[#align(center)[#text(fill: white, weight: "bold")[MPK MIDI]]],
      rect(fill: rgb("#51A3A3"), radius: 4pt, inset: 6pt)[#align(center)[#text(fill: white, weight: "bold")[DAW]]],
      rect(fill: rgb("#2A9D8F"), radius: 4pt, inset: 6pt)[#align(center)[#text(fill: white, weight: "bold")[Instruments]]],
      rect(fill: rgb("#E76F51"), radius: 4pt, inset: 6pt)[#align(center)[#text(fill: white, weight: "bold")[Audio mix]]],
      rect(fill: rgb("#E9C46A"), radius: 4pt, inset: 6pt)[#align(center)[#text(weight: "bold")[Video export]]],
    )
  ],
  caption: [MIDI controls software instruments. Audio is recorded, mixed, and exported.]
)
```

| Term | Meaning |
|---|---|
| MIDI track | Editable instructions: notes, timing, velocity, knob movement. |
| Audio track | A recorded waveform: voice, guitar, source clip, or exported beat. |
| Instrument plugin | Software that turns MIDI into sound. |
| Effect plugin | Software that changes sound: EQ, compression, reverb, delay, saturation. |
| Latency | Delay between playing and hearing. Use wired headphones and low buffer settings. |
| Buffer size | Audio setting: small buffer for recording, larger buffer for mixing. |

If you see MIDI notes but hear nothing, load an instrument. If you see an audio
waveform but cannot change its notes, remember that it is already sound, not
MIDI.

# Mac Setup

Start simple. Do not buy ten things before you can make one loop.

1. Plug the MPK directly into the Mac over USB.
2. Open Audio MIDI Setup in Applications > Utilities and confirm the device
   appears.
3. Pick one DAW to start. This manual now treats GarageBand and FL Studio as
   the two main paths. GarageBand is easiest on Mac; FL Studio is stronger for
   pattern-based beat work and step sequencing.
4. Use wired headphones. Bluetooth latency will make timing feel broken.
5. Create a project folder with `Source Video`, `Audio`, `Stems`, `Project`,
   `Exports`, and `Notes`.

| Gear | Recommendation |
|---|---|
| Built-in mic | OK for rough ideas, weak for final audio. |
| USB audio interface | Best next purchase for microphones, guitar, and lower-latency input. |
| Closed-back headphones | Prevent playback from leaking into a mic. |
| External monitor | Useful, not required. A laptop screen is enough for early projects. |

# Your Physical Rig: MPK, MOTU M4, Pre-73, and Mics

Your rig has two separate worlds:

- MIDI control: MPK mini to Mac over USB. This controls software instruments.
- Audio recording: microphones and preamps into the MOTU M4, then into
  GarageBand.

Keep those worlds separate in your head. The MPK does not plug into the MOTU
for this workflow. The MPK plugs into the Mac. The MOTU handles audio.

```{=typst}
#figure(
  rect(width: 100%, inset: 10pt, radius: 6pt, stroke: rgb("#D8D2C4"), fill: rgb("#FFFDF8"))[
    #text(weight: "bold")[Complete desk wiring]\
    #v(0.7em)
    #grid(columns: (1fr, 1fr, 1fr), gutter: 8pt,
      rect(fill: rgb("#246A73"), radius: 4pt, inset: 8pt)[#align(center)[#text(fill: white, weight: "bold")[MPK mini]#linebreak()#text(fill: white, size: 8pt)[USB MIDI to Mac]]],
      rect(fill: rgb("#51A3A3"), radius: 4pt, inset: 8pt)[#align(center)[#text(fill: white, weight: "bold")[Mac]#linebreak()#text(fill: white, size: 8pt)[GarageBand project]]],
      rect(fill: rgb("#2A9D8F"), radius: 4pt, inset: 8pt)[#align(center)[#text(fill: white, weight: "bold")[MOTU M4]#linebreak()#text(fill: white, size: 8pt)[audio in/out]]],
    )
    #v(0.8em)
    #grid(columns: (1fr, 1fr, 1fr), gutter: 8pt,
      rect(fill: rgb("#E76F51"), radius: 4pt, inset: 8pt)[#align(center)[#text(fill: white, weight: "bold")[Mic]#linebreak()#text(fill: white, size: 8pt)[voice / room / instrument]]],
      rect(fill: rgb("#E9C46A"), radius: 4pt, inset: 8pt)[#align(center)[#text(weight: "bold")[Pre-73]#linebreak()#text(size: 8pt)[optional color preamp]]],
      rect(fill: rgb("#293241"), radius: 4pt, inset: 8pt)[#align(center)[#text(fill: white, weight: "bold")[Headphones / monitors]#linebreak()#text(fill: white, size: 8pt)[listen from M4]]],
    )
  ],
  caption: [MIDI goes directly to the Mac; microphone audio goes through the M4.]
)
```

## Three Safe Connection Choices

| Use case | Cable path | Phantom power |
|---|---|---|
| Condenser mic through Pre-73 | Mic XLR -> Pre-73 mic input -> Pre-73 line output -> MOTU M4 rear line input 3 or 4 | Turn 48V on at the Pre-73. Keep MOTU 48V off. |
| Dynamic mic through Pre-73 | Mic XLR -> Pre-73 mic input -> Pre-73 line output -> MOTU M4 rear line input 3 or 4 | Off, unless the mic specifically requires phantom. |
| Mic directly into MOTU | Mic XLR -> MOTU M4 front input 1 or 2 | Use M4 48V only for condenser mics. Keep it off for dynamics/ribbons unless the mic manual says otherwise. |

The Pre-73 is a preamp. If you use it, the cleanest beginner path is to send
its line output into one of the M4 rear line inputs. That avoids running a
preamp into another preamp. If you must use an M4 front combo input, keep the
M4 gain low and watch the M4 meter carefully.

## Power-Up and Power-Down Order

Use this order every time until it becomes boring.

1. Turn monitor speakers down or off. Put headphones on the table, not on your
   ears.
2. Confirm phantom power is off on the Pre-73 and M4.
3. Connect the mic.
4. Connect Pre-73 output to M4 line input if using the Pre-73.
5. Connect M4 to Mac over USB.
6. Open GarageBand and select the M4 as input and output.
7. Turn on phantom only if the mic needs it, and only on the device feeding the
   mic.
8. Bring gain up slowly while speaking or playing.
9. If anything clips red, turn down the earlier gain stage first.
10. Before unplugging a condenser mic, turn phantom off and wait about 10
    seconds.

## Gain Staging With the Pre-73 and M4

Gain staging means each device receives a strong signal without overload.

| Stage | What to do | Watch |
|---|---|---|
| Pre-73 input gain | Raise until the mic feels present. More gain adds more preamp color. | Pre-73 meter should not live in overload. |
| Pre-73 output | Use it as the level sent to the M4. Lower output if you drove the input for color. | M4 input meter. |
| MOTU M4 line input | Prefer rear line input 3 or 4 for Pre-73 output. | Avoid red on the M4 meter. |
| GarageBand track | Arm the correct input and record. | Peaks around -12 dB to -6 dB are healthy. |

For a clean vocal, use moderate Pre-73 gain and enough output to feed the M4.
For a more colored vocal, raise Pre-73 gain and lower Pre-73 output so the M4
still receives a safe level.

## Monitoring on the MOTU M4

The M4 can let you hear inputs directly, before GarageBand latency. Use direct
monitoring when the delay bothers you while singing or playing.

| Situation | Monitoring choice |
|---|---|
| Recording vocal through mic | Use M4 direct monitoring if GarageBand feels delayed. |
| Playing MPK software instrument | Monitor through GarageBand; MIDI instruments must be heard from the software. |
| Overdubbing voice over beat | Balance GarageBand playback and live input so both are comfortable. |
| Mixing | Turn direct monitoring off if it doubles the input sound. |

# Installing and Checking the MPK

The exact menus vary by software, but the pattern is the same: the Mac sees the
MPK, the DAW enables it as a MIDI input, and an instrument track receives the
notes.

## GarageBand

1. Connect the MPK over USB.
2. Open GarageBand and create an empty project.
3. Choose Software Instrument.
4. Play the MPK keys. If you hear the selected instrument, the basic path is
   working.
5. Open GarageBand > Settings > Audio/MIDI if you need to refresh MIDI devices.

GarageBand is friendly for learning tracks, loops, software instruments, and
basic recording. It is less ideal for advanced video sync and live performance
mapping, but it is a good first week.

## GarageBand With the MOTU M4

Use this as your first real setup checklist.

1. Connect the M4 to the Mac.
2. Connect headphones or monitors to the M4, not the Mac headphone jack.
3. Open GarageBand > Settings > Audio/MIDI.
4. Set Output Device to the MOTU M4.
5. Set Input Device to the MOTU M4.
6. Create an Empty Project.
7. For a mic, choose the Audio track with the microphone icon.
8. Open Details and choose the correct input:
   - Input 1 or 2 for M4 front mic inputs.
   - Input 3 or 4 for M4 rear line inputs fed by the Pre-73.
9. Enable "I want to hear my instrument as I play and record" only if you are
   not using M4 direct monitoring, or if you need to hear GarageBand effects.
10. Record a 10-second test and play it back before doing a full take.

```{=typst}
#figure(
  rect(width: 100%, inset: 10pt, radius: 6pt, stroke: rgb("#D8D2C4"), fill: rgb("#FFFDF8"))[
    #text(weight: "bold")[GarageBand input map]\
    #v(0.7em)
    #grid(columns: (1fr, 1fr, 1fr, 1fr), gutter: 6pt,
      rect(fill: rgb("#246A73"), radius: 4pt, inset: 7pt)[#align(center)[#text(fill: white, weight: "bold")[Input 1]#linebreak()#text(fill: white, size: 8pt)[M4 front mic/inst]]],
      rect(fill: rgb("#246A73"), radius: 4pt, inset: 7pt)[#align(center)[#text(fill: white, weight: "bold")[Input 2]#linebreak()#text(fill: white, size: 8pt)[M4 front mic/inst]]],
      rect(fill: rgb("#E9C46A"), radius: 4pt, inset: 7pt)[#align(center)[#text(weight: "bold")[Input 3]#linebreak()#text(size: 8pt)[rear line / Pre-73]]],
      rect(fill: rgb("#E9C46A"), radius: 4pt, inset: 7pt)[#align(center)[#text(weight: "bold")[Input 4]#linebreak()#text(size: 8pt)[rear line / Pre-73]]],
    )
  ],
  caption: [In GarageBand, M4 hardware inputs appear as selectable track inputs.]
)
```

If the armed GarageBand track shows a meter but you hear nothing, check
monitoring. If the M4 meter moves but GarageBand does not, the wrong track input
is probably selected. If GarageBand records but playback comes from Mac
speakers, the output device is not set to the M4.

## FL Studio With the MPK and MOTU M4

FL Studio works well if you like patterns, drum grids, quick MIDI editing, and
clip-style arranging. On Mac, treat the M4 as the audio device and the MPK as a
MIDI input.

1. Connect the M4 to the Mac and connect headphones/monitors to the M4.
2. Connect the MPK mini to the Mac over USB.
3. Open FL Studio.
4. Open Options > Audio settings, or press F10 and choose the Audio tab.
5. In Input/output, select the MOTU M4/Core Audio device.
6. Set a small buffer for recording; raise it later if the project crackles.
7. Open Options > MIDI settings, or press F10 and choose MIDI.
8. In the Input list, select the MPK mini and enable it.
9. Confirm the MIDI activity light blinks when you play keys, pads, or knobs.
10. Add a Channel Rack instrument such as a drum plugin, sampler, FLEX, or a
    synth, then play the MPK.

For microphone recording in FL Studio on macOS, make sure macOS allows FL
Studio to access the microphone/audio input. Then choose the correct M4 input
on a Mixer insert before recording.

```{=typst}
#figure(
  rect(width: 100%, inset: 10pt, radius: 6pt, stroke: rgb("#D8D2C4"), fill: rgb("#FFFDF8"))[
    #text(weight: "bold")[GarageBand vs FL Studio routing]\
    #v(0.7em)
    #grid(columns: (1fr, 1fr), gutter: 10pt,
      rect(fill: rgb("#246A73"), radius: 5pt, inset: 8pt)[
        #text(fill: white, weight: "bold")[GarageBand]#linebreak()
        #text(fill: white, size: 8pt)[Settings > Audio/MIDI -> M4]#linebreak()
        #text(fill: white, size: 8pt)[Track input -> Input 1/2/3/4]#linebreak()
        #text(fill: white, size: 8pt)[Software Instrument -> MPK]
      ],
      rect(fill: rgb("#E76F51"), radius: 5pt, inset: 8pt)[
        #text(fill: white, weight: "bold")[FL Studio]#linebreak()
        #text(fill: white, size: 8pt)[F10 Audio -> M4]#linebreak()
        #text(fill: white, size: 8pt)[F10 MIDI -> enable MPK]#linebreak()
        #text(fill: white, size: 8pt)[Mixer insert input -> M4 input]
      ],
    )
  ],
  caption: [Both DAWs use the same hardware, but the setup screens are different.]
)
```

## GarageBand vs FL Studio: Which One for This Manual?

| Task | GarageBand | FL Studio |
|---|---|---|
| First vocal or mic recording | Easier. Audio tracks are straightforward. | Works, but routing through Mixer inserts takes more setup. |
| MPK keys for piano/synth | Very easy with Software Instrument tracks. | Easy after MIDI input is enabled. |
| Finger-drummed beat | Good enough for learning. | Excellent with Channel Rack and patterns. |
| Pattern variations | More timeline-oriented. | Very strong: Pattern 1, Pattern 2, Pattern 3. |
| Knob automation | Possible through Smart Controls/automation. | Strong through linking controls and automation clips. |
| Video sync | Basic. Often finish video elsewhere. | Usually finish video elsewhere; export audio/stems. |

Recommendation: start the mic/MOTU/Pre-73 setup in GarageBand because it is
clearer. Build drum-pattern fluency in FL Studio because the Channel Rack makes
pad sequencing feel natural. You can export stems from either DAW for video
editing.

## Logic Pro

Logic is the grown-up version of the GarageBand idea. Use it when you want
better mixing, Flex Time, automation, video import, and export control.

1. Create a Software Instrument track.
2. Choose a drum kit, synth bass, piano, or sampler.
3. Press Record and capture MIDI from the MPK.
4. Use the Piano Roll to fix notes.
5. Use Smart Controls or MIDI Learn to assign knobs.

## Ableton Live

Ableton is strong for looping, clips, warping, and performance. If your main
goal is live building like a visible remix performance, Ableton is worth
learning.

1. Enable the MPK as a MIDI input in Settings > Link/Tempo/MIDI.
2. Create a MIDI track with Drum Rack or an instrument.
3. Arm the track and play.
4. Use Session View for loops and Arrangement View for the final timeline.
5. Use Warp on source clips to lock them to tempo.

## MPC Beats

Akai's setup path uses MPC Beats and the included software bundle. Akai's own
setup article explains registration, the inMusic Software Center, installing
MPC Beats, AIR plugins, sample packs, and enabling the MPK input. The key idea:
the controller should appear in MIDI/Sync preferences, and its input should be
enabled for track/control use.

Do one sanity test in every DAW: open one piano instrument and play the keys. If
that works, the MPK is alive. Then test pads with a drum kit. Then test a knob
with one visible parameter.

# DAW Basics

A DAW has five zones: tracks, timeline, mixer, browser, and transport.

| Zone | What it does |
|---|---|
| Tracks | One row per sound: source clip, drums, bass, chords, lead, voice, FX. |
| Timeline | Time moves left to right. Bars and beats organize the music. |
| Mixer | Volume, pan, mute, solo, sends, and plugins. |
| Browser | Instruments, samples, loops, presets, and files. |
| Transport | Play, stop, record, tempo, metronome, loop range. |

Name tracks immediately. `Kick`, `Snare`, `Source Clip`, and `Bass` teach you
more than `Audio 1` and `MIDI 7`.

Save project versions:

- `01_import`
- `02_tempo`
- `03_drums`
- `04_bass_chords`
- `05_arrangement`
- `06_mix`
- `07_video_sync`

# Source Clip Preparation

The source clip is the heart of the remix. Spend more time choosing the right
moment than choosing the snare sample.

Good source material has at least one of these:

- A phrase that repeats naturally.
- A rhythm you can tap with your hand.
- A melody that suggests a key.
- A funny, surprising, emotional, or beautiful visual.
- Space between phrases where your music can answer.

Avoid source clips where every second is dense. If the clip is already full of
music, talking, crowd noise, and effects, it will be hard to add anything clean.

Practical source workflow:

1. Put the original file in `Source Video`.
2. Create a copy for editing, never your only original.
3. Extract or import the audio into the DAW.
4. Mark the best phrase.
5. Cut a two-bar or four-bar loop.
6. Add fades so the loop does not click.
7. Save a project version before warping.

```{=typst}
#figure(
  rect(width: 100%, inset: 10pt, radius: 6pt, stroke: rgb("#D8D2C4"), fill: rgb("#FFFDF8"))[
    #text(weight: "bold")[Source preparation]\
    #v(0.6em)
    #grid(columns: (1fr, 1fr, 1fr, 1fr), gutter: 7pt,
      rect(fill: rgb("#246A73"), radius: 4pt, inset: 7pt)[#align(center)[#text(fill: white, weight: "bold")[Original]]],
      rect(fill: rgb("#51A3A3"), radius: 4pt, inset: 7pt)[#align(center)[#text(fill: white, weight: "bold")[Best phrase]]],
      rect(fill: rgb("#2A9D8F"), radius: 4pt, inset: 7pt)[#align(center)[#text(fill: white, weight: "bold")[Clean loop]]],
      rect(fill: rgb("#E76F51"), radius: 4pt, inset: 7pt)[#align(center)[#text(fill: white, weight: "bold")[Arrangement]]],
    )
  ],
  caption: [Prepare the source before writing extra parts.]
)
```

# MPK Mapping for Remix Work

Map only what you will actually touch during performance.

| Control | Suggested beginner mapping |
|---|---|
| Pad 1 | Kick |
| Pad 2 | Snare or clap |
| Pad 3 | Closed hi-hat |
| Pad 4 | Open hi-hat |
| Pad 5 | Percussion or shaker |
| Pad 6 | Source clip chop |
| Pad 7 | Transition hit |
| Pad 8 | Crash, riser, or stop effect |
| Knob 1 | Drum group volume |
| Knob 2 | Bass volume |
| Knob 3 | Chords volume |
| Knob 4 | Lead volume |
| Knob 5 | Filter cutoff |
| Knob 6 | Reverb send |
| Knob 7 | Delay send |
| Knob 8 | Master/performance macro |

Good mapping sentence: "I want my left hand to open the filter while my right
hand plays the hook." If you cannot say the sentence, do not map it yet.

## Performance Knob Map

Use this as a stable performance map for the first month. You can change it
later, but consistency will teach your hands where everything lives.

| Knob | Assign to | Start position | Performance move |
|---|---|---:|---|
| K1 | Drum bus volume | 75% | Pull down for source-only intro; push up at groove entrance. |
| K2 | Bass volume | 70% | Bring in after the source hook is understood. |
| K3 | Chord/pad volume | 50% | Fade up under emotional vocal notes. |
| K4 | Lead/hook volume | 60% | Lift only when answering the source phrase. |
| K5 | Low-pass filter cutoff | 35% | Open over 2 or 4 bars into a drop. |
| K6 | Reverb send | 10% | Momentary lift on final words or transition hits. |
| K7 | Delay send | 0% | Throw one word or stab into a break. |
| K8 | Master performance macro | 50% | Map later to a combined filter/saturation/width move. |

```{=typst}
#figure(
  rect(width: 100%, inset: 10pt, radius: 6pt, stroke: rgb("#D8D2C4"), fill: rgb("#FFFDF8"))[
    #text(weight: "bold")[Knob movement timeline]\
    #v(0.7em)
    #grid(columns: (0.8fr, 1fr, 1fr, 1fr, 1fr), gutter: 5pt,
      [K1 drums], rect(fill: rgb("#246A73"), radius: 3pt, inset: 4pt)[#text(fill: white)[mute]], rect(fill: rgb("#246A73"), radius: 3pt, inset: 4pt)[#text(fill: white)[fade in]], rect(fill: rgb("#246A73"), radius: 3pt, inset: 4pt)[#text(fill: white)[full]], rect(fill: rgb("#246A73"), radius: 3pt, inset: 4pt)[#text(fill: white)[drop]],
      [K2 bass], [off], rect(fill: rgb("#2A9D8F"), radius: 3pt, inset: 4pt)[#text(fill: white)[enter]], rect(fill: rgb("#2A9D8F"), radius: 3pt, inset: 4pt)[#text(fill: white)[hold]], rect(fill: rgb("#2A9D8F"), radius: 3pt, inset: 4pt)[#text(fill: white)[push]],
      [K5 filter], rect(fill: rgb("#E9C46A"), radius: 3pt, inset: 4pt)[closed], rect(fill: rgb("#E9C46A"), radius: 3pt, inset: 4pt)[opening], rect(fill: rgb("#E9C46A"), radius: 3pt, inset: 4pt)[open], rect(fill: rgb("#E9C46A"), radius: 3pt, inset: 4pt)[snap],
      [K7 delay], [off], [off], rect(fill: rgb("#E76F51"), radius: 3pt, inset: 4pt)[#text(fill: white)[throw]], [off],
    )
  ],
  caption: [A simple four-section knob plan for intro, entrance, build, and drop.]
)
```

# Drum Programming on Pads

Finger drumming does not need to be flashy. For remix production, the goal is a
reliable groove.

Start with this pad layout:

| Pad | Sound | Why |
|---|---|---|
| 1 | Kick | Main pulse. |
| 2 | Snare | Backbeat. |
| 3 | Closed hat | Constant motion. |
| 4 | Open hat | Lift before changes. |
| 5 | Clap | Layer with snare for width. |
| 6 | Percussion | Style-specific flavor. |
| 7 | Crash | Section marker. |
| 8 | Vocal chop or hit | Source-related ear candy. |

Record drums in layers instead of all at once:

1. Kick only.
2. Snare/clap.
3. Hats.
4. Percussion.
5. Fills.

This makes editing easier. It also teaches you which part is actually causing a
timing problem.

## Pad Timing Grid

Count a four-beat bar as "1 e and a 2 e and a 3 e and a 4 e and a". Start with
these hits:

| Count | Pad | Sound |
|---|---|---|
| 1 | Pad 1 | Kick |
| 1 and | Pad 3 | Closed hat |
| 2 | Pad 2 | Snare or clap |
| 2 and | Pad 3 | Closed hat |
| 3 | Pad 1 | Kick |
| 3 and | Pad 3 | Closed hat |
| 4 | Pad 2 | Snare or clap |
| 4 and | Pad 4 | Open hat or lift |

Once that is steady, add Pad 6 on the gap after a source phrase, not during the
phrase. This keeps the source intelligible.

```{=typst}
#figure(
  rect(width: 100%, inset: 10pt, radius: 6pt, stroke: rgb("#D8D2C4"), fill: rgb("#FFFDF8"))[
    #text(weight: "bold")[One-bar pad sequence]\
    #v(0.7em)
    #grid(columns: (0.8fr, 1fr, 1fr, 1fr, 1fr), gutter: 5pt,
      [Beat], [1], [2], [3], [4],
      [Kick P1], rect(fill: rgb("#246A73"), radius: 3pt, inset: 4pt)[#text(fill: white)[hit]], [], rect(fill: rgb("#246A73"), radius: 3pt, inset: 4pt)[#text(fill: white)[hit]], [],
      [Snare P2], [], rect(fill: rgb("#E76F51"), radius: 3pt, inset: 4pt)[#text(fill: white)[hit]], [], rect(fill: rgb("#E76F51"), radius: 3pt, inset: 4pt)[#text(fill: white)[hit]],
      [Hat P3], rect(fill: rgb("#E9C46A"), radius: 3pt, inset: 4pt)[and], rect(fill: rgb("#E9C46A"), radius: 3pt, inset: 4pt)[and], rect(fill: rgb("#E9C46A"), radius: 3pt, inset: 4pt)[and], rect(fill: rgb("#E9C46A"), radius: 3pt, inset: 4pt)[and],
    )
  ],
  caption: [A first dance pattern using only three pads.]
)
```

# Playing Bass and Chords on Mini Keys

Mini keys are small, but they are enough for writing. Do not try to play like a
concert pianist at first. Use them as a sketchpad.

For bass:

- Find the root note that sounds stable under the source phrase.
- Play fewer notes than you think.
- Make the bass agree with the kick.
- Use octave jumps for energy.
- Use passing notes only near the end of a bar.

For chords:

- Start with triads: major, minor, suspended.
- Hold chords under long vocal notes.
- Use short offbeat stabs for dance energy.
- If the source vocal is busy, use fewer chords.

When in doubt, play the root note in the bass and a simple minor or major chord
above it. A simple correct part beats a clever crowded one.

# A 16-Bar Remix Performance Sequence

This is the practical heart of the workflow. It tells you what to record or
perform over 16 bars. Use it slowly at first, then make it musical.

| Bars | Source/video | Pads | Keys | Knobs | Record/film |
|---|---|---|---|---|---|
| 1-2 | Source clip alone | None | None | K1 drums down, K5 filter closed | Show source premise. |
| 3-4 | Source loop repeats | P3 light hats only | Hold root note quietly | K3 chords low | Film listening/reaction. |
| 5-8 | Groove starts | P1 kick, P2 clap, P3 hats | Bass root/fifth pattern | K1 drums up, K2 bass up | Film MPK pads. |
| 9-10 | Source phrase returns | Keep beat simple | Chord pad under long words | K5 slowly opens | Film keys/knobs. |
| 11-12 | Build | Add P4 open hats, P7 riser/crash | Bass octave lift | K6 reverb slightly up | Film knob sweep. |
| 13-16 | Drop/payoff | Full pad pattern, P6 chop answer | Bass + hook answer | K5 open, K7 delay throw at bar 16 | Film source + performance cuts. |

## Bar-by-Bar Beginner Script

| Bar | Action |
|---:|---|
| 1 | Press play on the source loop. Do not play yet. Let the viewer understand it. |
| 2 | Nod/count silently. Confirm the loop feels steady. |
| 3 | Tap Pad 3 hats on the offbeats. Keep them soft. |
| 4 | Add a quiet chord or bass root if the key is obvious. |
| 5 | Start Pad 1 kick on beats 1 and 3. |
| 6 | Add Pad 2 clap/snare on beats 2 and 4. |
| 7 | Add bass notes that line up with the kick. |
| 8 | Add a tiny fill with Pad 5 or Pad 6 at the end. |
| 9 | Bring source phrase back to the front. Do not overplay. |
| 10 | Turn K5 filter slowly upward. |
| 11 | Add open hat or shaker. |
| 12 | Turn K6 reverb up briefly on the last word. |
| 13 | Full drums, full bass, clear hook. |
| 14 | Play the answer phrase on keys. |
| 15 | Repeat the best musical idea, not a new one. |
| 16 | Use K7 delay throw, then stop or cut to source reaction. |

The first time, record this as separate passes. Later, perform more of it live.

## Where the Sequence Lives in Each DAW

| Musical part | GarageBand place | FL Studio place |
|---|---|---|
| Source clip audio | Audio track on the timeline | Audio clip in Playlist or sampler/audio channel |
| Kick/snare/hats | Drum Kit Designer or sampler instrument track | Channel Rack drum channels or FPC |
| Bass | Software Instrument bass track | Channel Rack instrument routed to bass Mixer insert |
| Chords/pads | Software Instrument track | Instrument channel routed to chords/pad Mixer insert |
| Source chops | Sampler or audio regions | Slicer/Sampler/audio clips in Playlist |
| Knob filter move | Smart Control/track automation | Link controller to plugin/filter, record automation or create automation clip |
| Reverb/delay throw | Track send or plugin automation | Mixer send/effect automation clip |
| Final arrangement | GarageBand timeline | FL Studio Playlist |

## FL Studio Pattern Version of the 16 Bars

If you choose FL Studio, think in patterns first and Playlist arrangement
second.

| Pattern | Bars | Contains | Trigger/arrange |
|---|---|---|---|
| Pattern 1 - Hats | 3-16 | P3 closed hats, optional P4 open hat | Put under most of the source loop. |
| Pattern 2 - Core beat | 5-16 | P1 kick, P2 clap/snare, P3 hats | Enter when the groove starts. |
| Pattern 3 - Bass | 5-16 | Root/fifth bass notes from MPK keys | Route to bass Mixer insert. |
| Pattern 4 - Chords | 9-16 | Sustained chords or offbeat stabs | Fade or filter into build. |
| Pattern 5 - Fills/chops | 8, 12, 16 | P5/P6/P7 fills, source hit, crash | Drop only at section edges. |
| Automation clip - Filter | 9-13 | K5 low-pass opening | Draw or record curve into drop. |
| Automation clip - Delay | 16 | K7 delay send throw | One short moment, then back to zero. |

In FL Studio, route drums, bass, chords, and source audio to separate Mixer
inserts early. That makes the M4-recorded mic, the source clip, and the MPK
instruments much easier to balance.

# Rhythm, Tempo, and Sync

The source clip must agree with the project tempo. Even a comic remix needs a
serious clock.

1. Import the source video or source audio.
2. Find the best two-bar or four-bar phrase.
3. Tap tempo while listening.
4. Loop the phrase against the metronome.
5. If it drifts, warp, flex, or slice the audio.
6. Build drums only after the source loop is stable.

| Problem | Fix |
|---|---|
| Source rushes ahead | Add warp/flex markers or slice phrases to the grid. |
| Tempo feels wrong | Try half-time or double-time. 92 BPM may feel like 184 BPM. |
| Drums sound stiff | Use swing, velocity variation, and lighter quantization. |
| Loop clicks | Add tiny fades at region edges. |

# Quantization, Swing, and Human Feel

Quantization moves MIDI notes toward the grid. It can fix sloppy timing, but it
can also remove personality.

Use these settings as a mindset:

| Material | Quantize amount |
|---|---|
| Kick in club beat | Strong quantize is usually fine. |
| Snare/clap | Mostly tight, with small variation if desired. |
| Hi-hats | Quantize, then vary velocity. |
| Percussion | Lighter quantize; keep some human push/pull. |
| Bass | Tight to kick, but not robotic. |
| Chords | Depends on style; stabs can be tight, pads can be loose. |
| Source clip | Warp only as much as needed to make the groove work. |

Swing shifts some subdivisions later, creating bounce. Try small swing amounts
before you rewrite a pattern. If a groove feels technically correct but boring,
vary velocity first, then try swing, then change notes.

# Recording Instruments and Voice

Kiffness-style production often feels like one person building a tiny band
around a clip.

| Source | How to record it |
|---|---|
| MPK keys | Create an instrument track, choose a sound, arm, record MIDI. |
| MPK pads | Create a drum/sampler track, map pads, record MIDI hits. |
| Voice | Use a USB mic or audio interface; monitor with wired headphones. |
| Guitar or bass | Plug into an interface; record dry if you want to change amp sound later. |
| Percussion | Mic real claps/shakers or use samples. Real layers help programmed drums. |

Record at healthy levels. Peaks around -12 dB to -6 dB are fine. If the
waveform looks like a rectangle, it clipped; turn down the input and record
again.

# Microphones, Interfaces, and Monitoring

For voice, acoustic instruments, and room percussion, the recording chain is:

```text
Voice/instrument -> microphone -> audio interface -> Mac/DAW -> headphones
```

If you use a USB microphone, the mic and interface are combined:

```text
Voice/instrument -> USB microphone -> Mac/DAW -> headphones
```

Monitoring means hearing yourself while recording. If monitoring is delayed,
you will play or sing late. Fixes:

- Use wired headphones.
- Lower the DAW buffer size while recording.
- Close CPU-heavy apps.
- Use direct monitoring on an audio interface when available.
- Record dry and add reverb after the take if latency is distracting.

Room noise matters. Turn off fans when possible. Stay close enough to the mic
that your voice is stronger than the room.

# Drums, Bass, Chords, and Hooks

Each layer has a job.

| Layer | Job |
|---|---|
| Kick | Defines dance pulse. |
| Snare/clap | Gives the backbeat. |
| Hi-hats | Add motion and subdivision. |
| Percussion | Adds style and regional feel. |
| Bass | Connects drums to harmony. |
| Chords | Add emotion without crowding the source. |
| Lead/hook | Answers the source phrase. |

Beginner two-bar pattern:

```text
Beat:  1       2       3       4
Kick:  X               X
Clap:          X               X
Hat:   x   x   x   x   x   x   x   x
Bass:  root        fifth root  walk
```

Start with drums and bass only. If that does not work, extra layers will not
rescue it.

# Arrangement Blueprint

A short remix still needs structure. Even 45 seconds can have a beginning,
middle, and payoff.

| Section | Length | Job |
|---|---:|---|
| Cold open | 2-5 seconds | Show the source premise immediately. |
| Setup loop | 4-8 bars | Let the source hook repeat cleanly. |
| Groove entrance | 4-8 bars | Add drums and bass. |
| Build | 2-4 bars | Filter, riser, snare fill, or visual setup. |
| Drop/payoff | 8-16 bars | Full remix energy. |
| Tag ending | 1-4 bars | Punchline, delay throw, stop, or source reaction. |

Kiffness-style videos often feel spontaneous, but the arrangement is doing real
work. The viewer is being taught the source, shown the transformation, and then
rewarded with the full version.

# Mixing From Zero

Mixing is deciding what the listener should notice first, second, and third.

1. Pull every fader down.
2. Bring up the source clip or lead vocal until it is clear.
3. Add kick and bass.
4. Add snare/clap and hats.
5. Add chords and hook instruments.
6. Add reverb, delay, risers, and fills last.
7. Check on headphones and laptop speakers.

| Tool | Beginner use |
|---|---|
| Volume | The main mix control. Use this before plugins. |
| Pan | Move support parts away from the center. |
| EQ | Remove mud and make room for voice. |
| Compression | Smooth levels or add punch. Use gently. |
| Reverb | Adds space. Too much pushes sounds away. |
| Delay | Rhythmic repeats, transition throws, endings. |
| Limiter | Prevents export clipping on the master. |

Simple EQ starting point: high-pass non-bass instruments around 80 to 150 Hz,
cut a little mud around 200 to 400 Hz if needed, and add presence around 2 to 5
kHz only when a sound needs clarity.

# Effects That Make Remixes Feel Finished

Use effects as musical punctuation.

| Effect | Use it for | Beginner warning |
|---|---|---|
| Filter sweep | Build into a drop or reveal a loop. | Do not leave every part filtered forever. |
| Reverb throw | Make one word or hit bloom. | Too much reverb makes the mix blurry. |
| Delay throw | Echo the last word before a break. | Time it to the project tempo. |
| Saturation | Add warmth and density. | Easy to overdo; compare before/after. |
| Sidechain compression | Make pads/bass pulse with kick. | Subtle is often better. |
| Riser/noise sweep | Signal a section change. | Keep it short in comedy or meme edits. |

Record effect moves with knobs. A visible knob turn is both an audio event and a
video event.

# Syncing Music to Video

The picture should feel musical.

```{=typst}
#figure(
  rect(width: 100%, inset: 10pt, radius: 6pt, stroke: rgb("#D8D2C4"), fill: rgb("#FFFDF8"))[
    #text(weight: "bold")[Video sync layers]\
    #v(0.6em)
    #grid(columns: (1fr, 4fr), gutter: 6pt,
      [Picture], rect(fill: rgb("#246A73"), radius: 3pt, inset: 4pt)[#text(fill: white)[setup | performance | payoff]],
      [Source audio], rect(fill: rgb("#E76F51"), radius: 3pt, inset: 4pt)[#text(fill: white)[hook phrase | repeat | response]],
      [Music], rect(fill: rgb("#2A9D8F"), radius: 3pt, inset: 4pt)[#text(fill: white)[intro | groove | drop | ending]],
      [Cuts], rect(fill: rgb("#E9C46A"), radius: 3pt, inset: 4pt)[beat cuts, reaction cuts, hand close-ups],
    )
  ],
  caption: [Treat the video edit as another rhythmic layer.]
)
```

Use a clap, visible consonant, drum transient, or hand motion as a sync anchor.
Cut to the source clip when it sings or speaks the hook. Cut to the MPK when a
new layer enters. Export a short test before rendering the final version.

# Export Settings

For learning, export often. Do not wait until a project is perfect before
checking a render.

Audio export targets:

| Use | Format |
|---|---|
| DAW mix for video editor | WAV or AIFF, 24-bit if available. |
| Quick sharing draft | MP3 or AAC. |
| Final video upload | Let the video editor encode audio with the video. |

Video export targets:

| Platform | Practical starting point |
|---|---|
| YouTube horizontal | 1920 x 1080, 24/30 fps, H.264 or H.265. |
| Shorts/Reels/TikTok | 1080 x 1920 vertical, 30 fps, H.264 or H.265. |
| Archive master | Highest quality your editor can reasonably store. |

Always watch the exported file, not only the DAW timeline. Exports can reveal
sync errors, missing fonts, muted tracks, clipping, and wrong aspect ratios.

# Case Study: Im Hashem Lo Yivneh Bayis

This reference shows how a choir phrase can become the emotional center of a
dance remix.

| Element | Study notes |
|---|---|
| Source role | The choir provides the hook and harmonic identity. |
| Production goal | Support the vocal phrase with a dance pulse without burying the choir. |
| MPK use | Pads for drums, keys for bass/chords, knobs for filter and reverb build. |
| Practice version | Use your own sung phrase or a licensed choir-like sample. |

Practice steps:

1. Choose a two-bar vocal or choir phrase with emotional lift.
2. Find the key by playing notes under it until one feels like home.
3. Program a four-on-the-floor kick.
4. Add clap/snare on beats 2 and 4.
5. Play a bass root on beat 1 and a passing note before beat 3.
6. Add warm chords under long syllables.
7. Open a filter or reverb send into the drop.

## Choir Remix Pad/Knob Sequence

| Bars | Pads | Keys | Knobs | Goal |
|---|---|---|---|---|
| 1-2 | None | Find and hold root quietly | K1 down, K3 low | Let the choir be the hook. |
| 3-4 | P3 hats only | Soft chord pad | K3 fade up | Add lift without stealing focus. |
| 5-8 | P1 four-on-floor, P2 clap | Bass on root and fifth | K1 and K2 up | Convert choir phrase into dance pulse. |
| 9-12 | Add P5 shaker | Chord inversions | K5 opens slowly | Build anticipation. |
| 13-16 | P7 crash at bar 13, P6 vocal chop answer | Hook answer melody | K6 reverb on final syllable | Payoff and emotional bloom. |
| 17 | Stop drums | None | K7 delay throw | Let the last choir word echo. |

For choir-like material, reverb is tempting. Use it as a moment, not as fog.
The source already has space and harmony; your mix should preserve the words.

# Case Study: Ievan Polkka

This reference is a strong study in turning a viral performance into a club
arrangement.

| Element | Study notes |
|---|---|
| Source role | The melody and performance personality are already strong. |
| Production goal | Make the source danceable without losing its playful identity. |
| MPK use | Pads for kick/snare/hat, keys for bass, note repeat for hats, knobs for delay throws. |
| Practice version | Use a public-domain folk melody or your own whistled phrase. |

Fast folk melodies often work over a simpler club foundation. Do not make every
part busy. Use bass to translate the melody into dance music. Place percussion
fills in the gaps between phrases.

## Folk/Club Remix Pad/Knob Sequence

| Bars | Pads | Keys | Knobs | Goal |
|---|---|---|---|---|
| 1-2 | None | None | K1 down | Let the source melody introduce itself. |
| 3-4 | P3 hats with Note Repeat | Root pulse | K5 half closed | Hint at tempo. |
| 5-8 | P1 kick, P2 clap, P3 hats | Root-fifth-octave bass | K1/K2 up | Make it club-readable. |
| 9-12 | P5 percussion between phrases | Short chord stabs | K7 tiny delay on phrase endings | Keep motion playful. |
| 13-16 | P4 open hat, P7 crash | Bass octaves | K5 opens, K8 macro up | Drop without crowding the melody. |
| 17-20 | P6 source chop answer | Simple lead response | K7 delay throw at the end | Turn the source into call-and-response. |

If the melody is fast, your hands should play less. Let the source do the
gymnastics while the MPK supplies weight and shape.

# Case Study: Insomnia

This reference points toward live-looping energy: build the track in visible
layers so viewers can feel each entrance.

| Element | Study notes |
|---|---|
| Source role | The Balkan musical character supplies rhythm, melodic flavor, and visual identity. |
| Production goal | Layer club drums under regional rhythm without flattening the feel. |
| MPK use | Pads for layered percussion, keys for stabs and bass, knobs for buildup effects. |
| Practice version | Record claps, a short vocal phrase, or a hand-played melody. |

Lock the downbeat, but do not destroy all timing personality. Some music feels
right because it leans ahead or relaxes behind the grid.

## Balkan/Live-Loop Pad/Knob Sequence

| Bars | Pads | Keys | Knobs | Goal |
|---|---|---|---|---|
| 1-2 | P5 hand percussion only | None | K1 low | Establish human rhythm. |
| 3-4 | Add P1 kick under percussion | Root drone | K2 barely up | Lock the downbeat. |
| 5-8 | P2 clap/snare, P3 hats | Offbeat chord stabs | K3 up | Blend club pulse with regional feel. |
| 9-12 | P6 source hit in gaps | Bass answer phrase | K5 opens | Build the loop visibly. |
| 13-16 | P4 open hat, P7 crash | Full bass + stabs | K6 small reverb lift | Full loop payoff. |
| 17-20 | Strip back to P5 then re-enter | Short lead answer | K7 delay throw | Create a break and return. |

For this style, avoid quantizing every percussion hit to perfection. Keep the
kick reliable, then let supporting percussion breathe.

# Live Looping and Performance Capture

Even if the final video is edited, practice live looping because it teaches fast
decisions.

| Loop layer | Performance tip |
|---|---|
| Drum loop | Record two bars; quantize lightly. |
| Bass loop | Keep it short and repeatable. |
| Chord loop | Use long notes or offbeat stabs. |
| Hook answer | Play a tiny phrase that comments on the source. |
| FX pass | Record knob movement after the notes are solid. |

Film hands, face, source clip, and DAW separately if needed. Record audio
directly in the DAW, not through the camera mic.

# Video Editing for Music Producers

Your edit should prove that the music is interacting with the source.

| Shot | Purpose |
|---|---|
| Source clip | Shows the premise. |
| MPK close-up | Shows pads, keys, and knob moves creating musical events. |
| DAW screen | Optional proof of layering. Use sparingly. |
| Face/performance | Adds reaction and humor. |
| Wide desk shot | Establishes the real setup. |

The first five seconds matter. Make the premise obvious, then let the musical
build carry the rest.

# Copyright, Collaboration, and Credits

Remix culture thrives on reference and transformation, but public uploads can
still run into copyright claims, takedowns, or blocked monetization.

Safer source choices:

- Your own videos and recordings.
- A friend's clip used with written permission.
- Public-domain recordings.
- Creative Commons material where the license allows remixing.
- Paid sample packs and licensed loops.

Good credit habits:

- Keep source URLs and permission notes in the project folder.
- Credit collaborators clearly.
- Do not imply endorsement by the original creator.
- If someone asks you to remove their clip, take the request seriously.

For practice, you can make private remixes that never leave your computer. For
public release, think like both a musician and a publisher.

# Practice Projects

| Project | Goal |
|---|---|
| One phrase, one beat | Take a legal two-bar phrase and build drums only. |
| Bass translation | Add a bass line that makes the phrase feel like a song. |
| Knob performance | Map filter and reverb, then record automation. |
| Live layer video | Film yourself adding drums, bass, and chords. |
| Full remix sketch | Make a 45-second intro, drop, break, and ending. |

Four-week plan:

- Week 1: MPK, MIDI, tempo, tracks, and simple drums.
- Week 2: three 15-second remixes from your own voice memos.
- Week 3: video sync and camera angles.
- Week 4: one finished 45 to 60 second remix.

# Troubleshooting

| Symptom | Likely fix |
|---|---|
| MPK not detected | Try another USB cable/port, avoid hubs, check Audio MIDI Setup, restart DAW. |
| Keys move meters but no sound | Load an instrument plugin and enable monitoring. |
| Pads trigger wrong sounds | Load the correct kit or remap pad notes. |
| Delay while playing | Use wired headphones, lower buffer size, close heavy apps. |
| Audio distorted | Lower input gain and record again. |
| Video drifts | Check tempo, warp/flex settings, frame rate, and variable-frame-rate source files. |
| Export too quiet | Balance the mix, use a limiter, compare at matched volume. |

Before panic: create a new empty project with one software piano track. If the
MPK plays that, the controller is fine and the problem is inside the original
session.

# Quick Reference

| Task | Fast path |
|---|---|
| Start project | Create folder, import source clip, save version `01_import`. |
| Find tempo | Tap tempo, loop source phrase, align to grid. |
| Build groove | Kick, clap, hat, bass. Stop before decoration. |
| Map MPK | Pads to drums; knobs to levels/filter/reverb/delay. |
| Record | Arm track, count-in, loop section, record multiple takes. |
| Mix | Balance source, drums, bass, chords, hooks, FX, limiter. |
| Sync video | Align source audio, cut to beats, export test. |
| Finish | Listen on headphones and laptop, fix, export final. |

# Sources and Further Learning

Primary reference videos:

- <https://www.youtube.com/watch?v=EGmXAu8geVg>
- <https://www.youtube.com/watch?v=CAyWN9ba9J8>
- <https://www.youtube.com/watch?v=hVJtPuuQK_s>

Akai references used for setup and controller behavior:

- Akai MPK mini MK3 product page: <https://www.akaipro.com/mpk-mini-mk3/>
- Akai MPK mini setup article: <https://support.akaipro.com/en/support/solutions/articles/69000798879-akai-pro-mpk-mini-mpk-mini-play-mpk-mini-plus-how-to-download-install-and-setup-the-included-so>
- Akai MPK mini Plus user guide: <https://cdn.inmusicbrands.com/akai/attachments/mpkminiplus/MPK%20mini%20Plus%20-%20User%20Guide%20-%20v1.2.pdf>

Hardware and DAW references used for the expanded setup:

- Apple Audio MIDI Setup for Mac: <https://support.apple.com/guide/audio-midi-setup/set-up-audio-devices-ams59f301fda/mac>
- Apple MIDI Studio setup for Mac: <https://support.apple.com/guide/audio-midi-setup/set-up-midi-devices-ams875bae1e0/mac>
- MOTU M4 product page: <https://motu.com/products/m-series/m4>
- MOTU M4 specifications: <https://motu.com/en-us/products/m-series/m4/specs/>
- Golden Age Audio Pre-73 MKIII: <https://goldenageaudio.com/outboard-hardware/preamps/pre-73-mk-iii/>
- Golden Age Project PRE-73 MKIII manual: <https://goldenagemusic.se/home/goldenageproject/manuals/manual_pre73mk3.pdf>
- FL Studio audio setup: <https://www.image-line.com/fl-studio-learning/fl-studio-online-manual/html/app_wiz2.htm>
- FL Studio audio settings: <https://www.image-line.com/fl-studio-learning/fl-studio-online-manual/html/envsettings_audio.htm>
- FL Studio MIDI settings: <https://www.image-line.com/fl-studio-learning/fl-studio-online-manual/html/envsettings_midi.htm>
- FL Studio audio recording: <https://www.image-line.com/fl-studio-learning/fl-studio-online-manual/html/recording_audio.htm>

Search terms for deeper study:

- GarageBand MIDI controller setup
- FL Studio MIDI settings MPK mini
- FL Studio audio recording MOTU M4
- Logic Pro Flex Time vocals
- Ableton Live warp audio to tempo
- MPC Beats MPK mini mapping
- DaVinci Resolve audio sync
- beginner EQ compression reverb delay
