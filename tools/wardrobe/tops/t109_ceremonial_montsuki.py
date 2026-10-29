"""Ceremonial Montsuki: the clan's formal black kimono for councils and funerals, a white under-collar,
five Senju crests (chest, sleeves and back) in white, a grey-green obi and long skirts to the shin."""
from kit import belt, flaps
from kit_senju import crest
from paint import cap, fabric, solid, strip_fabric

META = {
    "name": "Ceremonial Montsuki",
    "gender": "unisex",
    "description": "Formal black kimono with five white Senju crests, white under-collar, long skirts.",
    "tags": ["senju", "robe", "formal"],
    "requires": ["hakama"],
    "covers_waist": True,
}


def badge(g, pid, bone, pivot, face_name, seed, rotation=(0, 0, 0)):
    """A white crest at triple resolution on a plate flush with the cloth."""
    plate = g.piece(pid, bone, (-4, -4, -.5), (8, 8, 1), pivot=pivot, rotation=rotation, scale=(1 / 3, 1 / 3, 1 / 3))
    for face in plate.faces:
        fabric(face, "P", "smooth", seed, 2)
    crest(getattr(plate, face_name), 0, 0, "S4", bar="P2")


def build(g):
    body = g.part("body")
    strip_fabric(body, "P", "smooth", 1610, 2)
    cap(body, "P", texture="smooth", seed=1610)
    f = body.front
    # A deep V of white under-collar from both shoulders to the breastbone.
    for i in range(4):
        f.set(2 + i // 2, i, "S4"), f.set(5 - i // 2, i, "S4")
    f.set(3, 4, "S2"), f.set(4, 4, "S2")
    belt(g, "obi", y=7.6, role="A", height=2, buckle=None, inflate=.15)
    for face in flaps(g, "kimono", 9, "P", "smooth", 1611, width=9, top=10.0, front_z=-2.5, back_z=1.5):
        face.vline(4, 1, 8, "P1")
    for name, x in (("right", -4.7), ("left", 3.7)):
        side = g.piece(f"kimono_side_{name}", "TORSO", (0, 0, -2.0), (1, 9, 4), pivot=(x, 10.0, 0))
        solid(side, "P", "smooth", 1612, 2)
    badge(g, "crest_chest_right", "TORSO", (-2.4, 4.6, -2.1), "front", 1613)
    badge(g, "crest_chest_left", "TORSO", (2.4, 4.6, -2.1), "front", 1614)
    badge(g, "crest_back", "TORSO", (0, 2.0, 2.1), "back", 1615)
    for side, bone, ox in (("right", "RIGHT_ARM", -3.0), ("left", "LEFT_ARM", -1.0)):
        arm, sleeve = g.part(f"{side}_arm"), g.part(f"{side}_sleeve")
        strip_fabric(arm, "P", "smooth", 1616, 2, 0, 10)
        fabric(arm.top, "P", "smooth", 1616, 3)
        strip_fabric(sleeve, "P", "smooth", 1617, 2, 0, 9)
        fabric(sleeve.top, "P", "smooth", 1617, 3)
        pocket = g.piece(f"{side}_tamoto", bone, (ox + .5, 3.0, -2.5), (3, 7, 5), inflate=.05)
        solid(pocket, "P", "smooth", 1618, 2)
        pocket.bottom.fill("P1")
