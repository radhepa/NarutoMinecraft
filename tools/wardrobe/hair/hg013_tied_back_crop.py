"""Tied-Back Crop: chin-length hair pulled straight back off the face into a short stub of a tail at
the nape, two loose strands left at the temples."""
from anime import lock, ring_shell, sidelocks, tie
from paint import scalp

META = {"name": "Tied-Back Crop", "gender": "unisex",
        "description": "Hair pulled straight back into a short stub tail at the nape, loose strands at the temples."}


def build(g):
    scalp(g, 32830, side_rows=5, back_rows=8, sideburn=2)
    ring_shell(g, 32831, side_rows=4, back_rows=6, ring_row=1)
    tie(g, "tie", (0, -3.2, 4.6), (16, 0, 0), size=(3, 1, 2))
    lock(g, "stub", (0, -3.0, 4.8), (22, 0, 0), ((3, 2), (3, 1), (2, 1)), 2, 32832, ring=None, motion="sway")
    sidelocks(g, "temple", 4, seed=32835, x=4.4, z=-3.2, flare=6, width=1)
