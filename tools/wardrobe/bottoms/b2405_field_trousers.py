"""Field Medic Trousers: sturdy dark trousers tucked into tall wrapped boots, a holster on the left
thigh carrying a row of three antidote vials, and a leather belt."""
from kit import belt, footwear, legs
from kit_suzuran import vial
from paint import fabric, solid, strip_fabric

META = {"name": "Field Medic Trousers", "gender": "unisex",
        "description": "Dark trousers tucked into tall boots, a thigh holster of three antidote vials, leather belt.",
        "tags": ["shinobi"]}


def build(g):
    body = g.part("body")
    strip_fabric(body, "K", "twill", 24741, 3, 9, 11)
    fabric(body.bottom, "K", "twill", 24741, 2)
    legs(g, "K", "twill", 24742, 3, rows=(0, 6))
    footwear(g, "boot", top=6, role="D", base=2)
    belt(g, "waist_belt", y=9.0, role="L", height=1, buckle="M")
    holster = g.piece("holster", "LEFT_LEG", (-1, 0, -1.5), (1, 4, 3), pivot=(2.2, .6, 0))
    solid(holster, "L", "leather", 24743, 2)
    for i, (z, liquid) in enumerate(((-1.0, "D3"), (0, "S3"), (1.0, "D3"))):
        vial(g, f"vial_{i}", (2.9, .9, z), bone="LEFT_LEG", liquid=liquid, height=4)
