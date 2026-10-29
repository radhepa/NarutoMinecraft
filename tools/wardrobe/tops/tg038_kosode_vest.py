"""Kosode Vest: a crossed kosode with wide elbow sleeves under a short padded vest worn open, tied at
the waist with a broad accent obi: the older field dress some jonin never gave up."""
from kit_field import shirt, vest
from paint import k, solid

META = {
    "name": "Kosode Vest",
    "gender": "unisex",
    "description": "Crossed kosode with wide elbow sleeves under a short open padded vest and a broad obi.",
    "tags": ["shinobi", "wrap", "vest", "jonin"],
}


def build(g):
    body = shirt(g, "D", 32340, sleeve=-1)
    f = body.front
    for y in range(7):
        x = 2 + y * 4 // 6
        f.set(x, y, "S3"), f.set(min(7, x + 1), y, "D1")
    for side, sign in (("right", -1), ("left", 1)):
        arm = g.part(f"{side}_arm")
        for y in range(5):
            arm.strip.hline(0, 15, y, "D2")
        arm.top.fill("D3")
        cuff = g.piece(f"{side}_wide_sleeve", "RIGHT_ARM" if sign < 0 else "LEFT_ARM",
                       (-3.4 if sign < 0 else -1.6, 0, -2.5), (5, 7, 5), pivot=(0, -2.2, 0), rotation=(0, 0, 4 * sign))
        solid(cuff, "D", "weave", 32342 + (sign > 0), 2)
        for face in cuff.sides:
            face.hline(0, face.w - 1, 0, k("D", 3)), face.hline(0, face.w - 1, 6, k("D", 1))
            face.vline(face.w // 2, 2, 5, k("D", 1))
        cuff.bottom.fill("D0")
    vest(g, "P", 32344, hem=7, closure="open", ribs=(3, 6))
    obi = g.piece("obi", "TORSO", (-4.5, 0, -2.5), (9, 3, 5), pivot=(0, 7.6, 0), inflate=.22)
    solid(obi, "A", "weave", 32345, 2, edge=False)
    for face in obi.sides:
        face.hline(0, face.w - 1, 0, k("A", 3)), face.hline(0, face.w - 1, 2, k("A", 1))
    knot = g.piece("obi_knot", "TORSO", (-1.5, -1, 0), (3, 2, 1), pivot=(0, 9.0, 2.6))
    solid(knot, "A", "weave", 32346, 2)
