"""Florist Wrap: a short kimono-style wrap top printed with tiny blossoms, the collar crossed left
over right and edged in the accent, a wide obi with a flower knot and wide half sleeves."""
from kit import arm_x, belt
from kit_yamanaka import flower, petal_fabric
from paint import fabric, k, solid

META = {
    "name": "Florist Wrap",
    "gender": "unisex",
    "description": "Blossom-print wrap top with a crossed collar, a wide obi with a flower knot, wide half sleeves.",
    "tags": ["yamanaka", "florist", "robe"],
}


def build(g):
    body = g.part("body")
    for face in body.sides:
        petal_fabric(face, "S", 7550 + face.x0, 3)
    fabric(body.top, "S", "plain", 7550, 4), fabric(body.bottom, "S", "plain", 7551, 2)
    f = body.front
    for i in range(7):
        f.set(1 + i, i, "A2")
        if i + 2 <= 7:
            f.set(2 + i, i, "S2")
    f.set(0, 0, "A2")
    for face in (body.right, body.left, body.back):
        face.hline(0, face.w - 1, 0, "A2")
    obi = belt(g, "obi", y=6.8, role="P", height=3, buckle=None, inflate=.12)
    for face in obi.sides:
        face.hline(0, face.w - 1, 1, k("A", 2))
    flower(g, "obi_knot", (1.8, 8.3, -2.95), bone="TORSO", size=5)
    for side, bone in (("right", "RIGHT_ARM"), ("left", "LEFT_ARM")):
        arm = g.part(f"{side}_arm")
        for face in arm.sides:
            petal_fabric(face, "S", 7552, 3)
        fabric(arm.top, "S", "plain", 7552, 4)
        for face in arm.sides:
            for y in range(6, 12):
                face.hline(0, face.w - 1, y, None)
        sleeve = g.piece(f"{side}_wide_sleeve", bone, (arm_x(side) - .5, 2.4, -2.5), (5, 6, 5), inflate=.1)
        for face in sleeve.sides:
            petal_fabric(face, "S", 7553, 3)
        fabric(sleeve.top, "S", "plain", 7553, 4), sleeve.bottom.fill("S1")
        for face in sleeve.sides:
            face.hline(0, face.w - 1, 5, "A2")
