"""Smith's Trousers: heavy twill trousers with leather spats strapped over the shins against the
sparks, and stout leather work shoes."""
from kit import footwear
from paint import fabric, k, strip_fabric

META = {"name": "Smith's Trousers", "gender": "unisex",
        "description": "Heavy twill trousers with strapped leather spats over the shins, leather work shoes.",
        "tags": ["civilian", "trousers", "work"]}


def build(g):
    body = g.part("body")
    strip_fabric(body, "D", "twill", 36815, 2, 9, 11)
    fabric(body.bottom, "D", "twill", 36815, 1)
    for side in ("right", "left"):
        leg = g.part(f"{side}_leg")
        strip_fabric(leg, "D", "twill", 36816 + (side == "left"), 2, 0, 9)
        fabric(leg.top, "D", "twill", 36816, 2)
    footwear(g, "boot", top=5, role="L", base=2)
    for side in ("right", "left"):
        pants = g.part(f"{side}_pants")
        for face in pants.sides:
            face.hline(0, face.w - 1, 7, k("K", 2))
            face.hline(0, face.w - 1, 9, k("K", 2))
        pants.front.set(0, 7, "M3"), pants.front.set(0, 9, "M3")
