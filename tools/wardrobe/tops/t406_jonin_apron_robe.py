"""Jonin Robe: a jonin's long-sleeved off-white robe with a dark apron panel hanging to the knee
front and back, a wide wrapped belt, a fitted wrap collar and taped wrists."""
from kit_hyuga import obi, wrap_front
from paint import cap, fabric, solid, strip_fabric

META = {
    "name": "Jonin Robe",
    "gender": "unisex",
    "description": "Long-sleeved off-white robe, a dark knee-length apron panel front and back, wide belt.",
    "tags": ["shinobi", "hyuga", "robe", "wrap"],
    "covers_waist": True,
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "P", "velvet", 4761, 2)
    cap(body, "P", texture="velvet", seed=4761)
    wrap_front(body.front, trim="P0", rows=7)
    belt = obi(g, "belt", "D", y=7.4, height=3, knot=None, seed=4762)
    belt.front.hline(2, 6, 1, "D1")
    # The apron: a narrow dark panel front and back, from the belt to the knee, edged in lavender.
    for name, z, motion, face in (("apron_front", -2.95, "flap_front", "front"), ("apron_back", 1.95, "flap_back", "back")):
        panel = g.piece(name, "TORSO", (-2.5, 0, 0), (5, 9, 1), pivot=(0, 10.2, z), motion=motion)
        solid(panel, "D", "twill", 4764 + (z > 0), 2)
        f = getattr(panel, face)
        f.vline(0, 0, 8, "A2"), f.vline(4, 0, 8, "A2"), f.hline(0, 4, 8, "A2")
    for name, x in (("side_right", -5.0), ("side_left", 4.0)):
        side = g.piece(name, "TORSO", (0, 0, -2), (1, 5, 4), pivot=(x, 10.2, 0))
        solid(side, "P", "velvet", 4766, 2)
    for side in ("right", "left"):
        arm, sleeve = g.part(f"{side}_arm"), g.part(f"{side}_sleeve")
        strip_fabric(arm, "P", "velvet", 4767 + (side == "left"), 2, 0, 10)
        fabric(arm.top, "P", "velvet", 4767, 3)
        strip_fabric(sleeve, "P", "velvet", 4769, 2, 0, 7)
        sleeve.strip.hline(0, sleeve.strip.w - 1, 7, "P1")
        for y in (9, 10):
            for x in range(arm.strip.w):
                arm.strip.set(x, y, "S2" if (x + y) % 3 == 0 else "S3")
    collar = g.piece("collar", "TORSO", (-4.5, -.9, -2.6), (9, 1, 5), inflate=.06)
    solid(collar, "P", "velvet", 4770, 2)
    for face in collar.sides:
        face.hline(0, face.w - 1, 0, "P3")
