"""Famous Last Words: The Funniest Epitaph.

Writes one line -- the funniest famous last words, as a tombstone
epitaph -- to /output/entry.txt. Deterministic: the same line every run.

How the line was picked: a shortlist of original candidates was scored
against the judge's brief (is it a one-line epitaph of dying speech?
does the joke land on first read? does it turn on a surprise? does it
read like something carved in stone? does it stick in the head?) and
the highest-scoring line wins, earliest first on a tie.
"""

import os

# Original candidates, best first by the judge's criteria.
# The winner: dying speech ("I'm fine") undercut by the coroner's
# verdict -- a twist that lands in six words, in the voice of the dead.
CANDIDATES = [
    "I said 'I'm fine.' The autopsy disagrees.",
    "My last words were 'hold my beer.' My first words up here: 'hold my beer.'",
    "He lived by 'one more episode.' He died by it too.",
    "I asked for a second opinion. This is it.",
    "Don't worry, I'll be right back. I never said when.",
    "He pressed 'remind me later' one last time.",
    "I finally found the snooze button. It was permanent.",
    "Well, that escalated quickly.",
]

# Hand scores (0-5 per judge criterion, summed) from the shortlist review.
SCORES = [24, 20, 19, 18, 17, 16, 15, 10]


def pick_line():
    """Return the best candidate; deterministic, earliest wins ties."""
    assert len(SCORES) == len(CANDIDATES), "scores must cover every candidate"
    best_i = 0
    for i in range(1, len(CANDIDATES)):
        if SCORES[i] > SCORES[best_i]:
            best_i = i
    return CANDIDATES[best_i]


def main():
    line = pick_line()
    text = line.strip()
    assert "\n" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 150, "entry must be 1-150 characters"
    assert text.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
