"""Bloom Ponytail: a genin's high ponytail to the middle of the back, tied with a blossom, a fringe
split in two soft points at the brows and long face-framing locks to the collarbone."""
from anime import bangs, cel_box, lock, ring_shell, sidelocks, tie
from kit_yamanaka import flower
from paint import scalp

META = {"name": "Bloom Ponytail", "gender": "unisex",
        "description": "High ponytail to mid-back with a blossom tie, split fringe, long framing locks."}


def build(g):
    scalp(g, 7171, side_rows=5, back_rows=7, sideburn=3)
    ring_shell(g, 7172, side_rows=4, back_rows=6, ring_row=1)
    bangs(g, "fringe", [(-2.7, ((2, 2), (1, 1)), 20), (-1.0, ((3, 2), (1, 1)), 12), (1.0, ((3, 2), (1, 1)), -12),
                        (2.7, ((2, 2), (1, 1)), -20)], seed=7180)
    sidelocks(g, "frame", 10, seed=7185, x=4.3, z=-3.4, flare=3, width=2)
    tie(g, "tie", (0, -7.2, 4.4), (0, 0, 0), (3, 2, 3), y=-1, key="A2")
    flower(g, "bloom", (1.7, -7.6, 5.1), rotation=(0, 180, 0), size=5)
    root = g.piece("tail_root", "HEAD", (-2, -2, 0), (4, 3, 3), pivot=(0, -7.4, 5.0), rotation=(20, 0, 0))
    cel_box(root, 7190, base=2)
    lock(g, "ponytail", (0, -7.4, 6.2), (16, 0, 0), ((4, 3), (3, 4), (3, 4), (2, 3), (1, 2)), 3, 7195, ring=None,
         motion="sway")
