"""Regenerate a deck's .apkg and .csv from the live Anki collection.

    .venv/bin/python scripts/export.py powershell

The collection is the source of truth; this repository holds snapshots,
one folder per deck. Run with Anki closed after editing cards, then
review the CSV diff in git before committing: the CSV exists so every
card change is visible line by line, while the .apkg is the one-click
import.

Needs the anki library matching the installed app:
    python3 -m venv .venv && .venv/bin/pip install anki
"""

import csv
import html
import re
import sys
from pathlib import Path

from anki.collection import Collection, DeckIdLimit, ExportAnkiPackageOptions

# Folder name -> deck name in the collection. Add a line per published
# deck; only decks named here can be exported.
DECKS = {
    "powershell": "PowerShell",
    "python": "Python",
    "kql": "KQL",
    "bicep": "Bicep",
    "cybersecurity": "Cybersecurity",
}

COLLECTION = Path.home() / ".local/share/Anki2/User 1/collection.anki2"
ROOT = Path(__file__).resolve().parent.parent


def clean(value: str) -> str:
    value = re.sub(r"<[^>]+>", " ", value)
    return " ".join(html.unescape(value).split())


def export(folder: str) -> None:
    deck_name = DECKS[folder]
    out_dir = ROOT / folder
    out_dir.mkdir(exist_ok=True)
    col = Collection(str(COLLECTION))
    try:
        deck_id = col.decks.id_for_name(deck_name)
        exported = col.export_anki_package(
            out_path=str(out_dir / f"{folder}.apkg"),
            options=ExportAnkiPackageOptions(
                with_scheduling=False,
                with_media=True,
                with_deck_configs=False,
                legacy=True,
            ),
            limit=DeckIdLimit(deck_id),
        )
        note_ids = sorted(
            {col.get_card(cid).nid for cid in col.decks.cids(deck_id)}
        )
        rows = []
        for nid in note_ids:
            note = col.get_note(nid)
            rows.append([clean(note.fields[0]), clean(note.fields[1])])
        rows.sort(key=lambda row: row[0].lower())
        with (out_dir / f"{folder}.csv").open("w", newline="") as handle:
            writer = csv.writer(handle)
            writer.writerow(["front", "back"])
            writer.writerows(rows)
        print(f"{folder}: {exported} notes exported")
    finally:
        col.close()


def main() -> int:
    targets = sys.argv[1:]
    if not targets or any(t not in DECKS for t in targets):
        names = ", ".join(sorted(DECKS))
        print(f"usage: export.py <deck...>  where deck is one of: {names}",
              file=sys.stderr)
        return 1
    for target in targets:
        export(target)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
