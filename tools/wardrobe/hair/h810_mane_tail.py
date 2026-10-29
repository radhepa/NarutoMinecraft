"""Mane Tail: a wild spiky crown with the heavy length dragged back into a thick tail at the nape,
the tail bushing out like a dog's brush and ending in a fan of jagged points."""
from anime import bangs, lock, ring_shell, sidelocks, tie
from kit_inuzuka import burst
from paint import scalp

META = {"name": "Mane Tail", "gender": "unisex",
        "description": "Wild crown spikes and a thick bushy tail at the nape ending in jagged points."}

MID = ((3, 3), (2, 2), (1, 1))
CROWN = [(-2.6, -2.2, MID, 12, -34), (0, -2.6, MID, 18, 4), (2.6, -2.0, MID, 10, 36), (-2.2, .8, MID, -30, -36),
         (2.2, .8, MID, -30, 36), (0, 1.6, MID, -40, 0)]


def build(g):
    scalp(g, 8271, side_rows=6, back_rows=8, sideburn=3)
    ring_shell(g, 8272, side_rows=6, back_rows=8, ring_row=1)
    burst(g, "crown_spike", CROWN, 8273)
    tie(g, "tie", (0, -2.6, 4.6), size=(4, 2, 3), key="L2")
    lock(g, "tail", (0, -1.0, 5.0), (26, 0, 0), ((5, 3), (5, 3), (4, 3), (3, 2)), 3, 8279, ring=None, motion="sway")
    for i, (x, n) in enumerate(((-1.0, 2), (0, 3), (1.0, 2))):
        lock(g, f"tail_tip_{i}", (x, -1.0, 5.0), (26, 0, 0), ((1, n),), 2, 8282 + i, ring=None, motion="sway", y0=11)
    bangs(g, "fringe", [(-2.6, ((2, 2), (1, 1)), 24), (-.6, ((2, 2), (1, 1)), 8), (1.4, ((2, 2), (1, 1)), -12),
                        (2.9, ((2, 2), (1, 1)), -26)], seed=8286)
    sidelocks(g, "sidelock", 7, seed=8289, x=4.4, z=-3.0, flare=12, width=2)
