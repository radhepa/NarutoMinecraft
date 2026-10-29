"""Leaf Crop: short layered hair that lies in overlapping leaf-shaped points over the crown and down
the nape, close at the sides, with a light fringe of three points."""
from anime import bangs, lock, ring_shell
from paint import scalp

META = {"name": "Leaf Crop", "gender": "unisex",
        "description": "Short layered crop lying in leaf-shaped points over the crown and nape, close sides."}

LEAF = ((3, 2), (2, 2), (1, 1))


def build(g):
    scalp(g, 24101, side_rows=3, back_rows=6, sideburn=2)
    ring_shell(g, 24102, side_rows=3, back_rows=6, ring_row=1)
    for i, (x, z, rx, rz) in enumerate(((-2.2, -2.0, 70, 8), (.4, -2.2, 72, -4), (2.6, -1.6, 70, -12), (-1.2, .6, 84, 6),
                                        (1.6, .8, 84, -6))):
        lock(g, f"crown_{i}", (x, -8.3, z), (rx, 0, rz), LEAF, 1, 24105 + i * 5, ring=0)
    for i, x in enumerate((-2.6, 0, 2.6)):
        lock(g, f"nape_{i}", (x, -6.4, 4.35), (14, 0, 0), ((3, 3), (2, 2), (1, 1)), 1, 24130 + i * 5, ring=0)
    bangs(g, "fringe", [(-2.4, ((2, 2), (1, 1)), 14), (0, ((3, 2), (1, 1)), 4), (2.4, ((2, 2), (1, 1)), -14)],
          seed=24145)
