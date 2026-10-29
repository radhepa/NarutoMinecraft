"""Greave Boots: gunmetal trousers tucked into tall leather boots with steel greaves riveted over
the shins, a leather belt with a short length of chain at the hip: heavy gear for the clan's
seniors."""
from kit import footwear, legs, waistband
from kit_hagane import shin_guards
from paint import solid

META = {"name": "Greave Boots", "gender": "unisex",
        "description": "Gunmetal trousers in tall leather boots with riveted steel greaves, a belt with a chain.",
        "tags": ["shinobi"]}


def build(g):
    waistband(g, "P", "twill", 21992, 2)
    legs(g, "P", "twill", 21993, 2, rows=(0, 5))
    footwear(g, "boot", top=5, role="L", base=2)
    shin_guards(g, top=4.6, height=6, seed=21994, strap="L")
    belt = g.piece("waist_belt", "TORSO", (-4.6, 9.4, -2.6), (9, 1, 5), inflate=.08)
    solid(belt, "L", "leather", 21995, 2, edge=False)
    belt.front.set(4, 0, "M3")
    for i in range(3):
        link = g.piece(f"waist_chain_{i}", "TORSO", (0, 0, 0), (1, 1, 1), pivot=(3.4 + (i % 2) * .4, 10.4 + i, -2.9))
        solid(link, "M", "plain", 21995, 3, edge=False)
