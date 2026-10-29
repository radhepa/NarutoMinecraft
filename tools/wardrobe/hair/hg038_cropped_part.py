"""Cropped Part: a very short, even crop with a sharp side part and a squared hairline, nothing to
grab in a fight: a gate guard's or a weapons master's cut, and one that looks right going grey."""
from anime import cel_box, ring_shell
from kit_kurama import part_line
from paint import scalp

META = {"name": "Cropped Part", "gender": "unisex",
        "description": "A very short even crop with a sharp side part and a squared hairline."}


def build(g):
    scalp(g, 34900, side_rows=3, back_rows=5, sideburn=1, part=5, shadow=False)
    hat = ring_shell(g, 34901, side_rows=2, back_rows=4, ring_row=0)
    part_line(g, 5)
    hat.front.hline(0, 7, 0, "H3")
    for x in (0, 7):
        hat.front.set(x, 1, "H1")
    crown = g.piece("crop_crown", "HEAD", (-4, -8.6, -4), (8, 1, 8), inflate=.3)
    cel_box(crown, 34903, base=2, top_delta=1, clump=2)
