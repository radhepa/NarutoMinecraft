"""Clan Head Haori: the formal dress of the clan's head, a dark haori worn open over a kimono with a
white collar, wide sleeves to the forearm, a large crest on the back, small crests on the chest and
skirts to the knee."""
from kit import arm_bone, arm_x
from kit_uchiha import back_crest, chest_crest
from paint import cap, fabric, solid, strip_fabric

META = {
    "name": "Clan Head Haori",
    "gender": "unisex",
    "description": "Dark open haori over a kimono, white collar, wide sleeves, crests on the back and chest, knee skirts.",
    "tags": ["shinobi", "robe", "uchiha"],
    "covers_waist": True,
}


def build(g):
    body, jacket = g.part("body"), g.part("jacket")
    # The kimono beneath: wrapped left over right with a white collar edge.
    strip_fabric(body, "D", "weave", 3900, 2)
    cap(body, "D", seed=3900)
    for i in range(7):
        body.front.set(1 + i, i, "S3")
    body.strip.hline(0, body.strip.w - 1, 9, "K2"), body.strip.hline(0, body.strip.w - 1, 10, "K1")
    # The haori: open down the front, its lapels trimmed.
    strip_fabric(jacket, "P", "weave", 3901, 2)
    cap(jacket, "P", seed=3901)
    for y in range(12):
        for x in range(2, 6):
            jacket.front.clear(x, y)
        jacket.front.set(1, y, "P1"), jacket.front.set(6, y, "P1")
    back_crest(g, "P", pivot=(0, 1.0, 2.35), seed=3902)
    for i, x in enumerate((-3.1, 3.1)):
        chest_crest(g, f"chest_crest_{i}", x, y=2.0, z=-2.3, role="P", seed=3903)
    # Haori ties at the chest.
    tie = g.piece("haori_tie", "TORSO", (-1, 0, 0), (2, 1, 1), pivot=(0, 5.0, -2.85))
    solid(tie, "S", "weave", 3904, 3)
    # Skirts to the knee: two open front halves and the back.
    for name, x0, w, z, motion in (("skirt_front_right", -4.6, 3, -2.9, "flap_front"),
                                   ("skirt_front_left", 1.6, 3, -2.9, "flap_front"),
                                   ("skirt_back", -4.6, 9, 1.9, "flap_back")):
        skirt = g.piece(name, "TORSO", (0, 0, 0), (w, 7, 1), pivot=(x0, 11.4, z), motion=motion)
        solid(skirt, "P", "weave", 3905 + len(name) % 7, 2)
        for face in skirt.sides:
            face.hline(0, face.w - 1, 6, "P1")
    for name, x in (("skirt_right", -5.05), ("skirt_left", 4.05)):
        panel = g.piece(name, "TORSO", (0, 0, -2), (1, 6, 4), pivot=(x, 11.4, 0))
        solid(panel, "P", "weave", 3912, 2)
    for side in ("right", "left"):
        arm, sleeve = g.part(f"{side}_arm"), g.part(f"{side}_sleeve")
        strip_fabric(arm, "D", "weave", 3913, 2, 0, 10)
        fabric(arm.top, "D", "weave", 3913, 3)
        strip_fabric(sleeve, "P", "weave", 3914, 2, 0, 3)
        fabric(sleeve.top, "P", "weave", 3914, 3)
        wide = g.piece(f"{side}_wide_sleeve", arm_bone(side), (arm_x(side) - .7, 2.0, -2.7), (5, 6, 5), inflate=.12)
        solid(wide, "P", "weave", 3915, 2)
        for face in wide.sides:
            face.hline(0, face.w - 1, 5, "P1")
        wide.bottom.fill("P0")
