"""Cowlick Shag: a short untidy shag with one great cowlick spike standing up off the front of
the crown that no amount of water flattens, smaller spikes behind it."""
from anime import bangs, ring_shell, sidelocks
from kit_hagane import crown
from paint import scalp

META = {"name": "Cowlick Shag", "gender": "unisex",
        "description": "A short untidy shag with one big cowlick spike at the front of the crown."}

BIG = ((3, 3), (2, 2), (1, 1))
SMALL = ((2, 2), (1, 1))
SPIKES = [(.6, -2.4, BIG, 18, 14), (-2.6, -1.4, SMALL, -8, -50), (2.8, -.8, SMALL, -8, 52), (-1.2, 1.0, SMALL, -34, -14),
          (1.6, 1.2, SMALL, -34, 18), (-2.4, 3.0, SMALL, -66, -30), (0, 3.4, SMALL, -72, 0), (2.4, 3.0, SMALL, -66, 30)]


def build(g):
    scalp(g, 21760, side_rows=5, back_rows=8, sideburn=2)
    ring_shell(g, 21761, side_rows=5, back_rows=7, ring_row=1)
    crown(g, "spike", SPIKES, 21762)
    bangs(g, "fringe", [(-2.8, ((2, 2), (1, 1)), 24), (-1.0, ((2, 2), (1, 1)), 12), (1.0, ((2, 2), (1, 1)), -4),
                        (2.8, ((2, 2), (1, 1)), -24)], seed=21790)
    sidelocks(g, "frame", 5, seed=21800, x=4.3, z=-2.8, flare=16, width=2)
