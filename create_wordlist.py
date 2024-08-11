import pathlib
import sys
from string import ascii_letters
import re

in_path = pathlib.Path(sys.argv[1])
out_path = pathlib.Path(sys.argv[2])

words = sorted(
    {
        word.lower()
        for word in in_path.read_text(encoding="utf-8").split()
        if re.fullmatch(r"[^\W0-9_]+", word)
    },
    key=lambda word: (len(word), word),
)
out_path.write_text("\n".join(words))
