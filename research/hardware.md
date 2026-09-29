# Hardware research for Professional Podcast Audio

Research date: 2026-09-29. Manufacturer documents are the technical basis; recommendations below are explicitly starting points, not manufacturer-prescribed voice presets or measurements of this room. No recordings were made and no physical setting was changed.

## Verified equipment identity and evidence

- User photo `gear/IMG_6111.HEIC`, decoded by the main task to `gear/previews/rig-rear.jpg`, clearly identifies **PRE-73 PREMIER**, not the MKIV, Jr, or DLX. The PREMIER's high-pass choices are **80 Hz / OFF / 200 Hz**. Do not substitute the current MKIV's 170 Hz setting.
- The red unit is COMP-54. The photo establishes its control labels and positions below, but does not reveal its back-panel revision suffix or serial label. Use “COMP-54, as photographed”; do not assert MKIII solely because that is the current model.
- The BeesNeez PSU in the photo has MIC and PRE sockets and a pattern knob. The mic photo agrees with B67/269 appearance. The UT Twin87 is user-declared but not pictured in these two supplied files.

## Primary source register

1. [BeesNeez B67/269 product and FAQ](https://beesneezproaudio.com/product/u67-style-tube-microphone/) — current manufacturer description, power requirement, load, voicing and S2 explanations.
2. [BeesNeez B67/269 user guide](https://beesneezproaudio.com/wp-content/uploads/2026/05/BeesNeez-B67-269-User-Guide.pdf) — one-page manufacturer PDF; local `research/manuals/BeesNeez-B67-269-User-Guide.pdf`; preview PNG also saved for checking its diagram. This page has no startup, warm-up, voltage-discharge or shutdown timing instructions.
3. [BeesNeez PSU](https://beesneezproaudio.com/product/power-supply/) — manufacturer says supplies can be adjusted for particular tube microphones by contacting them. A matching connector does not establish PSU interchangeability.
4. [United Studio Technologies UT Twin87](https://unitedstudiotech.com/en/products/ut-twin87) — manufacturer's correct brand name (not “United Technologies”). Its Downloads section links the next document.
5. [UT Twin87 owner's manual](https://raddist-cms.s3.amazonaws.com/3613061b-6991-44a7-a400-de52a23979c2/United-UTTwin87-OwnersManual.pdf) — manufacturer-authored document hosted by its distribution CDN and linked from official product page; version 1.0 dated 2021-11-15, 11 PDF pages of two-page spreads. Local PDF and text downloaded.
6. [PRE-73 PREMIER product](https://goldenageaudio.com/outboard-hardware/premier-series-outboard-hardware/pre-73-premier-2/) and [PRE-73 PREMIER manual](https://goldenageaudio.com/wp-content/uploads/2026/04/PRE-73-PREMIER-manual.pdf) — exact photographed variant; local PDF downloaded.
7. [COMP-54 current manufacturer product](https://goldenageaudio.com/outboard-hardware/compressors/comp-54-mkiii/) — primary source for general circuitry and bypass/meter/termination controls. Current product revision is MKIII.
8. [COMP-54 manufacturer-authored manual, dealer-hosted mirror](https://www.adorama.com/col/productManuals/GACOMP54MK2.pdf) — two-page original Golden Age Project document; not a dealer review. It explains controls, 600-ohm termination and meter reference. The old manufacturer's indexed `https://goldenagemusic.se/home/goldenageproject/manuals/COMP-54-MKIII-manual.pdf` now returns 404. Current Golden Age product page did not offer a manual link. The mirrored manual was readable in the web tool; direct local download failed DNS. Treat revision-specific claims conservatively. Its document title is COMP-54; filename alone is not proof of the user's revision.
9. [MOTU M Series user guide](https://cdn-data.motu.com/manuals/usb-c-audio/M_Series_User_Guide.pdf) — local PDF and text downloaded. M4 quick reference printed page 8/PDF page 8, connections printed 18–19, monitoring printed 22–23, specifications printed 27–28.
10. [MOTU M4 specs](https://motu.com/en-us/products/m-series/m4/specs/) — URL fetch returned 502 during research. [MOTU Poland's M4 page](https://www.motu.com.pl/motuaudio/m4.html) states directly that hardware monitoring is mono/stereo for inputs 1–2 and stereo for inputs 3–4. The M Series manual's description of the rear 3–4 button points to the 1–2 explanation without clearly spelling out this important difference. Avoid claiming that holding 3–4 creates a centered mono monitor.

## Routing, power and common baseline

These are engineering recommendations derived from the documented connectors and levels. They should be illustrated using the user's photos plus original diagrams, rather than reproducing whole manual pages.

### BeesNeez chain

`B67/269 → supplied compatible 7-pin cable → matched BeesNeez PSU MIC socket → PSU PRE (3-pin microphone-level output) → PRE-73 PREMIER rear mic input → PRE main balanced OUT → COMP-54 balanced IN → COMP balanced OUT → M4 rear LINE IN 3 → USB → Mac`

- PRE LINE and DI off. PRE 48V **off**. M4 front 48V buttons **off**. The external tube PSU powers the microphone; its output still needs the microphone preamp.
- Use the PSU and 7-pin lead supplied/configured for this exact mic. Do not substitute another tube supply based on socket fit. Verify PSU mains rating against the local supply/label; do not describe an unseen voltage selector as present or automatically safe.
- Mute/lower monitoring; power off the mic supply before connecting or disconnecting the 7-pin lead. Restore power after cabling. Allow the mic to stabilize; record the same chosen stabilization interval for comparisons. No exact manufacturer warm-up time was found.
- Internal voicing changes require an unpowered, disconnected, cooled mic and the unit-specific manufacturer's handling instructions. The published guide shows physical access but does not specify a safe discharge interval. Never imply that an invented five/ten/thirty-minute wait makes exposed circuitry safe. Keep the tutorial able to complete an external-control baseline without opening the mic. Have BeesNeez confirm the procedure/revision before first internal access; do not open the PSU.

### United chain

`UT Twin87 → balanced 3-pin XLR → PRE-73 PREMIER rear mic input → PRE main balanced OUT → COMP-54 balanced IN → COMP balanced OUT → M4 rear LINE IN 3 → USB → Mac`

- No BeesNeez PSU in this chain. PRE LINE/DI off. Connect both cable ends with PRE 48V off, then turn PRE 48V **on**. M4 front 48V stays off.
- For disconnecting, lower monitoring, switch PRE phantom off, wait at least the PRE manual's approximately ten seconds, and follow the mic manual's discharge instruction before unplugging. Do not route the raw phantom-powered mic through a TRS/TT patchbay.
- The United manual requires intact XLR pin-1 grounding; avoid ground-lift microphone leads or defeating mains protective earth. With USB bus power and two-pin supplies, troubleshoot hum using proper grounded equipment and support, not improvised wiring.

### Shared connection details

- PRE → COMP: balanced XLR–XLR or balanced TRS–TRS main audio connections. COMP → M4 rear 3: balanced TRS–TRS, or XLR-female → TRS if using COMP's male XLR output. A balanced mono TRS cable is not a stereo microphone cable.
- Leave PRE INSERT unused. On the PREMIER it is an **unbalanced** low-level insert, roughly −10 to −18 dBu, tip send/ring return. It is not the simplest full-level connection for COMP-54.
- COMP is line level; it follows PRE, not the unamplified mic. Rear M4 input 3 has no front gain control. Manage its level upstream.
- Record **mono input 3**, not stereo 3–4. Center the DAW pan. Rear direct monitoring is stereo: an input only on 3 may sound left-only. Recommended rear-input tutorial: 3–4 hardware monitor off, DAW software monitor on, monitor mix toward PLAYBACK. Use headphones; keep speakers quiet while recording.
- Alternative when the performer needs centered hardware monitoring: route COMP to M4 **front input 1's TRS jack**, gain fully counterclockwise, 48V off; enable MON 1 in mono mode and turn DAW monitoring off. This uses M4's variable-gain input at minimum; it is not a documented complete preamp bypass. Change DAW source to mono 1 and recalibrate level.
- M4 documented max levels: rear line +18 dBu; front TRS +16 dBu at minimum gain; front XLR +10 dBu at minimum gain. Use a quarter-inch line connection for outboard output rather than the front XLR microphone socket. No phantom on TRS inputs.

## All PRE-73 PREMIER controls, as photographed

| Control | Meaning / available setting | Suggested initial value |
|---|---|---|
| POWER | Front on/off, matched external 24 V **AC** supply | On after cabling |
| 48V | Phantom on rear mic input | Off B67; on Twin87 after cabling |
| LINE | Pads input by 30 dB for line sources | Off for both mics, including B67 PSU output |
| DI | Front instrument input selection | Off; jack empty |
| LOW-Z | Off 1200 Ω / on 300 Ω | Off (1200 Ω) |
| GAIN | Mic switch spans 20–80 dB | Start 20–30 dB; raise by labeled steps to measured peaks |
| HIGHPASS | 80 Hz / OFF / 200 Hz, 6 dB/octave | Off for comparison; test 80 for final speech |
| AIR EQ | +3 / OFF / +6 dB around 30 kHz | Off |
| OUTPUT PAD | 0 / 14 dB attenuation after transformer | 0; avoid driving output stage for baseline |
| OUTPUT | Fine level trim ahead of output amplifier | At/near maximum for least drive, then trim to target |
| Ø | Polarity reversal | Normal; relevant only when summing paths |
| LEDs | Power and output level/clip indications | Observe, but M4/DAW input peak is final ADC check |
| Rear combo IN | Mic/line source, mode selected at front | Balanced XLR microphone lead |
| Rear XLR/TRS OUT | Main balanced line output | One main output to COMP |
| Rear INSERT | Unbalanced tip-send/ring-return, low internal level | Unused |
| Internal JP1 | 600 Ω output termination | Leave current factory/service configuration; log if known |

BeesNeez specifies a recommended load of at least about 1 kΩ; LOW-Z off is therefore the appropriate comparison baseline. The PRE manual says LOW-Z alters tone **and level**. It is an optional Twin87 test, not a default B67 setting. The PRE 14 dB pad reaches its nominal attenuation only with JP1 termination engaged. Do not promise a 14 dB measured drop without confirming that configuration. The PRE's second input gain stage enters above 50 dB; changing gain and compensating with OUTPUT changes tone as well as level.

## COMP-54 controls and photo-confirmed positions

| Control | Available settings / behavior | Proposed speech start |
|---|---|---|
| THRESHOLD | Stepped; photograph shows labels −10, −4, 0, +4, +10; extremes partially obscured | Start at highest threshold, then lower until chosen GR target |
| RATIO | 1.5:1, 2:1, 3:1, 4:1, 6:1 | 2:1 |
| ATTACK (ms) | 0.5, 1, 2, 3, 6, 12, 25, 50 | 12 ms |
| RECOVERY | 25, 50, 100, 400, 800 ms, 1.5 s, Auto 1, Auto 2 | 100 ms; test 400 ms if pumping |
| SC HP | OFF, 50 Hz, 100 Hz, 7 kHz | 100 Hz for speech; OFF for neutral control experiment |
| MAKEUP GAIN | Continuous, no exact dB scale visible | Minimum initially; adjust by meters and loudness match |
| POWER | On/off | On after wiring |
| LINK | Link compressor action with another matching unit | Off for this mono chain |
| IN/OUT / OUT | Compression out retains audio circuit coloration | Compression in only after clean calibration |
| METER | COMP/GR or OUTPUT | COMP/GR during recording |
| BYPASS | Hard bypass routes input directly to output | On for first clean calibration; off for compression |
| Rear 600 OHM TERM | Adds output transformer load | Engaged for modern high-impedance interface, per manual |
| Rear I/O | Parallel XLR/TRS line input/output connectors | One input source, balanced output to interface |

SC HP filters the **detector**, not the recorded audio path. The 100 Hz setting reduces low-frequency triggering; it does not remove rumble from the audio. The 7 kHz position can make compression respond mostly to sibilance, but the gain reduction still affects the whole signal; do not call it split-band de-essing. Auto modes depend on program material; no exact timing formula was located in the manufacturer document, so do not invent one.

The manufacturer-authored manual sets factory OUTPUT 0 VU at about +4 dBu and warns against prolonged needle slamming. COMP/GR mode is the useful tracking view. **0 VU is not 0 dBFS.** Under ideal calibration, +4 dBu into a rear input whose full scale is +18 dBu leaves about 14 dB margin; actual voice peaks still need observing. Do not direct the beginner to calibrate internal meter trimmers. A photographed “OUT” button means pressing it removes compression; do not confuse it with the separate BYPASS. State functional goals (“compression active,” “hard bypass off”) and verify GR, rather than relying on unclear photo button depth.

## B67/269 settings inventory

PSU pattern knob: nine positions spanning omni → cardioid → figure-eight, with intermediate patterns. Choose the **cardioid icon**, not an unverified clock position. For a one-person podcast, compare distance and angle in cardioid before exploring other patterns.

The official guide shows five internal functions. In the guide's own diagram orientation (not universally “left on the microphone”):

| Function | Diagram left | Diagram right |
|---|---|---|
| Pad | Off | −10 dB on |
| High-pass | Off | On |
| S2 bridge / broadcast filter | Off | On |
| Sound profile | New | Vintage |
| Voicing | 269 | 67 |

Do not assign SW1–SW5 numbering unless the actual unit markings match. The PDF has no electrical schematic or high-pass cutoff value; leave this HPF frequency unspecified. S2 is a separate LF filter, described by the manufacturer as rolling off below approximately 40 Hz. It is not identical to the mic's separate HPF.

Four voicing profiles: 67 Vintage/Old, 67 New, 269 Vintage/Old, 269 New. Manufacturer tonal descriptions are subjective; they are hypotheses to test on the user's voice. Proposed comparison baseline: cardioid, pad off, mic HPF off, S2 off, 67 Vintage. If opening has not been verified, use current documented voicing and mark it “as found / internal mode unverified” rather than telling the user an unknown factory default.

## UT Twin87 settings inventory

External: three-way polar pattern (omni/cardioid/figure-eight), HPF off/on, −10 dB pad off/on, Vintage/Modern circuit selection. Internal: RF-filter DIP group. Manufacturer specifies the HPF as **80 Hz at its 12 dB-down point**; that is not the same as a 12 dB/octave slope or conventional −3 dB cutoff.

Wait about ten seconds after Vintage/Modern switching before the take; polar-pattern changes also require settling. Modern is documented as hotter, so reset gain or match playback loudness before judging tone. Set pad off for ordinary speech; use it for actual microphone overload, not to solve post-preamp clipping.

The internal RF filter ships bypassed according to the manual. RF enabled in its illustrated orientation: switches 1 and 5 down, 2/3/4 up; bypass inverse; switch 6 always down. This is a coordinated switch group, not six independent tone presets. Follow the owner's guide illustrations and disconnect power before access. Leave it as found unless interference requires the documented optional procedure; log the state as unknown if not inspected. RF choice is distinct from the external HPF and Vintage/Modern switches.

Proposed normal baseline: cardioid, pad off, HPF off for comparison, Vintage first, RF as found. Modern second with matched capture peaks and matched listening loudness. Start with a pop filter and 15–20 cm mouth-to-capsule distance, 10–20° off axis; these are editorial test coordinates, not measured best settings.

## M4 control inventory and Mac notes

- Front gains 1/2: irrelevant to rear 3/4 capture. Leave minimum when unused. Front 48V 1/2 off for the outboard chain.
- MON 1/2: optional direct input monitors; holding switches mono/stereo mode for front pair. With rear3 software monitoring, keep both off.
- 3–4 button: rear-pair direct monitor. Off in the software-monitor route.
- INPUT MONITOR MIX: INPUT counterclockwise / PLAYBACK clockwise; for DAW monitoring turn toward PLAYBACK. It changes headphone/monitor blend, not recorded input gain.
- Large MONITOR: rear monitor-output listening volume. Small headphone knob: independent headphone listening volume. Neither changes recording gain. Raise from quiet to comfortable, no universal clock position.
- LCD: all input/output levels; red means overload, blue channel marker means hardware monitor active. MIDI unused in voice-only chain. USB provides power and audio. Rear outputs 1/2 are main monitor; 3/4 available separate outputs; RCA mirrors the corresponding TRS outputs.
- macOS class-compliant operation needs no driver for basic I/O; optional MOTU driver provides extra capabilities including loopback. Do not make driver installation mandatory for a first recording.
- Use M4 for both DAW input and output. A separate system output choice need not be changed if the DAW selects M4 explicitly. Audio MIDI Setup and the DAW must agree on sample rate; use DAW's supported rate. The Mac research agent should resolve GarageBand's rate constraints rather than assuming all DAWs expose a rate selector.

## Recommended comparison design (editorial, not manufacturer settings)

1. Save clean first takes with COMP hard-bypassed and all optional EQ/filters off. Fix chair, pop screen, mouth distance, angle, room treatment, and script. Record room tone plus normal, quiet and deliberately loud speech.
2. Calibrate each mic/profile independently. Set PRE gain/output while the loud test does not clip; aim ordinary peaks around −18 to −12 dBFS and loud peaks with at least 6 dB headroom. These targets are starting ranges, not mandatory delivery loudness. Do not use the same numeric gain merely to claim fairness when sensitivities differ.
3. Compare B67's four documented profiles against Twin87 Vintage and Modern, in cardioid, 15–20 cm, same clean chain. Repeat the script at least twice; alternate A/B/A order to reduce performance drift. Retain an unprocessed take.
4. First vary geometry (10, 15–20, 30 cm; 0°, 15°, 30°) for shortlisted modes. Then choose one high-pass location at a time: mic, PRE 80, PRE 200. Do not stack filters while deciding which helped. PRE 200 often removes desired voice body; audition rather than prescribe.
5. Compression stage: ratio 2:1, attack12 ms, recovery100 ms, SC HP100 Hz, link off, hard bypass off, compression in, meter GR. Lower threshold until normal phrases show 1–3 dB reduction and strong phrases roughly 4–6 dB. Restore output only enough to match bypass and keep ADC headroom. If pumping, compare recovery400 ms and Auto1. If consonants dull, compare attack25 ms; if peaks uncontrolled, compare6 ms.
6. To test every *setting*, use one-control sweeps, returning to the same reference after each sweep: all ratio positions; all attack positions; all recovery positions; OFF/50/100/7K detector filter; mic pad/HPF; PRE air/HP/polarity/impedance where applicable. Do not claim this exhausts all cross-products. Full combinations are both enormous and confounded. Fixed-threshold sweeps answer how a control behaves; reset-to-same-GR sweeps answer how different settings sound at comparable reduction. Label these experiments distinctly.
7. Compare live mic voicings by repeatable spoken takes. For compressor sweeps, optional offline replay through an M4 output into COMP can hold the performance fixed, but requires a dedicated send/return and monitoring safeguards; never feed interface line output into a phantom-powered microphone input. The simpler tutorial can omit physical reamping and retain repeated scripts.
8. Match **perceived/program loudness**, not peak level, before blind judging. Keep originals, create audition copies with gain only and match using a loudness meter or careful listening; randomize names, score naturalness/sibilance/room/comfort, and revisit next day. A tone change is not a win because it is louder.

Recommended take filename fields: date, microphone, mode, pattern, distance_cm, angle_deg, mic_pad, mic_HPF, S2_or_RF, PRE_gain, PRE_output_reference, PRE_HPF, PRE_AIR, PRE_pad, PRE_lowZ, COMP_ratio, attack_ms, recovery, threshold_mark, SC_HP, observed_GR, makeup_reference, input_number, DAW, sample_rate, notes. Photograph unlabeled continuous knobs and record a normalized clock position together with measured peaks; clock position alone is not an exact repeatable dB setting.

## Unresolved items to represent honestly

- COMP hardware revision and rear labels are not visible. Core control functions and photo labels are verified; no inference of an Insert jack or future revision-specific feature.
- B67 internal switch orientation/revision, current internal voicing, current S2/HPF states, exact safe access/discharge procedure and warm-up time are not established by the supplied photos/current one-page guide.
- Twin87 current switch states/RF state are not pictured. Do not say factory defaults were inspected.
- The PRE internal JP1 termination and actual compressor meter calibration are unknown. Do not claim analog-to-digital calibration has been measured.
- A book and browser tutorial cannot set analog knobs. Interactive selections must be called recall/checklist settings, with observed meters and listening determining final gain/threshold.
