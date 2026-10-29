"""Shaggy Mane: thick shoulder-length hair hacked short at the crown into spikes and left long
and ragged behind, every lock ending in a stiff point that kicks away from the neck."""
from anime import back_fan, bangs, ring_shell, sidelocks
from kit_hagane import crown
from paint import scalp

META = {"name": "Shaggy Mane", "gender": "unisex",
        "description": "Spiky crown over ragged shoulder-length hair, every lock kicking out in a point."}

MID = ((3, 2), (2, 2), (1, 1))
SPIKES = [(-2.4, -2.6, MID, -14, -30), (0, -3.0, MID, -18, 0), (2.4, -2.6, MID, -14, 30),
          (-1.4, -.4, MID, -40, -14), (1.4, -.4, MID, -40, 14)]


def build(g):
    scalp(g, 21700, side_rows=8, back_rows=8, sideburn=0)
    ring_shell(g, 21701, side_rows=8, back_rows=8, ring_row=1)
    crown(g, "spike", SPIKES, 21702)
    back_fan(g, "mane", [(-3.2, ((2, 8), (2, 2), (1, 1)), 14, 16), (-1.6, ((2, 9), (1, 2)), 6, 18),
                         (0, ((3, 9), (2, 2), (1, 1)), 0, 28), (1.6, ((2, 9), (1, 2)), -6, 18),
                         (3.2, ((2, 8), (2, 2), (1, 1)), -14, 16)], seed=21710, motion="sway")
    sidelocks(g, "side", 9, seed=21740, x=4.35, z=-2.2, flare=6, width=2)
    bangs(g, "fringe", [(-2.8, ((2, 3), (1, 1)), 22), (-.8, ((2, 2), (1, 1)), 8), (1.2, ((2, 2), (1, 1)), -10),
                        (2.9, ((2, 3), (1, 1)), -24)], seed=21750)
