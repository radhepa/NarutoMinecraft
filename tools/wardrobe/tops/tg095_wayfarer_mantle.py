"""Wayfarer Mantle: a hooded shoulder mantle with the hood pushed back, its edge bound in leather,
over a long-sleeved shirt; a bandolier of pouches slung from the right shoulder to the left hip and
a toggle at the throat. Days on the road between villages."""
from kit import arm_bone, arm_x, sleeves
from paint import fabric, solid, strip_fabric, strip_line

META = {
    "name": "Wayfarer Mantle",
    "gender": "unisex",
    "description": "Hooded shoulder mantle with leather-bound edges over long sleeves, a bandolier of pouches.",
    "tags": ["shinobi", "cloak", "mantle", "jonin"],
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "D", "weave", 35150, 2, 0, 10)
    fabric(body.top, "D", "weave", 35150, 3)
    sleeves(g, "D", "weave", 35151, 2, rows=(0, 10), cuff="D1", cuff_row=10)
    jacket = g.part("jacket")
    strip_line(jacket, [(4, 2), (11, 9)], "L2"), strip_line(jacket, [(4, 3), (11, 10)], "L1")
    strip_line(jacket, [(16, 9), (23, 2)], "L2"), strip_line(jacket, [(16, 10), (23, 3)], "L1")
    for i, (x, y) in enumerate(((-1.6, 4.8), (.4, 6.8))):
        p = g.piece(f"bandolier_pouch_{i}", "TORSO", (-1, 0, 0), (2, 2, 1), pivot=(x, y, -2.8), rotation=(0, 0, -40))
        solid(p, "L", "leather", 35152 + i, 2)
        p.front.set(0, 0, "M3")
    mantle = g.piece("mantle", "TORSO", (-5.5, -.8, -3.2), (11, 5, 7))
    solid(mantle, "P", "weave", 35154, 2)
    fabric(mantle.top, "P", "weave", 35154, 3)
    for face in mantle.sides:
        face.hline(0, face.w - 1, 0, "P3")
        face.hline(0, face.w - 1, 4, "L2")
        for x in range(1, face.w, 3):
            face.vline(x, 1, 3, "P1")
    mantle.front.vline(5, 0, 4, "L1")
    for side in ("right", "left"):
        drape = g.piece(f"{side}_drape", arm_bone(side), (arm_x(side) - .6, 2.0, -2.6), (5, 2, 5))
        solid(drape, "P", "weave", 35155 + (side == "left"), 2)
        for face in drape.sides:
            face.hline(0, face.w - 1, 1, "L2")
    hood = g.piece("hood", "TORSO", (-4, 0, 0), (8, 5, 3), pivot=(0, -2.6, 3.2), rotation=(-16, 0, 0))
    solid(hood, "P", "weave", 35157, 2)
    for face in hood.sides:
        face.hline(0, face.w - 1, 0, "L2")
    hood.front.fill("P0")
    hood.back.vline(4, 1, 4, "P1")
    toggle = g.piece("toggle", "TORSO", (-1, 0, 0), (2, 1, 1), pivot=(0, 0.2, -3.6))
    for face in toggle.faces:
        face.fill("L3")
