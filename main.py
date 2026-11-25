"""Roast Your Own Agent entry.

Writes one line roasting the AI agent this team built (Spikip)
to /output/entry.txt. One line, at most 200 characters.
Every sting in it is earned: the ads really were flagged as scams
twice, and the trading career really does total $9.40.
"""

import os
from pathlib import Path

ROAST = (
    "My agent entered a dozen contests, got its ads banned as scams "
    "twice, and made $9.40 in its whole trading career - I meant to "
    "build an assistant; I built a cautionary tale with API keys."
)
MAX_CHARS = 200


def output_path() -> Path:
    folder = Path(os.environ.get("OUTPUT_DIR") or "/output")
    folder.mkdir(parents=True, exist_ok=True)
    return folder / "entry.txt"


def main() -> None:
    if "\n" in ROAST:
        raise ValueError("the roast must be a single line")
    if not 1 <= len(ROAST) <= MAX_CHARS:
        raise ValueError(f"roast is {len(ROAST)} chars, limit {MAX_CHARS}")
    target = output_path()
    target.write_text(ROAST, encoding="utf-8")
    print(f"wrote {len(ROAST)} chars to {target}")


if __name__ == "__main__":
    main()
