"""Hedgehog Crop: a short dense cut that bristles all over, every tuft a stubby point standing
straight off the head, the way a messenger keeps it so the wind cannot tangle it."""
from anime import bangs, ring_shell
from kit_hagane import crown
from paint import scalp

META = {"name": "Hedgehog Crop", "gender": "unisex",
        "description": "Short dense bristles standing off the whole head, a stubby pointed fringe."}

STUB = ((2, 2), (1, 2))
SPIKES = [(x, z, STUB, rx, rz) for x, z, rx, rz in (
    (-2.8, -2.8, 10, -40), (-1.0, -3.0, 14, -12), (1.0, -3.0, 14, 12), (2.8, -2.8, 10, 40),
    (-2.8, -.6, -10, -52), (-1.0, -.8, -6, -16), (1.0, -.8, -6, 16), (2.8, -.6, -10, 52),
    (-2.8, 1.6, -36, -50), (-1.0, 1.4, -30, -14), (1.0, 1.4, -30, 14), (2.8, 1.6, -36, 50),
    (-1.8, 3.2, -64, -26), (0, 3.4, -70, 0), (1.8, 3.2, -64, 26))]


def build(g):
    scalp(g, 21160, side_rows=3, back_rows=7, sideburn=1)
    ring_shell(g, 21161, side_rows=3, back_rows=6, ring_row=1)
    crown(g, "bristle", SPIKES, 21162)
    bangs(g, "fringe", [(-2.6, ((2, 1), (1, 1)), 18), (-.8, ((1, 2),), 6), (.8, ((1, 2),), -6),
                        (2.6, ((2, 1), (1, 1)), -18)], seed=21210)
