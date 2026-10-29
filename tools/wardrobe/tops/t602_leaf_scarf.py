"""Leaf Scarf: the young Akimichi's short-sleeved coat worn open over a white shirt with the 食
crest, a thick white scarf wound round the neck with its ends hanging over the right lapel, and a belt."""
from kit import belt
from kit_akimichi import quilt, shoku_disc
from paint import fabric, solid, strip_fabric

META = {
    "name": "Leaf Scarf",
    "gender": "unisex",
    "description": "Open short-sleeved coat over a white shirt with the food crest, a thick white scarf.",
    "tags": ["shinobi", "genin", "akimichi"],
}


def build(g):
    body, jacket = g.part("body"), g.part("jacket")
    strip_fabric(body, "S", "weave", 6706, 2)
    fabric(body.top, "S", "weave", 6706, 3)
    strip_fabric(jacket, "P", "weave", 6707, 2, 0, 11)
    fabric(jacket.top, "P", "weave", 6707, 3)
    jacket.strip.hline(0, jacket.strip.w - 1, 11, "P1")
    f = jacket.front
    for y in range(12):
        for x in range(2, 6):
            f.set(x, y, None)
    f.vline(1, 0, 11, "P3"), f.vline(6, 0, 11, "P1")
    for face in (jacket.right, jacket.left):
        face.vline(face.w // 2, 3, 10, "P1")
    shoku_disc(g, "chest_crest", (.6, 4.8, -2.3), ground="S3", disc="S", ink="A1", rim="A2")
    # Short sleeves of the coat, the forearms bare.
    for side in ("right", "left"):
        arm, sleeve = g.part(f"{side}_arm"), g.part(f"{side}_sleeve")
        strip_fabric(arm, "S", "weave", 6708, 2, 0, 3)
        fabric(arm.top, "S", "weave", 6708, 3)
        strip_fabric(sleeve, "P", "weave", 6709 + (side == "left"), 2, 0, 4)
        fabric(sleeve.top, "P", "weave", 6709, 3)
        sleeve.strip.hline(0, sleeve.strip.w - 1, 4, "P1")
    # The scarf: a thick padded ring at the throat and two ends falling over the chest.
    ring = g.piece("scarf", "TORSO", (-4.5, -1.4, -2.7), (9, 3, 5), inflate=.22)
    solid(ring, "S", "weave", 6711, 3, edge=False)
    for face in ring.sides:
        quilt(face, "S", 6711, 2)
    for i, (x, h, rz) in enumerate(((-3.4, 6, 6), (-2.4, 5, -4))):
        end = g.piece(f"scarf_end_{i}", "TORSO", (-1, 0, -.5), (2, h, 1), pivot=(x, 1.2, -3.0), rotation=(0, 0, rz),
                      motion="sway")
        solid(end, "S", "weave", 6712 + i, 3)
        end.front.hline(0, 1, h - 1, "A2")
    belt(g, "belt", y=9.6, role="L", height=2, inflate=.3)
