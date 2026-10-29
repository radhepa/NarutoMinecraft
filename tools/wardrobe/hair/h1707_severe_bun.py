"""Severe Bun: every strand dragged back into a hard, flat knot low on the back of the head, held
by a steel pin pushed through it."""
from anime import cel_box, tie
from kit_morino import combed_back
from paint import solid

META = {"name": "Severe Bun", "gender": "unisex",
        "description": "Dragged back into a hard flat knot low on the back of the head, a steel pin through it."}


def build(g):
    combed_back(g, 17061, side_rows=4, back_rows=7, sideburn=0)
    tie(g, "bun_tie", (0, -4.6, 4.5), (0, 0, 0), (3, 1, 2), y=-.5)
    bun = g.piece("bun", "HEAD", (-2, -2, 0), (4, 3, 2), pivot=(0, -4.2, 4.9))
    cel_box(bun, 17062, ring=1)
    pin = g.piece("pin", "HEAD", (-3.5, -.5, -.5), (7, 1, 1), pivot=(0, -4.4, 6.0), rotation=(0, 0, -18))
    solid(pin, "M", "plain", 17063, 3)
