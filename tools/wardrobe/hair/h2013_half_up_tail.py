"""Half-up Tail: the top half of the hair drawn back into a short tail at the crown, the rest left
loose to the shoulders, a soft side fringe."""
from anime import bangs, curtain, ring_shell, sidelocks, tie
from kit_namiashi import wave_lock
from paint import scalp

META = {"name": "Half-up Tail", "gender": "unisex",
        "description": "Top half drawn back into a short crown tail, the rest loose to the shoulders."}


def build(g):
    scalp(g, 20361, side_rows=8, back_rows=8, sideburn=0)
    ring_shell(g, 20362, side_rows=8, back_rows=8, ring_row=1)
    curtain(g, "loose", (0, -6.4, 4.7), (6, 0, 0), 8, 9, hem=[(0, 2, 2), (3, 2, 2), (6, 2, 2)], seed=20363)
    tie(g, "tie", (0, -7.8, 4.4), (-20, 0, 0), size=(2, 1, 2), y=-.5, key="K2")
    wave_lock(g, "crown_tail", (0, -7.6, 4.9), (50, 0, 0), [(((2, 3),), 0, 0), (((1, 2),), -40, 0)], depth=2, seed=20370,
              motion="sway")
    sidelocks(g, "side", 8, seed=20380, x=4.4, z=-1.8, flare=3, width=2)
    bangs(g, "fringe", [(-2.8, ((2, 3), (1, 1)), 24), (-1.0, ((2, 2), (1, 1)), 28), (1.4, ((2, 2), (1, 1)), 30)],
          seed=20385)
