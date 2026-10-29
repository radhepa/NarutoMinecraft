"""Merchant's Slick: short hair oiled flat and combed from a side parting, one lock swept across
the top of the brow, neat at the ears and the nape for the shop counter."""
from anime import lock, ring_shell
from paint import scalp

META = {"name": "Merchant's Slick", "gender": "unisex",
        "description": "Short oiled hair combed from a side parting, one lock swept across the brow."}


def build(g):
    scalp(g, 36988, side_rows=4, back_rows=6, sideburn=2, part=2)
    ring_shell(g, 36989, side_rows=3, back_rows=5, ring_row=0)
    lock(g, "sweep", (-2.4, -8.5, -4.35), (-8, 0, -72), ((3, 3), (2, 2), (1, 1)), 1, 36990, ring=0)
