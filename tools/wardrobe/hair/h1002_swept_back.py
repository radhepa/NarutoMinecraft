"""Swept Back: Shino's grown-up look as the Academy teacher, hair brushed straight up off the
forehead and back into a tall, tidy crest of points that ends above the nape."""
from anime import ring_shell, spike
from paint import scalp

META = {"name": "Swept Back", "gender": "unisex",
        "description": "Hair brushed up off the forehead and back into a tall, tidy crest of points."}

# The front rises steeply, the rest lies back in long flat blades.
BLADES = [(-2.4, -3.0, ((3, 3), (2, 3), (1, 2)), -42, -6), (0, -3.2, ((4, 4), (3, 3), (2, 2), (1, 1)), -40, 0),
          (2.4, -3.0, ((3, 3), (2, 3), (1, 2)), -42, 6),
          (-2.0, .2, ((3, 3), (2, 3), (1, 1)), -66, -6), (2.0, .2, ((3, 3), (2, 3), (1, 1)), -66, 6),
          (0, 2.4, ((3, 3), (2, 2), (1, 1)), -84, 0)]


def build(g):
    scalp(g, 10031, side_rows=3, back_rows=6, sideburn=3)
    ring_shell(g, 10032, side_rows=3, back_rows=6, ring_row=1)
    for i, (x, z, segs, rx, rz) in enumerate(BLADES):
        spike(g, f"crest_{i}", (x, -7.8, z), (rx, 0, rz), segs, 2, 10040 + i)
