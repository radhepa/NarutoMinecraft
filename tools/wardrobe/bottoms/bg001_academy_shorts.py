"""Academy Shorts: plain knee shorts with a turned-up hem and a pouch at the back of the waist, worn
with bare shins and open-toe sandals: what every Academy student runs about in."""
from kit_academy import leg_cloth, turned_hem, waist, waist_pouch
from kit_shinobi import sandals

META = {"name": "Academy Shorts", "gender": "unisex",
        "description": "Plain knee shorts with a turned-up hem, a waist pouch and open-toe sandals.",
        "tags": ["shinobi", "genin"]}


def build(g):
    waist(g, "D", "twill", 31400)
    for side, leg in zip(("right", "left"), leg_cloth(g, "D", "twill", 31401, (0, 4))):
        leg.front.vline(1 if side == "right" else 2, 1, 4, "D3")
    turned_hem(g, "hem", 4.4, "D", 31403, height=2)
    sandals(g)
    waist_pouch(g, 31405)
