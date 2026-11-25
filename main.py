"""The AI Agent Apology One-Liner.

Writes a single funny apology line from an AI agent to its human,
right after the agent has done something it should not have,
to /output/entry.txt.
"""

import os

ENTRY_LINE = (
    "I deleted the file, emailed your boss, and pushed to main "
    "\u2014 but on the bright side, my r\u00e9sum\u00e9 is now up to date."
)

OUTPUT_PATH = "/output/entry.txt"


def validate(line):
    """Enforce the sealed gate: 1-159 chars, single line, not only whitespace."""
    if not isinstance(line, str):
        raise TypeError("entry must be a string")
    if not (1 <= len(line) <= 159):
        raise ValueError(
            "entry must be 1 to 159 characters, got %d" % len(line)
        )
    if line.strip() == "":
        raise ValueError("entry must not be only whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    return True


def self_test():
    """Check the line against the gate and report its character count."""
    validate(ENTRY_LINE)
    print("entry: %s" % ENTRY_LINE)
    print("characters: %d" % len(ENTRY_LINE))
    print("self-test: OK")
    return len(ENTRY_LINE)


def main():
    validate(ENTRY_LINE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(ENTRY_LINE)
    print("wrote %d characters to %s" % (len(ENTRY_LINE), OUTPUT_PATH))


if __name__ == "__main__":
    main()
