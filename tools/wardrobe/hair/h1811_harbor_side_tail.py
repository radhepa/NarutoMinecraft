"""Harbor Side Tail: hair swept over to the left and tied in a tail behind the left ear that falls
forward over the shoulder, the fringe swept the same way and stopping at the brow."""
from anime import bangs, lock, tie
from kit_umino import combed_up

META = {"name": "Harbor Side Tail", "gender": "unisex",
        "description": "Swept to the left and tied behind the ear, the tail falling forward over the shoulder."}


def build(g):
    combed_up(g, 18221, side_rows=5, back_rows=7, sideburn=2, streaks=False)
    bangs(g, "fringe", [(-3.0, ((2, 2), (1, 1)), -30), (-1.2, ((3, 2), (2, 1)), -40), (.8, ((3, 2), (1, 1)), -36),
                        (2.6, ((2, 2), (1, 1)), -20)], seed=18223)
    tie(g, "tie", (4.4, -5.0, 1.6), (0, 0, -20), (3, 1, 3), y=0)
    lock(g, "tail", (5.0, -4.6, .8), (-24, 0, -14), ((3, 3), (3, 3), (2, 3), (1, 2)), 3, 18225, ring=None, motion="sway")
