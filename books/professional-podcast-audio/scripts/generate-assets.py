#!/usr/bin/env python3
"""Original explanatory plates; user photographs are placed without retouching."""
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
import textwrap
ROOT=Path(__file__).resolve().parents[1]; OUT=ROOT/'assets'
INK='#182c38'; MUTED='#51636e'; PAPER='#f4f2e9'; TEAL='#007e87'; GOLD='#df9b35'; RED='#b14437'; BLUE='#3556a8'
FONT='/System/Library/Fonts/Supplemental/Arial.ttf'; BOLD='/System/Library/Fonts/Supplemental/Arial Bold.ttf'
def font(s,b=False): return ImageFont.truetype(BOLD if b else FONT,s)
def txt(d,xy,t,s=26,fill=INK,b=False): d.text(xy,t,font=font(s,b),fill=fill)
def wrap(d,xy,t,width=46,s=26,fill=INK,b=False):
    lines=[line for paragraph in t.split('\n') for line in (textwrap.wrap(paragraph,width=width) or [''])]
    d.multiline_text(xy,'\n'.join(lines),font=font(s,b),fill=fill,spacing=10)
    return xy[1]+len(lines)*(s+10)
def base(title,kicker='PROFESSIONAL PODCAST AUDIO',h=980):
    im=Image.new('RGB',(1600,h),PAPER); d=ImageDraw.Draw(im)
    txt(d,(65,40),kicker,20,TEAL,True); txt(d,(65,85),title,48,INK,True)
    d.line((65,158,1535,158),fill=GOLD,width=5)
    return im,d

def box(d,x,y,w,h,title,body,color=TEAL):
    d.rounded_rectangle((x,y,x+w,y+h),radius=20,fill='white',outline='#ccd4d4',width=2)
    d.rounded_rectangle((x,y,x+w,y+62),radius=20,fill=color)
    txt(d,(x+22,y+15),title,28,'white',True)
    wrap(d,(x+22,y+83),body,max(15,int(w/15.5)),25)
def save(im,name):im.save(OUT/name,optimize=True)
# Cover and landscape headboard use original user photo in a publication layout.
photo=Image.open(OUT/'beesneez-in-room.jpg').convert('RGB')
cover=Image.new('RGB',(1400,2000),INK); d=ImageDraw.Draw(cover)
photo.thumbnail((760,1120)); cover.paste(photo,(610,690))
txt(d,(85,88),'FIRST PAIR  /  MUSIC',27,'#7de0d7',True)
for y,t in [(215,'Professional'),(340,'Podcast'),(465,'Audio')]: txt(d,(78,y),t,112,'white',True)
d.rectangle((85,650,540,660),fill=GOLD)
wrap(d,(85,710),'Your microphones.\nYour Mac.\nA repeatable sound.',18,39,'white',True)
wrap(d,(85,980),'BeesNeez B67-269\nUT Twin87\nPRE-73 Premier\nCOMP-54\nMOTU M4',23,30,'#b9ced3')
wrap(d,(85,1520),'A color, step-by-step field manual for GarageBand and Ableton Live 12 Lite',23,33,'white')
txt(d,(85,1840),'ALEX Y KHRABROV'.replace('ALEX Y','ALEXY'),31,'white',True)
txt(d,(85,1900),'FIRST EDITION  /  2026',24,'#7de0d7')
save(cover,'cover.png')
head=Image.new('RGB',(1800,650),INK); d=ImageDraw.Draw(head)
p=Image.open(OUT/'hardware-stack.jpg').convert('RGB');p.thumbnail((800,560));head.paste(p,(990,45))
txt(d,(75,80),'PROFESSIONAL PODCAST AUDIO',50,'white',True)
wrap(d,(75,200),'Two microphones. One calibrated signal chain.',28,51,'white',True)
txt(d,(75,470),'BEESNEEZ  /  TWIN87  /  MAC',30,'#7de0d7',True);save(head,'headboard.png')
# two routes
im,d=base('Two microphones, one recording path')
box(d,65,210,460,240,'A  /  BeesNeez B67-269','Mic -> supplied multipin cable -> matching BeesNeez power supply -> PRE output',TEAL)
box(d,65,510,460,240,'B  /  United UT Twin87','Mic -> standard balanced XLR cable -> PRE-73 microphone input',BLUE)
box(d,590,210,410,240,'PRE-73 PREMIER','MIC mode. LOW-Z off. 48V OFF for BeesNeez; ON for Twin87.',RED)
box(d,1060,210,470,240,'COMP-54','Balanced line input. Start in hard bypass. Add 2-3 dB gain reduction later.',TEAL)
box(d,1060,510,470,240,'MOTU M4','Balanced TRS rear LINE IN 3. Fixed level; front GAIN knobs do not affect it.',BLUE)
box(d,590,510,410,240,'MAC / DAW','USB -> Core Audio -> mono Input 3 -> one voice track -> headphones',TEAL)
def arrow(points,color=INK):
    d.line(points,fill=color,width=6)
    x,y=points[-1];px,py=points[-2]
    if x>px: tip=[(x,y),(x-15,y-10),(x-15,y+10)]
    elif x<px: tip=[(x,y),(x+15,y-10),(x+15,y+10)]
    elif y>py: tip=[(x,y),(x-10,y-15),(x+10,y-15)]
    else: tip=[(x,y),(x-10,y+15),(x+10,y+15)]
    d.polygon(tip,fill=color)
arrow([(525,320),(585,320)])
arrow([(525,620),(555,620),(555,350),(585,350)],BLUE)
arrow([(1000,320),(1055,320)])
arrow([(1295,450),(1295,505)])
arrow([(1060,620),(1005,620)])
wrap(d,(65,820),'Connect with monitoring muted. Never connect the BeesNeez multipin microphone cable to the PRE-73 or MOTU. Follow the matching PSU labels.',90,30,RED,True);save(im,'signal-chain.png')
# preamp
im,d=base('PRE-73 Premier: safe baseline',h=1150)
items=[('48V','B67-269 OFF / Twin87 ON',RED),('LINE + DI','Both OFF: microphone input',TEAL),('LOW-Z','OFF: 1200 ohms',TEAL),('GAIN','Start 30 dB; calibrate by voice',BLUE),('HIGH PASS','OFF for raw comparison',TEAL),('AIR EQ','OFF for raw comparison',TEAL),('OUTPUT PAD','0 dB',TEAL),('OUTPUT','Near max; trim only as needed',BLUE),('POLARITY','Normal (not inverted)',TEAL)]
for i,(t,b,c) in enumerate(items):box(d,65+(i%3)*505,210+(i//3)*260,470,230,t,b,c)
wrap(d,(65,1020),'Knob positions are starting points. Match recorded levels after every mic, mode or distance change.',95,27,MUTED);save(im,'preamp-map.png')
im,d=base('COMP-54: set behavior, then level',h=1030)
items=[('1 / THRESHOLD','Start highest marked; lower until loud phrases show 2-3 dB GR.'),('2 / RATIO','2:1. Use 3:1 only after comparing at equal loudness.'),('3 / ATTACK','6 ms. Compare 3 and 12 ms; retain clear consonants.'),('4 / RECOVERY','100 ms. Try 400 ms if the noise floor breathes.'),('5 / SIDECHAIN HP','50 Hz for speech recipe; OFF for raw reference.'),('6 / MAKEUP','Start minimum; match engaged and bypass loudness.')]
for i,(t,b) in enumerate(items):box(d,65+(i%3)*505,210+(i//3)*300,470,270,t,b,TEAL if i%2==0 else BLUE)
wrap(d,(65,850),'LINK out. Meter COMP for gain reduction. COMP OUT disables compression; BYPASS skips the whole circuit. Neither control is a recording mute.',90,28,RED,True);save(im,'compressor-map.png')
im,d=base('Three different meters; three different jobs',h=880)
box(d,65,210,470,380,'PRE-73 LEDs','Watch analog headroom. Too much preamp gain can distort before the computer meter reaches red. Turn GAIN down if the clean reference sounds rough.',TEAL)
box(d,565,210,470,380,'COMP-54 VU','COMP: amount of gain reduction. Output: analog output level. These are not digital peak readings. Makeup gain can overload the next device.',GOLD)
box(d,1065,210,470,380,'M4 / DAW','dBFS: digital full scale. Aim loud rehearsal peaks around -12 dBFS, occasional peaks up to -6 dBFS. 0 dBFS is the ceiling.',BLUE)
wrap(d,(65,665),'Do the loudest line first. Leave room for laughter. A quieter clean recording is easier to finish than a clipped one.',88,32,INK,True);save(im,'meters.png')
im,d=base('Choose exactly one monitor path',h=820)
box(d,65,210,700,350,'PATH A / Software: rear Input 3','M4 3-4 monitor OFF. Input Monitor Mix toward PLAYBACK. DAW track monitoring ON, headphones connected to M4. Begin at 128 samples in Live; raise if clicks occur.',TEAL)
box(d,835,210,700,350,'PATH B / Hardware: rear Input 3','DAW track monitoring OFF. M4 3-4 monitor ON; Input Monitor Mix balances input/playback. Input 3 is the left side of this stereo pair. It is not a mono center monitor.',BLUE)
wrap(d,(65,640),'A short delay, hollow voice or comb filtering usually means both paths are active. Disable one and test again.',92,30,RED,True);save(im,'monitoring.png')
im,d=base('A fair comparison is a sequence',h=1090)
steps=[('01','RAW','B67 as found; verified profiles optional. Twin87 Vintage / Modern.'),('02','PLACE','15 / 20 / 30 cm. Mark mouth-to-capsule distance and angle.'),('03','CONTROL','One change per take: pad, filter, air, ratio, attack or recovery.'),('04','MATCH','Match speech loudness on copies. Keep raw takes untouched.'),('05','BLIND','Rename A / B, randomize order, score before revealing labels.'),('06','RECALL','Save the winning mic + every hardware + DAW setting together.')]
for i,(n,t,b) in enumerate(steps):
    y=210+i*132;txt(d,(70,y),n,49,TEAL,True);txt(d,(190,y),t,29,INK,True);wrap(d,(450,y),b,63,26)
    d.line((190,y+101,1515,y+101),fill='#c8d3d2',width=2)
save(im,'comparison.png')
im,d=base('Mac session: where each choice belongs',h=1040)
box(d,65,210,710,300,'macOS / AUDIO MIDI SETUP','Select MOTU M4. Microphone permission enabled for the chosen DAW. Use Standard mic mode when offered. Disable system noise processing for comparisons.',TEAL)
box(d,825,210,710,300,'GARAGEBAND / AUDIO-MIDI','Input: M4. Output: M4. Audio track: mono Input 3. Record 24-bit. Plug-ins off for raw reference. GarageBand uses its own project sample-rate workflow.',BLUE)
box(d,65,560,710,300,'LIVE 12 LITE / AUDIO','CoreAudio. Input/output: M4. 48 kHz. 24-bit. Mono Input 3 enabled. 128-sample buffer start. Arrangement record, Warp off for speech comparison.',BLUE)
box(d,825,560,710,300,'ARCHIVE / EXPORT','Keep unprocessed takes. Make separate edited masters. Normalize off for comparisons. Record actual exported sample rate, bit depth and mono/stereo format.',TEAL)
save(im,'mac-map.png')
im,d=base('Microphone placement is your first EQ',h=790)
d.ellipse((145,235,385,475),fill='#f5ceab',outline=INK,width=4);d.rectangle((760,260,900,470),fill='#99adb2',outline=INK,width=4)
d.line((435,345,710,345),fill=TEAL,width=8);txt(d,(430,280),'15-20 cm start',31,TEAL,True)
d.line((620,240,620,480),fill=INK,width=7);txt(d,(555,495),'Pop filter',25,INK,True)
wrap(d,(1010,245),'Speak across the front of the capsule, 15-30 degrees off-axis. Do not address the end of a side-address microphone.',25,27)
wrap(d,(90,610),'Keep the rear of the cardioid pattern toward the main noise source. Move soft treatment behind you to reduce the reflections the front of the mic hears.',95,28)
save(im,'placement.png')


im,d=base('GarageBand: build the mono voice track',h=1060)
box(d,65,210,470,290,'1 / SETTINGS','GarageBand > Settings > Audio/MIDI. Input Device M4. Output Device M4.',TEAL)
box(d,565,210,470,290,'2 / AUDIO TRACK','Empty Project > Audio (microphone). Smart Controls B > Recording Settings > Input 3. Mono format.',BLUE)
box(d,1065,210,470,290,'3 / CLEAN CAPTURE','Monitoring ON. M4 MON buttons OFF. Track pan center. Track level 0 dB. All effects and Noise Gate OFF.',TEAL)
box(d,65,550,710,280,'4 / ADVANCED','Recording depth 24-bit. Export projects at full volume OFF (older releases: Auto Normalize). GarageBand manages project sample rate.',BLUE)
box(d,825,550,710,280,'5 / RECORD AND EDIT','R records; Space stops. Command-T splits at playhead. A shows volume automation. Keep original takes in a saved copy.',TEAL)
wrap(d,(65,910),'Original menu map, not a screenshot. Check names against your installed GarageBand version.',90,28,MUTED);save(im,'garageband-map.png')
im,d=base('Live 12 Lite: route and arm one voice',h=1000)
box(d,65,210,710,300,'A / SETTINGS > AUDIO','CoreAudio. Input + Output M4. Sample rate 48000. Buffer 128 samples. Input Config: mono 3 ON. Output Config: stereo 1/2 ON.',TEAL)
box(d,825,210,710,300,'B / ARRANGEMENT AUDIO TRACK','Audio From: Ext. In > 3. Monitor: Auto. Arm: ON while recording. Audio To: Main. Pan center. Fader 0 dB. Sends -infinity.',BLUE)
box(d,65,560,710,270,'C / RECORD, WARP & LAUNCH','WAV / 24-bit. Auto-Warp Long Samples OFF for speech. Save the project. Arrangement Record + start transport.',BLUE)
box(d,825,560,710,270,'D / PLAYBACK AND EDIT','Stop and disarm. Clip Warp OFF. Transpose 0. Command-E splits. Use fade handles at quiet edit points. Collect All and Save.',TEAL)
wrap(d,(65,900),'Original function map. Audio track 3/4 is a stereo pair: choose mono 3 for this single cable.',94,27,MUTED);save(im,'live-map.png')
im,d=base('Export: inspect the file, not just the session',h=900)
box(d,65,210,470,370,'GARAGEBAND','Share > Export Song to Disk. WAVE / 24-bit. Intended range. Full-volume / Auto Normalize OFF. Stereo export expected; verify sample rate.',TEAL)
box(d,565,210,470,370,'LIVE 12 LITE','Export Audio/Video. Render Main. WAV / 24-bit / project rate. Normalize OFF. Loop OFF. Stereo master; final PCM dither as specified.',BLUE)
box(d,1065,210,470,370,'VERIFY','Listen from first word to last. Measure integrated loudness and true peak on exported file. Check format with afinfo. Keep raw take + edited master.',TEAL)
wrap(d,(65,670),'A microphone preset is not a delivery loudness target. Finish the episode, measure it, and retain a clean uncompressed master.',92,30,INK,True);save(im,'export-map.png')
print('Generated cover, headboard and eleven original plates.')
