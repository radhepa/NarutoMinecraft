"""Kikai Crest: sides cropped close and one ridge of spikes from brow to nape, standing like the
horn and back of a beetle."""
from anime import ring_shell, spike
from paint import scalp

META = {"name": "Kikai Crest", "gender": "unisex",
        "description": "Close-cropped sides under a single ridge of spikes from brow to nape."}

# (z, y, segments, tilt): the ridge runs over the centre of the head, the front horn tallest.
RIDGE = [(-3.0, -7.8, ((3, 3), (2, 2), (1, 2)), -8), (-1.0, -7.8, ((3, 3), (2, 2), (1, 1)), -30),
         (1.0, -7.8, ((3, 3), (2, 2), (1, 1)), -50), (3.0, -7.6, ((3, 2), (2, 2), (1, 1)), -70),
         (4.2, -5.6, ((3, 2), (2, 1), (1, 1)), -96)]


def build(g):
    scalp(g, 10131, side_rows=2, back_rows=5, sideburn=1)
    ring_shell(g, 10132, side_rows=1, back_rows=4, ring_row=0)
    for i, (z, y, segs, rx) in enumerate(RIDGE):
        spike(g, f"ridge_{i}", (0, y, z), (rx, 0, 0), segs, 3, 10140 + i)
