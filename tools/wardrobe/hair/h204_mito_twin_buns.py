"""Mito Twin Buns: hair parted down the middle and wound into two round buns high on either side of
the crown, each pierced by a pair of beaded hairpins and hung with a kanji tag, three clips over the brow, with the rest falling long and straight down
the back and two long locks framing the face."""
from anime import curtain, lock, ring_shell, sidelocks
from kit_uzumaki import bun, clip, hairpin
from paint import scalp, solid

META = {"name": "Mito Twin Buns", "gender": "female",
        "description": "Middle part, twin buns with beaded hairpins and kanji tags, three front clips, long straight hair down the back."}


def build(g):
    scalp(g, 2060, side_rows=6, back_rows=8, sideburn=4, part=3)
    ring_shell(g, 2061, side_rows=6, back_rows=8, ring_row=1)
    curtain(g, "curtain", (0, -5.6, 4.6), (-6, 0, 0), 9, 13, [(0, 3, 3), (3, 3, 2), (6, 3, 3)], seed=2062)
    for side, sign in (("right", -1), ("left", 1)):
        bun(g, f"bun_{side}", (3.0 * sign, -7.6, .8), (0, 0, 34 * -sign), (5, 4, 5), seed=2063 + (sign > 0))
        for i, (ry, rx) in enumerate(((30, 0), (-30, 14))):
            hairpin(g, f"pin_{side}_{i}", (6.8 * sign, -10.0, .8 + (i - .5) * 1.6), (rx, ry, 64 * sign), length=12)
    # The middle-parted fringe: two locks curving away from the part, the outer ones to the brow.
    for i, (x, segs, rz) in enumerate(((-.9, ((2, 1), (1, 1)), 38), (.9, ((2, 1), (1, 1)), -38),
                                      (-2.6, ((2, 2), (1, 1)), 18), (2.6, ((2, 2), (1, 1)), -18))):
        lock(g, f"fringe_{i}", (x, -8.55, -4.35), (-10, 0, rz), segs, 1, 2066 + i * 7, ring=0)
    sidelocks(g, "frame", 13, seed=2068, x=4.3, z=-3.4, flare=3, width=2)
    for i, x in enumerate((-1.6, 0, 1.6)):
        clip(g, f"clip_{i}", (x, -8.75, -3.4), (-80, 0, 90), length=2, key="M")
    for side, sign in (("right", -1), ("left", 1)):
        tag = g.piece(f"tag_{side}", "HEAD", (-.5, 0, -.5), (1, 3, 1), pivot=(4.9 * sign, -7.6, 1.6),
                      rotation=(0, 0, -10 * sign), motion="sway")
        solid(tag, "S", "plain", 2069, 3, edge=False)
        for f in tag.sides:
            f.set(0, 1, "K1"), f.set(0, 2, "A2")
