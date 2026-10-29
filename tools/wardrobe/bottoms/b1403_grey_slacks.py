"""Grey Slacks: the plain straight slacks Kurenai wore after the war, cuffed at the ankle, with tan
leather sandals."""
from kit import legs, waistband
from paint import fabric, strip_fabric

META = {"name": "Grey Slacks", "gender": "unisex",
        "description": "Plain straight slacks cuffed at the ankle, tan leather sandals.", "tags": ["shinobi", "casual"]}


def build(g):
    waistband(g, "D", "twill", 14920)
    for leg in legs(g, "D", "twill", 14921, rows=(0, 9)):
        leg.strip.hline(0, leg.strip.w - 1, 9, "D1")
    # Tan sandals: a leather strap over the instep and a heel, toes bare at the front.
    for side in ("right", "left"):
        leg, pants = g.part(f"{side}_leg"), g.part(f"{side}_pants")
        strip_fabric(leg, "L", "leather", 14922, 3, 10, 11)
        leg.front.set(1, 11, None), leg.front.set(2, 11, None)
        leg.bottom.fill("L1")
        for face in pants.sides:
            face.hline(0, face.w - 1, 11, "L1")
        pants.front.set(1, 11, None), pants.front.set(2, 11, None)
        pants.bottom.fill("L0")
