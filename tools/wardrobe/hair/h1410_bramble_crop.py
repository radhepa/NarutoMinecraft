"""Bramble Crop: a short, practical cut that keeps the clan's wave: tousled curls on top tumbling
forward into a short fringe, the sides and nape kept close."""
from anime import bangs
from kit_yuhi import wave_box, wave_shell
from paint import scalp

META = {"name": "Bramble Crop", "gender": "unisex",
        "description": "Short tousled wavy crop, curls on top tumbling into a short fringe, close sides."}


def build(g):
    scalp(g, 14361, side_rows=4, back_rows=6, sideburn=2)
    wave_shell(g, 14362, side_rows=3, back_rows=5, ring_row=1)
    bangs(g, "fringe", [(-2.6, ((2, 1), (1, 1)), 20), (-.9, ((2, 1), (1, 1)), 6), (.9, ((2, 1), (1, 1)), -8),
                        (2.6, ((2, 1), (1, 1)), -22)], seed=14370)
    # Tousled top: low, offset tufts sitting on the crown.
    for i, (x, z, w, d, rz, rx) in enumerate(((-2.2, -2.0, 3, 3, -12, 8), (1.4, -1.6, 4, 3, 10, -6), (-1.0, 1.2, 4, 3, 6, 10),
                                               (2.0, 2.4, 3, 2, -14, -10), (-2.8, 2.6, 3, 2, 16, 8))):
        tuft = g.piece(f"tuft_{i}", "HEAD", (-w / 2, -2, -d / 2), (w, 2, d), pivot=(x, -8.0, z), rotation=(rx, 0, rz))
        wave_box(tuft, 14380 + i, base=2, ring=0)
