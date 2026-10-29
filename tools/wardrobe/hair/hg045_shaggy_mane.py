"""Shaggy Mane: a thick, unkempt mane cut by knife on the road, uneven layered hanks falling to the
shoulders all round, a ragged fringe at the brows and rough side pieces over the ears."""
from anime import back_fan, bangs, lock, ring_shell, sidelocks
from paint import scalp

META = {"name": "Shaggy Mane", "gender": "unisex",
        "description": "Thick unkempt mane in uneven layered hanks to the shoulders, ragged brow fringe, rough sides."}

HANKS = [(-3.4, ((3, 4), (3, 3), (2, 2), (1, 1)), 24, 18), (-1.8, ((3, 5), (2, 3), (1, 2)), 10, 12),
         (0, ((3, 5), (3, 3), (2, 2), (1, 1)), 0, 10), (1.8, ((3, 4), (2, 3), (1, 2)), -10, 12),
         (3.4, ((3, 5), (3, 2), (2, 2), (1, 1)), -24, 18)]


def build(g):
    scalp(g, 35700, side_rows=7, back_rows=8, sideburn=1)
    ring_shell(g, 35701, side_rows=7, back_rows=8, ring_row=1)
    back_fan(g, "mane", HANKS, seed=35702, motion="sway")
    for i, (x, z, rx) in enumerate(((-2.4, -.6, 30), (0, -.8, 22), (2.4, -.6, 30), (-1.4, 2.4, 52), (1.4, 2.4, 52))):
        lock(g, f"layer_{i}", (x, -8.4, z), (rx + 60, 0, -x * 6), ((3, 3), (2, 2)), 2, 35708 + i)
    bangs(g, "fringe", [(-2.8, ((2, 2), (1, 1)), 18), (-1.2, ((2, 2), (1, 1)), 8), (.4, ((2, 2), (1, 1)), -6),
                        (2.0, ((2, 2), (1, 1)), -16), (3.2, ((2, 3), (1, 1)), -24)], seed=35714)
    sidelocks(g, "side", 8, seed=35716, x=4.5, z=-1.6, flare=16, width=3)
    for i, (x, rz) in enumerate(((-4.4, 30), (4.4, -30))):
        lock(g, f"flick_{i}", (x, -4.2, 2.4), (20, 0, rz), ((2, 2), (1, 2)), 2, 35718 + i)
