"""Ranger Boots: plain trousers tucked into tall soft leather boots that reach the knee, folded over
in a cuff at the top and strapped at the ankle: for long marches off the roads."""
from kit import footwear, leg_ring
from kit_field import trousers
from paint import k, solid

META = {"name": "Ranger Boots", "gender": "unisex",
        "description": "Trousers tucked into tall soft leather boots with a folded cuff and an ankle strap.",
        "tags": ["shinobi"]}


def build(g):
    trousers(g, "D", 32560, length=4)
    footwear(g, "boot", top=5)
    for ring in leg_ring(g, "boot_cuff", 4.4, "L", 2, (5, 2, 5), "leather"):
        for face in ring.sides:
            face.hline(0, face.w - 1, 0, k("L", 3))
    for side, bone in (("right", "RIGHT_LEG"), ("left", "LEFT_LEG")):
        band = g.piece(f"{side}_ankle_strap", bone, (-2.45, 9.0, -2.45), (5, 1, 5))
        solid(band, "K", "leather", 32563, 2, edge=False)
        band.front.set(2, 0, "M3")
