"""Padded Gambeson: a thick quilted jacket that doubles the wearer's girth, a white shawl collar
folded over the shoulders, a twisted rope belt with a sake gourd and long quilted sleeves."""
from kit_akimichi import gourd, lames, quilt
from paint import fabric, k, solid, strip_fabric

META = {
    "name": "Padded Gambeson",
    "gender": "unisex",
    "description": "Thick quilted jacket, white shawl collar, twisted rope belt with a gourd, quilted sleeves.",
    "tags": ["shinobi", "akimichi"],
}


def build(g):
    body, jacket = g.part("body"), g.part("jacket")
    for box in (body, jacket):
        for face in box.sides:
            quilt(face, "P", 6831, 2)
        fabric(box.top, "P", "weave", 6831, 3)
    jacket.front.vline(4, 0, 11, "P0")
    # Extra padding round the belly in two puffed rolls.
    for box in lames(g, "padding", [(4.0, 3, .35), (7.0, 2, .42)], seed=6832, lacing=None, texture="weave"):
        for face in box.sides:
            quilt(face, "P", 6833, 2)
        box.front.vline(4, 0, box.h - 1, "P0")
    # The shawl collar.
    shawl = g.piece("shawl", "TORSO", (-4.5, -1.2, -2.6), (9, 3, 5), inflate=.3)
    solid(shawl, "S", "weave", 6834, 3, edge=False)
    for face in shawl.sides:
        face.hline(0, face.w - 1, 2, "S1")
    shawl.front.vline(4, 0, 2, "S1")
    # The rope belt, twisted.
    rope = g.piece("rope_belt", "TORSO", (-4.5, 9.6, -2.5), (9, 1, 5), inflate=.45)
    for face in rope.faces:
        face.paint(lambda x, y, cur: k("A", 3 if x % 2 else 1))
    gourd(g, "gourd", (3.8, 10.8, -2.2), rotation=(0, 0, -10), motion="flap_front")
    for side in ("right", "left"):
        arm = g.part(f"{side}_arm")
        for face in arm.sides:
            quilt(face, "P", 6835 + (side == "left"), 2)
        fabric(arm.top, "P", "weave", 6835, 3)
        arm.strip.hline(0, arm.strip.w - 1, 11, "K2"), arm.strip.hline(0, arm.strip.w - 1, 10, "K1")
        strip_fabric(g.part(f"{side}_sleeve"), "P", "weave", 6837, 2, 0, 1)
