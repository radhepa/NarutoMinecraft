"""Wrapped Locks: straight collar-length hair with two long locks in front of the ears bound in
a cloth wrap at the jaw, the way a guard keeps them out of a needle's line."""
from anime import bangs, curtain, ring_shell, sidelocks, tie
from paint import scalp

META = {"name": "Wrapped Locks", "gender": "unisex",
        "description": "Collar-length hair, two long front locks bound in a cloth wrap at the jaw."}


def build(g):
    scalp(g, 16560, side_rows=6, back_rows=8, sideburn=1, part=3)
    ring_shell(g, 16561, side_rows=6, back_rows=8, ring_row=1)
    bangs(g, "fringe", [(-2.8, ((2, 2), (1, 1)), 18), (-1.2, ((2, 2),), 26), (1.2, ((2, 2),), -26),
                        (2.8, ((2, 2), (1, 1)), -18)], seed=16562)
    sidelocks(g, "frame", 10, seed=16570, x=4.5, z=-3.1, flare=2, width=2)
    for side, sign in (("right", -1), ("left", 1)):
        tie(g, f"frame_wrap_{side}", (4.5 * sign, -7.6, -3.1), (0, 0, 2 * -sign), size=(3, 3, 2), y=5.0, key="D1")
    curtain(g, "fall", (0, -6.6, 4.6), (-4, 0, 0), 9, 5, hem=[(0, 4, 1), (5, 4, 1)], seed=16580)
