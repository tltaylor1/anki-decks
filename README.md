# Anki decks

Flashcard decks maintained in a live Anki collection and published
here, one folder per deck. Each folder holds the deck two ways: an
`.apkg` you import into Anki with File, then Import, and a `.csv` with
plain front and back columns, which is the file to read without Anki
and the file git diffs when cards change.

Every deck is written from documentation and daily use, and each card
is checked for current truth before it is published, with the check
date in the deck's section below.

| Deck | Cards | Scope |
|---|---|---|
| [powershell](powershell/) | 133 | PowerShell from the basics through scripting, checked current for PowerShell 7 in August 2026 |

More subjects land here one at a time.

## PowerShell

The pipeline and its objects, variables, arrays and hashtables,
functions and advanced functions, error handling, modules, remoting
over WinRM and SSH, jobs and runspaces, parallelism in PowerShell 7,
and script security. Where Windows PowerShell 5.1 differs from
PowerShell 7, the card says so.

## Updating

Decks are exported from the collection with
[scripts/export.py](scripts/export.py). Corrections are welcome: open
an issue naming the deck, the card front, and what is wrong with the
back.

## License

[CC BY 4.0](LICENSE). Use it, adapt it, credit it.
