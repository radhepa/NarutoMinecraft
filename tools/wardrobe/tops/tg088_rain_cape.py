"""Rain Cape: a long oiled cape to the knees with a hood thrown back, clasped at the throat with a
steel ring, worn over a dark long-sleeved shirt and fingerless gloves; the cloth shines where the
rain runs off it."""
from kit import sleeves
from paint import fabric, k, solid, strip_fabric

META = {
    "name": "Rain Cape",
    "gender": "unisex",
    "description": "Long oiled cape to the knees with the hood thrown back and a steel ring clasp, over a dark shirt.",
    "tags": ["shinobi", "cloak", "jonin"],
    "covers_waist": True,
}


def oiled(face, seed):
    """Oiled cloth: smooth ground, long falling sheen streaks and a dark crease beside each."""
    fabric(face, "P", "smooth", seed, 2)
    for x in range(face.w):
        if x % 4 == 2:
            face.vline(x, 1, face.h - 2, "P3")
        elif x % 4 == 1:
            face.vline(x, 2, face.h - 1, "P1")
    face.hline(0, face.w - 1, 0, "P3")
    face.hline(0, face.w - 1, face.h - 1, "P0")


def build(g):
    body = g.part("body")
    strip_fabric(body, "K", "weave", 35080, 3)
    fabric(body.top, "K", "weave", 35080, 4)
    sleeves(g, "K", "weave", 35081, 3, rows=(0, 9))
    for side in ("right", "left"):
        arm = g.part(f"{side}_arm")
        strip_fabric(arm, "L", "leather", 35082, 1, 9, 10)
    shoulders = g.piece("cape_shoulders", "TORSO", (-5.5, -.8, -3.2), (11, 5, 7))
    solid(shoulders, "P", "smooth", 35083, 2)
    for face in shoulders.sides:
        oiled(face, 35083)
    fabric(shoulders.top, "P", "smooth", 35083, 3)
    back = g.piece("cape_back", "TORSO", (-5.5, 0, 0), (11, 18, 1), pivot=(0, 3.8, 3.4), motion="flap_back")
    solid(back, "P", "smooth", 35084, 2)
    oiled(back.back, 35084)
    # The front falls open from the clasp in two wide panels that wrap round the sides.
    for side, x in (("right", -3.3), ("left", 3.3)):
        panel = g.piece(f"cape_front_{side}", "TORSO", (-2, 0, 0), (4, 14, 1), pivot=(x, 3.8, -3.5),
                        rotation=(0, 14 if x < 0 else -14, 0), motion="flap_front")
        solid(panel, "P", "smooth", 35085 + (x > 0), 2)
        oiled(panel.front, 35085 + (x > 0))
    hood = g.piece("hood", "TORSO", (-3.5, 0, 0), (7, 4, 3), pivot=(0, -2.4, 2.6), rotation=(-12, 0, 0))
    solid(hood, "P", "smooth", 35087, 2)
    for face in hood.sides:
        face.hline(0, face.w - 1, 0, "P3")
    hood.front.fill("P0")
    clasp = g.piece("ring_clasp", "TORSO", (-1, -1, 0), (2, 2, 1), pivot=(0, -.2, -3.8))
    for face in clasp.faces:
        face.fill("M3")
    clasp.front.set(0, 0, "M4"), clasp.front.set(1, 1, "M1")
