#!/usr/bin/env python3
"""Native projection adapter; invoked only through firstpair-vault's gates."""
from __future__ import annotations

import argparse
import csv
import hashlib
import importlib.util
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys
from urllib.parse import unquote

sys.dont_write_bytecode = True
BOOK_ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("prepare", Path(__file__).with_name("prepare-vault-source.py"))
prepare = importlib.util.module_from_spec(spec)
spec.loader.exec_module(prepare)


def write_json(path: Path, value) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")


def process_gate() -> None:
    if sys.platform == "darwin":
        result = subprocess.run(["pgrep", "-x", "Obsidian"], capture_output=True)
        if result.returncode != 1:
            raise RuntimeError("Obsidian must be fully closed, and its process state must be readable")


def strip_image_attributes(text: str) -> str:
    """Obsidian does not interpret Pandoc's trailing image-size attributes."""
    return re.sub(r"(!\[[^\]]*\]\([^\n)]+\))\{[^}\n]*\b(?:width|height)\s*=[^}\n]*\}", r"\1", text)


def test_script(rows: list[dict]) -> tuple[dict, str]:
    for row in rows:
        match = re.search(r"Record this original test script at a natural pace:\s*\n((?:>[^\n]*(?:\n|$))+)", row["content"])
        if match:
            return row, match.group(1).strip()
    raise RuntimeError("The canonical manuscript has no original comparison test script")


def session_form(fields: list[str], title: str = "Session log") -> str:
    labels = {
        "date": "Date", "take_id": "Take / blind code", "audio_file": "Saved audio filename", "mic": "Microphone",
        "mode": "BeesNeez profile (67/269 and Vintage/New) or Twin87 Vintage/Modern", "pattern": "Polar pattern / PSU detent",
        "mic_pad": "Mic pad (-10 dB or off)", "mic_hpf": "Mic high-pass state", "bees_s2": "BeesNeez S2 bass-cut state",
        "rf_state": "Twin87 internal RF group (all switch positions, or as found)", "distance_cm": "Mouth-to-capsule distance (cm)",
        "angle_deg": "Off-axis angle (degrees)", "pre_gain_db": "PRE-73 input gain (dB)", "pre_output_mark": "PRE-73 output mark",
        "pre_48v": "PRE-73 48 V", "pre_line": "PRE-73 LINE mode", "pre_di": "PRE-73 DI mode", "pre_low_z": "PRE-73 LOW-Z / input impedance",
        "pre_hpf": "PRE-73 high-pass (OFF / 80 / 200 Hz)", "pre_air": "PRE-73 Air (OFF / +3 / +6 dB)",
        "pre_output_pad": "PRE-73 output pad (0 / 14 dB)", "pre_polarity": "PRE-73 polarity (normal / inverted)",
        "comp_bypass": "COMP-54 hard bypass", "comp_in_out": "COMP-54 compression IN/OUT", "comp_threshold_mark": "COMP-54 threshold mark",
        "comp_ratio": "COMP-54 ratio", "comp_attack_ms": "COMP-54 attack (ms)", "comp_recovery": "COMP-54 recovery (ms / s / Auto)",
        "comp_sc_hp": "COMP-54 sidechain HP (OFF / 50 Hz / 100 Hz / 7 kHz)", "comp_makeup_mark": "COMP-54 makeup mark",
        "comp_term": "COMP-54 rear termination", "comp_link": "COMP-54 LINK", "comp_meter": "COMP-54 meter selector (COMP / OUTPUT)",
        "gr_normal_db": "Normal gain reduction (dB)", "gr_max_db": "Maximum gain reduction (dB)", "m4_input": "M4 input socket and channel",
        "m4_gain_if_front": "M4 front gain mark (N/A for rear 3)", "m4_phantom": "M4 48 V", "monitor_path": "Only active monitoring route",
        "monitor_mix": "M4 MON / 3-4 / input-playback mix / headphone level", "daw_version": "DAW and exact version",
        "sample_rate_hz": "Session sample rate (Hz)", "bit_depth": "Recording / export bit depth", "buffer_samples": "Buffer (samples)",
        "plugins_and_values": "Every plug-in, bypass state and parameter value", "record_peak_dbfs": "Recorded peak (dBFS)",
        "matched_gain_db": "Gain applied to listening copy (dB)", "integrated_lufs": "Measured integrated loudness (LUFS)",
        "true_peak_dbtp": "Measured true peak (dBTP)", "channel_layout": "Mono / stereo layout", "intelligibility_1_5": "Intelligibility (1–5)",
        "body_1_5": "Body (1–5)", "sibilance_1_5": "Sibilance comfort (1–5)", "plosive_control_1_5": "Plosive control (1–5)",
        "room_control_1_5": "Room control (1–5)", "low_fatigue_1_5": "Low fatigue (1–5)", "decision": "Keep / reject / repeat",
        "notes": "Listening notes and uncertainties",
    }
    text = f"# {title}\n\nCopy this form to your personal notes for **each take**. Keep measured readings separate from suggested recipes. Use `unknown` or `as found` for unverified internal states; do not infer them from the profile name.\n\n[[Test script|Read the same test script]] · [[Worksheets|CSV worksheets]] · [[Home|Home]]\n\n"
    text += "| CSV field | Control or measurement | Your reading |\n| --- | --- | --- |\n"
    text += "".join(f"| `{field}` | {labels.get(field, field.replace('_', ' '))} | |\n" for field in fields)
    text += "\n## Setup details beyond the CSV columns\n\n| Detail | Your reading |\n| --- | --- |\n| Mac model / macOS version | |\n| Room / noise sources / chair and capsule position marks | |\n| Pop-filter position / mouth height | |\n| BeesNeez matched PSU / cable / power / warm-up state | |\n| BeesNeez S1 / S2 / S3 / S4 / S5 exact as-found states | |\n| Twin87 RF switch group exact as-found states | |\n| Manufacturer-approved handling procedure verified before internal changes | |\n| PRE-73 power / insert state / internal output termination as found | |\n| COMP-54 exact revision / rear switch legend / power | |\n| M4 USB / driver / loopback selection | |\n| DAW input/output pair / mono channel / track pan / track level / effects on capture | |\n| Room-tone duration / recorded noise notes | |\n| Export format / normalization / dither / loudness-meter tool | |\n| Photograph or drawing of your control positions | |\n\nInternal controls are not routine live adjustments. Keep the BeesNeez as found until its manufacturer confirms a safe unpowered procedure for your unit. Follow the Twin87 manual's unpowered procedure for its RF group.\n"
    return text


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--guide", type=Path, required=True)
    args = parser.parse_args()
    process_gate()
    status = subprocess.run(["git", "status", "--porcelain"], cwd=BOOK_ROOT, capture_output=True, text=True, check=True)
    if status.stdout.strip():
        raise RuntimeError("Commit the completed source and keep the music worktree clean before vault generation")
    revision = subprocess.run(["git", "rev-parse", "HEAD"], cwd=BOOK_ROOT, capture_output=True, text=True, check=True).stdout.strip()
    config = json.loads((BOOK_ROOT / "vault.build.json").read_text())
    rows = prepare.chapters()
    expected = [{key: row[key] for key in ("id", "title", "source")} for row in rows]
    if config["reader"] != expected:
        raise RuntimeError("Reader configuration is stale: run ./build.sh prepare-vault, then commit the source")
    for row in rows:
        if (BOOK_ROOT / row["source"]).read_text() != row["content"]:
            raise RuntimeError("Prepared chapter inputs are stale: run ./build.sh prepare-vault")
    source_row = next((row for row in rows if row["title"].startswith("Source register")), None)
    if not source_row:
        raise RuntimeError("The manuscript is missing its source register chapter")
    comparison_row, spoken_script = test_script(rows)
    worksheet_names = ("comparison-log.csv", "control-sweeps.csv")
    for name in worksheet_names:
        if not (BOOK_ROOT / name).is_file() or (BOOK_ROOT / name).is_symlink():
            raise RuntimeError(f"Missing regular source worksheet: {name}")
    with (BOOK_ROOT / "comparison-log.csv").open(newline="") as handle:
        recall_fields = next(csv.reader(handle))
    output = args.output.resolve()
    if output.exists():
        raise RuntimeError(f"Refusing to replace an existing output: {output}")
    output.mkdir(parents=True)
    (output / "Reader").mkdir()
    (output / "Assets").mkdir()
    (output / "_data").mkdir()
    asset_rows = {}

    def copy_asset(relative: str) -> str:
        candidate = (BOOK_ROOT / relative).resolve()
        if not candidate.is_relative_to(BOOK_ROOT / "assets") or not candidate.is_file() or candidate.is_symlink():
            raise RuntimeError(f"Illustration must be a regular source file under assets/: {relative}")
        name = candidate.relative_to(BOOK_ROOT / "assets").as_posix()
        if name in asset_rows:
            return f"../Assets/{name}"
        destination = output / "Assets" / name
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(candidate, destination)
        sha = hashlib.sha256(destination.read_bytes()).hexdigest()
        asset_rows[name] = {"id": f"visual-{prepare.slug(name)}", "kind": "visual", "label": name,
                            "path": f"Assets/{name}", "rights": "redistributable", "sha256": sha,
                            "source": str(candidate.relative_to(BOOK_ROOT)), "referencedBy": []}
        return f"../Assets/{name}"

    copy_asset("assets/cover.png")
    for index, row in enumerate(rows):
        def rewrite(match):
            raw = match.group(2).strip().removeprefix("<").removesuffix(">")
            if not raw.startswith("assets/"):
                return match.group(0)
            path = unquote(raw)
            rewritten = copy_asset(path)
            key = path.removeprefix("assets/")
            asset_rows[key]["referencedBy"].append(row["id"])
            return f"{match.group(1)}({rewritten})"

        content = strip_image_attributes(re.sub(r"(!?\[[^\]]*\])\(([^)]+)\)", rewrite, row["content"]))
        content = re.sub(r"^(#{1,6} .+?)\s*\{#[^}]+\}\s*$", r"\1", content, flags=re.MULTILINE)
        rail = ["[[Home|Home]]", "[[Contents|Contents]]", f"[[{source_row['path'][:-3]}|Sources]]"]
        if index:
            rail.insert(0, f"[[{rows[index - 1]['path'][:-3]}|Previous]]")
        if index + 1 < len(rows):
            rail.append(f"[[{rows[index + 1]['path'][:-3]}|Next]]")
        nav = " · ".join(rail)
        if index == 0:
            content = "![Professional Podcat Audio cover](../Assets/cover.png)\n\n" + content
        (output / row["path"]).write_text(nav + "\n\n" + content + "\n---\n\n" + nav + "\n", encoding="utf-8")
    reader_index = [{key: row[key] for key in ("id", "title", "path")} for row in rows]
    write_json(output / "_data/reader.json", reader_index)
    write_json(output / "_data/targets.json", list(asset_rows.values()))
    contents = "# Contents\n\n" + "\n".join(f"- [[{row['path'][:-3]}|{row['title']}]]" for row in rows) + "\n"
    (output / "Contents.md").write_text(contents)
    home = f"# Professional Podcat Audio\n\n[[{rows[0]['path'][:-3]}|Open the Reader]]\n\n[[Contents|Contents]] · [[Guide|First-use guide]]\n\n[[Recall template|Recall template]] · [[Session log|Session log]] · [[Test script|Test script]] · [[Worksheets|CSV worksheets]]\n\n[[{source_row['path'][:-3]}|Official source register]] · [[Sources|Provenance]] · [[Visuals|Illustrations]]\n"
    tutorial = BOOK_ROOT / "tutorial.html"
    if tutorial.is_file():
        (output / "Companion").mkdir()
        shutil.copyfile(tutorial, output / "Companion/tutorial.html")
        home += "\n[Open the interactive tutorial in a web browser](Companion/tutorial.html).\n"
    (output / "Home.md").write_text(home)
    guide = args.guide.read_text()
    (output / "Guide.md").write_text(guide)
    (output / "README.md").write_text(guide)
    (output / "Session log.md").write_text(session_form(recall_fields))
    (output / "Recall template.md").write_text(session_form(recall_fields, "Recall template"))
    (output / "Test script.md").write_text(f"# Test script\n\nThis is the book's original comparison passage, extracted verbatim from [[{comparison_row['path'][:-3]}|{comparison_row['title']}]]. Record at a natural pace and fixed mouth-to-capsule position.\n\n{spoken_script}\n\nMake three takes per condition. Allow each microphone its proper power and warm-up procedure. Capture the final ten seconds of room tone without changing gain. Repeated live speech measures normal performance variation too; identify a loudspeaker replay as a separate technical test.\n\n[[Recall template|Record every setting]] · [[Worksheets|Control sweeps]] · [[Home|Home]]\n")
    (output / "Worksheets").mkdir()
    worksheet_rows = []
    for name in worksheet_names:
        destination = output / "Worksheets" / name
        shutil.copyfile(BOOK_ROOT / name, destination)
        worksheet_rows.append({"source": name, "path": f"Worksheets/{name}", "sha256": hashlib.sha256(destination.read_bytes()).hexdigest()})
    (output / "Worksheets.md").write_text("# CSV worksheets\n\n- [Comparison log](Worksheets/comparison-log.csv): one blank row per take; save your personal results in a separate copy.\n- [Control sweeps](Worksheets/control-sweeps.csv): one-variable experiments, prerequisites and listening questions.\n\nOpen CSV files in Numbers, a spreadsheet application or a text editor. The control-sweep menu does not authorize powered internal adjustments. Retain the manufacturer prerequisites recorded in each row.\n\n[[Recall template|Markdown recall form]] · [[Test script|Original test script]] · [[Home|Home]]\n")
    (output / "Sources.md").write_text(f"# Sources and provenance\n\n[[{source_row['path'][:-3]}|Open the official source register and illustration credits]]\n\nThis vault projects the complete manuscript from music source revision `{revision}`. Manufacturer documentation is linked in the source register; full manufacturer PDFs are not bundled. Original explanatory prose and diagrams and the user's equipment photographs form the reader edition.\n\nThe chapter ledger records original manuscript line ranges and SHA-256 hashes. Visual and worksheet records identify each derivative's source path and byte hash. The Test script note reproduces the manuscript's original comparison passage exactly.\n\n[[Contents|Return to the chapter list]]\n")
    (output / "Visuals.md").write_text("# Illustrations\n\n" + "\n".join(f"- [{row['label']}]({row['path']})" for row in asset_rows.values()) + "\n")
    units_dir = output / "professional-podcat-audio/_data"
    units_dir.mkdir(parents=True)
    units = [{"id": row["id"], "kind": "chapter", "title": row["title"], "readerPath": row["path"],
              "source": "manuscript.md", "firstLine": row["firstLine"], "lastLine": row["lastLine"],
              "sourceSha256": row["sha256"], "sourceCommit": revision} for row in rows]
    (units_dir / "units.jsonl").write_text("".join(json.dumps(row) + "\n" for row in units))
    write_json(output / "SOURCE-MANIFEST.json", {"schema": "podcat-source-v1", "sourceCommit": revision,
               "manuscriptSha256": hashlib.sha256((BOOK_ROOT / "manuscript.md").read_bytes()).hexdigest(),
               "readerPages": len(rows), "assets": list(asset_rows.values()), "worksheets": worksheet_rows,
               "recallFields": recall_fields, "testScriptSource": comparison_row["path"],
               "testScriptSha256": hashlib.sha256(spoken_script.encode()).hexdigest(), "sourceRegister": source_row["path"]})
    obsidian = output / ".obsidian"
    obsidian.mkdir()
    write_json(obsidian / "community-plugins.json", [])
    write_json(obsidian / "core-plugins.json", ["file-explorer", "search", "bookmarks", "outline"])
    firstpair_root = Path.home() / "src/firstpair"
    plugin = firstpair_root / "publishing/vault/plugin/firstpair-reader"
    shutil.copytree(plugin, obsidian / "plugins/firstpair-reader")
    print(json.dumps({"vault": str(output), "readerPages": len(rows), "images": len(asset_rows)}, indent=2))


if __name__ == "__main__":
    main()
