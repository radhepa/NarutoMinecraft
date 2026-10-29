"""Rolled Trousers: work trousers rolled to just below the knee, bare shins, pale split-toe tabi and
straw sandals, a cloth tie at the waist: how the river crossers and paddy shinobi dress."""
from kit import legs, leg_ring, waistband
from kit_rugged import straw_sandals, tabi
from paint import solid

META = {"name": "Rolled Trousers", "gender": "unisex",
        "description": "Trousers rolled to below the knee, bare shins, pale tabi and straw sandals, a cloth waist tie.",
        "tags": ["shinobi", "genin"]}


def build(g):
    waistband(g, "P", "twill", 35340, 2)
    legs(g, "P", "twill", 35341, 2, rows=(0, 5))
    for ring in leg_ring(g, "roll", 5.0, "P", 3, (5, 2, 5), "twill"):
        for face in ring.sides:
            face.hline(0, face.w - 1, 0, "P4"), face.hline(0, face.w - 1, 1, "P1")
    tabi(g, rows=(8, 11))
    straw_sandals(g)
    for side in ("right", "left"):
        leg = g.part(f"{side}_leg")
        leg.strip.hline(0, leg.strip.w - 1, 8, "S2")
    tie = g.piece("waist_tie", "TORSO", (-4.5, 9.4, -2.5), (9, 1, 5), inflate=.15)
    solid(tie, "S", "weave", 35343, 2, edge=False)
