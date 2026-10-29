"""Rookie Jacket: a cropped short-sleeved jacket in steel grey left open over a mesh tee, a single
needle strap slung across the back and a dusky cloth band tied round the right upper arm."""
from kit_shinobi import mesh
from kit_shiranui import bandolier
from paint import cap, fabric, solid, strip_fabric

META = {
    "name": "Rookie Jacket",
    "gender": "unisex",
    "description": "Cropped short-sleeved steel jacket open over a mesh tee, a needle strap across the back.",
    "tags": ["shinobi", "genin"],
}


def build(g):
    body, jacket = g.part("body"), g.part("jacket")
    strip_fabric(body, "K", "weave", 16850, 2)
    mesh(body.front, 0, 0, 7, 8, "K3")
    cap(body, "K", seed=16850)
    strip_fabric(jacket, "P", "twill", 16851, 2, 0, 7)
    cap(jacket, "P", texture="twill", seed=16851)
    for y in range(8):
        for x in (3, 4):
            jacket.front.clear(x, y)
        jacket.front.set(2, y, "P3"), jacket.front.set(5, y, "P1")
    jacket.strip.hline(0, jacket.strip.w - 1, 7, "P1")
    bandolier(jacket.back, "L", rows=8, mirror=True)
    for side in ("right", "left"):
        sleeve = g.part(f"{side}_sleeve")
        strip_fabric(sleeve, "P", "twill", 16852 + (side == "left"), 2, 0, 3)
        fabric(sleeve.top, "P", "twill", 16852, 3)
        sleeve.strip.hline(0, sleeve.strip.w - 1, 3, "P1")
    knot = g.piece("arm_cloth", "RIGHT_ARM", (-3.45, 4.0, -2.45), (5, 1, 5))
    solid(knot, "D", "weave", 16854, 2)
