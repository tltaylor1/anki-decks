# Contributing

The decks are maintained in a live Anki collection and exported here, so
a change to a card is made in the collection and re-exported, never by
editing the published files directly: an edited CSV would drift from the
package file it is meant to mirror.

To correct a card, open an issue naming the deck, the card's front, and
what is wrong with the back, with a source where one helps. The correction
is applied in the collection, both files are regenerated with
`scripts/export.py`, and the CSV diff in the resulting commit shows exactly
what changed.

By contributing a correction you agree it is licensed under CC BY 4.0.
