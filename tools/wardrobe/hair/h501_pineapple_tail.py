"""Pineapple Tail: the Nara signature. Hair combed straight back off the brow and tied high on the
back of the crown in a short tail that bursts up and out in stiff spikes, two loose wisps at the
temples."""
from anime import sidelocks
from kit_nara import pineapple, pulled_back

META = {"name": "Pineapple Tail", "gender": "unisex",
        "description": "Combed back and tied high, a short tail bursting up in stiff spikes like a pineapple top."}

# (segments, tilt back, splay)
LONG = ((3, 3), (3, 2), (2, 2), (1, 2))
MID = ((3, 3), (2, 2), (1, 2))
SPIKES = [(LONG, -28, 0), (LONG, -46, -24), (LONG, -46, 24), (MID, -70, -10), (MID, -70, 10), (MID, -18, -38),
          (MID, -18, 38), (((2, 2), (1, 2)), -88, 0)]


def build(g):
    pulled_back(g, 5011, side_rows=3, back_rows=6, sideburn=3)
    pineapple(g, "tail", (0, -7.4, 4.2), SPIKES, seed=5020)
    sidelocks(g, "wisp", 4, seed=5040, x=4.35, z=-2.6, flare=6, width=1)
