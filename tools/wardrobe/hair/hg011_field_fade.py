"""Field Fade: sides and nape faded close to the scalp, a short dense layer left on top with a ragged
edge and a few points flicked up at the front hairline, well above the brows."""
from anime import cel_box, ring_shell, spike
from paint import scalp

META = {"name": "Field Fade", "gender": "unisex",
        "description": "Close-faded sides and nape, a short dense top with a few points flicked up at the front."}

FRONT = [(-2.4, -3.2, 22, -16), (-.6, -3.4, 26, -4), (1.2, -3.4, 24, 10), (2.8, -3.0, 20, 20)]


def build(g):
    scalp(g, 32800, side_rows=2, back_rows=4, sideburn=1, base=1)
    ring_shell(g, 32801, side_rows=1, back_rows=2, ring_row=None)
    top = g.piece("top_layer", "HEAD", (-4, -1.4, -4), (8, 2, 8), pivot=(0, -7.6, 0), inflate=.55)
    cel_box(top, 32802, ring=0)
    for i, (x, z, rx, rz) in enumerate(FRONT):
        spike(g, f"front_point_{i}", (x, -8.4, z), (rx, 0, rz), ((2, 1), (1, 1)), 2, 32803 + i)
    for i, (x, z, rx, rz) in enumerate(((-1.8, .6, -12, -18), (1.4, 1.4, -20, 16))):
        spike(g, f"crown_point_{i}", (x, -8.4, z), (rx, 0, rz), ((2, 1), (1, 1)), 2, 32808 + i)
