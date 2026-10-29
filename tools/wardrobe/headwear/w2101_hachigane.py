"""Hachigane: the old iron brow guard the clan is named for, a riveted steel plate tied across the
forehead on a rust cloth band, its tails hanging at the back; worn over the hair."""
from kit_hagane import plate
from paint import solid

META = {"name": "Hachigane", "gender": "unisex",
        "description": "A riveted steel brow plate tied across the forehead on a rust cloth band."}


def build(g):
    band = g.piece("band", "HEAD", (-4, -7.6, -4), (8, 1, 8), inflate=.6)
    solid(band, "A", "weave", 21997, 2, edge=False)
    brow = g.piece("brow_plate", "HEAD", (-3.5, -1, -.5), (7, 2, 1), pivot=(0, -7.1, -4.55))
    solid(brow, "M", "plain", 21998, 2, edge=False)
    plate(brow.front, 0, 0, 7, 2)
    for x in (0, 6):
        brow.front.set(x, 0, "M4"), brow.front.set(x, 1, "K1")
    brow.front.vline(3, 0, 1, "M1")
    knot = g.piece("knot", "HEAD", (-1, -1, 0), (2, 2, 1), pivot=(0, -7.1, 4.6))
    solid(knot, "A", "weave", 21999, 2)
    for i, (x, rz) in enumerate(((-.6, 14), (.6, -10))):
        tail = g.piece(f"tail_{i}", "HEAD", (-.5, 0, 0), (1, 5, 1), pivot=(x, -6.4, 4.9), rotation=(22, 0, rz),
                       motion="sway")
        solid(tail, "A", "weave", 21999, 2)
