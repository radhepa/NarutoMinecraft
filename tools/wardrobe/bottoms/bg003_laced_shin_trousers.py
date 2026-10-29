"""Laced Shin Trousers: loose trousers bound tight from the knee down with cloth wraps, a leather cord
laced in crosses over the wraps, and open-toe sandals."""
from kit_academy import leg_cloth, shin_wraps, waist, waist_pouch
from kit_shinobi import sandals
from paint import solid

META = {"name": "Laced Shin Trousers", "gender": "unisex",
        "description": "Loose trousers wrapped tight below the knee, cross-laced with a cord, open-toe sandals.",
        "tags": ["shinobi", "genin"]}


def build(g):
    waist(g, "S", "twill", 31430)
    leg_cloth(g, "S", "twill", 31431, (0, 5))
    shin_wraps(g, 6, 9, "S")
    for side in ("right", "left"):
        leg = g.part(f"{side}_leg")
        # One cross of cord over the front and back of each shin.
        for face in (leg.front, leg.back):
            for i, y in enumerate(range(6, 10)):
                face.set(i, y, "L3"), face.set(3 - i, y, "L3")
    sandals(g)
    for side, bone in (("right", "RIGHT_LEG"), ("left", "LEFT_LEG")):
        puff = g.piece(f"{side}_blouse", bone, (-2.5, 4.4, -2.5), (5, 2, 5))
        solid(puff, "S", "twill", 31433 + (side == "left"), 2)
        for face in puff.sides:
            face.hline(0, face.w - 1, 0, "S3")
    waist_pouch(g, 31435)
