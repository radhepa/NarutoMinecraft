"""Wrapped Hakama: a short travelling hakama ending at mid-calf, the shins below bound tight in pale
leg wraps down to straw sandals, the waist ties knotted at the front: a road-worn take on formal
dress that works with anything."""
from kit import legs, waistband
from kit_rugged import baggy_legs, leg_wraps, straw_sandals
from paint import solid

META = {"name": "Wrapped Hakama", "gender": "unisex",
        "description": "Short pleated hakama to mid-calf over tight pale leg wraps, straw sandals, front waist ties.",
        "tags": ["shinobi", "hakama"]}


def build(g):
    waistband(g, "P", "twill", 35320, 2)
    legs(g, "P", "twill", 35321, 2, rows=(0, 6), crease=False)
    baggy_legs(g, "hakama", "P", 35322, top=0.0, length=7, flare=5)
    leg_wraps(g, 7, 10)
    straw_sandals(g)
    tie = g.piece("waist_tie", "TORSO", (-4.5, 0, -2.5), (9, 1, 5), pivot=(0, 9.3, 0), inflate=.2)
    solid(tie, "P", "weave", 35324, 3, edge=False)
    knot = g.piece("waist_knot", "TORSO", (-1, 0, 0), (2, 2, 1), pivot=(0, 9.2, -2.9))
    solid(knot, "P", "weave", 35325, 3, edge=False)
    board = g.piece("waist_board", "TORSO", (-2.5, 0, 0), (5, 2, 1), pivot=(0, 9.0, 2.3))
    solid(board, "P", "twill", 35326, 2)
