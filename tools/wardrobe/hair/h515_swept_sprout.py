"""Swept Sprout: a long side-swept fringe falling to the brow over one eye's corner and down past
the cheek, the rest pulled up into a small spiky pineapple on the crown."""
from anime import bangs, sidelocks
from kit_nara import pineapple, pulled_back

META = {"name": "Swept Sprout", "gender": "unisex",
        "description": "A long side-swept fringe and framing lock, the rest pulled up in a small pineapple."}

S = ((3, 2), (2, 2), (1, 1))
SPIKES = [(S, -34, 0), (S, -52, -24), (S, -52, 24), (S, -14, -36), (S, -14, 36)]


def build(g):
    pulled_back(g, 5901, side_rows=4, back_rows=7, sideburn=2)
    pineapple(g, "tail", (0, -7.6, 3.6), SPIKES, seed=5910)
    bangs(g, "fringe", [(-3.1, ((3, 2), (2, 1)), 30), (-1.0, ((3, 2), (2, 1)), 52), (1.0, ((2, 2), (1, 1)), 44)],
          seed=5930)
    sidelocks(g, "frame", 8, seed=5950, x=4.35, z=-3.2, flare=3, width=2)
