"""Ranger Boots: trousers tucked into tall leather boots laced from the ankle to below the knee, a
knife strapped to the outside of the right boot and a buckled belt: for long marches over rock."""
from kit import belt, legs, waistband
from kit_rugged import soft_boots
from paint import solid

META = {"name": "Ranger Boots", "gender": "unisex",
        "description": "Trousers tucked into tall laced leather boots, a knife strapped to the right boot, a belt.",
        "tags": ["shinobi"]}


def build(g):
    waistband(g, "P", "twill", 35470, 2)
    legs(g, "P", "twill", 35471, 2, rows=(0, 4), crease=False)
    soft_boots(g, top=4, role="L", base=2, laces="S3")
    for side, bone in (("right", "RIGHT_LEG"), ("left", "LEFT_LEG")):
        cuff = g.piece(f"{side}_boot_top", bone, (-2.5, 3.6, -2.5), (5, 1, 5))
        solid(cuff, "L", "leather", 35472 + (side == "left"), 3, edge=False)
    hilt = g.piece("boot_knife", "RIGHT_LEG", (0, 0, 0), (1, 4, 1), pivot=(-2.9, 4.6, -.5))
    solid(hilt, "K", "leather", 35474, 2)
    hilt.top.fill("M3")
    belt(g, "waist_belt", y=9.4, role="L", height=1, buckle="M")
