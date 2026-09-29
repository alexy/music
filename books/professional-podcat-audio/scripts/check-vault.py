#!/usr/bin/env python3
"""Read-only, title-specific validation before FirstPair seals the vault."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import re
import csv
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, str(Path.home() / "src/firstpair/publishing/vault"))
from firstpair_vault.inventory import inventory


def main() -> None:
    root = Path(sys.argv[1]).resolve(strict=True)
    scanned = inventory(root)
    failures = list(scanned.broken_links) + list(scanned.unsafe_paths)
    for name in ("Home.md", "Contents.md", "Guide.md", "README.md", "Session log.md", "Recall template.md", "Test script.md", "Worksheets.md", "Worksheets/comparison-log.csv", "Worksheets/control-sweeps.csv", "Sources.md", "Visuals.md", "SOURCE-MANIFEST.json", "Assets/cover.png"):
        if not (root / name).is_file():
            failures.append(f"missing {name}")
    pages = json.loads((root / "_data/reader.json").read_text())
    manifest = json.loads((root / "SOURCE-MANIFEST.json").read_text())
    units = [json.loads(line) for line in (root / "professional-podcat-audio/_data/units.jsonl").read_text().splitlines()]
    if not pages or len(pages) != manifest["readerPages"] or len(pages) != len(units):
        failures.append("Reader page count differs from chapter provenance")
    if [page["id"] for page in pages] != [unit["id"] for unit in units]:
        failures.append("Reader order differs from provenance ledger")
    for page in pages:
        text = (root / page["path"]).read_text()
        if "[[Home|Home]]" not in text or "[[Contents|Contents]]" not in text:
            failures.append(f"missing static navigation: {page['path']}")
        if re.search(r"!\[[^\]]*\]\([^\n)]+\)\{[^}\n]*\b(?:width|height)\s*=", text):
            failures.append(f"unconverted Pandoc image dimensions: {page['path']}")
    if "../Assets/cover.png" not in (root / pages[0]["path"]).read_text():
        failures.append("first Reader page has no canonical cover")
    for asset in manifest["assets"]:
        path = root / asset["path"]
        if not path.is_file() or hashlib.sha256(path.read_bytes()).hexdigest() != asset["sha256"]:
            failures.append(f"image hash mismatch: {asset['path']}")
    for worksheet in manifest["worksheets"]:
        path = root / worksheet["path"]
        if not path.is_file() or hashlib.sha256(path.read_bytes()).hexdigest() != worksheet["sha256"]:
            failures.append(f"worksheet hash mismatch: {worksheet['path']}")
    with (root / "Worksheets/comparison-log.csv").open(newline="") as handle:
        fields = next(csv.reader(handle))
    if fields != manifest["recallFields"]:
        failures.append("comparison CSV header differs from recall manifest")
    for name in ("Session log.md", "Recall template.md"):
        text = (root / name).read_text()
        for field in fields:
            if f"| `{field}` |" not in text:
                failures.append(f"{name} omits CSV field: {field}")
        for detail in ("S1 / S2 / S3 / S4 / S5", "internal output termination", "RF switch group"):
            if detail not in text:
                failures.append(f"{name} omits internal-state recall: {detail}")
    spoken = re.search(r"(?:^|\n)((?:>[^\n]*(?:\n|$))+)", (root / "Test script.md").read_text())
    if not spoken or hashlib.sha256(spoken.group(1).strip().encode()).hexdigest() != manifest["testScriptSha256"]:
        failures.append("dedicated test script differs from the canonical passage")
    if not (root / manifest["testScriptSource"]).is_file():
        failures.append("test script has no source chapter")
    source_link = f"[[{manifest['sourceRegister'][:-3]}|"
    for name in ("Home.md", "Sources.md"):
        if source_link not in (root / name).read_text():
            failures.append(f"{name} has no direct source-register route")
    if (root / "README.md").read_bytes() != (root / "Guide.md").read_bytes():
        failures.append("README and Guide differ")
    if json.loads((root / ".obsidian/community-plugins.json").read_text()) != []:
        failures.append("community plugins must be disabled by default")
    canonical = Path.home() / "src/firstpair/publishing/vault/plugin/firstpair-reader"
    for name in ("main.js", "manifest.json", "styles.css"):
        if (root / ".obsidian/plugins/firstpair-reader" / name).read_bytes() != (canonical / name).read_bytes():
            failures.append(f"shared plugin differs: {name}")
    print(json.dumps({"passed": not failures, "readerPages": len(pages), "images": len(manifest["assets"]), "failures": failures}, indent=2))
    raise SystemExit(1 if failures else 0)


if __name__ == "__main__":
    main()
