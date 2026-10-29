"""Courier Breeches: light knee breeches cut for running, the calves wound in pale wraps down to
the ankle and light open-toe sandals."""
from kit import legs, waistband
from kit_shinobi import sandals
from kit_yamanaka import wrapped
from paint import solid

META = {"name": "Courier Breeches", "gender": "unisex",
        "description": "Light knee breeches, pale calf wraps to the ankle, open-toe sandals.",
        "tags": ["shinobi", "wrap"]}


def build(g):
    waistband(g, "D", "weave", 34620)
    for leg in legs(g, "D", "weave", 34621, rows=(0, 4), crease=False):
        wrapped(leg.strip, 0, 5, leg.strip.w - 1, 9, "S")
    sandals(g)
    for side, bone in (("right", "RIGHT_LEG"), ("left", "LEFT_LEG")):
        cuff = g.piece(f"{side}_knee_cuff", bone, (-2.5, 3.6, -2.5), (5, 1, 5))
        solid(cuff, "D", "weave", 34623, 2, edge=False)
        for face in cuff.sides:
            face.set(2, 0, "M3")
