"""Tide Tail: hair combed back and tied high on the crown, the tail falling down the back and
curling up and over at its end like a rolling wave, two short locks at the temples."""
from anime import bangs, ring_shell, sidelocks, tie
from kit_namiashi import wave_lock
from paint import scalp

META = {"name": "Tide Tail", "gender": "unisex",
        "description": "High ponytail falling down the back, its end rolling up and over like a wave."}


def build(g):
    scalp(g, 20151, side_rows=5, back_rows=8, sideburn=3)
    ring_shell(g, 20152, side_rows=5, back_rows=8, ring_row=1)
    tie(g, "tie", (0, -7.0, 4.5), (24, 0, 0), size=(3, 1, 2), y=-.5, key="K2")
    wave_lock(g, "tail", (0, -6.8, 4.7), (14, 0, 0), [(((3, 4), (3, 3)), 0, 0), (((2, 3),), 40, 0), (((2, 2),), 60, 0),
                                                     (((1, 2),), 60, 0)], depth=2, seed=20155, motion="sway")
    sidelocks(g, "temple", 4, seed=20170, x=4.3, z=-3.2, flare=5, width=1)
    bangs(g, "fringe", [(-2.6, ((2, 2), (1, 1)), 16), (2.6, ((2, 2), (1, 1)), -16)], seed=20175)
