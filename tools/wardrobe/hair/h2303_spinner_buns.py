"""Spinner Buns: two small round buns low behind the ears like a spider's spinnerets, each wound
with thread, and a light fringe parted off the brow."""
from anime import bangs, cel_box, ring_shell, tie
from paint import k, scalp

META = {"name": "Spinner Buns", "gender": "unisex",
        "description": "Two small thread-wound buns low behind the ears, a light parted fringe."}


def build(g):
    scalp(g, 23061, side_rows=5, back_rows=8, sideburn=2, part=3)
    ring_shell(g, 23062, side_rows=4, back_rows=8, ring_row=1)
    bangs(g, "fringe", [(-2.8, ((2, 2), (1, 1)), 14), (2.8, ((2, 2), (1, 1)), -14)], seed=23065)
    for side, sign in (("right", -1), ("left", 1)):
        pivot = (3.0 * sign, -3.4, 4.2)
        bun = g.piece(f"bun_{side}", "HEAD", (-1.5, -1.5, 0), (3, 3, 3), pivot=pivot, rotation=(20, 0, -8 * sign))
        cel_box(bun, 23070 + (sign > 0), ring=0)
        for f in bun.sides:
            f.hline(0, f.w - 1, 1, k("H", 1))
        tie(g, f"bun_wrap_{side}", pivot, (20, 0, -8 * sign), size=(4, 1, 1), y=-.2, key="A2")
