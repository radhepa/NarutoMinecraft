"""Dolphin Hoodie: a genin's zip hoodie in the clan color, the hood down on the shoulders, sea-blue
cuffs and drawstrings and the family's leaping dolphin in sand across the back."""
from kit_umino import dolphin
from paint import cap, fabric, solid, strip_fabric

META = {
    "name": "Dolphin Hoodie",
    "gender": "unisex",
    "description": "Zip hoodie with the hood down, sea-blue cuffs and drawstrings, a sand dolphin on the back.",
    "tags": ["shinobi", "genin"],
}


def build(g):
    body, jacket = g.part("body"), g.part("jacket")
    strip_fabric(body, "P", "weave", 18461, 2)
    cap(body, "P", texture="weave", seed=18461)
    strip_fabric(jacket, "P", "weave", 18462, 2)
    cap(jacket, "P", texture="weave", seed=18462)
    f = jacket.front
    f.vline(3, 0, 11, "M3"), f.vline(4, 0, 11, "P1")
    f.set(2, 1, "A3"), f.set(2, 2, "A2"), f.set(5, 1, "A3"), f.set(5, 2, "A2"), f.set(5, 3, "A2")
    f.hline(1, 2, 7, "P1"), f.hline(5, 6, 7, "P1")
    jacket.strip.hline(0, jacket.strip.w - 1, 10, "A2"), jacket.strip.hline(0, jacket.strip.w - 1, 11, "A1")
    for side in ("right", "left"):
        arm, sleeve = g.part(f"{side}_arm"), g.part(f"{side}_sleeve")
        strip_fabric(arm, "P", "weave", 18463, 2, 0, 11)
        fabric(arm.top, "P", "weave", 18463, 3)
        strip_fabric(sleeve, "P", "weave", 18464 + (side == "left"), 2, 0, 11)
        fabric(sleeve.top, "P", "weave", 18464, 3)
        sleeve.strip.hline(0, sleeve.strip.w - 1, 10, "A2"), sleeve.strip.hline(0, sleeve.strip.w - 1, 11, "A1")
    hood = g.piece("hood", "TORSO", (-4, -2, 0), (8, 3, 3), pivot=(0, .6, 2.0), rotation=(-12, 0, 0))
    solid(hood, "P", "weave", 18466, 2)
    hood.top.hline(0, 7, 1, "P0"), hood.top.hline(1, 6, 0, "P1")
    dolphin(g, "back_dolphin", "P", "S3", (0, 3.2, 2.62), seed=18467)
