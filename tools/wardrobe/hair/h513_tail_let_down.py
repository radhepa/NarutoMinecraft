"""Tail Let Down: the pineapple untied at the end of the day. Straight dark hair falling past the
jaw to the shoulders, still kinked into stiff points at the ends, the fringe pushed back."""
from anime import curtain, sidelocks
from kit_nara import pulled_back

META = {"name": "Tail Let Down", "gender": "unisex",
        "description": "The tail untied: hair falling to the shoulders in stiff points, fringe pushed back."}


def build(g):
    pulled_back(g, 5801, side_rows=7, back_rows=8, sideburn=1)
    curtain(g, "fall", (0, -6.4, 4.5), (8, 0, 0), 8, 6, hem=[(0, 2, 2), (2, 2, 3), (4, 2, 3), (6, 2, 2)], seed=5810)
    sidelocks(g, "frame", 9, seed=5830, x=4.35, z=-2.8, flare=4, width=2)
    sidelocks(g, "side", 8, seed=5840, x=4.4, z=.6, flare=6, width=2)
