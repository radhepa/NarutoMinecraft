"""Training Dogi: a bleached cotton dogi jacket with wide elbow-length sleeves, the lapels edged in a
contrasting band and crossed under a knotted belt in the accent color; sweat-worn at the collar from
years of morning drills."""
from kit import arm_bone, arm_x, belt, neckline
from paint import fabric, line, solid, strip_fabric

META = {
    "name": "Training Dogi",
    "gender": "unisex",
    "description": "Bleached cotton dogi with wide elbow sleeves, banded lapels and a knotted accent belt.",
    "tags": ["shinobi", "genin", "wrap", "taijutsu"],
}


def build(g):
    body, jacket = g.part("body"), g.part("jacket")
    strip_fabric(body, "S", "weave", 35110, 3, 0, 10)
    fabric(body.top, "S", "weave", 35110, 4)
    strip_fabric(jacket, "S", "weave", 35111, 3, 0, 9)
    fabric(jacket.top, "S", "weave", 35111, 4)
    for face in (body.front, jacket.front):
        neckline(face, "v", "S", base=3)
    f = jacket.front
    line(f, 1, 0, 4, 9, "P2"), line(f, 2, 0, 5, 9, "P1")
    line(f, 6, 0, 6, 3, "P2")
    jacket.strip.hline(0, jacket.strip.w - 1, 9, "S2")
    for face in (jacket.right, jacket.left):
        face.vline(face.w // 2, 1, 8, "S2")
    for side in ("right", "left"):
        arm = g.part(f"{side}_arm")
        strip_fabric(arm, "S", "weave", 35112, 3, 0, 4)
        fabric(arm.top, "S", "weave", 35112, 4)
        cuff = g.piece(f"{side}_wide_sleeve", arm_bone(side), (arm_x(side) - .7, 2.2, -2.7), (5, 3, 5), inflate=.1)
        solid(cuff, "S", "weave", 35113 + (side == "left"), 3)
        for face in cuff.sides:
            face.hline(0, face.w - 1, 2, "S2")
        cuff.bottom.fill("S1")
    obi = belt(g, "dogi_belt", y=9.3, role="A", buckle=None)
    obi.front.hline(0, obi.front.w - 1, 1, "A1")
    knot = g.piece("belt_knot", "TORSO", (-1, 0, 0), (2, 2, 1), pivot=(.4, 9.3, -2.9))
    solid(knot, "A", "weave", 35115, 2, edge=False)
    for i, (x, rz) in enumerate(((-.2, 14), (1.0, -10))):
        tail = g.piece(f"belt_tail_{i}", "TORSO", (-.5, 0, -.5), (1, 3, 1), pivot=(x, 11.0, -3.0), rotation=(0, 0, rz),
                       motion="flap_front")
        solid(tail, "A", "weave", 35116 + i, 2)
