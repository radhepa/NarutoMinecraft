"""Cowlick Crop: short hair cropped close at the sides, a brief fringe, and one stubborn cowlick that
springs up from the crown and curls forward no matter how it is flattened, with a second tuft behind."""
from anime import bangs, lock, ring_shell, spike
from paint import scalp

META = {"name": "Cowlick Crop", "gender": "unisex",
        "description": "Close-cropped sides, a brief fringe and one stubborn cowlick curling forward off the crown."}

TUFT = ((3, 1), (2, 1), (1, 1))


def build(g):
    scalp(g, 31750, side_rows=3, back_rows=6, sideburn=2)
    ring_shell(g, 31751, side_rows=3, back_rows=5, ring_row=1)
    for i, (x, z, rx, rz) in enumerate(((-2.4, -1.6, -16, -26), (2.4, -1.4, -14, 24), (-1.6, 1.6, 20, -18),
                                        (1.8, 1.8, 22, 20), (0, -2.6, -22, 0))):
        spike(g, f"crown_tuft_{i}", (x, -7.8, z), (rx, 0, rz), TUFT, 3, 31752 + i)
    # The cowlick: a lock that rises off the crown, bends over and curls toward the brow.
    spike(g, "cowlick_root", (.4, -8.2, -.4), (6, 0, 8), ((3, 2), (2, 2)), 2, 31758)
    lock(g, "cowlick_curl", (.9, -12.0, -.4), (-118, 0, 12), ((2, 2), (1, 2)), 2, 31760, ring=None)
    spike(g, "back_tuft", (-.6, -7.6, 2.8), (52, 0, -18), ((2, 2), (1, 1)), 2, 31762)
    bangs(g, "fringe", [(-2.4, ((2, 1), (1, 1)), 20), (-.4, ((2, 1), (1, 1)), 6), (1.8, ((2, 1), (1, 1)), -16)],
          seed=31764)
