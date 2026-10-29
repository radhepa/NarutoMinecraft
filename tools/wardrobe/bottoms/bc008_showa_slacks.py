"""Shopkeeper's Slacks: pressed wool slacks with a leather belt, the shop owner's town trousers
from the newer stores along the main street, with polished leather shoes."""
from kit import belt, footwear, legs
from paint import fabric, strip_fabric

META = {"name": "Shopkeeper's Slacks", "gender": "unisex",
        "description": "Pressed wool slacks with a leather belt and polished leather shoes.",
        "tags": ["civilian", "trousers", "casual"]}


def build(g):
    body = g.part("body")
    strip_fabric(body, "D", "twill", 36620, 2, 9, 11)
    fabric(body.bottom, "D", "twill", 36620, 1)
    legs(g, "D", "twill", 36621, rows=(0, 9))
    belt(g, "waist_belt", y=9.2, role="L", height=1, buckle="M")
    footwear(g, "shoe", top=10, role="L", base=1)
