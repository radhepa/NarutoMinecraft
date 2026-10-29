"""Crescent Tail: a high ponytail that sweeps back and curls up at the tip like the moon's horn,
with a short side fringe and a clean, high-tied nape: the sword dancer's tail."""
from anime import bangs, lock, ring_shell, tie
from paint import scalp

META = {"name": "Crescent Tail", "gender": "unisex",
        "description": "High ponytail sweeping back and curling up at the tip, short side fringe."}


def build(g):
    scalp(g, 15130, side_rows=5, back_rows=8, sideburn=3)
    ring_shell(g, 15131, side_rows=5, back_rows=8, ring_row=1)
    tie(g, "tie", (0, -6.8, 4.6), (20, 0, 0), size=(3, 1, 2), y=-.5)
    lock(g, "tail", (0, -6.6, 4.8), (16, 0, 0), ((3, 4), (3, 4), (3, 3)), 2, 15135, ring=1, motion="sway")
    # The tail's lower end bends back and the tip curls upward like the moon's horn.
    lock(g, "tail_curve", (0, 4.6, 7.8), (58, 0, 0), ((2, 3), (2, 2)), 2, 15138, ring=None, motion="sway")
    lock(g, "tail_tip", (0, 7.1, 11.8), (130, 0, 0), ((1, 2), (1, 1)), 1, 15141, ring=None, motion="sway")
    bangs(g, "fringe", [(-2.8, ((2, 2), (1, 1)), 20), (-1.0, ((2, 1), (1, 1)), 34), (1.6, ((2, 1),), -30),
                        (3.0, ((2, 2), (1, 1)), -16)], seed=15145)
