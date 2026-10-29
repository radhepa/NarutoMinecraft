"""Tabi Trousers: slim trousers tucked into soft split-toe tabi boots that lace up the shin, the boots
fastened with a row of hooks at the back: quiet feet for a genin learning stealth."""
from kit_academy import leg_cloth, waist, waist_pouch
from paint import fabric, strip_fabric

META = {"name": "Tabi Trousers", "gender": "unisex",
        "description": "Slim trousers tucked into split-toe tabi boots that lace up the shin.",
        "tags": ["shinobi", "genin"]}


def build(g):
    waist(g, "D", "twill", 31595)
    for side, leg in zip(("right", "left"), leg_cloth(g, "D", "twill", 31596, (0, 6))):
        leg.front.vline(1 if side == "right" else 2, 1, 5, "D3")
    for side in ("right", "left"):
        leg, pants = g.part(f"{side}_leg"), g.part(f"{side}_pants")
        strip_fabric(leg, "K", "smooth", 31598, 2, 7, 11)
        for face in pants.sides:
            fabric(face, "K", "smooth", 31599, 2, 0, 7, face.w, 5)
            face.hline(0, face.w - 1, 7, "K3")
            face.hline(0, face.w - 1, 11, "K0")
        pants.back.vline(1, 8, 10, "M3"), pants.back.vline(2, 8, 10, "M2")
        pants.front.vline(1, 8, 11, "K0")
        leg.front.vline(1, 11, 11, "K0")
        leg.bottom.fill("K0"), pants.bottom.fill("K0")
    waist_pouch(g, 31601, x=.5)
