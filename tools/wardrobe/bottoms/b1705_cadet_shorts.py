"""Cadet Shorts: dark slate shorts to the knee with turned-up cuffs, black leggings and short heavy
lace-up boots: the academy child of an interrogator's house."""
from kit import leg_ring, waistband
from kit_morino import heavy_boots
from paint import fabric, strip_fabric

META = {"name": "Cadet Shorts", "gender": "unisex",
        "description": "Dark slate knee shorts with turned cuffs over black leggings and short heavy boots.",
        "tags": ["shinobi", "genin"]}


def build(g):
    waistband(g, "D", "twill", 17441)
    for side in ("right", "left"):
        leg = g.part(f"{side}_leg")
        strip_fabric(leg, "D", "twill", 17442 + (side == "left"), 2, 0, 3)
        fabric(leg.top, "D", "twill", 17442, 2)
        strip_fabric(leg, "K", "smooth", 17444, 2, 4, 7)
    for ring in leg_ring(g, "cuff", 3.2, "D", 3, size=(5, 1, 5)):
        for face in ring.sides:
            face.hline(0, face.w - 1, 0, "D3")
    heavy_boots(g, top=8, strap="K", seed=17446)
    for side in ("right", "left"):
        pants = g.part(f"{side}_pants")
        pants.front.set(1, 8, "S3"), pants.front.set(2, 9, "S3")
