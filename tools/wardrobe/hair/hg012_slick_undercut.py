"""Slick Undercut: the sides and back cropped to stubble, the long top combed straight back from the
brow in flat locks that lift into a short quiff at the front and fan out over the crown."""
from anime import lock, spike
from paint import scalp

META = {"name": "Slick Undercut", "gender": "unisex",
        "description": "Stubble-short sides and back, long top combed straight back from a short front quiff."}

# (x, rz): locks laid back over the crown from the hairline.
TOP = [(-3.0, -6), (-1.5, -3), (0, 0), (1.5, 3), (3.0, 6)]


def build(g):
    scalp(g, 32815, side_rows=8, back_rows=8, sideburn=0, base=1, shadow=False)
    for i, (x, rz) in enumerate(TOP):
        lock(g, f"combed_{i}", (x, -8.4, -3.4), (86, 0, rz), ((2, 3), (2, 3), (2, 2), (1, 1)), 1, 32817 + i, ring=1)
    for i, x in enumerate((-1.2, 1.2)):
        spike(g, f"quiff_{i}", (x, -9.0, -3.4), (24, 0, 10 if x < 0 else -10), ((3, 1), (2, 1)), 2, 32822 + i)
