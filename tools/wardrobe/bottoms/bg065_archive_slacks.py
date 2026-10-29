"""Archive Slacks: narrow dark slacks gathered at the ankle over split-toe socks and straw sandals,
a cloth sash knotted at the hip: quiet clothes for long days among the shelves."""
from kit import belt, legs, waistband
from kit_hyuga import tabi
from paint import solid

META = {"name": "Archive Slacks", "gender": "unisex",
        "description": "Narrow dark slacks gathered at the ankle, cloth sash knotted at the hip, tabi and sandals.",
        "tags": ["shinobi"]}


def build(g):
    waistband(g, "K", "twill", 34480)
    legs(g, "K", "twill", 34481, rows=(0, 8), crease=False)
    tabi(g, "S", "K1", "K2")
    for side in ("right", "left"):
        g.part(f"{side}_leg").strip.hline(0, 15, 8, "K1")
    belt(g, "waist_sash", y=9.0, role="S", height=1, buckle=None, inflate=.12)
    knot = g.piece("waist_sash_knot", "TORSO", (-.5, 0, -.5), (1, 3, 1), pivot=(-3.6, 9.4, -2.9), rotation=(0, 0, -8),
                   motion="sway")
    solid(knot, "S", "weave", 34483, 2)
