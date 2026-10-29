"""Stem Ponytail: a long, smooth ponytail tied low at the nape with a green cord, hanging straight
down the back like a flower stem with a sprig of bells tied in at the knot, a centre part and two
face-framing locks."""
from anime import lock, ring_shell, sidelocks, tie
from kit_suzuran import bell_charm
from paint import scalp

META = {"name": "Stem Ponytail", "gender": "unisex",
        "description": "Long low ponytail tied with a green cord and a bell sprig, centre part, face-framing locks."}

TAIL = ((3, 3), (3, 3), (2, 3), (2, 3), (1, 2))


def build(g):
    scalp(g, 24031, side_rows=6, back_rows=8, sideburn=2, part=3)
    ring_shell(g, 24032, side_rows=5, back_rows=8, ring_row=1)
    lock(g, "part_right", (-1.6, -8.55, -4.35), (-10, 0, 34), ((3, 2), (2, 1)), 1, 24035, ring=0)
    lock(g, "part_left", (1.6, -8.55, -4.35), (-10, 0, -34), ((3, 2), (2, 1)), 1, 24036, ring=0)
    sidelocks(g, "frame", 6, seed=24037, flare=3)
    tie(g, "cord", (0, -2.2, 4.4), (0, 0, 0), (3, 1, 2), key="D2")
    lock(g, "tail", (0, -2.0, 4.6), (6, 0, 0), TAIL, 2, 24040, ring=None, motion="sway")
    bell_charm(g, "sprig", (1.0, -2.4, 5.6), rotation=(0, 180, 0))
