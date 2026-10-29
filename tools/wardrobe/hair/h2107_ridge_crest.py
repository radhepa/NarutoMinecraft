"""Ridge Crest: the sides cropped close and a single ridge of tall spikes left standing from the
brow to the nape like the comb of a helmet."""
from anime import bangs, ring_shell
from kit_hagane import crown
from paint import scalp

META = {"name": "Ridge Crest", "gender": "unisex",
        "description": "Close-cropped sides and one ridge of tall spikes from brow to nape."}

TALL = ((3, 3), (2, 2), (1, 2))
SPIKES = [(0, -3.2, TALL, 14, 0), (0, -1.2, TALL, -6, 0), (0, .8, TALL, -26, 0), (0, 2.8, TALL, -50, 0),
          (0, 3.8, ((3, 2), (2, 2), (1, 1)), -80, 0)]


def build(g):
    scalp(g, 21410, side_rows=1, back_rows=5, sideburn=1, base=1)
    ring_shell(g, 21411, side_rows=1, back_rows=4, ring_row=0, base=1)
    crown(g, "crest", SPIKES, 21412, depth=3)
    bangs(g, "fringe", [(0, ((3, 1), (1, 1)), 0)], seed=21430)
