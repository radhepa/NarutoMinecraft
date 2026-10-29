"""Torune Slick: Torune's close, combed-back hair, flat over the crown and gathered into a short
sheet with a pointed hem at the nape, two fine locks loose at the temples."""
from anime import curtain, ring_shell, sidelocks
from paint import scalp

META = {"name": "Torune Slick", "gender": "unisex",
        "description": "Close combed-back hair, a short pointed sheet at the nape, fine temple locks."}


def build(g):
    scalp(g, 10101, side_rows=4, back_rows=8, sideburn=2)
    hat = ring_shell(g, 10102, side_rows=4, back_rows=8, ring_row=2)
    # Combed lines raked straight back across the crown.
    for x in (1, 4, 6):
        hat.top.vline(x, 0, 7, "H1")
    curtain(g, "nape_sheet", (0, -4.6, 4.45), (6, 0, 0), 8, 3, hem=((0, 3, 2), (3, 2, 3), (5, 3, 2)), seed=10110)
    sidelocks(g, "temple", 5, seed=10120, x=4.35, z=-3.0, flare=5, width=1)
