"""Play Shorts: the village children's shorts, sturdy cotton with a patch sewn over a torn seat, an
elastic waist, long socks with a stripe pulled up the shins and scuffed cloth shoes."""
from kit_household import cloth_shoes, socks, trouser_legs, waist
from paint import solid

META = {"name": "Play Shorts", "gender": "unisex",
        "description": "Sturdy short shorts with a patched seat, elastic waist, long striped socks, cloth shoes.",
        "tags": ["civilian", "casual", "shorts"]}


def build(g):
    waist(g, "D", "twill", 37612, band="D1")
    trouser_legs(g, "D", "twill", 37613, rows=(0, 3))
    g.part("left_leg").back.rect(0, 0, 3, 2, "A2")
    g.part("left_leg").back.set(0, 0, "A3")
    socks(g, "S3", rows=(5, 9))
    for side in ("right", "left"):
        leg = g.part(f"{side}_leg")
        leg.strip.hline(0, leg.strip.w - 1, 6, "A2")
    cloth_shoes(g, "L", 2, strap="L3")
    for side, bone in (("right", "RIGHT_LEG"), ("left", "LEFT_LEG")):
        hem = g.piece(f"{side}_hem", bone, (-2.5, 2.6, -2.5), (5, 1, 5))
        solid(hem, "D", "twill", 37615, 2, edge=False)
