"""Strap Braid: hair combed back flat and plaited into one long braid down the spine, the way the
family's sword straps are plaited, bound at the root and the tail with dark cord."""
from anime import braid, lock, ring_shell, tie
from paint import scalp

META = {"name": "Strap Braid", "gender": "unisex",
        "description": "Hair combed back into one long braid down the spine, bound with dark cord."}

PIVOT, TILT = (0, -2.4, 4.7), (-6, 0, 0)


def build(g):
    scalp(g, 15330, side_rows=5, back_rows=8, sideburn=3)
    ring_shell(g, 15331, side_rows=5, back_rows=8, ring_row=1)
    tie(g, "root_tie", PIVOT, TILT, size=(3, 1, 3), y=-.2, key="D2")
    end = braid(g, "braid", PIVOT, TILT, links=6, width=3, seed=15335, y0=.8)
    tie(g, "tail_tie", PIVOT, TILT, size=(2, 1, 2), y=end - 2.6, key="D2", motion="sway")
    for i, (x, rz) in enumerate(((-2.4, 16), (2.4, -16))):
        lock(g, f"brow_{i}", (x, -8.55, -4.35), (-10, 0, rz), ((2, 2), (1, 1)), 1, 15345 + i, ring=0)
