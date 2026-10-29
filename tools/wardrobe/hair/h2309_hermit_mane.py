"""Hermit Mane: long, heavy, untamed hair of the mountain recluse, pushed back off the face and
falling in a wide sheet to the shoulder blades, its hem broken into ragged points."""
from anime import curtain, ring_shell, sidelocks
from paint import scalp

META = {"name": "Hermit Mane", "gender": "unisex",
        "description": "Long heavy hair pushed back off the face, falling wide to the shoulder blades in ragged points."}


def build(g):
    scalp(g, 23181, side_rows=7, back_rows=8, sideburn=1)
    ring_shell(g, 23182, side_rows=7, back_rows=8, ring_row=1)
    curtain(g, "mane", (0, -6.8, 4.7), (10, 0, 0), 9, 9, hem=((0, 2, 3), (2, 2, 2), (4, 2, 4), (7, 2, 2)), seed=23185)
    for side, sign in (("right", -1), ("left", 1)):
        curtain(g, f"mane_{side}", (3.9 * sign, -6.4, 2.6), (8, 0, 6 * sign), 2, 8, hem=((0, 2, 2),), seed=23190 + (sign > 0))
    sidelocks(g, "frame", 8, seed=23195, x=4.4, z=-3.0, flare=5, width=2)
