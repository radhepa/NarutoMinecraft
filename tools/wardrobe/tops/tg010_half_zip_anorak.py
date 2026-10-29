"""Half-Zip Anorak: a light pullover windbreaker with a contrast yoke across the chest, a half zip, a
pouch pocket and a drawcord hem: the genin sent out in the rain."""
from kit import collar
from kit_academy import ribbed, shirt
from paint import solid, strip_fabric

META = {
    "name": "Half-Zip Anorak",
    "gender": "unisex",
    "description": "Pullover windbreaker with a contrast chest yoke, half zip, pouch pocket and drawcord hem.",
    "tags": ["shinobi", "genin"],
}


def build(g):
    body, arms = shirt(g, "P", "smooth", 31140, sleeve=10)
    for face in body.sides:
        for y in (1, 2, 3):
            face.hline(0, face.w - 1, y, "S2")
        face.hline(0, face.w - 1, 4, "S1")
    f = body.front
    f.vline(4, 0, 4, "M3"), f.set(4, 0, "M4"), f.set(3, 4, "M2")
    f.rect(2, 6, 4, 3, "P2"), f.hline(2, 5, 6, "P3"), f.vline(1, 6, 8, "P1"), f.vline(6, 6, 8, "P1")
    for arm in arms:
        for y in (1, 2, 3):
            arm.strip.hline(0, arm.strip.w - 1, y, "S2")
        arm.strip.hline(0, arm.strip.w - 1, 4, "S1")
        ribbed(arm, (10,), "K")
        arm.front.vline(2, 5, 9, "P1")
    jacket = g.part("jacket")
    strip_fabric(jacket, "P", "smooth", 31141, 2, 10, 11)
    jacket.strip.hline(0, jacket.strip.w - 1, 10, "P3")
    jacket.strip.hline(0, jacket.strip.w - 1, 11, "P1")
    for i, x in enumerate((-3.2, 2.7)):
        toggle = g.piece(f"hem_toggle_{i}", "TORSO", (0, 0, 0), (1, 2, 1), pivot=(x, 11.0, -2.5), scale=(.5, .5, .5),
                         motion="flap_front")
        solid(toggle, "K", "plain", 31142 + i, 2, edge=False)
    neck = collar(g, "collar", "S", "smooth", height=2, y=-1.6)
    neck.front.vline(4, 0, 1, "M3")
