"""Elder Kosode: the clan elder's formal dress, a white kosode under a long knee-length overcoat in
the house colour with the bell crest on the back, the hem and broad sleeve mouths trimmed in
running bells, and a narrow violet obi."""
from kit import belt
from kit_suzuran import back_crest, bell_hem
from paint import cap, fabric, solid, strip_fabric

META = {
    "name": "Elder Kosode",
    "gender": "unisex",
    "description": "White kosode under a long knee-length overcoat with the bell crest, bell-trimmed hem and sleeves.",
    "tags": ["shinobi", "robe", "jonin"],
    "covers_waist": True,
}


def build(g):
    body, jacket = g.part("body"), g.part("jacket")
    strip_fabric(body, "S", "weave", 24601, 3)
    cap(body, "S", seed=24601, base=3)
    for y in range(4):
        body.front.set(3 - y // 2, y, "S1")
    strip_fabric(jacket, "P", "weave", 24602, 2)
    cap(jacket, "P", seed=24602)
    for y in range(12):
        for x in range(3, 5):
            jacket.front.clear(x, y)
        jacket.front.set(2, y, "D2"), jacket.front.set(5, y, "D2")
    belt(g, "obi", y=8.0, role="A", height=1, buckle=None, inflate=.02)
    for side in ("right", "left"):
        arm = g.part(f"{side}_arm")
        strip_fabric(arm, "S", "weave", 24603, 3, 0, 10)
        fabric(arm.top, "S", "weave", 24603, 4)
        bone = "RIGHT_ARM" if side == "right" else "LEFT_ARM"
        ox = -3.0 if side == "right" else -1.0
        cuff = g.piece(f"{side}_long_sleeve", bone, (ox - .7, -2.3, -2.7), (5, 10, 5), inflate=.15)
        solid(cuff, "P", "weave", 24604 + (side == "left"), 2)
        for face in cuff.sides:
            bell_hem(face, 6, step=3, start=1)
            face.hline(0, face.w - 1, 9, "P1")
        fabric(cuff.top, "P", "weave", 24604, 3)
        cuff.bottom.fill("P0")
    for name, x0, w, z, motion, face_name in (("coat_front_right", -4.6, 3, -2.95, "flap_front", "front"),
                                               ("coat_front_left", 1.6, 3, -2.95, "flap_front", "front"),
                                               ("coat_back", -4.6, 9, 1.95, "flap_back", "back")):
        skirt = g.piece(name, "TORSO", (0, 0, 0), (w, 8, 1), pivot=(x0, 11.4, z), motion=motion)
        solid(skirt, "P", "weave", 24606 + w, 2)
        bell_hem(getattr(skirt, face_name), 5, step=3)
    back_crest(g, ground="P2", ring="S3", pivot=(0, 1.2, 2.32))
