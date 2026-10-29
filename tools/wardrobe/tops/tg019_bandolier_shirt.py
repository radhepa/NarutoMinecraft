"""Bandolier Shirt: a short-sleeved button shirt with a leather bandolier slung from the right shoulder
to the left hip, three small pouches riding on it: the genin who packs for every mission."""
from kit_academy import shirt
from paint import k, solid

META = {
    "name": "Bandolier Shirt",
    "gender": "unisex",
    "description": "Short-sleeved button shirt with a leather bandolier across the chest carrying three pouches.",
    "tags": ["shinobi", "genin"],
    "tucked": True,
}

SLING = dict(pivot=(0, 4.6, -2.45), rotation=(0, 0, 38))


def build(g):
    body, arms = shirt(g, "P", "twill", 31270, sleeve=3)
    f = body.front
    f.vline(4, 0, 11, "P3"), f.vline(3, 1, 11, "P1")
    for y in (2, 5, 8):
        f.set(4, y, "M3")
    f.set(2, 0, "P3"), f.set(5, 0, "P3"), f.clear(3, 0), f.clear(4, 0)
    for arm in arms:
        arm.strip.hline(0, arm.strip.w - 1, 3, "P3")
        arm.strip.hline(0, arm.strip.w - 1, 2, "P1")
    strap = g.piece("bandolier", "TORSO", (-.5, -7, -.5), (1, 14, 1), **SLING)
    solid(strap, "L", "leather", 31271, 2, edge=False)
    back = g.piece("bandolier_back", "TORSO", (-.5, -7, -.5), (1, 14, 1), pivot=(0, 4.6, 2.45), rotation=(0, 0, -38))
    solid(back, "L", "leather", 31272, 2, edge=False)
    for i, t in enumerate((-3.2, -.8, 1.6)):
        pouch = g.piece(f"bandolier_pouch_{i}", "TORSO", (-1, t, -1.6), (2, 2, 1), **SLING)
        solid(pouch, "L", "leather", 31273 + i, 3)
        pouch.front.set(0, 0, k("L", 4)), pouch.front.set(1, 0, k("L", 4))
