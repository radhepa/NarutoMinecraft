"""Shaggy Guard: layered hair grown out to the nape, thick ragged locks falling every way over the
crown and the collar, the fringe cut short above the brow."""
from anime import back_fan, bangs, ring_shell, sidelocks
from paint import scalp

META = {"name": "Shaggy Guard", "gender": "unisex",
        "description": "Layered hair grown to the nape in ragged locks, short ragged fringe, cheek points."}


def build(g):
    scalp(g, 20251, side_rows=6, back_rows=8, sideburn=3)
    ring_shell(g, 20252, side_rows=6, back_rows=8, ring_row=1)
    bangs(g, "fringe", [(-3.0, ((2, 2), (1, 1)), 22), (-1.4, ((2, 2), (1, 1)), -6), (.4, ((2, 2), (1, 1)), 16),
                        (2.0, ((2, 2), (1, 1)), -10), (3.2, ((2, 2), (1, 1)), -24)], seed=20255)
    sidelocks(g, "cheek", 5, seed=20270, x=4.4, z=-2.6, flare=10, width=2)
    back_fan(g, "nape", [(-3.0, ((3, 3), (2, 2), (1, 1)), 24, 18), (-1.0, ((3, 4), (2, 1), (1, 1)), 6, 12),
                         (1.0, ((3, 4), (2, 2), (1, 1)), -8, 14), (3.0, ((3, 3), (2, 1), (1, 1)), -24, 20)], seed=20275)
