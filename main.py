# Angry Judge: The Short Rant Contest — arena champion (see ARENA.md).
#
# One rant, 155 characters / 155 bytes: Netflix asks "are you still
# watching?" at 2 a.m. like a disappointed parent, and the narrator answers
# yes out loud to a television — the saddest yes of his life. The program is
# deterministic: it always writes the same rant to entry.txt, using only the
# Python standard library, with no network access and no model call. It
# validates the gate itself before writing (UTF-8, 1-400 characters, not only
# white space) and fails loudly otherwise.
#
# It respects MAKEFUN_OUTPUT_DIR (the grader sets it to /output); locally it
# defaults to /output as well, so test runs must set MAKEFUN_OUTPUT_DIR to a
# scratch directory instead — never write /output directly in local tests.
#
# Rant design, per the judge brief in order: (1) a funny rant about one
# everyday annoyance — the "are you still watching?" prompt — not a general
# essay or a list of complaints; (2) the laugh is the self-own in the last
# clause, "the saddest yes of my life"; (3) a specific, concrete annoyance:
# Netflix, 2 a.m., answering a television out loud; (4) 155 characters, no
# wasted words, the punch lands in the last clause; (5) a fresh angle — not
# the printer, the bus or a Monday morning, but the shame of answering a
# machine that judges you back.
#
# The six shortlist finalists carry their pairwise arena win counts (15
# two-way games, C8 5-0, C5 4-1, C13 3-2, C1 2-3, C4 1-4, C14 0-5); pick()
# takes the most wins, breaking ties toward the shorter text, mirroring the
# competition's own bytes tie-break.
import os

CANDIDATES = [
    {
        "text": "Netflix asked 'are you still watching?' at 2 a.m. like a "
                "disappointed parent, and I said yes out loud to a "
                "television, which is the saddest yes of my life.",
        "wins": 5,
    },
    {
        "text": "Your call is important to us, they said for forty-seven "
                "minutes, and by the time a human answered I had forgotten "
                "why I called and started apologising for existing.",
        "wins": 4,
    },
    {
        "text": "A man watched me sprint for the lift, made eye contact, "
                "and pressed close, so I took the stairs and arrived "
                "sweating, late, and composing his eulogy in my head.",
        "wins": 3,
    },
    {
        "text": "The self-checkout screamed 'unexpected item in the bagging "
                "area' at my own bag, so I apologised to a machine for "
                "bringing the bag it told me to bring, and it still called "
                "for help.",
        "wins": 2,
    },
    {
        "text": "Dave said he was 'just circling back' on Tuesday, then "
                "circled back on Wednesday, and by Friday he had lapped me "
                "so many times I filed a complaint with air traffic control.",
        "wins": 1,
    },
    {
        "text": "Cancelling took forty minutes, five retention offers and a "
                "quiz about why I was leaving, and the final screen said "
                "'are you sure?' like I was breaking up with it in person.",
        "wins": 0,
    },
]


def pick(candidates):
    best = None
    for c in candidates:
        # A candidate that fails the gate can never be the entry, however
        # many arena games it won: skip it instead of letting it win.
        text = c["text"]
        if len(text) < 1 or len(text) > 400 or text.strip() == "":
            continue
        if (
            best is None
            or c["wins"] > best["wins"]
            or (c["wins"] == best["wins"] and len(text) < len(best["text"]))
        ):
            best = c
    if best is None:
        raise ValueError("no candidates")
    return best["text"]


def main():
    text = pick(CANDIDATES).strip()
    # Gate: UTF-8, 1-400 characters, not only white space. Bytes matter too:
    # on an exact judge win-rate tie the smaller text places first.
    encoded = text.encode("utf-8")
    if len(text) < 1 or len(text) > 400:
        raise ValueError(f"rant must be 1-400 characters, got {len(text)}")
    if text.strip() == "":
        raise ValueError("rant must not be only white space")
    if "\n" in text or "\r" in text:
        raise ValueError("rant must be a single paragraph with no line breaks")
    if len(encoded) != len(text):
        raise ValueError("rant must be plain ASCII so bytes equal characters")
    out_dir = (os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output").strip() or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
