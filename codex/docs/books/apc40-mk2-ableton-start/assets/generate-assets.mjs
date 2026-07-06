import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const outDir = path.dirname(fileURLToPath(import.meta.url));

const colors = {
  bg: "#f6f3eb",
  ink: "#20242b",
  panel: "#ffffff",
  line: "#b8b2a7",
  dark: "#242830",
  darker: "#171a20",
  blue: "#2f80ed",
  teal: "#189a86",
  green: "#3aa657",
  amber: "#f4a62a",
  red: "#d84a3a",
  purple: "#7a5cff",
  pink: "#d95f9f",
  gray: "#6b7280",
};

function esc(value) {
  return String(value)
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;");
}

function svg(name, width, height, body) {
  const text = `<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="${width}" height="${height}" viewBox="0 0 ${width} ${height}" role="img" aria-label="${esc(name)}">
  <defs>
    <style>
      .title { font: 700 28px Arial, sans-serif; fill: ${colors.ink}; }
      .subtitle { font: 400 16px Arial, sans-serif; fill: ${colors.gray}; }
      .label { font: 700 13px Arial, sans-serif; fill: ${colors.ink}; }
      .small { font: 400 11px Arial, sans-serif; fill: ${colors.ink}; }
      .tiny { font: 400 9px Arial, sans-serif; fill: ${colors.ink}; }
      .white { fill: #fff; }
      .mono { font: 700 10px Menlo, Consolas, monospace; fill: ${colors.ink}; }
    </style>
  </defs>
  <rect width="100%" height="100%" fill="${colors.bg}"/>
  ${body}
</svg>
`;
  fs.writeFileSync(path.join(outDir, name), text);
}

function text(x, y, value, cls = "small", anchor = "start") {
  return `<text x="${x}" y="${y}" class="${cls}" text-anchor="${anchor}">${esc(value)}</text>`;
}

function rect(x, y, w, h, fill, stroke = colors.line, rx = 6) {
  return `<rect x="${x}" y="${y}" width="${w}" height="${h}" rx="${rx}" fill="${fill}" stroke="${stroke}" stroke-width="1"/>`;
}

function line(x1, y1, x2, y2, stroke = colors.ink, width = 1) {
  return `<line x1="${x1}" y1="${y1}" x2="${x2}" y2="${y2}" stroke="${stroke}" stroke-width="${width}"/>`;
}

function knob(cx, cy, r, fill = colors.dark, label = "") {
  return `<circle cx="${cx}" cy="${cy}" r="${r}" fill="${fill}" stroke="#0a0c10" stroke-width="2"/>
${line(cx, cy, cx + r * 0.55, cy - r * 0.55, "#fff", 2)}
${label ? text(cx, cy + r + 13, label, "tiny", "middle") : ""}`;
}

function button(x, y, w, h, fill, label = "", cls = "tiny") {
  return `${rect(x, y, w, h, fill, "#111", 4)}${label ? text(x + w / 2, y + h / 2 + 3, label, cls, "middle") : ""}`;
}

function darkButton(x, y, w, h, label = "") {
  return `${rect(x, y, w, h, colors.dark, "#111", 4)}${label ? `<text x="${x + w / 2}" y="${y + h / 2 + 3}" style="font: 700 9px Arial, sans-serif; fill: #fff;" text-anchor="middle">${esc(label)}</text>` : ""}`;
}

function titleBlock(title, subtitle) {
  return `${text(34, 42, title, "title")}${text(36, 66, subtitle, "subtitle")}`;
}

function liveWindow(title, body) {
  return `
    ${rect(34, 86, 1132, 640, colors.panel, colors.line, 10)}
    ${rect(34, 86, 1132, 42, "#dedbd3", colors.line, 10)}
    ${text(60, 113, "Ableton Live 12 - " + title, "label")}
    ${body}
  `;
}

svg(
  "plate-01-live12-midi-settings.svg",
  1200,
  760,
  `${titleBlock("Ableton Live 12 setup: Link, Tempo and MIDI", "Set the APC40 MK2 as a native control surface before you touch mapping.")}
  ${liveWindow(
    "Settings",
    `
      ${rect(60, 150, 190, 540, "#f2f0eb", colors.line, 8)}
      ${["Audio", "Link, Tempo and MIDI", "File Folder", "Record Warp Launch", "Library", "Licenses"].map((v, i) =>
        rect(76, 172 + i * 48, 158, 34, i === 1 ? "#d7e8ff" : "#ffffff", colors.line, 5) +
        text(88, 194 + i * 48, v, i === 1 ? "label" : "small")
      ).join("")}
      ${text(282, 166, "Control Surface", "label")}
      ${text(530, 166, "Input", "label")}
      ${text(778, 166, "Output", "label")}
      ${rect(282, 184, 220, 38, "#fff", colors.blue, 5)}
      ${rect(530, 184, 220, 38, "#fff", colors.blue, 5)}
      ${rect(778, 184, 220, 38, "#fff", colors.blue, 5)}
      ${text(294, 208, "APC40 mkII", "label")}
      ${text(542, 208, "APC40 mkII", "label")}
      ${text(790, 208, "APC40 mkII", "label")}
      ${text(282, 272, "MIDI Ports", "label")}
      ${text(282, 302, "Port", "small")}
      ${text(690, 302, "Track", "small")}
      ${text(775, 302, "Sync", "small")}
      ${text(858, 302, "Remote", "small")}
      ${[
        ["Input: APC40 mkII", "On", "Off", "On"],
        ["Output: APC40 mkII", "On", "Off", "On"],
        ["Input: APC40 mkII DAW", "Off", "Off", "Off"],
        ["Output: APC40 mkII DAW", "Off", "Off", "Off"],
      ].map((row, i) => {
        const y = 322 + i * 46;
        return `${rect(282, y, 660, 34, i < 2 ? "#fbfff8" : "#fff", colors.line, 4)}
          ${text(300, y + 22, row[0], "small")}
          ${button(690, y + 7, 48, 20, row[1] === "On" ? colors.green : "#ddd", row[1], "tiny")}
          ${button(775, y + 7, 48, 20, row[2] === "On" ? colors.green : "#ddd", row[2], "tiny")}
          ${button(858, y + 7, 58, 20, row[3] === "On" ? colors.green : "#ddd", row[3], "tiny")}`;
      }).join("")}
      ${rect(282, 560, 790, 84, "#fff7de", "#e0b54b", 8)}
      ${text(306, 590, "Zero-to-one rule", "label")}
      ${text(306, 616, "If clip grid and faders work already, do not create MIDI mappings yet.", "small")}
      ${text(306, 640, "Use manual MIDI Map only after the native script is confirmed.", "small")}
    `
  )}`
);

function apcBody(highlight = {}) {
  const grid = [];
  const trackNames = ["DRUM", "PERC", "BASS", "KEYS", "TRPT", "HARM", "PAD", "FX"];
  const sceneNames = ["INTRO", "GROOVE", "HOOK", "BREAK", "END"];
  const clipColors = [colors.green, colors.amber, colors.blue, colors.purple, colors.red];
  for (let r = 0; r < 5; r++) {
    for (let c = 0; c < 8; c++) {
      grid.push(button(78 + c * 56, 132 + r * 48, 42, 34, clipColors[(r + c) % clipColors.length], `${c + 1}.${r + 1}`));
    }
    grid.push(button(542, 132 + r * 48, 62, 34, "#252a33", sceneNames[r], "tiny"));
  }
  const stops = trackNames.map((t, i) => button(78 + i * 56, 386, 42, 24, "#eee", "STOP"));
  const selectors = trackNames.map((t, i) => button(78 + i * 56, 420, 42, 24, "#d7e8ff", t));
  const trackButtons = trackNames.map((t, i) => {
    const x = 78 + i * 56;
    return `${button(x, 458, 42, 20, "#ececec", "#")}
      ${button(x, 482, 42, 20, "#ececec", "S")}
      ${button(x, 506, 42, 20, "#ececec", "REC")}`;
  });
  const faders = trackNames.map((t, i) => {
    const x = 82 + i * 56;
    const top = 550 + (i % 3) * 8;
    return `${rect(x, 548, 12, 108, "#d0d0d0", "#777", 3)}
      ${rect(x - 8, top + 40, 28, 12, colors.dark, "#111", 3)}
      ${text(x + 6, 676, t, "tiny", "middle")}`;
  });
  const channelKnobs = trackNames.map((_, i) => knob(96 + i * 56, 92, 13, colors.dark, `C${i + 1}`));
  const deviceKnobs = Array.from({ length: 8 }, (_, i) => knob(732 + (i % 4) * 72, 150 + Math.floor(i / 4) * 68, 18, colors.dark, `D${i + 1}`));
  return `
    ${rect(42, 82, 1070, 625, "#1d222a", "#090b0f", 14)}
    ${text(60, 112, "APC40 MK2 surface", "label")}
    ${channelKnobs.join("")}
    ${grid.join("")}
    ${stops.join("")}
    ${selectors.join("")}
    ${trackButtons.join("")}
    ${faders.join("")}
    ${button(624, 132, 72, 34, highlight.stopAll ? colors.red : "#eeeeee", "STOP ALL")}
    ${button(624, 182, 72, 30, "#eaeaea", "PAN")}
    ${button(624, 218, 72, 30, "#eaeaea", "SENDS")}
    ${button(624, 254, 72, 30, "#eaeaea", "USER")}
    ${deviceKnobs.join("")}
    ${button(718, 296, 70, 28, "#eaeaea", "DETAIL")}
    ${button(798, 296, 70, 28, "#eaeaea", "CLIP/DEV")}
    ${button(878, 296, 70, 28, "#eaeaea", "LOCK")}
    ${button(718, 352, 46, 28, "#eaeaea", "<")}
    ${button(770, 352, 46, 28, "#eaeaea", ">")}
    ${button(870, 352, 46, 28, "#eaeaea", "BANK")}
    ${button(920, 352, 46, 28, "#eaeaea", "SHIFT")}
    ${button(746, 414, 46, 28, "#eaeaea", "UP")}
    ${button(694, 454, 46, 28, "#eaeaea", "LEFT")}
    ${button(746, 454, 46, 28, "#eaeaea", "DOWN")}
    ${button(798, 454, 46, 28, "#eaeaea", "RIGHT")}
    ${rect(728, 548, 260, 18, "#c9c9c9", "#777", 4)}
    ${rect(812, 542, 28, 30, colors.dark, "#111", 4)}
    ${text(858, 590, "CROSSFADER", "tiny", "middle")}
    ${button(1008, 548, 70, 30, colors.green, "PLAY")}
    ${button(1008, 586, 70, 30, colors.red, "RECORD")}
    ${button(1008, 624, 70, 30, colors.amber, "SESSION")}
  `;
}

svg(
  "plate-02-apc40-surface-overview.svg",
  1200,
  760,
  `${titleBlock("APC40 MK2: every zone you will touch first", "The book begins with APC only: grid, scenes, faders, track buttons, device knobs, transport.")}
  ${apcBody()}`
);

svg(
  "plate-03-session-template-oh-long-johnson.svg",
  1200,
  760,
  `${titleBlock("Ableton Session View template for the Kiffness practice set", "Eight tracks by five scenes match the visible APC grid exactly.")}
  ${liveWindow(
    "Session View",
    `
      ${text(76, 158, "Global Quantization: 1 Bar", "label")}
      ${text(330, 158, "Tempo: 96 BPM starter", "label")}
      ${text(590, 158, "Scene Launch is on the right edge", "label")}
      ${["DRUMS", "PERC", "BASS", "KEYS", "TRUMPET", "HARMONY", "PADS", "FX"].map((t, i) =>
        rect(70 + i * 122, 190, 108, 34, "#eef2ff", colors.line, 5) +
        text(124 + i * 122, 212, t, "label", "middle")
      ).join("")}
      ${["Intro", "Groove", "Hook", "Break", "Ending"].map((s, r) => {
        const row = [];
        for (let c = 0; c < 8; c++) {
          const names = [
            ["hat click", "shaker", "sub", "keys", "mute", "air", "pad", "noise"],
            ["kick snare", "darbuka", "bass", "keys", "trumpet", "harm 1", "pad", "delay"],
            ["full drums", "perc fill", "bass 2", "keys 2", "trpt hook", "harm 2", "wide pad", "riser"],
            ["snare off", "darbuka", "bass hold", "keys dub", "trpt stab", "vox chop", "filter pad", "impact"],
            ["drums end", "perc end", "bass end", "keys end", "trpt end", "harm end", "pad tail", "verb tail"],
          ];
          row.push(rect(70 + c * 122, 238 + r * 78, 108, 54, ["#dff7e4", "#fff0cf", "#dbeafe", "#ede9fe", "#ffe4e6"][r], colors.line, 5));
          row.push(text(124 + c * 122, 268 + r * 78, names[r][c], "tiny", "middle"));
        }
        row.push(button(1062, 248 + r * 78, 70, 34, colors.dark, s, "tiny"));
        return row.join("");
      }).join("")}
      ${text(76, 684, "APC rule: one column equals one track, one row equals one scene. A row button launches a full musical moment.", "label")}
    `
  )}`
);

svg(
  "plate-04-apc-grid-performance-map.svg",
  1200,
  760,
  `${titleBlock("APC grid performance map: what each row does", "Use this as the top-down hardware cheat sheet while practicing the track.")}
  ${apcBody()}
  ${rect(650, 104, 430, 160, "#fff", colors.line, 8)}
  ${text(674, 136, "Scene rows", "label")}
  ${text(674, 164, "1 Intro: tiny texture, no pressure", "small")}
  ${text(674, 188, "2 Groove: core loop enters", "small")}
  ${text(674, 212, "3 Hook: full Kiffness moment", "small")}
  ${text(674, 236, "4 Break: strip drums and create space", "small")}
  ${text(674, 260, "5 End: tails, stop, and clean finish", "small")}
  ${rect(650, 284, 430, 126, "#fff", colors.line, 8)}
  ${text(674, 316, "How to press", "label")}
  ${text(674, 344, "Start with a scene button on the right.", "small")}
  ${text(674, 368, "Then add or swap individual clips in the grid.", "small")}
  ${text(674, 392, "If lost, press STOP ALL and return to Intro.", "small")}`
);

svg(
  "plate-05-mixer-and-fader-moves.svg",
  1200,
  760,
  `${titleBlock("Mixer practice: faders, mutes, solo, record arm", "The APC40 MK2 is an Ableton mixer you can play with both hands.")}
  ${apcBody()}
  ${rect(650, 104, 440, 222, "#fff", colors.line, 8)}
  ${text(674, 136, "Starter fader targets", "label")}
  ${[
    "Drums: -6 dB, never louder than master",
    "Percussion: start low, fade up in Hook",
    "Bass: stable center, no sudden drops",
    "Keys and pads: fade for width",
    "Trumpet and harmony: feature, then tuck back",
    "FX: low until transitions",
  ].map((v, i) => text(674, 166 + i * 26, v, "small")).join("")}
  ${rect(650, 356, 440, 150, "#fff7de", "#e0b54b", 8)}
  ${text(674, 388, "First performance move", "label")}
  ${text(674, 418, "Launch Groove, then use only faders for 60 seconds.", "small")}
  ${text(674, 444, "Mute with Track Activator buttons, not the mouse.", "small")}
  ${text(674, 470, "Solo only while diagnosing. Do not solo during the take.", "small")}`
);

svg(
  "plate-06-device-and-send-controls.svg",
  1200,
  760,
  `${titleBlock("Device, pan, sends, and user modes", "Two knob rows have different jobs. Learn them separately before improvising.")}
  ${apcBody()}
  ${rect(650, 104, 440, 180, "#fff", colors.line, 8)}
  ${text(674, 136, "Channel control knobs", "label")}
  ${text(674, 164, "PAN: eight knobs pan the current eight tracks.", "small")}
  ${text(674, 190, "SENDS: eight knobs control Send A by default.", "small")}
  ${text(674, 216, "Hold SENDS + Track Selector 2 for Send B.", "small")}
  ${text(674, 242, "USER: manual MIDI mappings only after native setup works.", "small")}
  ${rect(650, 314, 440, 196, "#fff", colors.line, 8)}
  ${text(674, 346, "Device control knobs", "label")}
  ${text(674, 374, "Select a track. Press CLIP/DEV until Device View appears.", "small")}
  ${text(674, 400, "Device Left/Right chooses the device.", "small")}
  ${text(674, 426, "D1-D8 control the selected device bank.", "small")}
  ${text(674, 452, "Bank Left/Right moves to another bank.", "small")}
  ${text(674, 478, "Device Lock keeps those knobs on the same device.", "small")}`
);

svg(
  "plate-07-clip-launch-states.svg",
  1200,
  760,
  `${titleBlock("Clip launch states and what the lights mean", "The lights tell you whether a slot is empty, queued, playing, or stopped.")}
  ${liveWindow(
    "Clip States",
    `
      ${rect(82, 170, 460, 460, "#20242b", "#111", 12)}
      ${[
        ["Empty slot", "#343942", "No clip here. Pressing does nothing."],
        ["Loaded, stopped", colors.blue, "Clip exists and can be launched."],
        ["Queued", colors.amber, "Will launch on the next quantized beat/bar."],
        ["Playing", colors.green, "Clip is running now."],
        ["Stop queued", colors.red, "This track will stop at the next boundary."],
      ].map((row, i) =>
        `${button(124, 214 + i * 72, 58, 42, row[1], "")}
         ${text(210, 238 + i * 72, row[0], "label")}
         ${text(210, 260 + i * 72, row[2], "small")}`
      ).join("")}
      ${rect(610, 170, 470, 238, "#fff", colors.line, 8)}
      ${text(640, 206, "Starter launch settings", "label")}
      ${text(640, 240, "Global Quantization: 1 Bar", "small")}
      ${text(640, 268, "Clip Launch Mode: Trigger", "small")}
      ${text(640, 296, "Legato: Off for beginners", "small")}
      ${text(640, 324, "Follow Actions: Off until the grid feels natural", "small")}
      ${text(640, 352, "Warp: On for audio loops that must stay in tempo", "small")}
      ${rect(610, 450, 470, 118, "#fff7de", "#e0b54b", 8)}
      ${text(640, 486, "Hands rule", "label")}
      ${text(640, 518, "Right hand launches scenes.", "small")}
      ${text(640, 546, "Left hand rides faders and mutes.", "small")}
    `
  )}`
);

svg(
  "plate-08-record-to-arrangement.svg",
  1200,
  760,
  `${titleBlock("Record an APC performance into Arrangement", "Session View is for playing. Arrangement View captures the performance.")}
  ${liveWindow(
    "Record Performance",
    `
      ${rect(76, 158, 1020, 98, "#f4f4f5", colors.line, 8)}
      ${button(104, 190, 70, 34, colors.green, "PLAY")}
      ${button(190, 190, 88, 34, colors.red, "ARR REC")}
      ${button(294, 190, 106, 34, colors.amber, "SESSION REC")}
      ${text(436, 212, "Press Arrangement Record if you want Live to log scene launches, clip launches, fader moves, and mutes.", "small")}
      ${rect(76, 306, 1020, 280, "#fff", colors.line, 8)}
      ${[0,1,2,3,4,5,6,7].map((i) => {
        const y = 336 + i * 28;
        return `${text(98, y + 17, ["DRUMS","PERC","BASS","KEYS","TRPT","HARM","PADS","FX"][i], "tiny")}
          ${rect(180, y, 860, 18, i % 2 ? "#dbeafe" : "#dcfce7", "#fff", 3)}
          ${rect(180 + i * 44, y, 80, 18, i % 2 ? colors.blue : colors.green, "#fff", 3)}`;
      }).join("")}
      ${text(96, 640, "After the take: press Stop twice, switch to Arrangement, listen, then save as 'APC Oh Long Johnson Practice 01'.", "label")}
    `
  )}`
);

svg(
  "plate-09-oh-long-johnson-track-map.svg",
  1200,
  760,
  `${titleBlock("Kiffness exercise track: Oh Long Johnson", "This track is chosen because it uses enough layers to justify the APC40 MK2 surface.")}
  ${rect(60, 104, 1080, 560, "#fff", colors.line, 10)}
  ${text(92, 146, "Practice target: recreate the structure, not the copyrighted recording.", "label")}
  ${[
    ["1 DRUMS", "kick, snare, hi-hat, snare-off break"],
    ["2 PERC", "darbuka, shaker, percussion fill"],
    ["3 BASS", "main bass, bass hold, ending bass"],
    ["4 KEYS", "keys, dub keys, short stabs"],
    ["5 TRUMPET", "trumpet hook, open trumpet, stabs"],
    ["6 HARMONY", "vocal harmony 1, vocal harmony 2, chop"],
    ["7 PADS", "pads, wide pad, filtered pad tail"],
    ["8 FX", "delay throw, riser, impact, verb tail"],
  ].map((row, i) => {
    const y = 190 + i * 48;
    return `${rect(96, y, 160, 34, ["#dcfce7", "#fff0cf", "#dbeafe", "#ede9fe"][i % 4], colors.line, 5)}
      ${text(118, y + 22, row[0], "label")}
      ${text(286, y + 22, row[1], "small")}`;
  }).join("")}
  ${rect(92, 594, 970, 44, "#fff7de", "#e0b54b", 8)}
  ${text(118, 622, "The goal is a legal, original practice set inspired by the visible layer logic, using your own sounds.", "label")}`
);

svg(
  "plate-10-troubleshooting-flow.svg",
  1200,
  760,
  `${titleBlock("Troubleshooting: when the APC does not behave", "Fix recognition first, then native control, then manual mapping.")}
  ${[
    ["USB connected and APC powered?", "Try another cable/port. Avoid hubs for first setup."],
    ["Does Live show APC40 mkII in Settings?", "Select Control Surface, Input, and Output manually."],
    ["Does the grid rectangle move in Session View?", "Native script is alive. Do not MIDI-map yet."],
    ["Do faders move track volumes?", "If no, check Output port and Remote On."],
    ["Do clips launch on the grid?", "Use Session View, loaded clips, Global Quantization 1 Bar."],
    ["Still stuck?", "Close Live, unplug nonessential MIDI gear, reopen, then reconnect APC."],
  ].map((row, i) => {
    const x = 110 + (i % 2) * 500;
    const y = 124 + Math.floor(i / 2) * 170;
    return `${rect(x, y, 420, 100, "#fff", colors.line, 8)}
      ${text(x + 24, y + 34, `${i + 1}. ${row[0]}`, "label")}
      ${text(x + 24, y + 66, row[1], "small")}
      ${i < 4 ? line(x + 210, y + 104, x + 210, y + 146, colors.gray, 2) : ""}`;
  }).join("")}
  ${rect(250, 642, 700, 54, "#fff7de", "#e0b54b", 8)}
  ${text(600, 676, "Most APC problems are setup-state problems, not broken hardware.", "label", "middle")}`
);

svg(
  "plate-11-dont-cry-tonight-apc-map.svg",
  1200,
  760,
  `${titleBlock("Don't Cry Tonight APC40 remix study", "Eight tracks by eight scenes: use APC grid, scene launch, faders, mutes, sends, and device macros.")}
  ${liveWindow(
    "Session View",
    `
      ${text(70, 156, "Tempo: 116-122 BPM", "label")}
      ${text(288, 156, "Global Quantization: 1 Bar", "label")}
      ${text(560, 156, "Practice length: 64 bars", "label")}
      ${["KICK", "CLAP", "HATS", "BASS", "CHORDS", "LEAD", "PAD", "FX"].map((t, i) =>
        rect(62 + i * 118, 188, 104, 32, "#eef2ff", colors.line, 5) +
        text(114 + i * 118, 209, t, "label", "middle")
      ).join("")}
      ${[
        ["Intro", ["soft kick", "", "hat pulse", "", "filtered", "", "dark pad", "noise"]],
        ["Groove", ["4-on-floor", "backbeat", "8th hats", "octave", "low stab", "", "pad", "short riser"]],
        ["Verse", ["kick", "clap", "hat lift", "bass", "chords", "lead/vocal", "pad", "delay"]],
        ["Lift", ["kick", "clap", "open hat", "bass", "filter open", "answer", "wide pad", "riser"]],
        ["Chorus A", ["full kick", "clap", "hat+open", "full bass", "wide chords", "main hook", "wide pad", "crash"]],
        ["Chorus B", ["full kick", "clap fill", "hat fill", "bass var", "chords var", "hook var", "pad high", "delay throw"]],
        ["Break", ["", "", "hat ghost", "bass hold", "pad chord", "lead/vocal", "filter pad", "impact"]],
        ["Tag/End", ["kick end", "clap end", "hat end", "bass end", "chord end", "final hook", "tail", "verb tail"]],
      ].map((row, r) => {
        const y = 238 + r * 52;
        const cells = row[1].map((name, c) =>
          rect(62 + c * 118, y, 104, 36, ["#dcfce7", "#fff0cf", "#dbeafe", "#ede9fe", "#ffe4e6", "#ccfbf1", "#f3e8ff", "#e5e7eb"][c], colors.line, 5) +
          text(114 + c * 118, y + 23, name || "empty", "tiny", "middle")
        ).join("");
        return cells + darkButton(1026, y + 2, 78, 30, row[0]);
      }).join("")}
      ${rect(72, 668, 970, 34, "#fff7de", "#e0b54b", 8)}
      ${text(96, 690, "Legal practice rule: rebuild the feel with your own sounds, cleared vocals, or a lead-synth stand-in.", "label")}
    `
  )}`
);

// ---------------------------------------------------------------------------
// Plates 12-21: complete-newbie detail pass for the Don't Cry Tonight build.
// ---------------------------------------------------------------------------

function wtext(x, y, value, cls = "small", anchor = "start") {
  const styles = {
    title: "font: 700 28px Arial, sans-serif;",
    label: "font: 700 13px Arial, sans-serif;",
    small: "font: 400 11px Arial, sans-serif;",
    tiny: "font: 400 9px Arial, sans-serif;",
  };
  return `<text x="${x}" y="${y}" style="${styles[cls] || styles.small} fill: #edf2f7;" text-anchor="${anchor}">${esc(value)}</text>`;
}

svg(
  "plate-12-ableton-first-launch.svg",
  1200,
  760,
  `${titleBlock("Your first look at Ableton Live 12", "Six zones matter on day one. Everything in this book happens in these zones.")}
  ${liveWindow(
    "Session View (press Tab if you see a horizontal timeline instead)",
    `
      ${rect(60, 144, 88, 30, "#eef2ff", colors.blue, 5)}
      ${text(74, 164, "118 BPM", "label")}
      ${button(160, 144, 44, 30, colors.green, "PLAY")}
      ${button(210, 144, 44, 30, "#eee", "STOP")}
      ${button(260, 144, 44, 30, colors.red, "REC")}
      ${rect(316, 144, 96, 30, "#eef2ff", colors.blue, 5)}
      ${text(330, 164, "Q: 1 Bar", "label")}
      ${text(430, 164, "6. Control bar: tempo, transport, Global Quantization", "small")}
      ${rect(60, 190, 200, 496, "#f2f0eb", colors.line, 8)}
      ${text(76, 218, "1. Browser", "label")}
      ${["Sounds", "Drums", "Instruments", "Audio Effects", "MIDI Effects", "Samples", "Clips"].map((v, i) =>
        text(88, 250 + i * 30, v, i === 1 ? "label" : "small")
      ).join("")}
      ${text(76, 480, "Find kits, presets,", "small")}
      ${text(76, 500, "and samples here.", "small")}
      ${text(76, 520, "Drag them onto", "small")}
      ${text(76, 540, "tracks.", "small")}
      ${["KICK", "CLAP", "HATS", "BASS"].map((t, i) =>
        rect(292 + i * 130, 190, 116, 34, "#eef2ff", colors.line, 5) +
        text(350 + i * 130, 212, t, "label", "middle")
      ).join("")}
      ${text(858, 212, "2. Tracks (columns)", "label")}
      ${[0, 1, 2, 3].map((r) =>
        [0, 1, 2, 3].map((c) =>
          rect(292 + c * 130, 238 + r * 56, 116, 42, r === 0 && c < 3 ? "#dcfce7" : "#f6f6f4", colors.line, 5) +
          (r === 0 && c < 3 ? text(350 + c * 130, 264 + r * 56, "clip", "tiny", "middle") : "")
        ).join("")
      ).join("")}
      ${text(858, 262, "3. Clip slots: one loop", "small")}
      ${text(858, 282, "lives in one slot", "small")}
      ${[0, 1, 2, 3].map((r) => button(1006, 242 + r * 56, 64, 34, colors.dark, `Scene ${r + 1}`, "tiny")).join("")}
      ${text(858, 330, "4. Scenes (rows):", "small")}
      ${text(858, 350, "launch a whole row", "small")}
      ${rect(292, 474, 520, 34, "#ffe9d6", colors.amber, 5)}
      ${text(552, 496, "5. Master track: the final volume of everything", "small", "middle")}
      ${rect(292, 530, 786, 150, "#fff7de", "#e0b54b", 8)}
      ${text(316, 562, "Two keys to memorize before anything else", "label")}
      ${text(316, 592, "Tab switches Session View (grid) and Arrangement View (timeline). The APC drives the grid.", "small")}
      ${text(316, 616, "Spacebar starts and stops playback. When lost, press Spacebar, breathe, and look at the grid.", "small")}
      ${text(316, 640, "A DAW is just a program that plays loops and records what you do. Ableton is the DAW. The APC is the remote control.", "small")}
    `
  )}`
);

svg(
  "plate-13-browser-load-instrument.svg",
  1200,
  760,
  `${titleBlock("Loading sounds from the browser", "Every track in the Don't Cry Tonight set starts as a drag from the browser.")}
  ${liveWindow(
    "Browser",
    `
      ${rect(60, 150, 250, 530, "#f2f0eb", colors.line, 8)}
      ${text(76, 178, "Categories", "label")}
      ${["Sounds", "Drums", "Instruments", "Audio Effects", "Samples"].map((v, i) =>
        rect(76, 194 + i * 40, 218, 30, v === "Drums" ? "#d7e8ff" : "#fff", colors.line, 5) +
        text(90, 214 + i * 40, v, v === "Drums" ? "label" : "small")
      ).join("")}
      ${text(76, 420, "Search box: type what", "small")}
      ${text(76, 440, "you want, e.g. '909'", "small")}
      ${rect(76, 452, 218, 30, "#fff", colors.blue, 5)}
      ${text(90, 472, "909  x", "mono")}
      ${rect(340, 150, 360, 530, "#fff", colors.line, 8)}
      ${text(360, 178, "Results", "label")}
      ${[
        ["909 Core Kit.adg", true],
        ["Kit-Core 909.adg", false],
        ["909 Clap.aif", false],
        ["909 Hats Closed.aif", false],
        ["909 Hats Open.aif", false],
      ].map((row, i) =>
        rect(360, 194 + i * 40, 320, 30, row[1] ? "#dff7e4" : "#fff", colors.line, 5) +
        text(374, 214 + i * 40, row[0], row[1] ? "label" : "small")
      ).join("")}
      ${text(360, 420, "Preview: click once and Live", "small")}
      ${text(360, 440, "auditions the sound. Double-click", "small")}
      ${text(360, 460, "loads it onto the selected track.", "small")}
      ${line(700, 320, 790, 320, colors.teal, 3)}
      ${text(745, 306, "drag", "label", "middle")}
      ${["KICK", "CLAP", "HATS", "BASS", "CHORDS"].map((t, i) =>
        rect(800 + (i % 3) * 96, 190 + Math.floor(i / 3) * 120, 84, 30, i === 0 ? "#dff7e4" : "#eef2ff", i === 0 ? colors.green : colors.line, 5) +
        text(842 + (i % 3) * 96, 210 + Math.floor(i / 3) * 120, t, "tiny", "middle")
      ).join("")}
      ${rect(730, 380, 400, 120, "#fff", colors.line, 8)}
      ${text(750, 410, "Starter picks for this book", "label")}
      ${text(750, 436, "Drums: a 909-style kit on KICK, CLAP, HATS", "small")}
      ${text(750, 458, "Bass: Instruments > Drift > a 'Bass' preset", "small")}
      ${text(750, 480, "Chords/Pad: Drift or Analog 'Pad' preset", "small")}
      ${rect(730, 520, 400, 130, "#fff7de", "#e0b54b", 8)}
      ${text(750, 550, "One kit, three tracks", "label")}
      ${text(750, 576, "Load the same 909 kit on KICK, CLAP, and", "small")}
      ${text(750, 598, "HATS. Each track plays different notes of it,", "small")}
      ${text(750, 620, "so each APC column controls one drum job.", "small")}
    `
  )}`
);

svg(
  "plate-14-create-midi-clip.svg",
  1200,
  760,
  `${titleBlock("Creating and drawing a MIDI clip", "Double-click an empty slot, then draw notes in the piano roll below.")}
  ${liveWindow(
    "Clip View",
    `
      ${text(70, 158, "1. Double-click the empty KICK slot in Scene 2. A one-bar empty clip appears and starts looping silently.", "small")}
      ${rect(70, 174, 116, 42, "#dcfce7", colors.green, 5)}
      ${text(128, 200, "1 Bar", "tiny", "middle")}
      ${text(210, 200, "2. The bottom of the screen becomes Clip View: the piano roll.", "small")}
      ${rect(70, 240, 1020, 320, "#20242b", "#111", 10)}
      ${wtext(92, 268, "Piano roll: time runs left to right, pitch runs bottom to top", "label")}
      ${["C2", "A#1", "F#1", "D1", "C1"].map((n, i) =>
        rect(92, 292 + i * 46, 52, 38, "#303945", "#111", 4) +
        `<text x="118" y="${316 + i * 46}" style="font: 700 11px Arial; fill: #fff;" text-anchor="middle">${n}</text>`
      ).join("")}
      ${Array.from({ length: 16 }, (_, i) =>
        line(156 + i * 58, 292, 156 + i * 58, 512, i % 4 === 0 ? "#4a5462" : "#2c333d", i % 4 === 0 ? 2 : 1)
      ).join("")}
      ${[0, 4, 8, 12].map((s) => rect(158 + s * 58, 476, 54, 36, colors.green, "#0a0", 4)).join("")}
      ${wtext(92, 540, "3. Draw kick notes at C1 on steps 1, 5, 9, 13 (every quarter note). Enable Draw Mode with the B key, then click.", "small")}
      ${rect(70, 580, 1020, 100, "#fff7de", "#e0b54b", 8)}
      ${text(94, 612, "Checkpoint", "label")}
      ${text(94, 638, "Press the clip's play triangle (or the matching APC grid button). You should hear a steady four-on-the-floor kick.", "small")}
      ${text(94, 662, "If you hear nothing: is the track's little speaker (Track Activator) on? Is the fader up? Is an instrument loaded?", "small")}
    `
  )}`
);

function stepLane(x, y, label, note, active, color, cellW = 52) {
  const cells = Array.from({ length: 16 }, (_, i) =>
    rect(x + 150 + i * (cellW + 4), y, cellW, 34, active.includes(i + 1) ? color : "#141a22", i % 4 === 0 ? "#5a6572" : "#39434f", 4)
  ).join("");
  return `${rect(x, y, 92, 34, "#303945", "#111", 4)}
    <text x="${x + 46}" y="${y + 22}" style="font: 700 11px Arial; fill: #fff;" text-anchor="middle">${esc(label)}</text>
    <text x="${x + 118}" y="${y + 22}" style="font: 700 10px Menlo, monospace; fill: #9fb0c0;" text-anchor="middle">${esc(note)}</text>
    ${cells}`;
}

svg(
  "plate-15-drum-patterns.svg",
  1200,
  760,
  `${titleBlock("The three drum clips, step by step", "One bar = 16 steps. Numbers below show the 1/16 grid; bold columns are the beats.")}
  ${rect(42, 92, 1116, 380, "#20242b", "#111", 12)}
  ${wtext(64, 124, "GROOVE scene drum patterns (draw these exactly, then adjust by ear)", "label")}
  ${stepLane(64, 150, "KICK", "C1", [1, 5, 9, 13], colors.green)}
  ${stepLane(64, 200, "CLAP", "D1", [5, 13], colors.amber)}
  ${stepLane(64, 250, "CL HAT", "F#1", [1, 3, 5, 7, 9, 11, 13, 15], colors.blue)}
  ${stepLane(64, 300, "OP HAT", "A#1", [3, 7, 11, 15], colors.purple)}
  ${Array.from({ length: 16 }, (_, i) =>
    `<text x="${240 + i * 56}" y="${368}" style="font: ${i % 4 === 0 ? 700 : 400} 11px Arial; fill: #cad4de;" text-anchor="middle">${i + 1}</text>`
  ).join("")}
  ${wtext(64, 404, "KICK on every beat (1, 5, 9, 13) is the Italo-disco pulse. CLAP on beats 2 and 4 (steps 5, 13).", "small")}
  ${wtext(64, 428, "Closed hats on every eighth (odd steps). Open hats on the off-beats (3, 7, 11, 15) - the disco 'and'.", "small")}
  ${rect(42, 492, 1116, 200, "#fff", colors.line, 10)}
  ${text(64, 524, "Scene variations from the same three clips", "label")}
  ${[
    "INTRO: copy KICK clip, delete steps 5 and 13, lower velocity to ~70. Copy CL HAT only.",
    "LIFT: same as GROOVE plus OP HAT velocity up to ~110 for urgency.",
    "CHORUS: GROOVE patterns as-is; add a CLAP fill in the last bar (steps 13, 14, 15, 16).",
    "BREAK: delete KICK and CLAP clips entirely; keep only CL HAT at velocity ~50 (ghost hats).",
    "TAG/END: GROOVE patterns; you will fade and stop them from the APC, not edit them.",
  ].map((v, i) => text(64, 554 + i * 26, v, "small")).join("")}`
);

svg(
  "plate-16-bass-chords-piano-roll.svg",
  1200,
  760,
  `${titleBlock("Octave bass and chord pads in the piano roll", "The practice key is A minor. Draw these blocks, then trust your ears over the diagram.")}
  ${rect(42, 92, 1116, 240, "#20242b", "#111", 12)}
  ${wtext(64, 122, "BASS clip (1 bar, loops): the Italo octave bounce", "label")}
  ${["A2", "A1"].map((n, i) =>
    rect(64, 146 + i * 60, 52, 50, "#303945", "#111", 4) +
    `<text x="90" y="${176 + i * 60}" style="font: 700 11px Arial; fill: #fff;" text-anchor="middle">${n}</text>`
  ).join("")}
  ${Array.from({ length: 8 }, (_, i) =>
    rect(136 + i * 124, i % 2 === 0 ? 206 : 146, 112, 50, i % 2 === 0 ? colors.purple : "#8f7bff", "#111", 4) +
    `<text x="${192 + i * 124}" y="${(i % 2 === 0 ? 236 : 176)}" style="font: 700 10px Arial; fill: #fff;" text-anchor="middle">${i % 2 === 0 ? "A1" : "A2"}</text>`
  ).join("")}
  ${wtext(64, 290, "Eighth notes alternating low A (A1) and the A one octave up (A2). Every note the same length.", "small")}
  ${wtext(64, 314, "When the chords change in longer clips, move the whole pattern to the new root: F, C, G.", "small")}
  ${rect(42, 356, 1116, 250, "#20242b", "#111", 12)}
  ${wtext(64, 386, "CHORDS clip (4 bars, loops): one held chord per bar", "label")}
  ${["Am", "F", "C", "G"].map((c, i) =>
    rect(90 + i * 268, 410, 250, 120, ["#7a5cff", "#d95f9f", "#189a86", "#f4a62a"][i], "#111", 8) +
    `<text x="${215 + i * 268}" y="${462}" style="font: 700 22px Arial; fill: #fff;" text-anchor="middle">${c}</text>` +
    `<text x="${215 + i * 268}" y="${492}" style="font: 400 12px Arial; fill: #f2f2f2;" text-anchor="middle">${["A2 C3 E3", "F2 A2 C3", "C3 E3 G3", "G2 B2 D3"][i]}</text>`
  ).join("")}
  ${wtext(64, 560, "Bar 1: A minor. Bar 2: F major. Bar 3: C major. Bar 4: G major. Hold each chord for the whole bar.", "small")}
  ${wtext(64, 584, "This is a stand-in progression for practice. If you rebuild the song by ear, adjust chords to match what you hear.", "small")}
  ${rect(42, 630, 1116, 62, "#fff7de", "#e0b54b", 8)}
  ${text(66, 656, "LEAD starter: play or draw a short answer phrase (5 to 9 notes) from the A minor scale in bar 4 only.", "label")}
  ${text(66, 678, "Leaving bars 1-3 empty makes the lead feel like a hook, not wallpaper.", "small")}`
);

svg(
  "plate-17-tempo-warp.svg",
  1200,
  760,
  `${titleBlock("Tempo, metronome, count-in, quantization, warp", "Five small settings that make the practice set feel professional.")}
  ${liveWindow(
    "Control Bar and Clip Settings",
    `
      ${rect(70, 156, 110, 40, "#eef2ff", colors.blue, 6)}
      ${text(125, 182, "118.00", "title", "middle")}
      ${text(200, 170, "1. Tempo: click and type 118, press Enter.", "small")}
      ${text(200, 192, "Safe range for this study: 116-122 BPM.", "small")}
      ${button(70, 222, 56, 34, "#eee", "MET")}
      ${text(146, 244, "2. Metronome: on while drawing clips, off while performing.", "small")}
      ${rect(70, 282, 110, 34, "#eef2ff", colors.blue, 6)}
      ${text(125, 304, "1 Bar", "label", "middle")}
      ${text(200, 304, "3. Global Quantization: keep at 1 Bar. Every launch waits for the next bar line.", "small")}
      ${rect(70, 342, 480, 120, "#f2f0eb", colors.line, 8)}
      ${text(92, 372, "4. Count-In (Settings > Record Warp Launch)", "label")}
      ${text(92, 398, "Set Count-In to 1 Bar. When you record, Live", "small")}
      ${text(92, 420, "clicks one bar of 4 beats before capturing.", "small")}
      ${text(92, 442, "Your hands get ready instead of scrambling.", "small")}
      ${rect(580, 342, 510, 120, "#f2f0eb", colors.line, 8)}
      ${text(602, 372, "5. Warp (audio clips only)", "label")}
      ${text(602, 398, "If you drop in an audio loop (a riser, a noise", "small")}
      ${text(602, 420, "sweep), enable Warp in Clip View so it follows", "small")}
      ${text(602, 442, "your 118 BPM instead of its own speed.", "small")}
      ${rect(70, 494, 1020, 180, "#fff7de", "#e0b54b", 8)}
      ${text(94, 526, "Why 1 Bar quantization is a beginner superpower", "label")}
      ${text(94, 554, "You can press a scene button up to a bar early. Live holds the launch until the bar line, so nothing ever", "small")}
      ${text(94, 578, "starts off-beat. Press early, then move your hand calmly to the faders. The machine keeps the time;", "small")}
      ${text(94, 602, "you keep the intent. Later, try 1/4 quantization for fast clip juggling - but not in the first week.", "small")}
      ${text(94, 640, "If a launch ever feels 'late', you did not miss - you pressed after the bar line. Count '1-2-3-4' and press on '4'.", "small")}
    `
  )}`
);

svg(
  "plate-18-apc-scene-navigation.svg",
  1200,
  760,
  `${titleBlock("Reaching scenes 6-8: moving the APC window", "The APC sees five scenes at a time. The red ring in Live shows which five.")}
  ${[0, 1].map((panel) => {
    const x = 60 + panel * 420;
    const ringTop = panel === 0 ? 0 : 3;
    const rows = Array.from({ length: 8 }, (_, r) =>
      Array.from({ length: 8 }, (_, c) =>
        rect(x + 24 + c * 40, 170 + r * 44, 34, 34, r < 6 ? ["#dcfce7", "#fff0cf", "#dbeafe", "#ede9fe", "#ffe4e6", "#ccfbf1"][r] : "#f1f1ef", colors.line, 3)
      ).join("") +
      text(x + 352, 192 + r * 44, ["INTRO", "GROOVE", "VERSE", "LIFT", "CHOR A", "CHOR B", "BREAK", "TAG"][r], "tiny")
    ).join("");
    return `${rect(x, 130, 400, 440, "#fff", colors.line, 10)}
      ${text(x + 24, 158, panel === 0 ? "Before: ring covers scenes 1-5" : "After Down x3: ring covers scenes 4-8", "label")}
      ${rows}
      <rect x="${x + 18}" y="${164 + ringTop * 44}" width="330" height="${5 * 44 + 4}" fill="none" stroke="${colors.red}" stroke-width="4" rx="6"/>`;
  }).join("")}
  ${rect(920, 130, 240, 440, "#1d222a", "#090b0f", 12)}
  ${text(940, 162, "APC arrow cluster", "label")}
  ${button(1002, 200, 56, 36, "#eaeaea", "UP")}
  ${button(940, 250, 56, 36, "#eaeaea", "LEFT")}
  ${button(1002, 250, 56, 36, colors.amber, "DOWN")}
  ${button(1064, 250, 56, 36, "#eaeaea", "RIGHT")}
  ${button(940, 320, 76, 32, "#eaeaea", "BANK")}
  ${text(940, 380, "Down = move ring", "small")}
  ${text(940, 400, "one scene lower.", "small")}
  ${text(940, 424, "Press 3 times after", "small")}
  ${text(940, 444, "CHORUS A so rows", "small")}
  ${text(940, 464, "6-8 land on the grid.", "small")}
  ${text(940, 494, "Bank + Down jumps", "small")}
  ${text(940, 514, "5 scenes at once -", "small")}
  ${text(940, 534, "too far for this set.", "small")}
  ${rect(60, 600, 1100, 90, "#fff7de", "#e0b54b", 8)}
  ${text(84, 632, "Practice the move dry", "label")}
  ${text(84, 658, "Launch CHORUS A. While it plays 8 bars, press Down, Down, Down, and rest your finger on the CHORUS B scene", "small")}
  ${text(84, 680, "button. Launch it on the count of 4. The audience hears one seamless song; your hands did a quiet relocation.", "small")}`
);

svg(
  "plate-19-dct-performance-timeline.svg",
  1200,
  760,
  `${titleBlock("Don't Cry Tonight: the 64-bar performance score", "Read left to right. Each column is one 8-bar section. Do the moves in each row.")}
  ${(() => {
    const sections = ["INTRO", "GROOVE", "VERSE", "LIFT", "CHOR A", "CHOR B", "BREAK", "TAG/END"];
    const lanes = [
      ["Scene", ["Launch 1", "Launch 2", "Launch 3", "Launch 4", "Launch 5", "Down x3, launch 6", "Launch 7", "Launch 8"], "#dbeafe"],
      ["Faders", ["PAD+FX low", "raise KICK CLAP HATS BASS", "LEAD up, HATS -1", "PAD+FX up", "CHORDS LEAD PAD up", "FX down after throw", "KICK CLAP down", "fade KICK BASS"], "#dcfce7"],
      ["Mutes", ["-", "CLAP off 1 bar, on", "-", "KICK off last beat", "-", "BASS off 1 beat", "KICK CLAP HATS off", "LEAD off after hook"], "#fff0cf"],
      ["Sends/Macros", ["D1 closed, Rev on PAD", "returns dry", "small Delay B on LEAD", "open D1 slowly, FX up", "Rev A on CHORDS LEAD PAD", "D3/D4 throw, pull back", "D5 bloom up", "D5+D7 up, then still"], "#ede9fe"],
    ];
    const colW = 124;
    const x0 = 150;
    let out = "";
    sections.forEach((s, i) => {
      out += rect(x0 + i * colW, 110, colW - 8, 34, "#20242b", "#111", 5);
      out += `<text x="${x0 + i * colW + (colW - 8) / 2}" y="132" style="font: 700 11px Arial; fill: #fff;" text-anchor="middle">${s}</text>`;
      out += text(x0 + i * colW + (colW - 8) / 2, 160, `bars ${i * 8 + 1}-${i * 8 + 8}`, "tiny", "middle");
    });
    lanes.forEach((lane, li) => {
      const y = 180 + li * 118;
      out += rect(34, y, 104, 108, "#20242b", "#111", 6);
      out += `<text x="86" y="${y + 60}" style="font: 700 12px Arial; fill: #fff;" text-anchor="middle">${lane[0]}</text>`;
      lane[1].forEach((cell, i) => {
        out += rect(x0 + i * colW, y, colW - 8, 108, lane[2], colors.line, 5);
        const words = cell.split(" ");
        let lines = [""];
        words.forEach((w) => {
          if ((lines[lines.length - 1] + " " + w).trim().length > 13) lines.push(w);
          else lines[lines.length - 1] = (lines[lines.length - 1] + " " + w).trim();
        });
        lines.slice(0, 5).forEach((ln, li2) => {
          out += `<text x="${x0 + i * colW + (colW - 8) / 2}" y="${y + 28 + li2 * 18}" style="font: 400 10px Arial; fill: ${colors.ink};" text-anchor="middle">${esc(ln)}</text>`;
        });
      });
    });
    return out;
  })()}
  ${rect(34, 662, 1124, 62, "#fff7de", "#e0b54b", 8)}
  ${text(58, 688, "Print this page or keep it on a second screen. One column per 8 bars; when in doubt, do less.", "label")}
  ${text(58, 710, "The only mandatory moves: launch each scene in order, and press Down three times during CHORUS A.", "small")}`
);

svg(
  "plate-20-video-segment-map.svg",
  1200,
  760,
  `${titleBlock("Video segments mapped to book chapters", "Watch small chunks right before the chapter that uses them. Use each video's chapter list to jump.")}
  ${(() => {
    const rows = [
      ["Meet Ableton Live 12", "MusicRadar Tech, Live 12 Session View", "opening overview segment"],
      ["Cable, Power, Settings", "Akai official APC40 mkII video", "'Setup' portion at the start"],
      ["Clip Grid Basics", "Meta Mind Music walkthrough", "'Clip/Session controls' chapter"],
      ["Faders And Mutes", "Meta Mind Music walkthrough", "'Mixer controls' chapter"],
      ["Device Knobs, Sends", "Meta Mind Music walkthrough", "'Device controls' chapter"],
      ["Build The Practice Set", "Isotonik Studios set preparation", "whole video (9:40)"],
      ["Performance Passes", "Random Noise workflow video", "any performance demo segment"],
      ["Record To Arrangement", "Tony Tyson quick guide", "arrangement-on-the-fly segment"],
    ];
    return rows.map((row, i) => {
      const y = 112 + i * 70;
      return `${rect(50, y, 330, 56, "#eef2ff", colors.line, 8)}
        ${text(70, y + 34, row[0], "label")}
        ${line(380, y + 28, 440, y + 28, colors.teal, 3)}
        ${rect(440, y, 420, 56, "#fff", colors.line, 8)}
        ${text(460, y + 24, row[1], "label")}
        ${text(460, y + 44, row[2], "small")}`;
    }).join("");
  })()}
  ${rect(890, 112, 270, 546, "#fff7de", "#e0b54b", 10)}
  ${text(912, 144, "How to watch", "label")}
  ${[
    "Watch the chunk once",
    "without touching gear.",
    "",
    "Do the chapter with",
    "your own hands.",
    "",
    "Rewatch only the part",
    "that surprised you.",
    "",
    "Never binge all the",
    "videos in one sitting -",
    "fingers learn faster",
    "than eyes.",
  ].map((v, i) => text(912, 176 + i * 24, v, "small")).join("")}`
);

svg(
  "plate-21-export-audio.svg",
  1200,
  760,
  `${titleBlock("Exporting your recorded performance", "File > Export Audio/Video. These settings produce one clean WAV of your take.")}
  ${liveWindow(
    "Export Audio/Video",
    `
      ${rect(300, 150, 600, 470, "#f7f7f5", colors.line, 10)}
      ${text(330, 184, "Export Audio/Video", "title")}
      ${[
        ["Rendered Track", "Master"],
        ["Render Start", "1.1.1"],
        ["Render Length", "64 bars (to the end of your take)"],
        ["Sample Rate", "44100"],
        ["Encode PCM", "On - WAV, 16 bit"],
        ["Normalize", "Off"],
        ["Encode MP3", "On if you want a quick share file"],
      ].map((row, i) => {
        const y = 214 + i * 48;
        return `${text(330, y + 20, row[0], "label")}
          ${rect(540, y, 330, 32, "#fff", colors.blue, 5)}
          ${text(554, y + 21, row[1], "small")}`;
      }).join("")}
      ${button(700, 566, 170, 38, colors.green, "EXPORT")}
      ${rect(60, 190, 210, 300, "#fff", colors.line, 8)}
      ${text(80, 220, "Before export", "label")}
      ${["Select 1.1.1 to end", "of the recording in", "Arrangement View,", "or set the loop", "brace over the take.", "", "Listen once all the", "way through first."].map((v, i) => text(80, 250 + i * 26, v, "small")).join("")}
      ${rect(930, 190, 220, 300, "#fff7de", "#e0b54b", 8)}
      ${text(950, 220, "Name it like a", "label")}
      ${text(950, 240, "release", "label")}
      ${["", "dct-apc-practice-", "take01.wav", "", "Keep every take.", "Take 5 will embarrass", "take 1 - that is the", "whole point."].map((v, i) => text(950, 262 + i * 26, v, "small")).join("")}
    `
  )}`
);
