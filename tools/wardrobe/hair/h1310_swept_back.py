"""Swept Back: combed hard back from the brow and behind the ears, flat and glossy, the ends
turning up in short points at the nape: a statesman's look for the clan's advisers."""
from anime import cel_box, ring_shell, spike
from paint import scalp

META = {"name": "Swept Back", "gender": "unisex",
        "description": "Combed hard back from the brow, flat and glossy, ends turning up in short points at the nape."}


def build(g):
    scalp(g, 13297, side_rows=4, back_rows=7, sideburn=2)
    ring_shell(g, 13298, side_rows=4, back_rows=7, ring_row=0)
    crown = g.piece("crown", "HEAD", (-4.5, -8.5, -4.2), (9, 1, 9))
    cel_box(crown, 13298, ring=0, clump=2)
    brow = g.piece("brow_roll", "HEAD", (-4, -9, -4.6), (8, 2, 2))
    cel_box(brow, 13299, ring=0, clump=2)
    for i, (x, rz) in enumerate(((-2.6, -16), (0, 0), (2.6, 16))):
        spike(g, f"nape_flick_{i}", (x, -1.2, 4.3), (-34, 0, rz), ((3, 1), (2, 1), (1, 1)), 1, 13303 + i)
