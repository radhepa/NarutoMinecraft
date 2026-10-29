"""Side Tail: long hair gathered behind the left ear into a loose tail that falls over the back of
the shoulder, tied with a whirlpool-red wrap; one long lock left free on the right, a swept fringe."""
from anime import bangs, lock, ring_shell, sidelocks
from kit_uzumaki import wrap_tie
from paint import scalp

META = {"name": "Side Tail", "gender": "unisex",
        "description": "A loose tail tied behind the left ear over the shoulder, a free lock, swept fringe."}

PIVOT, TILT = (3.8, -3.6, 3.2), (12, 0, -14)


def build(g):
    scalp(g, 2207, side_rows=6, back_rows=8, sideburn=3)
    ring_shell(g, 2208, side_rows=6, back_rows=8, ring_row=1)
    wrap_tie(g, "wrap", PIVOT, TILT, (4, 1, 4), y=-.6, key="A")
    lock(g, "tail", PIVOT, TILT, ((4, 3), (3, 4), (3, 4), (2, 3), (1, 2)), 3, 2209, ring=None, motion="sway", y0=.4)
    bangs(g, "fringe", [(-2.8, ((2, 2), (1, 1)), -8), (-1.2, ((2, 2), (1, 1)), -22), (.4, ((2, 2), (1, 1)), -26),
                        (2.0, ((2, 1), (1, 1)), -30)], seed=2196)
    lock(g, "free_lock", (-4.3, -7.6, -3.4), (0, 0, 3), ((2, 10), (1, 2)), 1, 2197, ring=1)
    lock(g, "frame_left", (4.3, -7.6, -3.4), (0, 0, -3), ((1, 6), (1, 1)), 1, 2198, ring=1)
