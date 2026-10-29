"""Undercut Braid: the right side shaved to stubble, the rest swept over to the left in a long
side-parted fall that clears the eyes, and a single long braid down the back from the crown, its
end wrapped in leather."""
from anime import braid, lock, tie
from paint import hair_face, k, rnd

META = {"name": "Undercut Braid", "gender": "unisex",
        "description": "Right side shaved, the rest swept to the left side, one long braid down the back with a leather end."}


def build(g):
    head, hat = g.part("head"), g.part("hat")
    hair_face(head.top, 35800, 2)
    hair_face(head.back, 35801, 2)
    hair_face(head.left, 35802, 2, rows=range(7))
    for y in range(6):
        for x in range(8):
            head.right.set(x, y, "X1" if rnd(x, y, 35803) < .75 else "X2")
    head.front.hline(0, 7, 0, "H1")
    for x in range(8):
        for y in range(8):
            if x >= 2:
                hat.top.set(x, y, k("H", 3 if x >= 4 else 2))
        hat.left.set(x, 0, k("H", 2)), hat.left.set(x, 1, k("H", 2))
        hat.back.set(x, 0, k("H", 2))
    # The swept-over top: locks from the part laid across to the left and down past the ear.
    for i, (z, segs) in enumerate(((-3.0, ((3, 3), (2, 2), (1, 2))), (-1.0, ((3, 3), (2, 3), (1, 2))),
                                   (1.0, ((3, 3), (2, 2), (1, 1))), (3.0, ((3, 3), (2, 2), (1, 1))))):
        lock(g, f"sweep_{i}", (-.4, -8.3, z), (0, 0, -96), segs[:2], 2, 35805 + i, ring=0)
    lock(g, "fall_left", (4.5, -7.2, -2.0), (0, 0, -10), ((2, 5), (1, 2)), 2, 35810)
    tie(g, "braid_root", (0, -7.4, 4.4), (-20, 0, 0), (3, 2, 3))
    end = braid(g, "braid", (0, -6.4, 4.6), (-6, 0, 0), links=7, width=3, seed=35812)
    tie(g, "braid_wrap", (0, -6.4, 4.6), (-6, 0, 0), (2, 2, 2), y=end - 3.6, key="L2", motion="sway")
