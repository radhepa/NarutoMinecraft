"""Watch Haori: the night-watch captain's long haori, open over a charcoal under-kimono, pleated
like a curtain all round its knee-length hem, deep sleeves hanging below the arms, moon-grey cords
tied across the chest and a muffler worn down with its ends on the chest."""
from kit import arm_bone, arm_x, flaps, sleeves
from kit_tobari import muffler, pleats
from paint import cap, solid, strip_fabric

META = {
    "name": "Watch Haori",
    "gender": "unisex",
    "description": "Knee-length pleated haori open over a charcoal kimono, deep sleeves, grey chest cords, a muffler.",
    "tags": ["shinobi", "robe", "jonin"],
    "covers_waist": True,
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "D", "weave", 25480, 2)
    cap(body, "D", seed=25480)
    jacket = g.part("jacket")
    strip_fabric(jacket, "P", "twill", 25481, 2)
    cap(jacket, "P", texture="twill", seed=25481)
    for x in (3, 4):
        for y in range(12):
            jacket.front.clear(x, y)
    jacket.front.vline(2, 0, 11, "S3"), jacket.front.vline(5, 0, 11, "S3")
    for face in (jacket.back, jacket.right, jacket.left):
        for x in range(1, face.w, 3):
            face.vline(x, 4, 11, "P1")
    cord = g.piece("chest_cord", "TORSO", (-1.5, 0, 0), (3, 1, 1), pivot=(0, 4.0, -2.45))
    solid(cord, "S", "plain", 25482, 3, edge=False)
    for arm in sleeves(g, "P", "twill", 25483, rows=(0, 8), layer="sleeve"):
        arm.strip.hline(0, arm.strip.w - 1, 8, "P1")
    for side in ("right", "left"):
        sl = g.piece(f"{side}_deep_sleeve", arm_bone(side), (arm_x(side) - .3, 3, -2.3), (5, 6, 5), inflate=.05)
        solid(sl, "P", "twill", 25485 + (side == "left"), 2)
        for face in sl.sides:
            pleats(face, "P")
        sl.bottom.fill("P0")
    sleeves(g, "D", "weave", 25488, rows=(0, 11))
    for face in flaps(g, "hem", 9, "P", "twill", 25487, slit=False):
        pleats(face, "P")
    muffler(g, "muffler", "S", "knit", 25489, tails="front")
