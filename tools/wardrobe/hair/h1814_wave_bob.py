"""Wave Bob: a chin-length bob that flips outward at the ends like a curling wave, a straight fringe
cut just above the brows and the sides tucked behind the ears' line."""
from anime import bangs, lock, ring_shell
from paint import scalp

META = {"name": "Wave Bob", "gender": "unisex",
        "description": "Chin-length bob flipping outward at the ends like a wave, a straight fringe above the brows."}


def build(g):
    scalp(g, 18281, side_rows=8, back_rows=8, sideburn=0)
    ring_shell(g, 18282, side_rows=7, back_rows=8, ring_row=1)
    bangs(g, "fringe", [(-2.6, ((2, 2), (1, 1)), 8), (-.9, ((2, 2),), 2), (.9, ((2, 2),), -2), (2.6, ((2, 2), (1, 1)), -8)],
          seed=18284)
    for side, sign in (("right", -1), ("left", 1)):
        lock(g, f"side_{side}", (4.4 * sign, -7.4, -1.0), (0, 0, -4 * sign), ((2, 6), (2, 1)), 5, 18286 + (sign > 0))
        lock(g, f"flip_{side}", (4.6 * sign, -.4, -1.0), (0, 0, -45 * sign), ((2, 2), (1, 1)), 4, 18290 + (sign > 0))
    lock(g, "nape", (0, -6.8, 4.4), (4, 0, 0), ((8, 6),), 1, 18294)
    for i, sign in enumerate((-1, 1)):
        lock(g, f"nape_flip_{i}", (2.4 * sign, -.6, 4.6), (-60, 0, -40 * sign), ((3, 2), (1, 1)), 1, 18296 + i)
