"""Kennel Boots: sturdy trousers tucked into tall leather boots turned down at the top in a cuff of
fur, a leather belt with a hanging lead clip: for mud, snow and long days at the kennels."""
from kit import footwear, legs, waistband
from kit_inuzuka import fur_box
from paint import solid

META = {"name": "Kennel Boots", "gender": "unisex",
        "description": "Trousers tucked into tall leather boots with fur-cuffed tops, a belt with a lead clip.",
        "tags": ["shinobi"]}


def build(g):
    waistband(g, "D", "twill", 8810, 2)
    legs(g, "D", "twill", 8811, 2, rows=(0, 5))
    footwear(g, "boot", top=5, role="L", base=2)
    for side, bone in (("right", "RIGHT_LEG"), ("left", "LEFT_LEG")):
        cuff = g.piece(f"{side}_fur_cuff", bone, (-2.5, 4.6, -2.5), (5, 2, 5))
        fur_box(cuff, "S", 8813 + (side == "left"), 2)
    belt = g.piece("waist_belt", "TORSO", (-4.6, 9.4, -2.6), (9, 1, 5), inflate=.08)
    solid(belt, "L", "leather", 8815, 2, edge=False)
    belt.front.set(4, 0, "M3")
    clip = g.piece("waist_clip", "TORSO", (0, 0, 0), (1, 2, 1), pivot=(3.6, 9.6, -2.9))
    solid(clip, "M", "plain", 8816, 3, edge=False)
