"""Swept Crop: short hair cut close at the nape and sides, soft layered points over the crown and
one long fringe swept across the brow to the wearer's right, stopping on the eye line."""
from anime import lock, ring_shell, spike
from paint import scalp

META = {"name": "Swept Crop", "gender": "unisex",
        "description": "Close nape and sides, soft layered crown, a long fringe swept to the right."}

TUFT = ((3, 2), (2, 1), (1, 1))
CROWN = [(-1.8, -.6, TUFT, -30, 30), (1.4, -.4, TUFT, -30, 20), (-1.4, 2.2, TUFT, -70, -10), (1.6, 2.2, TUFT, -70, 12)]
SWOOP = [(3.0, ((2, 1), (1, 1)), 20), (1.6, ((3, 2), (2, 2), (1, 1)), 58), (-.1, ((3, 2), (2, 2), (1, 1)), 60),
         (-1.8, ((3, 2), (2, 1)), 44)]


def build(g):
    scalp(g, 7071, side_rows=3, back_rows=6, sideburn=2)
    ring_shell(g, 7072, side_rows=3, back_rows=5, ring_row=1)
    for i, (x, z, segs, rx, rz) in enumerate(CROWN):
        spike(g, f"crown_{i}", (x, -7.8, z), (rx, 0, rz), segs, 3, 7075 + i)
    for i, (x, segs, rz) in enumerate(SWOOP):
        lock(g, f"swoop_{i}", (x, -8.55, -4.35), (-10, 0, rz), segs, 1, 7080 + i * 7, ring=0)
    lock(g, "temple", (-4.4, -7.6, -3.0), (0, 0, 8), ((2, 3), (1, 2)), 1, 7095)
