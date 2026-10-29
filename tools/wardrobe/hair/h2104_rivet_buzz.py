"""Rivet Buzz: hair shorn close to the skull for summer gate duty, a few stubby points left
standing at the crown and a ragged hairline."""
from anime import bangs, ring_shell
from kit_hagane import crown
from paint import scalp

META = {"name": "Rivet Buzz", "gender": "unisex",
        "description": "Close-shorn hair with a few stubby points at the crown and a ragged hairline."}

NUB = ((2, 1), (1, 1))
SPIKES = [(-1.6, -2.4, NUB, 10, -20), (.6, -2.6, NUB, 14, 10), (-.6, -.2, NUB, -10, -6), (1.8, .2, NUB, -14, 24),
          (-2.2, 2.0, NUB, -40, -24), (.4, 2.4, NUB, -46, 4)]


def build(g):
    scalp(g, 21270, side_rows=2, back_rows=6, sideburn=1, base=1)
    ring_shell(g, 21271, side_rows=2, back_rows=5, ring_row=1, base=1)
    crown(g, "nub", SPIKES, 21272, depth=1, base=1)
    bangs(g, "fringe", [(-2.4, ((2, 1),), 10), (0, ((2, 1),), 0), (2.4, ((2, 1),), -10)], seed=21290, base=1)
