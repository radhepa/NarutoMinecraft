"""Stone Plates: the guardians' armor, overlapping lamellae lacquered in umber like weathered rock
over a plum gambeson, ochre lacing between the rows and broad stone pauldrons on the shoulders."""
from kit import body, sleeves
from paint import k, solid

META = {
    "name": "Stone Plates",
    "gender": "unisex",
    "description": "Umber lamellar armor laced in ochre over a plum gambeson, broad stone pauldrons.",
    "tags": ["shinobi", "armor"],
}


def build(g):
    body(g, "P", "quilt", 23551)
    sleeves(g, "P", "quilt", 23552, rows=(0, 11), cuff="L1")
    plates = body(g, "L", "leather", 23553, layer="jacket", rows=(0, 9))
    for face in plates.sides:
        for y in (2, 5, 8):
            face.hline(0, face.w - 1, y, "A2")
            face.hline(0, face.w - 1, y - 1, k("L", 1))
        for x in range(0, face.w, 3):
            for y in (0, 3, 6):
                face.set(x, y, k("L", 1))
        face.hline(0, face.w - 1, 9, k("L", 0))
    for side, bone, x in (("right", "RIGHT_ARM", -3.5), ("left", "LEFT_ARM", -1.5)):
        for i, (y, h) in enumerate(((-2.4, 2), (-.4, 2))):
            p = g.piece(f"{side}_pauldron_{i}", bone, (x, y, -2.6), (5, h, 5), inflate=.1)
            solid(p, "L", "leather", 23556 + i, 2 - i)
            for face in p.sides:
                face.hline(0, face.w - 1, h - 1, "A2")
