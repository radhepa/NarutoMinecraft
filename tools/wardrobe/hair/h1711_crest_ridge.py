"""Crest Ridge: the sides shaved to stubble, a short stiff ridge of hair left standing down the
middle of the head from brow to nape."""
from anime import spike
from kit_morino import clipped

META = {"name": "Crest Ridge", "gender": "unisex",
        "description": "Shaved sides with a short stiff ridge of hair standing from brow to nape."}

TUFT = ((2, 2), (2, 1), (1, 1))
# (z, rx)
RIDGE = [(-3.4, 24), (-2.0, 14), (-.6, 6), (.8, -4), (2.2, -14), (3.4, -30)]


def build(g):
    clipped(g, 17101, side_rows=4, back_rows=6)
    for i, (z, rx) in enumerate(RIDGE):
        spike(g, f"ridge_{i}", (0, -8.0, z), (rx, 0, 0), TUFT, 2, 17103 + i * 3)
