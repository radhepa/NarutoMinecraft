"""Hackle Crest: the sides cut close and the top grown into a ridge of tall spikes from brow to nape,
raised like a hound's hackles, the front spike leaning forward over a bare forehead."""
from anime import lock
from kit_inuzuka import burst
from paint import scalp

META = {"name": "Hackle Crest", "gender": "unisex",
        "description": "Close-cut sides and a ridge of tall spikes from brow to nape, like raised hackles."}

TALL = ((3, 3), (2, 3), (1, 2))
CREST = [(0, -3.2, ((3, 2), (2, 2), (1, 1)), 30, 0), (0, -1.6, TALL, 6, 0), (0, .2, ((3, 4), (2, 3), (1, 2)), -14, 0),
         (0, 2.0, TALL, -38, 0), (0, 3.4, ((3, 2), (2, 2), (1, 1)), -70, 0), (-.9, -.6, ((2, 2), (1, 2)), 0, -18),
         (.9, -.6, ((2, 2), (1, 2)), 0, 18), (-.9, 1.6, ((2, 2), (1, 2)), -26, -20), (.9, 1.6, ((2, 2), (1, 2)), -26, 20)]


def build(g):
    scalp(g, 8241, side_rows=2, back_rows=4, sideburn=2, base=1)
    head = g.part("head")
    head.top.vline(2, 0, 7, "H2"), head.top.vline(5, 0, 7, "H2")
    for x in (3, 4):
        head.top.vline(x, 0, 7, "H3")
    burst(g, "crown_crest", CREST, 8243, depth=2)
    lock(g, "nape_tail", (0, -4.4, 4.1), (36, 0, 0), ((2, 2), (1, 2)), 1, 8252)
