"""Regenerate powershell.apkg and powershell.csv from the live Anki
collection.

The collection is the source of truth; this repository holds snapshots.
Run this after editing cards in Anki, with Anki closed, then review the
CSV diff in git before committing: the CSV exists so every card change
is visible line by line, while the .apkg is the one-click import.

Needs the anki library matching the installed app:
    python3 -m venv .venv && .venv/bin/pip install anki
    .venv/bin/python scripts/export.py
"""

import csv
import html
import re
from pathlib import Path

from anki.collection import Collection, DeckIdLimit, ExportAnkiPackageOptions

DECK = "PowerShell"
COLLECTION = Path.home() / ".local/share/Anki2/User 1/collection.anki2"
ROOT = Path(__file__).resolve().parent.parent
STEM = "powershell"


def clean(value: str) -> str:
    value = re.sub(r"<[^>]+>", " ", value)
    return " ".join(html.unescape(value).split())


def main() -> None:
    col = Collection(str(COLLECTION))
    try:
        deck_id = col.decks.id_for_name(DECK)
        exported = col.export_anki_package(
            out_path=str(ROOT / f"{STEM}.apkg"),
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
        with (ROOT / f"{STEM}.csv").open("w", newline="") as handle:
            writer = csv.writer(handle)
            writer.writerow(["front", "back"])
            writer.writerows(rows)
        print(f"{exported} notes exported to {STEM}.apkg and {STEM}.csv")
    finally:
        col.close()


if __name__ == "__main__":
    main()
