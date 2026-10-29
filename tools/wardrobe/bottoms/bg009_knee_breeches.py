"""Knee Breeches: breeches bloused over a band at the knee, ribbed leg warmers from the knee to the
ankle and open-toe sandals: an old-fashioned cut the Academy still sees on cold mornings."""
from kit_academy import leg_cloth, waist, waist_pouch
from kit_shinobi import sandals
from paint import solid, strip_fabric

META = {"name": "Knee Breeches", "gender": "unisex",
        "description": "Breeches bloused at the knee, ribbed leg warmers to the ankle and open-toe sandals.",
        "tags": ["shinobi", "genin"]}


def build(g):
    waist(g, "S", "twill", 31520)
    leg_cloth(g, "S", "twill", 31521, (0, 5))
    for side, bone in (("right", "RIGHT_LEG"), ("left", "LEFT_LEG")):
        leg, pants = g.part(f"{side}_leg"), g.part(f"{side}_pants")
        strip_fabric(leg, "K", "rib", 31523, 2, 6, 9)
        strip_fabric(pants, "K", "rib", 31524, 2, 6, 9)
        pants.strip.hline(0, pants.strip.w - 1, 6, "K3")
        blouse = g.piece(f"{side}_knee_blouse", bone, (-2.5, 3.6, -2.5), (5, 2, 5))
        solid(blouse, "S", "twill", 31525 + (side == "left"), 2)
        for face in blouse.sides:
            face.hline(0, face.w - 1, 1, "A2")
    sandals(g)
    waist_pouch(g, 31527)
