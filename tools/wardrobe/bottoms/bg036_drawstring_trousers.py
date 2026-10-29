"""Drawstring Trousers: loose trousers gathered at the waist by a drawcord in the accent colour, its
ends hanging at the front, the legs tied close at the ankle above open-toe sandals."""
from kit import leg_ring
from kit_field import trousers
from kit_shinobi import sandals
from paint import k, solid

META = {"name": "Drawstring Trousers", "gender": "unisex",
        "description": "Loose trousers with an accent drawcord at the waist, tied close at the ankle, sandals.",
        "tags": ["shinobi"]}


def build(g):
    trousers(g, "D", 32700, length=9, texture="weave")
    for side in ("right", "left"):
        leg = g.part(f"{side}_leg")
        for x in (0, 5, 10, 14):
            leg.strip.vline(x, 1, 7, k("D", 1))
    for ring in leg_ring(g, "ankle_tie", 8.4, "D", 2, (5, 1, 5), "weave"):
        for face in ring.sides:
            face.hline(0, face.w - 1, 0, k("A", 2))
    sandals(g)
    for i, (x, rz) in enumerate(((-.6, 6), (.6, -6))):
        cord = g.piece(f"waist_cord_{i}", "TORSO", (-.5, 0, -.5), (1, 3, 1), pivot=(x, 9.6, -2.4), rotation=(0, 0, rz),
                       scale=(.5, 1, .5), motion="sway")
        solid(cord, "A", "plain", 32703 + i, 2)
