"""Warden's Tail: long straight hair drawn back from the face and tied low at the nape, the tail
hanging flat and heavy to the shoulder blades in a squared end."""
from anime import curtain, tie
from kit_morino import combed_back

META = {"name": "Warden's Tail", "gender": "unisex",
        "description": "Long straight hair tied low at the nape, a flat heavy tail to the shoulder blades."}


def build(g):
    combed_back(g, 17161, side_rows=5, back_rows=8, sideburn=1)
    pivot, tilt = (0, -2.8, 4.6), (12, 0, 0)
    tie(g, "tie", pivot, tilt, (4, 1, 2), y=-.5, key="K2")
    curtain(g, "tail", pivot, tilt, 4, 7, hem=[(0, 2, 1), (2, 2, 1)], seed=17162, depth=2)
