#!/usr/bin/env python3
from pathlib import Path
import json,csv,io
root=Path(__file__).resolve().parents[1]
data=json.loads((root/'presets.json').read_text())
def table(rows):return '\n| Control | Set / verify |\n|---|---|\n'+''.join(f'| {k} | {v} |\n' for k,v in rows)+'\n'
text='# Six microphone-and-chain recall cards\n\nThese cards join the microphone-specific power and mode settings to three shared toolchain recipes. Complete the gain calibration every time you change mic, mode, distance or delivery. The suggested starting values are identical where no measurement justifies a difference. Save the final calibrated versions separately for each mic.\n\n'
for mic in data['mics']:
    text+=f"## {mic['name']}: mic settings for all three cards\n\n"
    text+=table([('Power',mic['power']),('Mode', '; '.join(mic['modes'])),('Pattern',mic['pattern']),('Pad',mic['pad']),('Filter',mic['filter']),('Other internal state',mic['hf'])])
    text+=mic['modeNote']+'\n\n'
    for preset in data['presets']:
        text+=f"### {mic['id'].upper()} / {preset['name']}\n\n{preset['description']}\n\n**Placement:** {preset['distance']}.\n\n"
        text+='**PRE-73 Premier**\n'+table({**preset['pre'], '48V': 'OFF; BeesNeez uses its matching PSU' if mic['id']=='bees' else 'ON after XLR is connected'}.items())
        text+='**COMP-54**\n'+table(preset['comp'].items())
        text+=f"**DAW:** {preset['processing']} Use the selected DAW card below; keep a separate saved session for this microphone.\n\n"
text+='## M4 settings for every card\n'+table(data['m4'].items())
for v in data['daws'].values():
    text+='## '+v['name']+' settings for every card\n'+table(v['settings'].items())+'\n'+v['finish']+'\n\n'
text+='## Write your calibrated recall\n\nRecord the take filename, PRE gain detent and OUTPUT mark, COMP threshold mark and MAKEUP mark, observed loudest input peak, usual and maximum gain reduction, actual DAW plug-in settings, output channel layout, LUFS and true peak. A suggested recipe becomes your preset only after this record is complete.\n'
(root/'chapters/03-recall-cards.md').write_text(text)
# Manuscript intentionally assembled from source chapters; no renderer-specific hidden blocks.
daw=root/'chapters/03-daw.md'
dawtext=daw.read_text()
dawtext=dawtext.replace('## Prepare macOS before opening a project','![Settings map: use the application-specific choices below rather than treating every Mac audio menu as the same control.](assets/mac-map.png)\n\n## Prepare macOS before opening a project')
parts=[(root/'chapters/01-foundations.md').read_text(),(root/'chapters/02-hardware.md').read_text(),dawtext,(root/'chapters/03-recall-cards.md').read_text(),(root/'chapters/04-testing-and-recall.md').read_text()]
man='\n\n'.join(parts)
# Portable ASCII hyphens to avoid nonbreaking dash glyphs; normal punctuation supported by fonts.
man=man.replace('\u2011','-').replace('\u2010','-')
(root/'manuscript.md').write_text(man+'\n')
# Session comparison log is intentionally empty: no invented measurements.
fields=['date','take_id','audio_file','mic','mode','pattern','mic_pad','mic_hpf','bees_s2','rf_state','distance_cm','angle_deg','pre_gain_db','pre_output_mark','pre_48v','pre_line','pre_di','pre_low_z','pre_hpf','pre_air','pre_output_pad','pre_polarity','comp_bypass','comp_in_out','comp_threshold_mark','comp_ratio','comp_attack_ms','comp_recovery','comp_sc_hp','comp_makeup_mark','comp_term','comp_link','comp_meter','gr_normal_db','gr_max_db','m4_input','m4_gain_if_front','m4_phantom','monitor_path','monitor_mix','daw_version','sample_rate_hz','bit_depth','buffer_samples','plugins_and_values','record_peak_dbfs','matched_gain_db','integrated_lufs','true_peak_dbtp','channel_layout','intelligibility_1_5','body_1_5','sibilance_1_5','plosive_control_1_5','room_control_1_5','low_fatigue_1_5','decision','notes']
with (root/'comparison-log.csv').open('w') as f:csv.writer(f).writerow(fields)
sweeps=[
('Geometry','Distance','15 cm;20 cm;30 cm','Both','Recalibrate safe capture, then match playback','Proximity bass, room, plosives'),
('Geometry','Angle','0 degrees;15 degrees;30 degrees','Both','Keep distance fixed','Sibilance and breath'),
('Mic','Pattern','cardioid;omni;figure-eight','Both','Mute and allow settling; recalibrate','Room pickup'),
('Mic','Intermediate pattern','all remaining PSU pattern detents','Bees','Mark by icon/detent; fixed position','Room rejection'),
('Mic','Profile','67 Vintage;67 New;269 Vintage;269 New','Bees','Only after manufacturer confirms safe unpowered handling; otherwise as found','Voicing at equal loudness'),
('Mic','Profile','Vintage;Modern','Twin87','Mute, allow about10s settling, recalibrate','Voicing at equal loudness'),
('Mic','Pad','off;-10 dB','Both','Bees internal only if procedure verified; power-safe changes','Mic overload vs added gain demand'),
('Mic','High-pass','off;on','Both','Bees internal only if verified; other filters off','Rumble/body'),
('Mic','S2','off;on','Bees','Internal verified procedure only','Low bass shaping'),
('Mic','RF group','as found;documented enabled/bypass group','Twin87','Optional interference troubleshooting; unpowered manual procedure only','RF rejection, not routine tone control'),
('PRE','Gain/output','reference;one gain step up + output reduced','Both','Safe peaks and matched listening; do not clip','Coloration'),
('PRE','LOW-Z','1200;300 ohms','Twin87','Level recalibration; Bees remains1200 baseline','Tone and sensitivity'),
('PRE','High-pass','OFF;80 Hz;200 Hz','Both','Other audio high-passes off','Rumble/body'),
('PRE','Air','OFF;+3 dB;+6 dB','Both','Match output; no assumed enhancement','Openness/noise'),
('PRE','Output pad','0;14 dB','Both','Compensated test; nominal attenuation depends on termination','Drive/headroom'),
('PRE','Polarity','normal;inverted','Both','Single isolated track only; avoid summing','Waveform sign, no expected solo tone change'),
('PRE','48V / LINE / DI / power','functional checks only','Both','Correct source and mic power, never live sweep','Routing'),
('PRE','Insert / internal termination','leave as configured','Both','No routine internal service','No test required'),
('COMP','Circuit','hard bypass;compression out;compression in','Both','Match loudness, check ADC peak','Color vs gain control'),
('COMP','Threshold','target0;target1;target3;target6 dB GR','Both','Record actual threshold mark','Reduction amount'),
('COMP','Ratio','1.5:1;2:1;3:1;4:1;6:1','Both','Label fixed-threshold vs equal-GR test','Level control'),
('COMP','Attack','0.5;1;2;3;6;12;25;50 ms','Both','Only attack changes within sweep','Consonants/peaks'),
('COMP','Recovery','25;50;100;400;800 ms;1.5 s;Auto1;Auto2','Both','Only recovery changes','Pumping and gaps'),
('COMP','SC HP','OFF;50 Hz;100 Hz;7 kHz','Both','Detector filter, not audio high-pass','LF/sibilant triggering'),
('COMP','Makeup','minimum;matched-bypass level','Both','No calibrated dB scale; measure output','Level not tone preference'),
('COMP','Meter','COMP;OUTPUT','Both','Read correct scale','GR vs analog output'),
('COMP','Link / rear termination / power','unlinked;termination per manual;power on','Both','Functional check; no second COMP present','Routing/load'),
('M4','Input','rear3;optional front1TRS','Both','Front1 min gain/48Voff/DAWmono1; recalibrate','Monitor path/headroom'),
('M4','Monitoring','software;optional front1 direct mono','Both','Exactly one path; rear3 direct left only','Latency'),
('M4','Listening levels','headphones comfortable;monitor down','Both','Do not use listening controls to set capture','Comfort'),
('DAW','Buffer','128;256;512 samples in Live','Both','No buffer quality claim; GB app-managed','Latency and crackles'),
('DAW','Rate/depth','GB native/24-bit;Live48k/24-bit','Both','For direct A/B use same rate/layout','Workflow check'),
('DAW','EQ','flat;one band at a time','Both','Exact same recorded take and matched loudness','Corrective benefit'),
('DAW','Compressor','bypass;2:1 gentle;threshold sweep','Both','Exact same take; avoid double compression','Steadiness'),
('DAW','Limiter','bypass;TruePeak -1.5dB ceiling','Both','Post only; rendered-file loudness/peak check','Delivery protection'),
('DAW','Export','normalize off;24-bitWAV;specified layout','Both','Listen full exported file','No truncation or changed level')]
with (root/'control-sweeps.csv').open('w') as f:
 w=csv.writer(f);w.writerow(['stage','control','candidate_settings','mic','prerequisite','listening_question']);w.writerows(sweeps)
print(f'{len(man.split())} words; {man.count(chr(10)+"# ")+1} chapters; {len(sweeps)} control sweeps')
