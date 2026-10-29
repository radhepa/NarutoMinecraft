"""Watch Crop: the night watch's practical cut, short and close at the sides and nape so a hood sits
flat, a little length left on top brushed forward into a few soft points over the brow."""
from anime import bangs, ring_shell, spike
from paint import scalp

META = {"name": "Watch Crop", "gender": "unisex",
        "description": "Close-cropped sides and nape, short top brushed forward into soft points."}

TUFT = ((3, 1), (2, 1), (1, 1))


def build(g):
    scalp(g, 25020, side_rows=4, back_rows=6, sideburn=1)
    ring_shell(g, 25021, side_rows=3, back_rows=5, ring_row=1)
    for i, (x, z, rx, rz) in enumerate(((-2.0, -1.6, -34, -10), (.6, -1.8, -38, 6), (2.6, -.4, -26, 18))):
        spike(g, f"top_{i}", (x, -7.8, z), (rx, 0, rz), TUFT, 3, 25022 + i)
    bangs(g, "fringe", [(-2.4, ((2, 2), (1, 1)), 12), (-.4, ((2, 1), (1, 1)), 4), (1.8, ((2, 2), (1, 1)), -10)],
          seed=25026)
