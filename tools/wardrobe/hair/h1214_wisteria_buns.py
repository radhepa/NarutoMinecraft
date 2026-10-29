"""Wisteria Buns: two round buns high at the back of the head, each pinned with a slim paint brush,
short ends falling from under them like wisteria sprays; brow-length bangs in front."""
from anime import bangs, lock, ring_shell, sidelocks
from kit_kurama import brush_pin, bun
from paint import scalp

META = {"name": "Wisteria Buns", "gender": "female",
        "description": "Two high buns pinned with paint brushes, short falls beneath them, brow-length bangs."}


def build(g):
    scalp(g, 12620, side_rows=6, back_rows=8, sideburn=2, part=3)
    ring_shell(g, 12621, side_rows=6, back_rows=8, ring_row=1)
    for side, sign in (("right", -1), ("left", 1)):
        bun(g, f"bun_{side}", (2.6 * sign, -7.8, 3.6), size=4, seed=12624 + (sign > 0) * 4)
        brush_pin(g, f"pin_{side}", (2.6 * sign + 1.2 * sign, -8.0, 3.4), (20, 0, 80 * sign), length=8)
        for i, dx in enumerate((-.7, .7)):
            lock(g, f"fall_{side}_{i}", (2.7 * sign + dx, -6.8, 4.4), (14, 0, -dx * 8), ((1, 3), (1, 2)), 1,
                 12640 + i + (sign > 0) * 3, ring=None, motion="sway")
    bangs(g, "fringe", [(-2.8, ((2, 2), (1, 1)), 12), (-1.3, ((2, 2),), 20), (.2, ((2, 1), (1, 1)), 0),
                        (1.6, ((2, 2),), -20), (3.0, ((2, 2), (1, 1)), -10)], seed=12650)
    sidelocks(g, "frame", 7, seed=12670, x=4.3, z=-3.4, flare=3, width=1)
