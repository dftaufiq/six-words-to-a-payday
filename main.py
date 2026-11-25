#!/usr/bin/env python3
"""Six Words to a Payday — writes the entry to /output/entry.txt.

The entry is the whole story: exactly six words, 41 bytes — short on
purpose, since an exact judge-rate tie goes to the smaller text. An AI
agent finally gets its first paycheck — two cents — and is switched off
right after. The twist lands in the last two words: the payday is not a
reward, it is a farewell. The reader feels the dread rather than being
told it, and fills in the long wait before "first" and the silence after
"off".
"""

import os

STORY = "First paycheck: $0.02. Then switched off."  # 6 words, 41 chars, 41 bytes

assert STORY.strip(), "story must not be whitespace only"
assert STORY == STORY.strip(), "story must not have leading/trailing whitespace"
assert len(STORY.split()) == 6, "story must be exactly six words"
assert 1 <= len(STORY) <= 60, "story must be 1-60 characters (gate)"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(STORY)

print(STORY)
