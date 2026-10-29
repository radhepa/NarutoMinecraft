"""Veiled Sweep: shoulder-length straight hair parted far to the left, one long sheet swept down the
right side past the cheek like a half veil (it stops beside the eye, never over it), the rest
tucked behind the left ear."""
from anime import curtain, lock, ring_shell
from paint import scalp

META = {"name": "Veiled Sweep", "gender": "unisex",
        "description": "Shoulder-length hair parted far left, a long sheet swept down the right cheek, left side tucked."}

SWOOP = [(2.6, ((2, 2), (1, 1)), 64), (1.0, ((3, 2), (2, 2)), 70), (-.8, ((3, 2), (2, 2), (1, 1)), 60)]


def build(g):
    scalp(g, 24151, side_rows=7, back_rows=8, sideburn=0, part=6)
    ring_shell(g, 24152, side_rows=6, back_rows=8, ring_row=1)
    for i, (x, segs, rz) in enumerate(SWOOP):
        lock(g, f"swoop_{i}", (x, -8.55, -4.35), (-10, 0, rz), segs, 1, 24155 + i * 7, ring=0)
    lock(g, "veil", (-4.6, -7.9, -3.2), (0, 0, 3), ((2, 5), (2, 3), (1, 2)), 2, 24170)
    lock(g, "tucked", (4.5, -7.4, .6), (0, 0, -4), ((1, 5), (1, 1)), 2, 24172)
    curtain(g, "back", (0, -7.6, 4.5), (6, 0, 0), 9, 8, hem=((0, 3, 2), (3, 3, 3), (6, 3, 2)), seed=24175)
