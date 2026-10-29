"""Root Buzz: the Foundation's field cut, clipped close all round with a little texture on the
crown and a short blunt hairline, nothing to catch in a mask strap or a hood."""
from anime import spike
from paint import scalp

META = {"name": "Root Buzz", "gender": "unisex", "description": "Close-clipped field cut with a little texture on the crown."}

TUFT = ((2, 1), (1, 1))
CROWN = [(-2.0, -1.4, -10, -10), (.6, -1.8, -12, 8), (2.4, .4, 6, 16), (-1.2, 1.6, 14, -12), (1.0, .2, 0, 0)]


def build(g):
    scalp(g, 13099, side_rows=3, back_rows=5, sideburn=1)
    for i, (x, z, rx, rz) in enumerate(CROWN):
        spike(g, f"crown_tuft_{i}", (x, -7.9, z), (rx, 0, rz), TUFT, 2, 13105 + i)
