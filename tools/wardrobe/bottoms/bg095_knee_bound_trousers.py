"""Knee-Bound Trousers: loose trousers bound tight with leather straps below the knee and at the
ankle so the cloth blouses out between, worn over open sandals with a pouch at the back of the belt."""
from kit import legs, leg_ring, pouch, waistband
from kit_shinobi import sandals
from paint import solid

META = {"name": "Knee-Bound Trousers", "gender": "unisex",
        "description": "Loose trousers bloused between leather straps below the knee and at the ankle, sandals, a pouch.",
        "tags": ["shinobi", "genin"]}


def build(g):
    waistband(g, "P", "twill", 35450, 2)
    legs(g, "P", "twill", 35451, 2, rows=(0, 9), crease=False)
    for i, y in enumerate((5.0, 8.6)):
        for ring in leg_ring(g, f"strap_{i}", y, "L", 2, (5, 1, 5), "leather", inflate=.02):
            for face in ring.sides:
                face.set(face.w // 2, 0, "M3")
    for ring in leg_ring(g, "blouse", 6.0, "P", 2, (5, 2, 5), "twill"):
        for face in ring.sides:
            face.hline(0, face.w - 1, 0, "P3")
            for x in range(0, face.w, 2):
                face.set(x, 1, "P1")
    sandals(g)
    belt = g.piece("waist_belt", "TORSO", (-4.6, 9.4, -2.6), (9, 1, 5), inflate=.1)
    solid(belt, "L", "leather", 35455, 2, edge=False)
    pouch(g, "waist_pouch", (0, 10.0, 2.6), size=(3, 2, 1), flap="M3")
