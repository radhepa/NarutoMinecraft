"""Mesh Shorts Boots: fitted shorts with a split hem, chain-mesh tights below them and short
lace-up boots to the shin, a thin low belt with a pouch."""
from kit import footwear, pouch
from kit_shinobi import mesh
from paint import fabric, solid, strip_fabric

META = {"name": "Mesh Shorts Boots", "gender": "unisex",
        "description": "Fitted split-hem shorts, mesh tights, short lace-up boots, a low belt with a pouch.",
        "tags": ["shinobi"]}


def build(g):
    body = g.part("body")
    strip_fabric(body, "P", "plain", 33740, 2, 9, 11)
    fabric(body.bottom, "P", "plain", 33740, 1)
    for side in ("right", "left"):
        leg = g.part(f"{side}_leg")
        strip_fabric(leg, "P", "plain", 33741, 2, 0, 1)
        fabric(leg.top, "P", "plain", 33741, 2)
        strip_fabric(leg, "K", "plain", 33742, 1, 2, 7)
        mesh(leg.strip, 0, 2, 15, 7, "K3")
        (leg.right if side == "right" else leg.left).set(1, 1, "P0")
    footwear(g, "boot", top=7, role="L", base=2)
    for side in ("right", "left"):
        g.part(f"{side}_pants").front.set(1, 8, "S3"), g.part(f"{side}_pants").front.set(2, 9, "S3")
    low = g.piece("waist_belt", "TORSO", (-4.6, 0, -2.6), (9, 1, 5), pivot=(0, 10.0, 0), inflate=.1)
    solid(low, "L", "leather", 33743, 2, edge=False)
    pouch(g, "waist_pouch", (3.0, 10.6, -2.3), size=(2, 2, 1), role="L", flap="L3")
