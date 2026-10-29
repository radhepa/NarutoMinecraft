"""Herder Wrap: the deer herder's practical tail. Hair pulled back to a high spiky tail whose root is
bound in a strip of shadow-black cloth, its tails hanging down the back of the head."""
from anime import sidelocks
from kit_nara import pineapple, pulled_back
from paint import solid

META = {"name": "Herder Wrap", "gender": "unisex",
        "description": "High spiky tail bound at the root in a black cloth wrap with hanging ends."}

MID = ((3, 3), (2, 2), (1, 2))
SPIKES = [(MID, -34, 0), (MID, -50, -26), (MID, -50, 26), (((2, 2), (1, 2)), -72, 0), (((2, 3), (1, 2)), -20, -38),
          (((2, 3), (1, 2)), -20, 38)]


def build(g):
    pulled_back(g, 5551, side_rows=3, back_rows=6, sideburn=3)
    pineapple(g, "tail", (0, -7.4, 4.2), SPIKES, seed=5560, tie_key="K2")
    wrap = g.piece("wrap", "HEAD", (-2, 1, -2), (4, 2, 4), pivot=(0, -7.4, 4.2), rotation=(-30, 0, 0), inflate=.15)
    solid(wrap, "K", "weave", 5580, 2, edge=False)
    for i, (x, rz) in enumerate(((-.6, 12), (.6, -8))):
        end = g.piece(f"wrap_end_{i}", "HEAD", (-.5, 0, 0), (1, 4 - i, 1), pivot=(x, -6.0, 5.6), rotation=(14, 0, rz),
                      motion="sway")
        solid(end, "K", "weave", 5585 + i, 2)
    sidelocks(g, "wisp", 4, seed=5590, x=4.35, z=-2.6, flare=6, width=1)
