"""Messenger Sweep: hair raked straight back by a life of running dispatches, every spike lying
low and streaming behind the head, the longest past the nape, a short fringe torn up off the brow."""
from anime import bangs, ring_shell
from kit_hagane import crown
from paint import scalp

META = {"name": "Messenger Sweep", "gender": "unisex",
        "description": "Spikes raked flat and streaming back past the nape, a short fringe torn off the brow."}

LONG = ((3, 3), (2, 3), (1, 2))
MID = ((3, 2), (2, 2), (1, 1))
SPIKES = [(-2.6, -2.6, MID, -64, -16), (0, -3.0, LONG, -70, 0), (2.6, -2.6, MID, -64, 16),
          (-1.4, -.2, LONG, -76, -8), (1.4, -.2, LONG, -76, 8), (-3.2, 1.6, MID, -86, -30), (3.2, 1.6, MID, -86, 30),
          (0, 2.0, LONG, -92, 0)]


def build(g):
    scalp(g, 21360, side_rows=4, back_rows=7, sideburn=2)
    ring_shell(g, 21361, side_rows=4, back_rows=6, ring_row=1)
    crown(g, "streak", SPIKES, 21362)
    bangs(g, "fringe", [(-2.6, ((2, 1), (1, 1)), 30), (-.6, ((2, 1),), 10), (1.4, ((2, 1), (1, 1)), -20)], seed=21400)
