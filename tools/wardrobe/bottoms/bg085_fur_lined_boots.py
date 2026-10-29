"""Fur-Lined Boots: heavy trousers tucked into tall leather boots lined with fur that spills over the
tops, laced up the front, a wide belt with a hanging horn flask: for the snow line."""
from kit import belt, legs, waistband
from kit_rugged import shag_box, soft_boots
from paint import solid

META = {"name": "Fur-Lined Boots", "gender": "unisex",
        "description": "Heavy trousers tucked into tall laced leather boots with fur spilling over the tops, a flask.",
        "tags": ["shinobi"]}


def build(g):
    waistband(g, "D", "twill", 35350, 2)
    legs(g, "D", "twill", 35351, 2, rows=(0, 6))
    soft_boots(g, top=6, role="L", laces="S2")
    for side, bone in (("right", "RIGHT_LEG"), ("left", "LEFT_LEG")):
        cuff = g.piece(f"{side}_fur_top", bone, (-2.5, 5.2, -2.5), (5, 2, 5))
        shag_box(cuff, "S", 35352 + (side == "left"), 2)
        sole = g.piece(f"{side}_boot_sole", bone, (-2.2, 11.2, -2.4), (4, 1, 5), inflate=.08)
        solid(sole, "K", "leather", 35354, 2, edge=False)
    belt(g, "waist_belt", y=9.2, role="L", height=2, buckle="M")
    flask = g.piece("waist_flask", "TORSO", (0, 0, 0), (2, 3, 2), pivot=(3.4, 10.0, -1.0))
    solid(flask, "L", "leather", 35355, 3)
    flask.top.fill("K2")
