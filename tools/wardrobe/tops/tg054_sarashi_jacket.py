"""Sarashi Jacket: a chest wrap of pale binding under a short sleeveless jacket that falls open,
the jacket's hem cut on a slant, bandaged upper arms and a cord belt."""
from kit_kunoichi import obi
from kit_shinobi import bandage
from paint import fabric, strip_fabric

META = {
    "name": "Sarashi Jacket",
    "gender": "unisex",
    "description": "Pale chest binding under a short open sleeveless jacket, bandaged arms, cord belt.",
    "tags": ["shinobi", "chunin"],
}


def build(g):
    body, jacket = g.part("body"), g.part("jacket")
    bandage(body.strip, 0, 1, body.strip.w - 1, 6)
    fabric(body.top, "S", "plain", 33260, 3)
    strip_fabric(jacket, "P", "weave", 33261, 2, 0, 8)
    fabric(jacket.top, "P", "weave", 33261, 3)
    for y in range(9):
        for x in range(2, 6):
            jacket.front.clear(x, y)
        jacket.front.set(1, y, "P3"), jacket.front.set(6, y, "P1")
    for x in range(jacket.strip.w):
        jacket.strip.set(x, 8, "P1")
    jacket.front.clear(1, 8), jacket.front.clear(6, 8)
    for side in ("right", "left"):
        arm = g.part(f"{side}_arm")
        bandage(arm.strip, 0, 1, arm.strip.w - 1, 4)
    obi(g, "cord_belt", y=9.6, role="S", height=1, knot="side", seed=33263)
