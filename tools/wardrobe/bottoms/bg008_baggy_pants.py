"""Baggy Pants: roomy trousers that balloon over the thigh and gather into a wrapped band at the ankle,
a knotted cloth belt and open-toe sandals: the genin who trains in borrowed clothes."""
from kit_academy import leg_cloth, waist
from kit_shinobi import sandals
from paint import k, solid

META = {"name": "Baggy Pants", "gender": "unisex",
        "description": "Roomy trousers ballooning over the thigh, gathered at the ankle, a knotted cloth belt.",
        "tags": ["shinobi", "genin"]}


def build(g):
    waist(g, "K", "weave", 31505)
    leg_cloth(g, "K", "weave", 31506, (0, 9))
    for side in ("right", "left"):
        leg = g.part(f"{side}_leg")
        leg.strip.hline(0, leg.strip.w - 1, 9, "S3")
    sandals(g)
    for side, bone in (("right", "RIGHT_LEG"), ("left", "LEFT_LEG")):
        balloon = g.piece(f"{side}_balloon", bone, (-2.5, 2.0, -2.5), (5, 6, 5))
        solid(balloon, "K", "weave", 31508 + (side == "left"), 2)
        for face in balloon.sides:
            face.hline(0, face.w - 1, 0, "K3")
            face.vline(face.w // 2, 1, 5, "K1")
        cuff = g.piece(f"{side}_ankle_band", bone, (-2.3, 8.2, -2.3), (5, 2, 5), scale=(.92, 1, .92))
        solid(cuff, "S", "plain", 31510, 3, edge=False)
        for face in cuff.sides:
            face.hline(0, face.w - 1, 1, "S2")
    belt = g.piece("waist_belt", "TORSO", (-4.6, 9.2, -2.6), (9, 1, 5), inflate=.06)
    solid(belt, "A", "weave", 31511, 2, edge=False)
    knot = g.piece("waist_knot", "TORSO", (0, 0, 0), (1, 2, 1), pivot=(-2.6, 9.4, -2.9), rotation=(0, 0, 12),
                   motion="flap_front")
    solid(knot, "A", "weave", 31512, 2)
    knot.front.set(0, 1, k("A", 1))
