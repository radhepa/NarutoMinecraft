"""Armorer Coat: the weapons master's sleeveless half-coat over a fitted shirt, two blade
bandoliers crossed on the chest, a short blade slung across the small of the back and steel
forearm guards: the jonin who keeps the village's arsenal and teaches every edge in it."""
from kit_shinobi import tanto
from kit_specialist import bandolier, coat_skirts, shirt
from paint import cap, strip_fabric

META = {
    "name": "Armorer Coat",
    "gender": "unisex",
    "description": "Sleeveless half-coat over a shirt, crossed kunai bandoliers, a blade across the back, steel guards.",
    "tags": ["shinobi", "coat", "jonin"],
}


def build(g):
    shirt(g, "S", "weave", 34380)
    jacket = g.part("jacket")
    strip_fabric(jacket, "P", "twill", 34382, 2)
    cap(jacket, "P", texture="twill", seed=34382)
    for y in range(12):
        for x in range(3, 5):
            jacket.front.clear(x, y)
        jacket.front.set(2, y, "A2"), jacket.front.set(5, y, "A2")
    for side in ("right", "left"):
        sleeve = g.part(f"{side}_sleeve")
        strip_fabric(sleeve, "M", "plain", 34383 + (side == "left"), 2, 6, 10)
        sleeve.strip.hline(0, sleeve.strip.w - 1, 6, "M4"), sleeve.strip.hline(0, sleeve.strip.w - 1, 10, "M1")
        sleeve.strip.hline(0, sleeve.strip.w - 1, 8, "L2")
    bandolier(g, "bandolier_r", "right", blades=3, seed=34385)
    bandolier(g, "bandolier_l", "left", blades=3, seed=34390, face_z=-2.8)
    tanto(g, "back_blade", pivot=(-3.0, 8.4, 2.9), rotation=(0, 0, -80), length=7)
    coat_skirts(g, "coat_skirt", 4, "P", "twill", 34395, edge="A2")
