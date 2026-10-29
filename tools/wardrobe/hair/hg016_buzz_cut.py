"""Buzz Cut: hair clipped to an even short pile all over, a crisp squared hairline at the brow and the
temples: the jonin who stopped bothering."""
from anime import cel_box
from paint import scalp

META = {"name": "Buzz Cut", "gender": "unisex",
        "description": "Even short pile all over with a crisp squared hairline."}


def build(g):
    scalp(g, 32880, side_rows=4, back_rows=7, sideburn=1, base=1)
    pile = g.piece("pile", "HEAD", (-4, 0, -4), (8, 1, 8), pivot=(0, -8.0, 0), inflate=.12)
    cel_box(pile, 32881, base=1, top_delta=1, clump=4)
