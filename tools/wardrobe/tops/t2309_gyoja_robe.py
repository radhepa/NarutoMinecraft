"""Gyoja Robe: the chief's white mountain-ascetic robe after En no Gyoja, a plum lapel crossing the
breast, wide sleeves bound at the wrist, a heavy string of prayer beads round the neck and a plum
sash with long tails."""
from kit import belt, body, flaps, sleeves
from paint import k, solid

META = {
    "name": "Gyoja Robe",
    "gender": "unisex",
    "description": "White ascetic's robe with a plum lapel, wide bound sleeves, prayer beads and a plum sash.",
    "tags": ["shinobi", "robe"],
    "covers_waist": True,
}


def build(g):
    body(g, "S", "weave", 23641)
    robe = body(g, "S", "weave", 23642, layer="jacket")
    f = robe.front
    for y in range(9):
        x = min(7, 1 + y // 2 + y // 3)
        f.set(x, y, "P2"), f.set(max(0, x - 1), y, "P3")
    robe.back.hline(0, 7, 0, "P2")
    for arm in sleeves(g, "S", "weave", 23643, rows=(0, 11), layer="sleeve"):
        for face in arm.sides:
            face.hline(0, face.w - 1, 10, "P2"), face.hline(0, face.w - 1, 11, "P1")
            face.vline(face.w // 2, 0, 9, k("S", 1))
    sash = belt(g, "sash", y=8.6, role="P", height=2, buckle=None)
    sash.front.vline(4, 0, 1, "P1")
    for i, x in enumerate((-.6, .6)):
        tail = g.piece(f"sash_tail_{i}", "TORSO", (-.5, 0, 0), (1, 6, 1), pivot=(x, 10.4, -2.85), rotation=(0, 0, 8 - 16 * i),
                       motion="flap_front")
        solid(tail, "P", "weave", 23646 + i, 2)
    for i in range(9):   # the prayer beads, from shoulder to shoulder round the front of the neck
        x = -3.4 + i * .85
        y = .2 + (1.6 - abs(x) * .45)
        bead = g.piece(f"bead_{i}", "TORSO", (-.5, -.5, -.5), (1, 1, 1), pivot=(x, y, -2.75), scale=(.8, .8, .8))
        solid(bead, "L", "smooth", 23650 + i, 3 if i % 4 else 1, edge=False)
    for face in flaps(g, "robe", 5, "S", "weave", 23660, hem=k("P", 2)):
        face.vline(4, 1, 4, k("S", 1))
