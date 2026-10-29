"""Winter Knit: a calm village look for cold evenings: a soft knitted sweater with a ribbed hem and
cuffs and a long indigo scarf wound twice round the neck, one end down the chest and one behind."""
from paint import cap, fabric, solid, strip_fabric

META = {
    "name": "Winter Knit",
    "gender": "unisex",
    "description": "Soft knitted sweater, ribbed hem and cuffs, a long indigo scarf wound round the neck.",
    "tags": ["shinobi", "genin"],
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "P", "knit", 15790, 2)
    cap(body, "P", texture="knit", seed=15790)
    for y in (10, 11):
        for x in range(body.strip.w):
            body.strip.set(x, y, "P1" if x % 2 else "P3")
    for side in ("right", "left"):
        arm = g.part(f"{side}_arm")
        strip_fabric(arm, "P", "knit", 15791 + (side == "left"), 2, 0, 10)
        fabric(arm.top, "P", "knit", 15791, 3)
        for x in range(arm.strip.w):
            arm.strip.set(x, 10, "P1" if x % 2 else "P3")
    wrap = g.piece("scarf", "TORSO", (-4.5, -1.6, -2.6), (9, 3, 5), inflate=.15)
    solid(wrap, "D", "knit", 15793, 3, edge=False)
    for face in wrap.sides:
        face.hline(0, face.w - 1, 1, "D2")
    front = g.piece("scarf_front", "TORSO", (-1, 0, 0), (2, 7, 1), pivot=(-2.0, 1.2, -3.0), rotation=(0, 0, 4),
                    motion="sway")
    solid(front, "D", "knit", 15794, 3)
    front.front.hline(0, 1, 6, "A2")
    back = g.piece("scarf_back", "TORSO", (-1, 0, -1), (2, 6, 1), pivot=(1.8, 1.2, 3.0), rotation=(0, 0, -6),
                   motion="sway")
    solid(back, "D", "knit", 15795, 3)
    back.back.hline(0, 1, 5, "A2")
