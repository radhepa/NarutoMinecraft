"""Braided Spikes: back-swept crown spikes with the long hair beneath plaited into a single tight
braid down the back, tied off in rust cord: the way the clan's women keep long hair out of a fight."""
from anime import bangs, braid, ring_shell, sidelocks, tie
from kit_hagane import crown
from paint import scalp

META = {"name": "Braided Spikes", "gender": "unisex",
        "description": "Back-swept crown spikes over one tight braid down the back, tied in rust cord."}

MID = ((3, 2), (2, 2), (1, 1))
SPIKES = [(-2.4, -2.8, MID, -22, -26), (0, -3.2, MID, -26, 0), (2.4, -2.8, MID, -22, 26),
          (-1.4, -.4, MID, -48, -12), (1.4, -.4, MID, -48, 12), (0, 1.6, MID, -64, 0)]


def build(g):
    scalp(g, 21810, side_rows=6, back_rows=8, sideburn=2)
    ring_shell(g, 21811, side_rows=6, back_rows=8, ring_row=1)
    crown(g, "spike", SPIKES, 21812)
    pivot = (0, -2.0, 4.1)
    end = braid(g, "braid", pivot, (8, 0, 0), links=6, width=3, seed=21830)
    tie(g, "cord", pivot, (8, 0, 0), size=(2, 1, 2), key="A2", y=end - 2, motion="sway")
    bangs(g, "fringe", [(-2.8, ((2, 2), (1, 1)), 22), (-.8, ((2, 2), (1, 1)), 8), (1.2, ((2, 2), (1, 1)), -10),
                        (2.9, ((2, 2), (1, 1)), -22)], seed=21850)
    sidelocks(g, "frame", 7, seed=21860, x=4.35, z=-3.2, flare=6, width=2)
