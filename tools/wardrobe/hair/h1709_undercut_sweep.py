"""Undercut Sweep: the sides and nape shaved to stubble under a long top combed over hard to one
side, the swept ends hanging past the temple."""
from anime import lock
from kit_morino import clipped
from paint import hair_face, k

META = {"name": "Undercut Sweep", "gender": "unisex",
        "description": "Shaved sides and nape under a long top combed hard over to one side."}

# Locks laid across the crown from the part, pointing over to the right temple: (z, length)
SWEEP = [(-3.0, ((2, 3), (2, 2), (1, 2))), (-1.5, ((2, 3), (2, 2), (1, 2))), (0, ((2, 3), (2, 2), (1, 1))),
         (1.5, ((2, 3), (2, 2), (1, 1))), (3.0, ((2, 3), (1, 2)))]


def build(g):
    clipped(g, 17081, side_rows=5, back_rows=6, crown=False)
    for i, (z, segs) in enumerate(SWEEP):
        lock(g, f"sweep_{i}", (3.0, -8.3, z), (0, 0, 108 + i * 2), segs, 2, 17083 + i * 5, ring=0)
    head = g.part("head")
    hair_face(head.top, 17082)
    head.top.vline(5, 0, 7, k("H", 0))
