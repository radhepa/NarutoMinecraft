"""Greaved Trousers: plain field trousers with steel greaves strapped over the shins and round knee
caps, the hems tucked down into open sandals and a buckled belt: for shinobi who block kicks with
their legs."""
from kit import belt, legs, waistband
from kit_rugged import shin_guard
from kit_shinobi import sandals

META = {"name": "Greaved Trousers", "gender": "unisex",
        "description": "Field trousers with strapped steel greaves and knee caps, open sandals, a buckled belt.",
        "tags": ["shinobi", "armor"]}


def build(g):
    waistband(g, "P", "twill", 35330, 2)
    legs(g, "P", "twill", 35331, 2, rows=(0, 9))
    for side in ("right", "left"):
        g.part(f"{side}_leg").strip.hline(0, 15, 9, "P1")
    shin_guard(g, "greave", "M", 35332, top=5.0, length=4, strap="L1", knee=True, texture="plain")
    sandals(g)
    belt(g, "waist_belt", y=9.4, role="L", height=1, buckle="M")
