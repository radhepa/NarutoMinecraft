"""Dungaree Shorts: the bottom half of a pair of dungarees, sturdy knee shorts with a rolled hem, side
buttons and a hammer loop. One garment with the Dungaree Bib and always worn with it."""
from kit_academy import leg_cloth, turned_hem, waist
from kit_shinobi import sandals
from paint import solid

META = {"name": "Dungaree Shorts", "gender": "unisex",
        "description": "Dungaree knee shorts with a rolled hem, side buttons and a hammer loop.",
        "tags": ["shinobi", "genin"], "locked_to": "tg020_dungaree_bib"}


def build(g):
    body = waist(g, "D", "twill", 31685, band="D2")
    for face in (body.right, body.left):
        face.set(1, 9, "M3")
    for side, leg in zip(("right", "left"), leg_cloth(g, "D", "twill", 31686, (0, 4))):
        leg.front.vline(1 if side == "right" else 2, 1, 4, "D3")
    turned_hem(g, "roll", 4.2, "D", 31688, height=2, base=3)
    sandals(g)
    loop = g.piece("hammer_loop", "LEFT_LEG", (0, 0, 0), (1, 3, 1), pivot=(2.1, .6, -.5))
    solid(loop, "D", "twill", 31690, 3)
