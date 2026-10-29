"""Nape Chignon: long hair parted in the middle and smoothed back into a round knot low at the nape,
pinned with a wooden comb, with two long locks left to frame the face."""
from anime import bangs, ring_shell, sidelocks
from kit_senju import bun
from paint import k, scalp

META = {"name": "Nape Chignon", "gender": "unisex",
        "description": "Centre parting, hair smoothed into a round knot at the nape with a comb, long framing locks."}


def build(g):
    scalp(g, 1448, side_rows=6, back_rows=8, sideburn=3, part=3)
    ring_shell(g, 1449, side_rows=6, back_rows=8, ring_row=1)
    bun(g, "chignon", (0, -2.6, 5.9), (5, 4, 3), seed=1453)
    comb = g.piece("chignon_comb", "HEAD", (-3, -.5, -.5), (6, 1, 1), pivot=(0, -4.4, 6.6), rotation=(0, 0, -14))
    for f in comb.faces:
        f.fill("L3")
    comb.front.hline(0, 5, 0, k("L", 4))
    bangs(g, "fringe", [(-2.8, ((2, 2), (1, 1)), 14), (2.8, ((2, 2), (1, 1)), -14)], seed=1463)
    sidelocks(g, "frame", 11, seed=1468, x=4.3, z=-3.4, flare=3, width=1)
