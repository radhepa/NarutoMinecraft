"""Sawdust Crop: short tousled hair kept clear of the work, small blunt tufts all over the crown
pushed every which way, a choppy fringe well above the brows and close-cut sides."""
from anime import bangs, ring_shell, spike
from paint import scalp

META = {"name": "Sawdust Crop", "gender": "unisex",
        "description": "Short tousled tufts pushed every which way, a choppy short fringe, close sides."}

TUFT = ((2, 2), (1, 1))


def build(g):
    scalp(g, 22001, side_rows=3, back_rows=6, sideburn=2)
    ring_shell(g, 22002, side_rows=3, back_rows=6, ring_row=1)
    for i, (x, z, rx, rz) in enumerate(((-2.6, -2.6, -30, -40), (-.6, -2.8, -36, 12), (1.8, -2.4, -24, 44),
                                        (-1.8, -.2, 6, -22), (.8, .2, -8, 30), (2.6, 1.6, 28, 14),
                                        (-2.4, 2.2, 30, -30), (0, 2.8, 40, 6))):
        spike(g, f"tuft_{i}", (x, -7.8, z), (rx, 0, rz), TUFT, 2, 22004 + i)
    bangs(g, "fringe", [(-2.4, ((2, 1), (1, 1)), 30), (-.4, ((2, 1),), -14), (1.6, ((2, 1), (1, 1)), 22),
                        (3.0, ((1, 2),), -10)], seed=22013)
