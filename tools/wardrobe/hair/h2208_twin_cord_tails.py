"""Twin Cord Tails: two low tails behind the ears, each bound with a cedar-red cord a little way down
so the ends flare, a blunt fringe cut straight across above the brows and short sideburns."""
from anime import bangs, cel_box, lock, ring_shell, tie
from paint import scalp

META = {"name": "Twin Cord Tails", "gender": "unisex",
        "description": "Two low tails behind the ears bound in cedar cord, a blunt straight fringe."}


def build(g):
    scalp(g, 22141, side_rows=6, back_rows=8, sideburn=2)
    ring_shell(g, 22142, side_rows=6, back_rows=8, ring_row=1)
    for side, sign in (("right", -1), ("left", 1)):
        pivot, rot = (3.0 * sign, -3.2, 3.8), (16, 0, -6 * sign)
        root = g.piece(f"root_{side}", "HEAD", (-1.5, -1, -1.5), (3, 2, 3), pivot=pivot, rotation=rot)
        cel_box(root, 22143 + (sign > 0))
        tie(g, f"cord_{side}", pivot, rot, (3, 1, 3), y=1.0, key="A2", motion="sway")
        lock(g, f"tail_{side}", pivot, rot, ((3, 2), (3, 3), (2, 2), (1, 1)), 2, 22146 + (sign > 0) * 5,
             ring=None, motion="sway", y0=2.0)
    bangs(g, "fringe", [(x, ((2, 2),), 0) for x in (-2.8, -.9, .9, 2.8)], seed=22156)
