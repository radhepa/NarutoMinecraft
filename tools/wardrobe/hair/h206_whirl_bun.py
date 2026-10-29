"""Whirl Bun: everything gathered up into one bun on the crown, wound in three tiers that turn
like a whirlpool, held by a beaded hairpin; short pointed bangs and two thin face strands."""
from anime import bangs, cel_box, ring_shell, sidelocks
from kit_uzumaki import hairpin, wrap_tie
from paint import k, scalp

META = {"name": "Whirl Bun", "gender": "unisex",
        "description": "A crown bun wound in turning tiers like a whirlpool, a beaded pin, short bangs."}

TIERS = [((5, 2, 5), 0), ((4, 1, 4), 30), ((3, 1, 3), 60)]


def build(g):
    scalp(g, 2100, side_rows=5, back_rows=7, sideburn=3)
    ring_shell(g, 2101, side_rows=4, back_rows=6, ring_row=1)
    wrap_tie(g, "base", (0, -8.4, 1.2), (0, 0, 0), (5, 1, 5), key="A")
    y = -8.4
    for i, ((w, h, d), ry) in enumerate(TIERS):
        y -= h
        tier = g.piece(f"tier_{i}", "HEAD", (-w / 2, 0, -d / 2), (w, h, d), pivot=(0, y, 1.2), rotation=(0, ry, 0))
        cel_box(tier, 2102 + i, 2 + (i == len(TIERS) - 1), ring=None, top_delta=1)
        for f in tier.sides:
            f.set(0, 0, k("H", 1))
            f.set(f.w - 1, f.h - 1, k("H", 3))
    hairpin(g, "pin", (3.6, -10.4, 1.6), (0, 20, 60), length=14)
    bangs(g, "fringe", [(-2.6, ((2, 2), (1, 1)), 20), (-.9, ((2, 1), (1, 1)), 10), (.9, ((2, 1), (1, 1)), -10),
                        (2.6, ((2, 2), (1, 1)), -20)], seed=2107)
    sidelocks(g, "frame", 8, seed=2108, x=4.3, z=-3.6, flare=2, width=1)
