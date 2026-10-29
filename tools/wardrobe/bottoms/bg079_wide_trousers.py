"""Wide Trousers: loose wide-legged trousers in the field cut, unpleated, the hems gathered just above
the ankle with a tie, over open-toe sandals."""
from kit import leg_ring, waistband
from kit_shinobi import sandals
from paint import fabric, k, solid, strip_fabric

META = {"name": "Wide Trousers", "gender": "unisex",
        "description": "Loose wide-legged trousers gathered above the ankle with ties, sandals.",
        "tags": ["shinobi"]}


def build(g):
    waistband(g, "D", "weave", 34760)
    for side, bone, sign in (("right", "RIGHT_LEG", -1), ("left", "LEFT_LEG", 1)):
        leg = g.part(f"{side}_leg")
        strip_fabric(leg, "D", "weave", 34761, 2, 0, 9)
        fabric(leg.top, "D", "weave", 34761, 2)
        wide = g.piece(f"{side}_wide_leg", bone, (-2.6, .4, -2.6), (5, 8, 5), rotation=(0, 0, -3 * sign), inflate=.18)
        solid(wide, "D", "weave", 34762 + (sign > 0), 2)
        for face in wide.sides:
            face.vline(1, 1, 7, k("D", 1)), face.vline(3, 2, 7, k("D", 3))
        wide.bottom.fill(k("D", 0))
    sandals(g)
    leg_ring(g, "ankle_tie", 8.6, "S", 3, size=(5, 1, 5), inflate=.05)
