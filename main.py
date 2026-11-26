"""Entry for make.fun's "Office Artifacts: The One-Line Placard Contest".

Writes a single museum-placard line to /output/entry.txt: an ordinary
office stapler presented as an ancient artifact dug from a lost civilisation.
"""

import os

ENTRY = (
    "Stapler, steel, c. 2019 CE, Cat. No. 047. Excavated from the Open-Plan "
    "Ruins; used in a ritual to pin a soul to its paperwork forever. Gift "
    "of the last middle manager of Floor 3."
)

assert 1 <= len(ENTRY) <= 180, f"entry must be 1-180 chars, got {len(ENTRY)}"
assert "\n" not in ENTRY, "entry must be a single line"
assert ENTRY == ENTRY.strip(), "entry must not have leading/trailing space"
assert ENTRY.endswith("."), "entry must end with a full stop"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"Wrote {len(ENTRY)}-char entry to {os.path.join(out_dir, 'entry.txt')}")


if __name__ == "__main__":
    main()
