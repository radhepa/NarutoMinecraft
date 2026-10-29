"""Climbing Pants: close three-quarter trousers ending at mid-calf, feet and ankles wrapped in cloth
for grip on rock, a coil of rope hung at the right hip and a plain belt: made for cliff paths."""
from kit import legs, leg_ring, waistband
from kit_rugged import leg_wraps, rope_face
from paint import solid

META = {"name": "Climbing Pants", "gender": "unisex",
        "description": "Close three-quarter trousers, cloth-wrapped feet for grip, a coil of rope at the hip.",
        "tags": ["shinobi", "genin"]}


def build(g):
    waistband(g, "P", "twill", 35480, 2)
    legs(g, "P", "twill", 35481, 2, rows=(0, 6), crease=False)
    for ring in leg_ring(g, "cuff", 6.2, "P", 1, (5, 1, 5), "twill"):
        for face in ring.sides:
            face.hline(0, face.w - 1, 0, "P1")
    leg_wraps(g, 8, 11)
    for side in ("right", "left"):
        leg, pants = g.part(f"{side}_leg"), g.part(f"{side}_pants")
        leg.bottom.fill("S1")
        for face in pants.sides:
            face.hline(0, face.w - 1, 11, "S1")
        pants.bottom.fill("K0")
    coil = g.piece("waist_rope_coil", "TORSO", (0, 0, -2), (1, 4, 4), pivot=(-4.6, 9.4, 0))
    for face in coil.faces:
        rope_face(face, "S", 2)
    belt = g.piece("waist_belt", "TORSO", (-4.6, 9.4, -2.6), (9, 1, 5), inflate=.1)
    solid(belt, "K", "leather", 35483, 3, edge=False)
