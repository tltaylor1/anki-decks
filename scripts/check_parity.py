#!/usr/bin/env python3
"""The parity gate: each deck's .apkg and .csv describe the same cards.

Both files come out of one export, so they agree the day they are
written. Nothing held them together afterward: a CSV edited by hand,
or a package replaced alone, would drift silently. This opens each
package (a zip holding an SQLite collection), cleans every note the
way export.py cleans it, and compares the set of cards with the CSV.
It also checks the README's deck and card counts against the files.
Standard library only.
"""
import csv
import html
import re
import sqlite3
import sys
import tempfile
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SEPARATOR = "\x1f"


def clean(value: str) -> str:
    value = re.sub(r"<[^>]+>", " ", value)
    return " ".join(html.unescape(value).split())


def package_cards(apkg: Path) -> set[tuple[str, str]]:
    with zipfile.ZipFile(apkg) as archive, tempfile.TemporaryDirectory() as tmp:
        member = "collection.anki21" if "collection.anki21" in archive.namelist() else "collection.anki2"
        path = archive.extract(member, tmp)
        conn = sqlite3.connect(path)
        try:
            rows = conn.execute("select flds from notes").fetchall()
        finally:
            conn.close()
    cards = set()
    for (fields,) in rows:
        parts = fields.split(SEPARATOR)
        cards.add((clean(parts[0]), clean(parts[1]) if len(parts) > 1 else ""))
    return cards


def csv_cards(path: Path) -> set[tuple[str, str]]:
    with path.open(newline="") as handle:
        reader = csv.DictReader(handle)
        return {(row["front"], row["back"]) for row in reader}


def main() -> int:
    failures = []
    decks = sorted(p.parent for p in ROOT.glob("*/*.apkg"))
    total = 0
    for folder in decks:
        apkg = folder / f"{folder.name}.apkg"
        table = folder / f"{folder.name}.csv"
        if not table.exists():
            failures.append(f"{folder.name}: package without a CSV twin")
            continue
        packaged, listed = package_cards(apkg), csv_cards(table)
        total += len(listed)
        if packaged != listed:
            only_pkg = len(packaged - listed)
            only_csv = len(listed - packaged)
            failures.append(
                f"{folder.name}: {only_pkg} card(s) only in the package, {only_csv} only in the CSV"
            )
    readme = (ROOT / "README.md").read_text()
    stated_cards = re.search(r"([\d,]+) cards", readme)
    if stated_cards and int(stated_cards.group(1).replace(",", "")) != total:
        failures.append(f"README states {stated_cards.group(1)} cards; the CSVs hold {total}")
    words = {"seven": 7, "six": 6, "eight": 8, "five": 5, "nine": 9, "ten": 10}
    stated_decks = re.search(r"\b(\w+) (?:Anki )?decks\b", readme, re.I)
    if stated_decks:
        word = stated_decks.group(1).lower()
        if word in words and words[word] != len(decks):
            failures.append(f"README states {word} decks; there are {len(decks)}")
    for line in failures:
        print(line)
    if failures:
        return 1
    print(f"parity holds: {len(decks)} decks, {total} cards, package and CSV agree in each")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
