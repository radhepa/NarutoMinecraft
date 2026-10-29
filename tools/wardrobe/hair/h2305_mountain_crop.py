"""Mountain Crop: short hair cropped close at the sides and back, a little longer and roughed up on
top, the plain cut of a clansman who works the mountain terraces."""
from anime import ring_shell, spike
from paint import scalp

META = {"name": "Mountain Crop", "gender": "unisex",
        "description": "Short close crop at the sides and back, roughed-up longer on top."}

TUFTS = [(-2.2, -2.2, -30, -16), (.4, -2.6, -34, 4), (2.6, -2.0, -30, 18), (-1.2, .6, -56, -10), (1.6, .8, -58, 12)]


def build(g):
    scalp(g, 23101, side_rows=3, back_rows=5, sideburn=1)
    ring_shell(g, 23102, side_rows=2, back_rows=4, ring_row=0)
    for i, (x, z, rx, rz) in enumerate(TUFTS):
        spike(g, f"crown_tuft_{i}", (x, -7.9, z), (rx, 0, rz), ((3, 1), (2, 1)), 3, 23105 + i)
