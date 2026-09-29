# Your Mac becomes the recorder

This chapter uses the microphone, PRE-73 and COMP-54 settings established in the hardware chapters. The COMP-54 output feeds **MOTU M4 rear line Input 3**, and the M4 connects to the Mac by USB. One microphone is one mono recording channel. Neither a stereo input pair nor a second microphone track improves that recording. The native software recipes below are starting points proposed for this book; they are not manufacturer presets or measurements of your voice.

Software reference date: **29 September 2026**. Apple's current online guide identifies GarageBand 10.4.14. Ableton's manual covers Live 12 across editions, so an illustrated device appearing in that manual does not automatically mean Lite includes it. Interface wording can vary with the installed point release. Match the named function when an older version says Preferences instead of Settings.

## Prepare macOS before opening a project

1. Connect the M4 directly to the Mac if practical. Connect wired headphones to the M4. Keep loudspeakers off during microphone recording and bring the headphone volume up gradually.
2. Open **System Settings → Privacy & Security → Microphone**. Allow GarageBand and Ableton Live when they request access. A permission called “microphone” also covers the M4's audio inputs. If an application was denied access, quit it, change the permission and reopen it. [Apple: microphone access](https://support.apple.com/guide/mac-help/control-access-to-the-microphone-on-mac-mchla1b1e1fe/mac); [Ableton: microphone access and Mic Mode](https://help.ableton.com/hc/en-us/articles/360001381780-Microphone-access-and-Mic-Mode-on-macOS).
3. While the recording application is using audio input, inspect the macOS microphone menu in the menu bar or Control Center. Select that application and set **Mic Mode: Standard**. Voice Isolation can change external audio as well as the built-in microphone. If no Mic Mode icon is offered, that feature may not apply to the application. [Apple: check Mic Mode](https://support.apple.com/en-us/121587).
4. Open **Applications → Utilities → Audio MIDI Setup**. Choose **Window → Show Audio Devices** if necessary, then select **M4**. Inspect its Format setting and keep the default clock source. Use 44,100 Hz for this book's GarageBand sessions and 48,000 Hz for new Live sessions unless a collaborator requires a different rate. These are workflow choices. The DAW can change the device rate, so inspect it again after opening the project. [Apple: set up audio devices](https://support.apple.com/guide/audio-midi-setup/set-up-audio-devices-ams59f301fda/mac).
5. Close other audio applications during the first test. Use the M4 for both recording input and headphone playback; do not introduce an Aggregate Device for this single-interface setup. Turn on a Focus mode to reduce interruptions.

**GarageBand sample-rate caveat.** GarageBand for Mac does not expose Live's project sample-rate control. Treat this as a 44.1 kHz workflow; setting the M4 to 48 kHz in Audio MIDI Setup is not a reliable way to create a 48 kHz GarageBand project. Inspect a short exported WAVE file before committing to a required delivery rate. On a Mac, the read-only Terminal command `afinfo "/full/path/to/test.wav"` reports the file format. If a production requires controlled 48 kHz recording and export, use Live. Apple's current Mac guide documents input/output and bit-depth settings but does not document a GarageBand project sample-rate selector; do not borrow iPhone documentation as proof of Mac behavior.

## Choose one path for hearing yourself

For this book's rear Input 3 chain, the simple default is **software monitoring**: listen through the DAW with M4 hardware MON buttons off. In GarageBand enable Monitoring for the voice track. In Live use Monitor **Auto** and arm that track. The M4's input/playback mix control must allow the computer playback signal through. A stereo direct-monitor path could otherwise put a single rear input in one ear; software mono input centers the voice.

Rear 3–4 direct monitoring is stereo: Input 3 is heard on the left and Input 4 on the right. For a centered hardware-monitor alternative, connect the COMP-54 to front Input 1 through its TRS line jack, set front gain fully counterclockwise, keep 48V off and use MON 1 in mono mode. Move Input Monitor Mix away from PLAYBACK toward center or INPUT to hear that direct path. Change the DAW source to mono Input 1 and recalibrate. Disable software monitoring: GarageBand Monitoring off, or Live Monitor Off. Recording can still occur with software monitoring off. Do not listen to both paths at once: their different delays can make a voice hollow, doubled or phasey. A track set to Live's **In** monitors continuously and suppresses clip playback, so **Auto** is usually easier for recording followed by listening. [Apple: input monitoring](https://support.apple.com/guide/garageband/turn-on-input-monitoring-for-audio-tracks-gbnd4bc15233/mac); [Ableton: Routing and I/O, Monitoring](https://www.ableton.com/en/manual/routing-and-i-o/#monitoring).

## Establish the recording level

Make a loud rehearsal before the real take. Read your most excited sentence, laugh once and return to normal narration. Use the hardware gain procedure to place normal speech peaks approximately between **−18 and −12 dBFS**, with occasional excited peaks below **−6 dBFS**. These are conservative recording targets, not a required loudness standard. A quiet-looking waveform can be perfectly usable. A waveform with flattened peaks and audible crackle needs investigation.

The track fader controls playback; it does not rescue an overloaded microphone, preamp, compressor input or M4 converter. For rear Input 3, reduce the level arriving from the external chain when the M4 input clips. Twenty-four-bit recording leaves useful headroom. Saving into a 32-bit floating-point file cannot undo analog distortion or clipping that already occurred in the M4 converter.

# GarageBand: a complete spoken-word session

![GarageBand recording controls, drawn as a function map so the sequence remains legible across point releases.](assets/garageband-map.png)

## Build your clean template

1. Choose **File → New → Empty Project**. Create an Audio track for microphone or line input.
2. Open **GarageBand → Settings → Audio/MIDI** and select **M4** for Input Device and Output Device.
3. Select the new track and open **Smart Controls** with **B**. In Recording Settings choose **Input 3**, with the input-format button set to **mono**. If Input 3 is missing, recheck the application's Input Device. A dimmed recording-level control means gain must be set on the external device. [Apple: connect a microphone](https://support.apple.com/guide/garageband/connect-a-microphone-gbnd4f4680f6/mac).
4. Rename the track `B67-269 — CLEAN` or `TWIN87 — CLEAN`. Center its pan and start its volume at 0 dB. Set Monitoring according to the single monitoring path above.
5. In **Settings → Advanced**, choose **24-bit** recording before recording or importing anything. Disable **Export projects at full volume**; older versions may call this **Auto Normalize**. This prevents an export option from undoing deliberate headroom or changing comparison levels. [Apple: Advanced settings](https://support.apple.com/guide/garageband/change-advanced-settings-gbnded6e79bc/mac).
6. Turn off the metronome, count-in and cycle recording for the first narration. Choose a time display if it helps you read minutes and seconds. Tempo and key have no creative role in this unwarped spoken recording.
7. Inspect the Plug-ins area. Bypass the voice patch's effects, disable Noise Gate and set Ambience/Reverb sends to zero. Do the same inspection on the master track. Save as `Podcast — Clean Capture.band`.

**Checkpoint:** speaking moves the M4 Input 3 meter and the intended GarageBand track meter; the voice is centered in the headphones; a recorded test plays back with the intended microphone sound. If tapping near the Mac produces a much louder result than speaking near your microphone, check that M4 is selected instead of the built-in microphone.

## Record and protect the original

Save an episode copy before recording. Put the playhead at the beginning, select the voice track and press **R**. Capture ten seconds of room tone, your name and the setting ID, then the program. Press Space to stop. Play the beginning, a loud passage and the ending. Apple documents recording on the selected audio track from the playhead; record enable controls matter when recording several tracks. [Apple: record audio](https://support.apple.com/guide/garageband/record-to-an-audio-track-gbnd302d468d/mac).

Keep the clean take in a separate saved project before editing. “Clean” here means no software processing; hardware compression already printed into the audio is permanent. For a recoverable microphone test, bypass the COMP-54 during capture. For normal episodes, keep its reduction modest and save its settings photograph.

When a sentence goes wrong, pause, take a quiet breath and restart the whole sentence. A full replacement is usually easier to edit naturally than a replacement syllable. Record one minute of quiet room tone at the end if a fan, traffic or air conditioning might change during the session.

## Edit for natural speech

Select a region, place the playhead at an edit and choose **Edit → Split Regions at Playhead** or press **Command-T**. Split before and after an unwanted phrase, delete that region and move the following material into place. Work from a saved copy; leave enough air around consonants. [Apple: split regions](https://support.apple.com/guide/garageband/split-regions-gbnd76fcce04/mac).

Retain ordinary breaths and short pauses. Remove distractions rather than every human sound. If a cut clicks, move the edit into quieter material and use a short volume ramp. Press **A** to show automation, select Volume and place points around the transition. Four points let you reduce only a breath or mouth noise while preserving the levels on either side. Start with a 3–6 dB reduction; listen in context. Do not automate every breath into digital silence. [Apple: show automation](https://support.apple.com/guide/garageband/show-track-automation-curves-gbnd939b92d8/mac); [Apple: automation points](https://support.apple.com/guide/garageband/add-and-edit-automation-points-gbnd65471e12/mac).

## GarageBand processing card

Work on an edited copy. Open Smart Controls, expand Plug-ins and insert **Channel EQ**, then **Compressor**. Click a plug-in slot to open its controls; its power button enables a meaningful bypass comparison. Preserve the original track before applying changes. [Apple: effect plug-ins](https://support.apple.com/guide/garageband/add-and-edit-effect-plug-ins-gbndac55f7f8/mac).

| Control | B67-269 starting value | Twin87 starting value |
|---|---|---|
| EQ high-pass | 70 Hz, 12 dB/octave, Q about 0.71; off if PRE high-pass suffices | 70 Hz, 12 dB/octave, Q about 0.71; off if PRE high-pass suffices |
| EQ low shelf | Off | Off |
| EQ bell at 250 Hz | 0 dB, Q 1.0 | 0 dB, Q 1.0 |
| EQ bell at 3 kHz | 0 dB, Q 0.7 | 0 dB, Q 0.7 |
| EQ high shelf / low-pass | Off / off | Off / off |
| Other EQ bands | Off; EQ output 0 dB | Off; EQ output 0 dB |
| Compressor Threshold | Begin −18 dB; adjust to the actual take | Begin −18 dB; adjust to the actual take |
| Compressor Ratio | 2:1 | 2:1 |
| Compressor Attack | 20 ms | 20 ms |
| Compressor Gain | 0 dB initially; match bypass loudness | 0 dB initially; match bypass loudness |
| Noise Gate, reverb, echo | Off | Off |

Select EQ bands using the colored symbols, then edit frequency, gain/slope and Q in the numeric fields. The neutral bells are preparation, not mandatory boosts or cuts. The GarageBand compressor's simplified window may expose only Threshold, Ratio, Attack and Gain; do not search for Live's release, knee and sidechain controls there. [Apple: EQ controls](https://support.apple.com/guide/garageband/use-the-eq-effect-gbnd56ab9fca/mac).

The identical starting values are deliberate. A microphone name cannot determine the right EQ for an unknown voice and room. After matching levels, try a **−2 dB cut near 250 Hz** only if that take is muddy. Try **−1 to −2 dB in the high range** only if it is persistently sharp. Change placement before forcing a large EQ correction. For isolated sibilants, lower those short passages with automation; a static treble cut also dulls vowels and is not a selective de-esser.

If hardware compression already controls the take, leave the software Compressor bypassed first. If extra control helps, lower its threshold gradually while listening for steady sentences, intact consonants and quiet breaths. Match bypassed and processed loudness with Gain before judging. Stop when processing makes words less lively or the room noise noticeably swells.

## Export a GarageBand master

Save the final project. Set the intended region/cycle range, choose **Share → Export Song to Disk**, select **WAVE** and **24-bit uncompressed** when offered. Export the intended range, not an accidental empty tail. GarageBand exports stereo; a mono voice centered in that export is expected. Keep automatic full-volume export disabled. Listen to the exported file from start to finish. [Apple: export songs](https://support.apple.com/guide/garageband/export-songs-to-disk-or-icloud-gbnd7cbf5ed9/mac).

![Separate export choices from checks on the resulting file.](assets/export-map.png)

Call this file `episode-001_edit-master.wav`. A clean, balanced export with headroom is a valuable deliverable even before loudness finishing. To use the book's fully specified final limiter, import this master into Live, disable Warp and follow the finishing procedure below. Do not recompress an already controlled voice just because the second DAW offers another compressor.

# Ableton Live 12 Lite: precise capture and finishing

![Live routing and recording controls. This is an original teaching diagram rather than a screenshot.](assets/live-map.png)

## Configure the project

Lite supports eight audio/MIDI tracks and eight mono input channels. This session needs only one microphone track and, optionally, a second comparison track. The recipe uses **Channel EQ, Compressor and Limiter**, which the official Lite comparison includes. **EQ Eight and Gate are not included in Lite.** [Ableton: edition comparison including Lite](https://www.ableton.com/en/upgrade-live/).

Open **Live → Settings → Audio**. Set the following before recording:

| Setting | Value for this chain |
|---|---|
| Driver Type | CoreAudio |
| Audio Input Device / Output Device | M4 / M4 |
| In/Out Sample Rate | 48,000 Hz for new Live sessions; 44,100 Hz for direct GarageBand comparison |
| Input Config | Enable mono 3; enable other inputs only when used |
| Output Config | Enable stereo 1/2 |
| Buffer Size | Start 128 samples for software monitoring; try 256 if it crackles |
| Driver Error Compensation | Leave default unless actually measured |
| Test Tone | Off before speaking |

The buffer is a latency/stability tradeoff, not a quality setting. At 48 kHz, 128 samples represents about 2.7 ms per buffer; actual round-trip latency includes additional input, output and processing delays. If a stable buffer feels too slow, simplify the monitored chain. For supported hardware direct monitoring, 256 or 512 samples can be comfortable because that listening path bypasses the DAW. [Ableton: interface setup](https://help.ableton.com/hc/en-us/articles/211476789-Setting-up-an-Audio-Interface).

In **Settings → Record, Warp & Launch**, select WAV and 24-bit recording. Turn **Auto-Warp Long Samples** off for spoken-word imports. Leave Create Fades on Clip Edges on. Save a new project before the take so the recording has a clear home. [Ableton: recording file types](https://www.ableton.com/en/manual/recording-new-clips/#setting-up-file-types).

Switch to **Arrangement View** with Tab. Insert an audio track, name it for the microphone and set **Audio From: Ext. In → 3**. Set Monitor **Auto** for software monitoring, arm the track and route **Audio To: Main**. Set pan center, track volume 0 dB, sends to minus infinity and Main volume 0 dB. Remove unneeded template effects and turn off the metronome. Mono 3 records a mono file; 3/4 records a pair and is wrong for this one-cable chain. [Ableton: external audio routing](https://www.ableton.com/en/manual/routing-and-i-o/#external-audio-inout).

## Capture, edit and save

Click Arrangement Record and start the transport. Capture room tone, setting ID and speech. Stop, disarm and listen back. Duplicate the Set before editing. Check each narration clip's **Warp: Off**, **Transpose: 0** and clip gain before comparing versions. Imported music can follow its own needs; speech should keep its original timing and pitch.

Expand the audio track so its waveform is readable. Select an unwanted time range and split at its boundaries with **Command-E**. Remove the mistake and close the gap by moving the following material. With automation hidden, reveal the small fade handles at clip edges. Use short fades around edits and longer crossfades only where they sound natural. Adjacent clips support crossfades; a default tiny fade avoids many clicks. [Ableton: Arrangement editing and fades](https://www.ableton.com/en/manual/arrangement-view/#audio-clip-fades-and-crossfades).

Reduce loud breaths or individual consonants with clip gain or volume automation. Rehearse the edit at normal listening level, then quietly: an edit that seems smooth only at high volume may still interrupt a sentence. Preserve a clean Set and use **Collect All and Save** when moving the project to another drive so referenced audio travels with it.

## Lite processing and final limiter cards

Add these devices in order. These author-proposed settings apply to either microphone; save independent copies once the listening test establishes a useful difference.

| Device/control | Starting setting |
|---|---|
| Channel EQ HP 80 Hz | On if PRE high-pass is off; audition off if a low voice becomes thin |
| Channel EQ Low / Mid / High | 0 / 0 / 0 dB |
| Channel EQ Mid frequency / Output | 250 Hz / 0 dB |
| Compressor Mode / envelope | RMS / Log |
| Compressor Threshold / Ratio | −18 dB starting threshold / 2:1 |
| Compressor Attack / Release | 20 ms / 120 ms; Auto Release off |
| Compressor Knee / Lookahead | 6 dB / 0 ms |
| Compressor Makeup / Out / Dry-Wet | Off / 0 dB initially / 100% |
| Compressor external sidechain / detector EQ | Off / off |
| Main Limiter Ceiling / ceiling mode | −1.5 dB / True Peak, if present |
| Limiter Input Gain / Maximize | 0 dB initially / off |
| Limiter Release / Auto | 100 ms if manual / Auto on |
| Limiter Lookahead / Routing / Link | 3 ms / L-R / 100% |
| Main fader / devices after Limiter | 0 dB / none |

Channel EQ has a fixed 80 Hz high-pass and a sweepable mid band. Compressor's threshold must be adjusted against the actual recording; aim initially for only 1–3 dB additional reduction on louder words, especially after the COMP-54. Current Limiter offers True Peak, while older Live 12 versions may have fewer controls. If True Peak or another listed control is absent, use the available controls, keep at least 2 dB sample-peak headroom and verify true peaks in the rendered file. [Ableton: Audio Effect Reference, Channel EQ, Compressor and Limiter](https://www.ableton.com/en/manual/live-audio-effect-reference/).

Raise level before the final Limiter only after balancing sentences. If it frequently removes more than about 3 dB, fix the loud phrases or ease the target instead of flattening the whole episode. Bypass comparisons need matched loudness. Louder nearly always sounds more exciting on a quick comparison.

## Export and verify the delivery file

Select the finished time range. Choose **File → Export Audio/Video** or **Command-Shift-R**. Render **Main**; choose WAV, 24-bit and the project sample rate. Set **Normalize off** and **Render as Loop off**. Keep Convert to Mono off for a stereo master. For a final 24-bit PCM render, Triangular dither is a reasonable choice; use 32-bit with no dither if further mastering is planned. Live's optional MP3 export is fixed at 320 kbps, so use an encoder or hosting service when a different delivery bitrate is required. [Ableton: exporting audio](https://www.ableton.com/en/manual/managing-files-and-sets/#exporting-audio-and-video).

Measure the exported file, because a limiter ceiling is not a loudness meter. Apple recommends about **−16 LKFS, ±1 dB**, with true peak at or below **−1 dBFS**; this book leaves extra peak margin at −1.5 dBTP. A common mono convention of −19 LUFS is not Apple's blanket requirement. Follow your destination's current specification and label mono versus stereo clearly. [Apple Podcasts: audio requirements](https://podcasters.apple.com/support/893-audio-requirements).

If FFmpeg is installed, this read-only analysis produces an integrated-loudness and true-peak summary without changing the audio:

```sh
ffmpeg -hide_banner -i "episode-001_master.wav" \
  -af "ebur128=peak=true" -f null -
```

Read the final Integrated loudness `I` and True peak summary. Keep the same channel layout and measurement method for every comparison. If the final stereo file measures −19 LUFS and peaks have room, try approximately 3 dB more gain before the limiter, export and measure again. This arithmetic is a starting estimate; limiting changes the result. [FFmpeg: ebur128 scanner](https://ffmpeg.org/ffmpeg-filters.html#ebur128).

Listen to the encoded delivery file too, using headphones and an ordinary small speaker. Check the first word, last word, edit joins, room noise and loudest laugh. Keep the DAW project, clean recording, edited WAV and delivered file as separate named artifacts.

# Compare the microphones without fooling yourself

## Two different questions require two tests

**The controlled test** asks what changes when the microphone or one setting changes. **The finished-voice test** asks which complete setup produces the episode you prefer. Keep separate results. A heavily processed Twin87 versus a clean B67-269 can be a useful finished-chain comparison, but cannot identify the microphone alone as the cause.

Use one microphone at a time through the same cable path, preamp, compressor and rear M4 input. Two microphones side by side do not occupy the same acoustic position, and one external channel cannot provide identical simultaneous processing to both. Mark the capsule position, chair position and pop-filter distance; allow each microphone its appropriate power and warm-up procedure from the hardware chapter. Never hurry a powered mic swap to preserve test timing.

Record this original test script at a natural pace:

> Welcome to Professional Podcast Audio. Today we are comparing a calm voice, a clear explanation and a brighter announcement. Peter packed a paper parcel. Six soft sentences should stay smooth. Now I will speak quietly, then return to my usual level. This next sentence is more excited, but I will keep the same distance. One, two, three. And now, ten seconds of room tone.

Use three takes per condition. Speech changes between performances; repeated takes help reveal whether the difference survives normal variation. If you need an exactly repeatable sound for a technical check, replay a recorded voice through one fixed loudspeaker. Label that as a loudspeaker test: its sound and room interaction differ from a live speaker.

## Work through a controlled sequence

| Test | Change | Hold steady |
|---|---|---|
| 01 Reference | B67-269 versus Twin87 | Cardioid, same capsule position, COMP-54 bypassed, DAW effects off |
| 02 Placement | 15, 20 and 30 cm mouth-to-capsule distance | Mic mode, angle and gain; assess raw difference, then level-match copies |
| 03 Angle | Straight on, 15°, 30° off axis | Distance, mic position and hardware settings |
| 04 Mic voicing | Available B67-269 voicings or Twin87 Vintage/Modern | Pattern, distance, chain; follow mic switching procedure |
| 05 Pattern | Cardioid versus another pattern | Voice position and room; rear sound pickup is part of this test |
| 06 PRE-73 | One impedance or gain/output comparison | Mic, position, compressor bypass, matched recording peaks |
| 07 COMP-54 | Bypass versus gentle compression | Same mic and preamp; match output level for listening |
| 08 DAW processing | Clean versus one EQ or compression change | Use a duplicate of the exact same recorded take |
| 09 Finished chain | Best repeatable setup for each microphone | Same script, delivery loudness, listening level and export format |

Do not test every combination at once. Finish placement first, then voicing, then compression. An apparent need for severe processing often disappears after a small positioning change. Each test ends with a saved decision: keep, reject or repeat.

## Match listening level, then hide the names

For microphone preference, adjust the PRE-73 separately for each mic to obtain similar safe recording peaks. Identical gain-knob positions are not a fairness requirement because microphone sensitivity can differ. A separate fixed-gain test can document sensitivity; label it accordingly and still match playback levels before judging tone.

Export equal spoken passages with effects bypassed and normalization off. Measure both in the same channel layout, then turn the louder file down by the loudness difference. For example, A at −22 LUFS and B at −19.5 LUFS calls for approximately **−2.5 dB on B**. Do not peak-normalize as a substitute: equal highest peaks can still leave different average loudness. Keep the matched copies under clipping and leave raw files untouched.

Put A and B on separate tracks with identical output routing. In GarageBand use track Volume; in Live use clip gain or track Volume. Solo one at a time, never sum both. Have someone assign neutral file names if possible; otherwise conceal the track labels while listening. Score warmth, intelligibility, sibilance, plosives, room pickup and fatigue from 1–5. Also write one plain sentence: “I can follow quiet words more easily,” for example, is more actionable than “better.”

Finish with two saved recall sheets. Each must include mic/model and voicing, polar pattern, pad/filter state, distance/angle, PRE-73 gain/output/impedance, COMP-54 settings and observed reduction, M4 input, DAW version, sample rate, every enabled plug-in value, export layout and measured loudness. Save one final **B67-269** template and one final **Twin87** template. Your own verified settings now replace the book's starting values.
