"""Elder's Long Tie: the clan elders' look, after Murakumo and Uroko Kurama. Long straight hair parted
in the middle, falling loose from the crown and tied once, low, halfway down the back, the end running
on below the tie; long strands frame the face to the chest."""
from anime import curtain, lock, ring_shell, sidelocks, tie
from paint import scalp

META = {"name": "Elder's Long Tie", "gender": "unisex",
        "description": "Long hair parted in the middle, loosely tied low down the back, long face-framing strands."}


def build(g):
    scalp(g, 12520, side_rows=7, back_rows=8, sideburn=3, part=3)
    ring_shell(g, 12521, side_rows=7, back_rows=8, ring_row=1)
    curtain(g, "back", (0, -6.4, 4.6), (-10, 0, 0), 7, 7, seed=12522)
    tie(g, "tie", (0, -6.4, 4.6), (-10, 0, 0), size=(4, 1, 2), y=7.0, key="A1")
    lock(g, "tail", (0, -6.4, 4.6), (-8, 0, 0), ((5, 3), (4, 3), (3, 2), (2, 1)), 1, 12530, ring=None, motion="sway", y0=8.0)
    sidelocks(g, "frame", 12, seed=12540, x=4.3, z=-3.3, flare=2, width=2)
    lock(g, "part_0", (-1.0, -8.5, -4.3), (-10, 0, 30), ((2, 2), (1, 1)), 1, 12550, ring=0)
    lock(g, "part_1", (1.0, -8.5, -4.3), (-10, 0, -30), ((2, 2), (1, 1)), 1, 12552, ring=0)
