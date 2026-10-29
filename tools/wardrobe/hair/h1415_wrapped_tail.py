"""Wrapped Tail: long wavy hair drawn into a low tail and bound down its length in bandage cloth,
the clan's wraps carried into the hair, with the wavy end spilling free below the last turn."""
from anime import bangs, tie
from kit_yuhi import wave_lock, wave_shell
from paint import scalp

META = {"name": "Wrapped Tail", "gender": "unisex",
        "description": "Long low tail bound in bandage cloth down its length, a wavy end spilling free."}


def build(g):
    scalp(g, 14561, side_rows=6, back_rows=8, sideburn=3)
    wave_shell(g, 14562, side_rows=6, back_rows=8, ring_row=1)
    bangs(g, "fringe", [(-2.8, ((2, 2), (1, 1)), 20), (-1.2, ((2, 1), (1, 1)), 30), (1.2, ((2, 1), (1, 1)), -30),
                        (2.8, ((2, 2), (1, 1)), -20)], seed=14570)
    pivot, rot = (0, -1.8, 4.8), (12, 0, 0)
    wave_lock(g, "tail", pivot, rot, ((3, 3), (3, 3), (3, 3), (3, 2), (2, 2), (1, 1)), 2, 14575, ring=None, motion="sway", amp=0)
    for i, y in enumerate((-.4, 2.0, 4.4, 6.8)):
        tie(g, f"wrap_{i}", pivot, rot, size=(4, 1, 3), y=y, key="S3" if i % 2 == 0 else "S2", motion="sway")
    for side, sign in (("right", -1), ("left", 1)):
        wave_lock(g, f"frame_{side}", (4.3 * sign, -7.6, -3.3), (0, 0, -5 * sign), ((2, 3), (2, 3), (1, 2)), 1,
                  14580 + (sign > 0), amp=.35, flip=sign > 0)
