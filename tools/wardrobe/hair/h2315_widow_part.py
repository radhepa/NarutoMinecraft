"""Widow Part: long straight hair parted dead in the centre, falling in two curtains past the
cheeks to the collarbones and in a straight sheet down the back."""
from anime import curtain, ring_shell, sidelocks
from paint import scalp

META = {"name": "Widow Part", "gender": "unisex",
        "description": "Long straight centre-parted hair, curtains past the cheeks and a straight sheet down the back."}


def build(g):
    scalp(g, 23301, side_rows=8, back_rows=8, sideburn=0, part=3)
    hat = ring_shell(g, 23302, side_rows=7, back_rows=8, ring_row=1)
    hat.top.vline(3, 0, 7, "H0"), hat.top.vline(4, 0, 7, "H3")
    curtain(g, "sheet", (0, -4.0, 4.6), (6, 0, 0), 8, 10, hem=((1, 2, 2), (5, 2, 2)), seed=23305)
    sidelocks(g, "curtain", 11, seed=23310, x=4.3, z=-3.3, flare=3, width=2)
