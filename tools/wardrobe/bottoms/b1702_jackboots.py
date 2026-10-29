"""Jackboots: black trousers under knee-high black jackboots, stiff shafts with a steel-capped toe,
a black belt with a steel buckle at the waist."""
from kit import belt, legs, waistband
from kit_morino import heavy_boots

META = {"name": "Jackboots", "gender": "unisex",
        "description": "Black trousers under knee-high stiff black jackboots with steel-capped toes.",
        "tags": ["shinobi"]}


def build(g):
    waistband(g, "K", "twill", 17411)
    legs(g, "K", "twill", 17412, rows=(0, 4))
    heavy_boots(g, top=4, strap="K", seed=17414)
    for side in ("right", "left"):
        pants = g.part(f"{side}_pants")
        pants.front.hline(0, 3, 10, "M2")
    belt(g, "waist_belt", y=9.4, role="K", buckle="M")
