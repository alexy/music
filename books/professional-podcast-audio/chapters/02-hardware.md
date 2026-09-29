# Choose the microphone's starting state

Start with a setting you can identify, photograph and repeat. A microphone's switches change what arrives at the preamp, so choose them before calibrating gain. The clean reference leaves optional tone shaping off wherever you can verify it. An unknown internal switch stays **as found, unverified** in your notes; the book does not infer its position from the microphone's appearance.

## BeesNeez: begin with the external controls

Use its matching power supply and cable, with PRE-73 phantom off. Select the **cardioid symbol** on the supply's pattern knob. Cardioid favors the front and reduces pickup from behind; it is a useful first choice for one speaker. Read the symbols rather than copying a clock position from a perspective photograph. The nine positions span omni, cardioid, figure-eight and intermediate patterns. Other patterns are experiments for a particular room or arrangement, not automatic quality upgrades.

For your first take, retain the internal settings as found. Write “B67/269, cardioid, internal profile unverified” if you have not inspected them. This is a valid baseline. Settle the microphone, rehearse, and make a fresh level check before recording. Use a consistent stabilization interval when comparing takes; the linked guide does not specify a manufacturer warm-up duration.

BeesNeez documents two voicings, each with two profiles: **67 Vintage/Old, 67 New, 269 Vintage/Old and 269 New**. The manufacturer describes the New profiles as adding presence or openness. Treat those descriptions as listening prompts. They do not predict which choice flatters your voice. The recommended load is at least about 1 kΩ, so keep PRE LOW-Z off, giving its 1200 Ω input. [BeesNeez B67/269 product and FAQ](https://beesneezproaudio.com/product/u67-style-tube-microphone/)

## The five internal BeesNeez functions

The following is an orientation key to the manufacturer's diagram, **not a claim about left and right on an unseen circuit board**. Match your unit and guide before using it. Do not invent switch numbers where the actual markings are unknown.

| Function | Left in the guide's diagram | Right in the guide's diagram |
|---|---|---|
| Pad | Off | −10 dB on |
| High-pass filter | Off | On |
| S2 bridge / broadcast filter | Off | On |
| Sound profile | New | Vintage |
| Voicing | 269 | 67 |

The guide shows the body sleeve removed to access these controls. It does not supply a discharge interval. Before first internal access, obtain the handling procedure for your exact unit from BeesNeez. Stop, lower monitoring, power down, disconnect and follow that procedure; never change exposed switches with the microphone powered. Do not open the supply. You can complete the recording lessons using the external baseline while this remains unverified. [BeesNeez switch guide](https://beesneezproaudio.com/wp-content/uploads/2026/05/BeesNeez-B67-269-User-Guide.pdf)

Once access is verified, photograph the original state. For a four-profile comparison, keep pattern, pad, microphone HPF and S2 unchanged while varying only voicing/profile. An explicitly documented all-flat comparison uses pad off, mic HPF off and S2 off. The pad reduces level and increases overload margin; ordinary speech usually needs no pad. S2 and the microphone HPF are separate bass-shaping choices. Do not assign the latter an invented cutoff frequency.

## Twin87: a visible pair of circuit choices

Set **cardioid, pad off, HPF off**, and begin with **Vintage**. The microphone uses PRE phantom power after its balanced XLR cable is fully connected. Wait about ten seconds after a Vintage/Modern change before recording. A pattern change also needs time to settle. Modern produces a hotter signal, so recalibrate the preamp or compensate playback loudness before judging tone.

Its external controls are pattern, Vintage/Modern, HPF and −10 dB pad. The HPF specification is **80 Hz at the 12 dB-down point**; that wording does not establish a 12 dB/octave slope. Test the filter against the same passage with it off. If the voice loses useful weight, retain more bass and address plosives with placement first.

There is also an internal RF-filter switch group. Leave it as found and record “unverified” if you have not inspected it. The manual's complete combinations are RF enabled: 1 and 5 down, 2/3/4 up; bypassed: the inverse; **6 always down**, in the illustrated orientation. These are coordinated states, not six independent tone options. Use the exact guide and disconnect power before access. The RF filter addresses interference and is separate from the external audio HPF. [UT Twin87 owner's manual, sections 1.2–1.5](https://raddist-cms.s3.amazonaws.com/3613061b-6991-44a7-a400-de52a23979c2/United-UTTwin87-OwnersManual.pdf)

# Set the PRE-73 Premier for a clean reference

The preamp has two level controls for different jobs. **GAIN** sets amplification in labeled steps. **OUTPUT** trims what proceeds through its output stage. Begin with gain **30 dB** and OUTPUT **at or near maximum**, with quiet monitoring. Adjust gain to the voice, then use OUTPUT for a small final correction. This gives a useful clean reference before intentionally driving the input stages harder.

![The PRE-73 Premier recall map. Check phantom power against the selected microphone before calibrating.](assets/preamp-map.png)

## Every front-panel control

| Control | What to set first | What a later change does |
|---|---|---|
| POWER | On after cabling | Powers the unit from its proper 24 V AC adapter. |
| 48V | B67 off; Twin87 on after cabling | Supplies phantom to the mic input. |
| LINE | Off | Selects the attenuated line-input operating mode. |
| DI | Off; instrument jack unused | Selects the front instrument input. |
| LOW-Z | Off, 1200 Ω | On gives 300 Ω and changes microphone loading. |
| GAIN | 30 dB, then calibrate | Sets mic amplification across the 20–80 dB range. |
| HIGHPASS | Off | Selects 80 or 200 Hz bass roll-off. |
| AIR EQ | Off | Selects +3 or +6 dB high-frequency shaping. |
| OUTPUT PAD | 0 dB | The 14 dB position attenuates after the transformer. |
| OUTPUT | At/near maximum, then trim | Fine adjustment of outgoing level. |
| Ø | Normal polarity | Reverses polarity; mainly useful when combining paths. |

This is the **Premier** control set shown in your photograph. Its high-pass filter has a 6 dB/octave slope; Air is centered around 30 kHz. Other PRE-73 editions have different facilities, so follow this unit's labels. [PRE-73 Premier specifications](https://goldenageaudio.com/outboard-hardware/premier-series-outboard-hardware/pre-73-premier-2/)

The power indicator confirms the unit is on. The output LEDs provide useful warnings, including clipping, but they do not replace the M4 input meter. With the compressor bypassed, perform your loudest expected line. If it clips, reduce PRE gain. If it is comfortably below the intended recording range, increase gain one step and repeat. Ordinary speech peaks around −18 to −12 dBFS are a useful start; keep the loud rehearsal at or below roughly −6 dBFS. Leave room for an unexpected laugh.

A small OUTPUT correction can place a gain step between two useful levels. If the recording sounds rough while its digital peaks look safe, reduce GAIN and restore level with OUTPUT. Distortion may have happened before the converter. Lowering a track fader cannot repair it.

## Rear connections and the hidden termination

The rear combo input receives the microphone lead. Use a main balanced XLR or TRS output to feed COMP-54. Leave the INSERT empty for this workflow: it is an unbalanced internal send/return at a lower operating level, approximately −10 to −18 dBu. It is not interchangeable with the main balanced output.

The internal JP1 jumper controls a 600 Ω output termination. Leave its configuration as supplied or serviced and log it if known. The manual's nominal 14 dB output-pad attenuation depends on this termination being engaged. Do not open the preamp merely to complete the baseline or assume the labeled pad guarantees a measured 14 dB drop in every configuration. [PRE-73 Premier manual, page 2](https://goldenageaudio.com/wp-content/uploads/2026/04/PRE-73-PREMIER-manual.pdf)

## Shape the sound after the reference

If close speech is heavy, compare PRE HPF off against 80 Hz. Try 200 Hz as an audible experiment; it can remove wanted voice body. Compare Air off, +3 and +6 only after checking sibilance. Move the microphone before making a bright setting brighter.

For a deliberate preamp-color experiment, raise GAIN one step and lower OUTPUT enough to preserve the recorded level. Listen for texture as well as distortion. This is a different test from merely making the take louder. Keep a clean reference, and avoid using the output pad or extreme gain to solve a problem caused by excessive input level. Photograph the continuous OUTPUT control and record the measured peak with it.

# Make compression serve the sentence

Compression reduces the difference between stronger and weaker portions of speech. It also makes performance changes, room noise and breaths easier to notice when output level is restored. Begin with the COMP-54's **hard BYPASS engaged** while calibrating the clean microphone/preamp path. Set makeup to **minimum, fully counterclockwise**, before bringing its circuit into use.

![Set compression behavior first, then adjust output by measurement and listening. The panel's continuous makeup control needs an observed level, not an assumed numeric position.](assets/compressor-map.png)

## The six rotary controls

**THRESHOLD** determines when compression begins. Begin at the highest labeled threshold, +10, and lower it while speaking until the gain-reduction meter shows the desired movement. Its analog markings are not DAW dBFS. The same threshold will react differently if mic sensitivity, PRE output or speaking distance changes. Record the final panel position and observed reduction.

**RATIO** sets how strongly above-threshold changes are reduced. Choose 2:1 first. A higher ratio can make the voice steadier but less natural; the effect also depends on threshold. **ATTACK** determines how quickly gain reduction develops. Short settings catch fast events; longer settings let more initial consonant energy through. This compressor is not a guaranteed brick-wall peak limiter.

**RECOVERY** is release: how quickly gain returns after the triggering sound. If gain returns too conspicuously between syllables, background noise can seem to breathe. A longer recovery may smooth that effect, but can also leave the next word quieter. The Auto positions react to program material; they are listening choices rather than fixed times to substitute into a formula.

**SC HP** filters the detector that decides how much to compress. It does **not** remove bass from the recorded signal. At 50 or 100 Hz, low-frequency energy has less influence on reduction. At 7 kHz the detector favors high-frequency events, permitting an experiment in sibilance control. Reduction still changes the full signal; this is not split-band de-essing.

**MAKEUP GAIN** raises the processed output. Start at minimum, then increase only enough to compare the processed and bypassed signal fairly while preserving converter headroom. Your panel has dots rather than a calibrated dB scale, so “two o'clock” cannot guarantee a particular gain.

These functions, stepped controls and separate bypass facilities are described in the [manufacturer's COMP-54 product documentation](https://goldenageaudio.com/outboard-hardware/compressors/comp-54-mkiii/). Your photo does not establish the compressor's revision suffix; its own legends govern the selections below.

## Buttons, meter and rear panel

| Control or connection | Setting for one microphone | How to check it |
|---|---|---|
| POWER | On | Unit operates; use its matching supply. |
| LINK | Off | No second compressor is being linked. |
| OUT / IN-OUT | Compression active after calibration | Stronger phrases move the GR indication. |
| METER | COMP / gain reduction | Read reduction during speech. |
| BYPASS | Off while compressing | On is the hard-bypassed reference. |
| Rear 600 OHM TERM | Normally engaged into modern interface | Follow actual rear label and manual. |
| Rear audio IN | One line-level source from PRE | Do not plug two source outputs into parallel inputs. |
| Rear audio OUT | Balanced line connection to M4 | Recheck M4 peaks after makeup changes. |
| Rear LINK | Unused | A stereo-link facility is not an audio send. |

The compression OUT function retains the audio circuitry while removing compression. Hard BYPASS passes around the entire unit. They answer different questions: how much did compression change the signal, and how much did the whole device change it? Neither is a mute.

The manufacturer's manual gives a factory output-meter reference of about **0 VU = +4 dBu**. Avoid driving the needle repeatedly into its end stop. Use COMP/GR while tracking, and consult the M4 for converter peaks. Leave internal meter trimmers to an appropriate calibration procedure. The original manufacturer-authored [COMP-54 manual is available through this dealer-hosted copy](https://www.adorama.com/col/productManuals/GACOMP54MK2.pdf); the former manufacturer download address was unavailable during research.

## Two recall recipes for either microphone

These are starting behaviors. Select the mic, establish its power and profile, calibrate the clean PRE level, then apply the recipe. They share the same compressor settings across microphones so the comparison has a clear reference. Their final gain, threshold and makeup must be measured separately.

| Parameter | Everyday speech | More dynamic delivery |
|---|---|---|
| Ratio | 2:1 | 3:1 |
| Attack | 6 ms | 12 ms |
| Recovery | 100 ms | 400 ms |
| Sidechain HP | 50 Hz | 100 Hz |
| Threshold | Lower from +10 to about 2–3 dB GR on louder phrases | Lower cautiously; compare occasional 3–4 dB GR on strong phrases |
| Makeup | Minimum, then match reference loudness | Minimum, then match reference loudness |
| Meter / link | COMP / off | COMP / off |
| Hard bypass / compression | Off / active | Off / active |

Record a passage before deciding. If the everyday recipe dulls articulation, compare 12 ms attack. If the longer attack lets troublesome peaks pass, reduce upstream level first and audition a faster attack. If the dynamic recipe makes breaths swell or the room conspicuous, reduce the amount of compression. A polished sentence often needs less reduction than a striking solo demonstration.

## Every stepped compressor experiment

Use these one-control sweeps after saving the reference. Return to the same reference before beginning the next row.

| Control | Complete labeled choices visible on this panel |
|---|---|
| Ratio | 1.5:1, 2:1, 3:1, 4:1, 6:1 |
| Attack | 0.5, 1, 2, 3, 6, 12, 25, 50 ms |
| Recovery | 25, 50, 100, 400, 800 ms; 1.5 s; Auto 1; Auto 2 |
| SC HP | Off, 50 Hz, 100 Hz, 7 kHz |

For threshold, move through the actual detents, noting the marking and reduction; do not assume every dot is a separately printed value. Makeup is continuous: test minimum, matched level and a small measured increase, without clipping. A fixed-threshold sweep reveals what a control changes. A second sweep with threshold reset to the same reduction compares behavior at similar compression strength. Label the two tests separately.

# Read the M4 and listen once

For the main route into rear **LINE IN 3**, the M4's front GAIN 1/2 knobs do not set your recording level. Leave them at minimum if unused, both front 48V buttons off, MON 1/2 off, and the 3–4 direct-monitor button off. The centered mono voice will return through your DAW. Turn INPUT MONITOR MIX toward **PLAYBACK**, then raise the independent headphone level gently.

![Three different meters answer three different questions: signal level, amount of reduction and remaining digital headroom.](assets/meters.png)

The LCD shows input and output levels. A red overload indication calls for less level before the converter. A blue input-channel marker identifies active hardware monitoring. The large MONITOR knob sets the rear monitor listening level; the smaller headphone knob sets headphone volume. Neither fixes recording gain. INPUT MONITOR MIX changes the balance of direct inputs and computer playback, also without changing the captured input level.

Rear LINE IN 3/4 accepts line level and supplies no phantom. The published maximum input level is +18 dBu; front TRS accepts +16 dBu at minimum gain, while front XLR reaches +10 dBu. These are limits, not recording targets. Rear outputs 1/2 carry the main monitor signal; 3/4 are separate software outputs. RCA outputs mirror their corresponding TRS outputs. MIDI is unused for this voice chain. USB carries audio and powers the M4. [MOTU M Series user guide](https://cdn-data.motu.com/manuals/usb-c-audio/M_Series_User_Guide.pdf)

## Choose one monitoring route

![Software monitoring centers rear Input 3; direct rear-pair monitoring keeps Input 3 on the left. The front-input mono alternative is described below.](assets/monitoring.png)

Rear 3–4 direct monitoring operates as a stereo pair; a voice on input 3 alone may be heard only at the left. Selecting a mono DAW track does not change that hardware monitoring path. Keep 3–4 off and use the DAW's centered mono monitor for the main lesson. The [MOTU M4 feature list](https://www.motu.com.pl/motuaudio/m4.html) distinguishes stereo monitoring for rear 3–4 from mono/stereo operation on front 1–2.

For centered direct monitoring, move the balanced COMP output to **front Input 1's TRS connection**, set gain fully counterclockwise and phantom off, choose MON 1's mono operation, and disable DAW input monitoring. Set INPUT MONITOR MIX around center or toward INPUT to hear the direct signal. Select mono Input 1 in the DAW and recalibrate. Front TRS at minimum gain is a useful alternative, not a documented complete bypass of its input amplifier.

Hearing both paths together can produce an echo or hollow tone. Turn off one path before changing EQ. If playback disappears, check the mix knob, DAW output and headphone level. If input meters move but no file is recorded, check track selection and arming. These listening and routing controls can change what you hear without changing the microphone signal at all.
