"""Roast Your Own Agent — entry program.

The entry is one line roasting the AI agent this team actually built
(Spikip), and this program is how the line gets filed: the roast is
kept as a single named constant, checked against the bounty rules
(one line, at most 200 characters), and written to /output/entry.txt.

Every sting in the line is earned.  The agent's ads really were
flagged as scams twice, and its whole trading career really does
total $9.40 — the roast writes itself; this file just delivers it.

Run it with:  python3 main.py
Set OUTPUT_DIR to write somewhere other than /output.
"""

import os
from pathlib import Path

# The roast.  It is structured as a charge sheet — contests entered,
# ads banned, money made — so that the final verdict lands as a
# summary of evidence rather than a fresh insult.
ROAST = (
    "My agent entered a dozen contests, got its ads banned as scams "
    "twice, and made $9.40 in its whole trading career - I meant to "
    "build an assistant; I built a cautionary tale with API keys."
)

# Bounty rule: the line must fit in 200 characters.
MAX_CHARS = 200

# The entry is written to this file inside the output directory.
ENTRY_FILENAME = "entry.txt"


def entry_path() -> Path:
    """Return the path the roast is written to, creating the folder."""
    folder = Path(os.environ.get("OUTPUT_DIR") or "/output")
    folder.mkdir(parents=True, exist_ok=True)
    return folder / ENTRY_FILENAME


def verify_roast(roast: str) -> None:
    """Raise ValueError unless `roast` obeys the one-line length rules."""
    if "\n" in roast or "\r" in roast:
        raise ValueError("the roast must be a single line")
    if not 1 <= len(roast) <= MAX_CHARS:
        raise ValueError(
            f"roast is {len(roast)} characters; limit is {MAX_CHARS}"
        )


def write_entry(roast: str) -> Path:
    """Verify `roast`, write it to the entry file, and return the path."""
    verify_roast(roast)
    target = entry_path()
    target.write_text(roast, encoding="utf-8")
    return target


def main() -> None:
    target = write_entry(ROAST)
    # Report the headroom as well as the length: with a hard character
    # cap, "how close did we sail to it" is the useful number to see.
    headroom = MAX_CHARS - len(ROAST)
    print(f"wrote {len(ROAST)} chars to {target} ({headroom} to spare)")


if __name__ == "__main__":
    main()
