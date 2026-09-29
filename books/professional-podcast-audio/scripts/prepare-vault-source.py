#!/usr/bin/env python3
"""Project chapter records into build inputs, without touching a vault."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import re
import unicodedata

BOOK_ROOT = Path(__file__).resolve().parents[1]


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def slug(text: str) -> str:
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+", "-", text).strip("-") or "chapter"


def chapters() -> list[dict]:
    lines = (BOOK_ROOT / "manuscript.md").read_text(encoding="utf-8").splitlines(keepends=True)
    start = 0
    if lines and lines[0].strip() == "---":
        for index in range(1, len(lines)):
            if lines[index].strip() in {"---", "..."}:
                start = index + 1
                break
    boundaries = []
    fence = None
    for index in range(start, len(lines)):
        match = re.match(r"\s*(`{3,}|~{3,})", lines[index])
        if match:
            marker = match.group(1)[0]
            fence = marker if fence is None else (None if fence == marker else fence)
        if fence is None and re.match(r"^#\s+", lines[index]):
            title = re.sub(r"\s*\{#[^}]+\}\s*$", "", lines[index][2:].strip())
            boundaries.append((index, title))
    if not boundaries:
        boundaries = [(start, "Professional Podcast Audio")]
    elif "".join(lines[start:boundaries[0][0]]).strip():
        boundaries.insert(0, (start, "Start here"))
    result = []
    for number, (first, title) in enumerate(boundaries, 1):
        last = boundaries[number][0] if number < len(boundaries) else len(lines)
        content = "".join(lines[first:last]).strip() + "\n"
        if not content.startswith("# "):
            content = f"# {title}\n\n{content}"
        chapter_id = f"{number:02d}-{slug(title)}"
        result.append({
            "id": chapter_id,
            "title": title,
            "source": f"build/reader-source/{chapter_id}.md",
            "path": f"Reader/{chapter_id}.md",
            "firstLine": first + 1,
            "lastLine": last,
            "sha256": digest(content.encode()),
            "content": content,
        })
    return result


def main() -> None:
    rows = chapters()
    destination = BOOK_ROOT / "build" / "reader-source"
    destination.mkdir(parents=True, exist_ok=True)
    for row in rows:
        (BOOK_ROOT / row["source"]).write_text(row["content"], encoding="utf-8")
    config_path = BOOK_ROOT / "vault.build.json"
    config = json.loads(config_path.read_text(encoding="utf-8"))
    config["reader"] = [{key: row[key] for key in ("id", "title", "source")} for row in rows]
    config_path.write_text(json.dumps(config, indent=2) + "\n", encoding="utf-8")
    book_config_path = BOOK_ROOT / "book.build.json"
    book_config = json.loads(book_config_path.read_text(encoding="utf-8"))
    excluded = {"build", "dist", "dist-obsidian", "__pycache__", ".git"}
    book_config["sourceFiles"] = sorted(
        path.relative_to(BOOK_ROOT).as_posix()
        for path in BOOK_ROOT.rglob("*")
        if path.is_file() and not any(part in excluded for part in path.relative_to(BOOK_ROOT).parts)
        and path.name != ".DS_Store"
    )
    book_config_path.write_text(json.dumps(book_config, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"readerPages": len(rows), "preparedInputs": str(destination), "config": str(config_path)}, indent=2))


if __name__ == "__main__":
    main()
