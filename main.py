"""Write the tired dark lord's monologue to the output directory.

Pure standard library only. The text is fixed: exactly 100 words,
500 characters, so it passes the 1-600 character gate every run.
"""

import os
from pathlib import Path

MONOLOGUE = (
    "The little knight stands before me, sword up, all fire. "
    "I like fire. It saves me the candles. "
    "The rite is set, the moon is right, my ravens did their part, "
    "and by dawn my flags will fly from here to the Grey Sea. "
    "Kneel. Kneel, and I shall be kind \u2014 once the books are done. "
    "The books! Nine towns owe me grain, four owe me gold, "
    "and the quill weighs more than my sword. "
    "Sit. Drink. The dark can wait one night. "
    "It has waited a thousand years. "
    "Tomorrow, hero. Tomorrow I end your world. "
    "Tonight\u2026 I sit."
)


def main() -> None:
    # The gate accepts 1-600 characters; fail loudly instead of
    # writing an invalid entry if the text ever drifts out of range.
    assert 1 <= len(MONOLOGUE) <= 600, len(MONOLOGUE)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(MONOLOGUE, encoding="utf-8")


if __name__ == "__main__":
    main()
