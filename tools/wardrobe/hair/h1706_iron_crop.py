"""Iron Crop: a short, blunt crop cut in one straight line across the brow and level round the
ears, heavy and square."""
from anime import ring_shell
from kit_morino import nape_hem
from paint import scalp


META = {"name": "Iron Crop", "gender": "unisex",
        "description": "Short blunt crop cut straight across the brow and level round the ears."}


def build(g):
    nape_hem(g, 17055, y=-2.4)
    scalp(g, 17051, side_rows=5, back_rows=6, sideburn=1)
    hat = ring_shell(g, 17052, side_rows=5, back_rows=6, ring_row=1)
    hat.front.hline(0, 7, 0, "H3")
    hat.front.hline(0, 7, 1, "H2")
    hat.front.hline(0, 7, 2, "H1")
