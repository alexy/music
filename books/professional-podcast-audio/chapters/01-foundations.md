# Your first repeatable voice recording

This book is built around the equipment on your desk: a BeesNeez B67-269 tube microphone, a United **Studio Technologies** UT Twin87, a Golden Age **PRE-73 Premier**, a COMP-54 compressor, and a MOTU M4 connected to a Mac. The purpose is simple: make a voice recording you can trust, repeat it tomorrow, and hear what each microphone and control really changes.

A professional result is a repeatable process. Your voice, distance from the capsule, room reflections and performance matter before a compressor or EQ. We will first record a clean reference, then add modest processing, then compare equal-loudness copies. You will finish with a saved session and a recall sheet that covers the whole chain.

## What is verified, and what you must measure

**Manufacturer facts** describe what a jack, switch or software control does. They are linked to the official documents in the source register. **Starting recipes** are editorial suggestions for spoken voice. They have not been acoustically tested on your voice or in your room. A gain number, threshold or distance in a recipe is a place to begin, not a promise of the best sound. **Your measured result** is the meter reading and listening note you write down after recording.

The photographs in this book are your supplied images from `gear/`. They identify the PRE-73 Premier and show the real microphone and stack. They do not establish hidden rear wiring, switch engagement or the precise compressor revision. A perspective photo is not a calibrated recall sheet. The color diagrams are original teaching illustrations, not manufacturer screenshots or pixel-accurate panel drawings.

The main hardware path uses the M4's rear **LINE IN 3**. That keeps the signal from the external preamp and compressor out of the M4's adjustable front gain stage. We will monitor a centered mono track through the DAW. A separate alternative explains how to use the front TRS input when you need centered direct monitoring.

![Your BeesNeez in its shock mount. The capsule is addressed from the side; the room and hard desk surfaces are part of the sound.](assets/beesneez-in-room.jpg){width=68%}

## Three working sessions

1. **First sound, about 30 minutes.** Connect one microphone, set safe power, bypass compression, choose mono Input 3, rehearse loudly, then record a minute of speech.
2. **Comparison, about 60 minutes.** Capture the BeesNeez as found and both Twin87 modes. Add the four internal BeesNeez profiles only after its manufacturer confirms the safe handling procedure for your revision. Match speech loudness, blind the labels, and score the result. Repeat the top two at different distances.
3. **Production template, about 45 minutes.** Choose one setup, add only needed filtering and compression, edit a short episode, export and listen to the complete file.

If you already have a recording, retain it. Save a new project for this work so old plug-ins, normalization settings and routings cannot silently color the test.

## A four-line safety card

- **BeesNeez:** use its matching power supply and supplied multipin cable. Keep PRE-73 phantom **OFF**.
- **Twin87:** use an ordinary balanced XLR mic cable. Turn PRE-73 phantom **ON only after connecting** the microphone.
- **Both:** keep M4 phantom **OFF** in the outboard chain. The PRE-73 already supplies any required mic gain and phantom.
- **Every change:** lower headphone/speaker levels and stop recording before changing cables, power or microphone modes. Follow the device's own instructions for its supplied power system.

A tube mic supply is not a generic phantom-power adapter. Never experiment with a multipin cable from another microphone. Do not open a powered supply or service mains circuits. If the BeesNeez model, cable or switch plate differs from the linked guide, use the matching guide before changing it.

## The minimum accessory kit

Have the microphone's proper mount, a pop filter, a stable stand, closed-back headphones, a balanced XLR mic cable, balanced line cables between outboard units, a balanced cable ending in a TRS quarter-inch plug for M4 Input 3, and the M4's USB connection. The BeesNeez adds its own supply and supplied mic cable. The gear photos do not show every rear connector; confirm the sockets before powering up.

Use one balanced output per link. XLR and TRS describe connector formats; they do not by themselves mean microphone level. The signal leaving the PRE-73 is line level. Label the destination end of each cable: `PRE IN`, `COMP IN`, `M4 IN 3`.

# Read the desk before turning a knob

![Your hardware, left to right and top to bottom: MOTU M4, red COMP-54, PRE-73 Premier, and the BeesNeez supply at the right.](assets/hardware-stack.jpg)

The photo identifies the preamp as **PRE-73 PREMIER**, not a generic PRE-73 MkII or MkIII. Its high-pass filter, Air EQ and output pad deserve their own entries in every recall sheet. The compressor photo shows threshold, ratio, attack, recovery, sidechain HP, makeup, meter selector, power, link, compression in/out and bypass controls. Follow the panel legends when a manual covers a different revision.

## The signal path, in plain language

The microphone turns pressure into a small electrical signal. The PRE-73 raises that signal to a usable analog line level. The COMP-54 can reduce dynamic range before the signal reaches the interface. The M4 converts the analog signal into digital samples. GarageBand or Live stores those samples on an audio track. Software effects and editing shape the finished program after capture.

![Choose the microphone branch first; the remainder of the recording path is shared.](assets/signal-chain.png)

The order matters. Turning a DAW fader down cannot undo a clipped microphone, overloaded preamp or clipped converter. Conversely, a quiet-looking waveform can still contain analog distortion if you used too much preamp gain and then turned its output down. Listen and watch the meter at each stage.

## The 12-step cable and power sequence

1. Stop the DAW transport. Turn headphones down. Mute or turn down speakers.
2. Turn PRE-73 48V off. Leave both M4 48V buttons off. Power down the BeesNeez supply before attaching or removing its microphone cable; allow it to discharge according to its supplied instructions.
3. Mount the chosen mic securely. Do not let a heavy cable pull sideways on its connector.
4. For the BeesNeez, connect the supplied multipin cable from mic to matching PSU `MIC`. Connect PSU `PRE` output to the PRE-73 microphone input with the appropriate balanced XLR lead. For the Twin87, connect mic XLR directly to the PRE-73 microphone input.
5. Connect the PRE-73 balanced main output to the COMP-54 balanced input. Do not use the preamp's unbalanced insert for this baseline.
6. Connect the COMP-54 balanced output to M4 rear `LINE IN 3`, using a balanced TRS plug at the M4. Leave Input 4 unused.
7. Connect M4 by USB to the Mac. Connect headphones to the M4. Keep speaker level low.
8. Set the PRE-73 to mic mode: LINE off, DI off, LOW-Z off, polarity normal, high-pass off, Air off, output pad 0 dB. Begin with gain 30 dB and output at or near maximum; lower gain or trim output if the rehearsal needs less level.
9. Power the PRE and compressor; engage COMP-54 hard bypass. Leave the compressor's makeup gain at minimum; it has no calibrated dB scale.
10. For BeesNeez only, turn on its matching supply with PRE phantom still off. Allow the microphone to settle; make a fresh level check after it is stable. This book does not invent a manufacturer warm-up duration.
11. For Twin87 only, with cabling complete and monitors down, turn on PRE phantom and let the mic settle. Choose cardioid and the desired mode. Its manual calls for about ten seconds of stabilization after Vintage/Modern changes.
12. Select M4 input and output in the DAW, create mono Input 3, raise headphones gently, rehearse your loudest line and calibrate.

For shutdown, stop recording and lower monitors first. Turn Twin87 phantom off and allow discharge before unplugging. Turn off the BeesNeez supply and follow its discharge guidance before disconnecting its mic. Turn off unused hardware. Do not patch live microphones to save a few seconds.

## Place the microphone before calibrating

Start around **20 cm mouth-to-capsule**, with a pop filter between you and the mic and the mic about 15-30 degrees to the side of your direct breath. Both microphones are side-address models. Speak toward the front capsule face rather than the top of the grille. For the Twin87 the front is the side with its logo and controls identified in the manual; for the BeesNeez use the marked front shown in its guide.

![A placement diagram, not a scale drawing. Measure from your mouth to the capsule region, not to the stand.](assets/placement.png)

Mark the stand and chair positions. Keep the capsule near mouth height. Point the rear of a cardioid mic toward the strongest unwanted noise when practical. Place soft absorption behind the speaker to catch the reflections that return toward the mic's sensitive front. Keep the mic away from a large bare desktop when possible; a boom or raised stand can help. Test a folded blanket or absorber safely positioned out of frame before buying anything.

Record ten seconds of room tone. Listen for computer fans, street sound, heating, loose cables touching the stand, chair squeaks and table taps. Fix the largest physical cause before turning on a gate. A gate cannot remove noise while you are speaking.
