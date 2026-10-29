"""Hive Bun: everything pulled up and wound into a round bun high on the crown, ringed like a
hive and held by a dark tie, with short wisps at the temples."""
from anime import cel_box, ring_shell, sidelocks, tie
from paint import k, scalp

META = {"name": "Hive Bun", "gender": "unisex",
        "description": "Hair pulled up into a ringed bun high on the crown, short wisps at the temples."}


def build(g):
    scalp(g, 10221, side_rows=5, back_rows=8, sideburn=2)
    hat = ring_shell(g, 10222, side_rows=4, back_rows=8, ring_row=1)
    for x in range(0, 8, 2):
        hat.back.vline(x, 1, 6, "H1")
    tie(g, "bun_tie", (0, -8.2, 1.4), (-20, 0, 0), size=(3, 1, 3))
    bun = g.piece("bun", "HEAD", (-2.5, -5, -2.5), (5, 4, 5), pivot=(0, -8.0, 1.6), rotation=(-20, 0, 0))
    cel_box(bun, 10230, ring=1)
    for f in bun.sides:   # the hive rings
        f.hline(0, f.w - 1, 2, k("H", 1))
    cap = g.piece("bun_top", "HEAD", (-1.5, -6, -1.5), (3, 1, 3), pivot=(0, -8.0, 1.6), rotation=(-20, 0, 0))
    cel_box(cap, 10232, top_delta=2)
    sidelocks(g, "wisp", 5, seed=10240, x=4.3, z=-3.4, flare=4, width=1)
