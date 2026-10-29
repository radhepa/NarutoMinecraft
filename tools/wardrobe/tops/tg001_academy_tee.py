"""Academy Tee: the plain short-sleeved tee half the Academy wears to class, with a ringer collar and
sleeve bands in a contrast color and a small leaf printed on the chest."""
from glyphs import LEAF, stamp
from kit_academy import shirt
from paint import fabric, k

META = {
    "name": "Academy Tee",
    "gender": "unisex",
    "description": "Short-sleeved tee with a contrast ringer collar and sleeve bands, a small leaf on the chest.",
    "tags": ["shinobi", "genin"],
}


def build(g):
    body, arms = shirt(g, "P", "plain", 31000, sleeve=3, trim="S3")
    f = body.front
    f.hline(2, 5, 0, "S3"), f.set(1, 0, "S2"), f.set(6, 0, "S2"), f.hline(3, 4, 1, "S2")
    body.back.hline(1, 6, 0, "S3")
    for face in (body.right, body.left):
        face.vline(1, 2, 10, "P1")
    for arm in arms:
        arm.strip.hline(0, arm.strip.w - 1, 2, "P1")
    crest = g.piece("chest_leaf", "TORSO", (-4, 0, -1), (8, 8, 1), pivot=(1.6, 2.4, -2.02), scale=(.5, .5, .5))
    fabric(crest.front, "P", "plain", 31001, 2)
    stamp(crest.front, LEAF, 0, 0, {"#": "A2"})
    for face in (crest.top, crest.bottom, crest.right, crest.left, crest.back):
        face.fill(k("P", 2))
