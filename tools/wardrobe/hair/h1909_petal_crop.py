"""Petal Crop: short hair cropped close at the nape, the fringe cut into rounded petal points that
stop on the brows, and soft layered tufts over the crown."""
from anime import lock, ring_shell, spike
from paint import scalp

META = {"name": "Petal Crop", "gender": "unisex",
        "description": "Short crop, a fringe of rounded petal points on the brows, soft crown tufts."}

PETAL = ((3, 2), (2, 1))
FRINGE = [(-3.0, PETAL, 10), (-1.0, PETAL, 4), (1.0, PETAL, -4), (3.0, PETAL, -10)]
CROWN = [(-1.6, -.4, -24, 26), (1.6, -.4, -24, -26), (0, 1.8, -64, 0)]


def build(g):
    scalp(g, 19231, side_rows=4, back_rows=6, sideburn=2)
    ring_shell(g, 19232, side_rows=4, back_rows=5, ring_row=1)
    for i, (x, segs, rz) in enumerate(FRINGE):
        lock(g, f"petal_{i}", (x, -8.55, -4.35), (-10, 0, rz), segs, 1, 19235 + i * 7, ring=0)
    for i, (x, z, rx, rz) in enumerate(CROWN):
        spike(g, f"tuft_{i}", (x, -7.8, z), (rx, 0, rz), ((3, 2), (2, 1)), 3, 19265 + i)
    for side, sign in (("right", -1), ("left", 1)):
        lock(g, f"ear_{side}", (4.3 * sign, -7.6, -1.6), (0, 0, -4 * sign), ((2, 3), (1, 1)), 1, 19270 + (sign > 0))
