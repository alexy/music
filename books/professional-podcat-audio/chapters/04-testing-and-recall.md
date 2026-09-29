# A laboratory you can run at your desk

The comparison chapter explains a fair audition. This chapter turns that method into a complete test plan. You do not need to record every possible combination. You need a baseline, a clearly named variable, a repeatable passage and a decision. Keep the factory manuals beside this book when checking an unfamiliar switch.

![Work in this order. A mic-mode test and a complete finished-chain test answer different questions.](assets/comparison.png)

## The baseline and six named microphone profiles

Start with **B-ASFOUND** and **T-VINTAGE**. Record three takes of each, alternating microphone order when time allows. Add **T-MODERN** after the documented settling time and recalibrate. If the manufacturer has confirmed your unit's safe internal handling procedure, add the four BeesNeez states: **B-67-VINTAGE**, **B-67-NEW**, **B-269-VINTAGE**, **B-269-NEW**. Do not infer a hidden switch from the sound of a recording. Unknown settings stay “unknown” in the log.

For each profile, use the raw recipe: cardioid, COMP hard bypass, PRE high-pass and Air off, M4 rear Input 3, no DAW processing. A BeesNeez with unknown internal filters remains an **as-found system comparison**, not a proof that its bare capsule or circuit is flat. The other microphone's raw take is still useful; the label states the limit.

Record the same script and room tone. Write the actual PRE gain and output, input peak, capsule distance and microphone state for every file. Rename each audio file before moving on. An example is `2026-09-29_T-MODERN_raw_20cm_take02.wav`. Use simple filenames so exports, backups and the vault can all refer to the same take.

## Test every control without testing every combination

The accompanying `control-sweeps.csv` names the controls, candidate positions, prerequisites and listening question. It covers the user controls of both mics and the shared chain. Continuous controls such as output level and makeup gain have infinitely many possible positions, so test defined reference points and write the actual mark. Do not claim a finite preset matrix exhausts them.

Use this five-part method for each sweep:

1. Recall the clean reference and record ten seconds of it.
2. Change exactly one selected control. For a discrete control, use the next printed position. For a continuous control, choose a clearly measurable target such as matched bypass loudness. For the stepped threshold, choose the nearest detent producing 1, 3 or 6 dB indicated gain reduction.
3. Record the same passage. Note peak level and any audible overload.
4. Return to the reference and record it again. This A/B/A pattern helps expose changing performance or room noise.
5. Loudness-match listening copies, score blind if possible, and write “keep,” “reject,” or “repeat.”

There are two valid compressor experiments. In a **fixed-threshold sweep**, leave threshold and makeup unchanged as you change ratio, attack or recovery; this shows how the control changes level and envelope. In an **equal-reduction sweep**, reset threshold to produce the same approximate reduction and then match output loudness; this better isolates the audible envelope. Name the experiment in the log. Mixing their conclusions is misleading.

## A manageable order for the full sweep

| Pass | Conditions | What to listen for |
|---|---|---|
| Placement | 15, 20, 30 cm; then 0, 15, 30 degrees | Plosives, proximity bass, room sound, consistency |
| Mic identity | Bees as found; Twin Vintage/Modern; verified Bees profiles later | Intelligibility and fatigue after loudness matching |
| Polar pattern | Cardioid first; omni and figure-eight; Bees intermediate positions if needed | Room pickup and rear sensitivity, not just bass |
| Microphone pad | Off versus -10 dB, then level-match | Actual microphone overload; unnecessary attenuation adds gain demand |
| Mic LF filters | Each available filter separately, only when accessible through verified procedure | Rumble versus lost voice body |
| PRE high-pass | Off, 80 Hz, 200 Hz | Plosive/desk rumble versus thin voice |
| PRE Air | Off, +3, +6 dB | Subjective openness versus hiss/sharpness; no assumed benefit |
| PRE impedance | Twin87 at 1200/300 ohms; Bees stays 1200 baseline | Tone and level change; recheck gain |
| PRE gain/output | Clean low-gain/high-output versus one gain step up/output reduced | Coloration at equal loudness and safe peaks |
| COMP ratio | 1.5, 2, 3, 4, 6:1 | Sentence steadiness and flattened emphasis |
| COMP attack | 0.5, 1, 2, 3, 6, 12, 25, 50 ms | Consonant clarity and escaped peaks |
| COMP recovery | 25, 50, 100, 400, 800 ms, 1.5 s, Auto 1, Auto 2 | Pumping, breaths and recovery between phrases |
| COMP detector | Off, 50 Hz, 100 Hz, 7 kHz | Low-frequency triggering versus sibilant triggering |
| DAW finishing | Exact same take; one device/control changed at a time | Whether the effect earns its place |

Polarity has no expected tonal benefit on an isolated mono track. Test it only to learn that the waveform flips or when summing correlated paths. LINE and DI are source-routing choices, not microphone tone auditions. Phantom, mains power and connector selection are setup controls, not sweeps to perform during recording. The CSV labels these as functional checks rather than listening experiments.

## Use the two DAWs as a cross-check

A clean take should not acquire a new personality just by opening it in a different DAW. Export one 24-bit reference, import the same file into both applications, disable every effect and normalization option, center the pan and keep sample rates consistent. Disable Warp in Live. Match playback loudness and compare. If they differ, inspect routing, pan law, stereo/mono layout, automatic processing and level before attributing the difference to a “DAW sound.”

For a microphone comparison, stay inside one DAW and one rate. For a DAW comparison, use the same recorded file. Changing microphone, performance and software at once prevents a useful conclusion.

## A practical scoring sheet

Score six qualities from 1 (poor for your purpose) to 5 (excellent): intelligibility, natural body, controlled sibilance, controlled plosives, low room distraction and low listening fatigue. Define “better” before the test: for a long explanatory podcast, easy-to-follow quiet words may matter more than a dramatic bass sound.

Add a one-sentence observation and one action. For example: “At 15 cm the P sounds hit hard; use 20 cm and move 15 degrees sideways.” This is a better recall instruction than “less boomy.” Repeat promising conditions on another day. If the winner changes across three takes, report a tie and choose the more comfortable or repeatable setup.

Do not compare the unadjusted loudness of the room-tone files as proof of microphone self-noise. Different mic sensitivity and gain, room activity, spectral balance and editing all matter. A household room-tone comparison is a **system-noise and room-pickup test**. It is useful without pretending to be an anechoic laboratory specification.

# Daily operation and fault finding

## Your preflight in under two minutes

Open the saved template for the chosen mic. Read the phantom-power line aloud. Check the actual microphone position and pattern. Confirm PRE LINE/DI off, the correct high-pass state, compressor bypass/active state, M4 mono Input 3 and exactly one monitor path. Record the loudest sentence. Check the input peak, listen back and say the setting ID at the beginning of the take. Then record the episode.

Afterward, save and copy the project. Export a listening file, verify the entire duration and write the filename on the recall note. Keep the raw recording separate from the edited master. Save a photo of the physical panel after changes, but also write the numbers: a photo can hide a pushbutton state.

## Troubleshoot from upstream to downstream

| Symptom | First check | Next action |
|---|---|---|
| No M4 input meter | Mic power, PRE mic mode, COMP bypass, correct line cable | Follow the chain one unit at a time; lower monitors before repatching |
| M4 meter moves, DAW does not | M4 selected, macOS permission, mono Input 3 enabled | Check track source and record selection/arm |
| Voice appears only in left ear | Rear 3-4 direct monitoring or stereo 3/4 track | Use DAW mono 3 with 3-4 MON off |
| Hollow or doubled voice | Hardware and software monitoring both active | Disable one path; replay a recording to distinguish monitor from file |
| Clean in bypass, distorted active | COMP input, makeup, output or M4 level | Reduce upstream level and makeup; do not fix with DAW fader |
| Distortion despite safe digital peak | Mic/preamp overload or intentional preamp drive | Reduce PRE gain, restore clean output trim, retry; test mic pad only if mic overload is suspected |
| Loud plosives | Direct breath striking capsule | Move off axis, use pop filter, increase distance before more EQ |
| Thin, brittle voice | Several high-pass filters, PRE 200 Hz, excessive treble shaping | Bypass filters one at a time and compare at equal loudness |
| Room noise rises after each word | Fast recovery or too much compression/makeup | Reduce GR and compare 400 ms recovery; improve room noise |
| Crackles only in software monitoring | Buffer too small, CPU load, USB issue | Try 256 samples in Live, bypass heavy effects, test direct USB |
| Voice changes when Mac modes change | Voice Isolation or software processing | Select Standard Mic Mode when available; remove hidden effects |
| Export unexpectedly loud | Automatic normalize/full-volume export | Disable it, check master processing and export again |
| Hum or RF interference | Cable integrity and device grounding | Use proper balanced leads and manufacturer advice; never defeat protective earth |

## Three useful level distinctions

**Recording peaks** protect the converter and preserve headroom. **Gain reduction** tells you how hard a compressor is working. **Integrated loudness** describes the average perceptual level of the finished file. None can substitute for the others. A podcast can peak safely but remain too quiet; a loud master can still contain clipped raw audio; a VU meter at zero does not mean a digital peak at zero.

Leave capture headroom. Measure the exported file against your destination's requirements, listen to the encoded version, and retain an uncompressed master.

# Your Obsidian book and interactive tutorial

The PDF is the fixed-layout desk edition. EPUB is the reflowable reader. The Obsidian edition splits the same manuscript into linked chapter notes, retains the illustrations, and adds a home page, recall template, test script and sources. Open the generated vault as its own vault; begin at `Home.md`. The optional FirstPair reader plugin is disabled by default, so normal Markdown reading does not depend on trusting a community plugin.

Use the vault's session template for actual measurements. Duplicate it for each recording and keep user notes in your own working copy. Generated editions can be rebuilt from source; your listening observations should not be placed where a rebuild will overwrite them. A source/units ledger allows the edition to be checked against the manuscript.

The browser tutorial begins with **microphone**, then **known mode**, **recipe**, and **DAW**. Its three recipes are Raw reference, Everyday spoken voice and Expressive voice. Each view gives the complete mic/power, PRE, COMP, M4 and software settings. Follow the numbered steps, mark checkpoints, then print the recall card or export your comparison log as CSV. Progress and logs are stored in that browser on that device. Export them before clearing browser data or changing browsers.

Selecting a microphone in the tutorial changes displayed instructions only. It does not send commands to the preamp, switch phantom power or inspect the real hardware. The internal BeesNeez profile choices record a known physical state; they do not authorize opening or changing a powered microphone. The tutorial remains useful with the safe as-found option.

# Source register and illustration credits

Manuals are linked, not republished. Recipes, script and diagrams are original synthesis. Sources were checked on 29 September 2026; installed software may differ. References use printed page numbers where available.

| Source | Used for |
|---|---|
| [BeesNeez B67/269 product and FAQ](https://beesneezproaudio.com/product/u67-style-tube-microphone/) | Supply, load, pattern and profile context |
| [BeesNeez B67/269 one-page user guide](https://beesneezproaudio.com/wp-content/uploads/2026/05/BeesNeez-B67-269-User-Guide.pdf) | Five internal switch functions and diagram orientation |
| [BeesNeez power supplies](https://beesneezproaudio.com/product/power-supply/) | Supply compatibility requires matching configuration |
| [United UT Twin87 product/downloads](https://unitedstudiotech.com/en/products/ut-twin87) | Product identity and official manual access |
| [UT Twin87 owner's manual](https://raddist-cms.s3.amazonaws.com/3613061b-6991-44a7-a400-de52a23979c2/United-UTTwin87-OwnersManual.pdf) | External controls, switching, grounding and internal RF group |
| [PRE-73 Premier product](https://goldenageaudio.com/outboard-hardware/premier-series-outboard-hardware/pre-73-premier-2/) | Exact photographed model |
| [PRE-73 Premier manual](https://goldenageaudio.com/wp-content/uploads/2026/04/PRE-73-PREMIER-manual.pdf) | Input modes, 80/200 Hz filters, Air, pad, output and insert |
| [COMP-54 manufacturer product](https://goldenageaudio.com/outboard-hardware/compressors/comp-54-mkiii/) | Current model controls; revision kept explicit |
| [Golden Age COMP-54 manual, dealer-hosted original](https://www.adorama.com/col/productManuals/GACOMP54MK2.pdf) | Manufacturer-authored operation text; original manufacturer PDF URL was unavailable |
| [MOTU M Series User Guide](https://cdn-data.motu.com/manuals/usb-c-audio/M_Series_User_Guide.pdf) | M4 quick reference p.8, connections pp.18-19, monitoring pp.22-23, specifications pp.27-28 |
| [MOTU Poland M4](https://www.motu.com.pl/motuaudio/m4.html) | Explicit stereo rear 3-4 direct-monitor description |
| [GarageBand for Mac guide](https://support.apple.com/guide/garageband/welcome/mac) | Setup, monitoring, effects, editing and export; individual sections linked in chapters |
| [Live 12 manual](https://www.ableton.com/en/manual/welcome-to-live/) | Audio routing, editing, device and export controls |
| [Ableton Lite edition comparison](https://www.ableton.com/en/upgrade-live/) | Devices available in Lite; do not assume Suite features |
| [Apple Podcasts audio requirements](https://podcasters.apple.com/support/893-audio-requirements) | Finished delivery loudness and true-peak guidance |
| [FFmpeg ebur128 documentation](https://ffmpeg.org/ffmpeg-filters.html#ebur128) | Optional measurement of exported files |

Photographs: owner-supplied `IMG_6110.HEIC` (BeesNeez) and `IMG_6111.HEIC` (stack), converted without retouching. Twin87 is not pictured. Cover, diagrams and layout are original. No manufacturer endorsement is implied.

## Edition notes

First edition, 1.0.0. Instructions were source-checked; no acoustic tests were performed. Complete the empty worksheets with your own recordings and measurements.
