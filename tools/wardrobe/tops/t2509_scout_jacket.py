"""Scout Jacket: a short, close-fitting zip jacket for genin on night patrol, a high standing collar
zipped to the chin, the hood worn down, a slanted chest pocket, grey cuffs and the lantern charm
clipped to the belt."""
from kit import belt, collar, sleeves
from kit_tobari import hood_down, lantern
from paint import cap, strip_fabric

META = {
    "name": "Scout Jacket",
    "gender": "unisex",
    "description": "Short zip jacket, a high zipped collar, the hood down, a chest pocket, grey cuffs, a lantern charm.",
    "tags": ["shinobi", "genin"],
}


def build(g):
    for layer, seed in (("body", 25540), ("jacket", 25541)):
        box = g.part(layer)
        strip_fabric(box, "P", "plain", seed, 2)
        cap(box, "P", seed=seed)
    jacket = g.part("jacket")
    jacket.front.vline(4, 0, 10, "M3"), jacket.front.vline(3, 0, 10, "P0")
    jacket.strip.hline(0, jacket.strip.w - 1, 10, "S2"), jacket.strip.hline(0, jacket.strip.w - 1, 11, "S1")
    for x, y in ((5, 3), (6, 2)):
        jacket.front.set(x, y, "P0")
    jacket.front.hline(5, 6, 4, "P1")
    for arm in sleeves(g, "P", "plain", 25542, rows=(0, 11)):
        arm.strip.hline(0, arm.strip.w - 1, 10, "S3"), arm.strip.hline(0, arm.strip.w - 1, 11, "S2")
        arm.strip.hline(0, arm.strip.w - 1, 5, "P1")
    col = collar(g, "collar", "P", "plain", height=3, y=-2.2)
    col.front.vline(4, 0, 2, "M3")
    hood_down(g, "hood", "P", "plain", 25544)
    belt(g, "belt", y=9.8, role="K", height=1)
    lantern(g, "lantern", pivot=(2.6, 10.6, -2.9))
