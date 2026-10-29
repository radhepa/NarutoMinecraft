"""House Trousers: plain straight cotton trousers with a pressed crease, a drawstring waist and a
turned-up cuff above soft cloth shoes; the everyday trousers of the village's men and women."""
from kit_household import cloth_shoes, trouser_legs, waist
from paint import solid

META = {"name": "House Trousers", "gender": "unisex",
        "description": "Straight cotton trousers with a crease, drawstring waist, turned-up cuffs, cloth shoes.",
        "tags": ["civilian", "casual", "trousers"]}


def build(g):
    body = waist(g, "D", "twill", 37564, band="D3")
    body.front.set(3, 10, "S3"), body.front.set(4, 10, "S3")
    trouser_legs(g, "D", "twill", 37565, rows=(0, 9), crease="D3")
    cloth_shoes(g, "K", 2)
    for side, bone in (("right", "RIGHT_LEG"), ("left", "LEFT_LEG")):
        cuff = g.piece(f"{side}_cuff", bone, (-2.5, 8.6, -2.5), (5, 1, 5))
        solid(cuff, "D", "twill", 37567, 3, edge=False)
