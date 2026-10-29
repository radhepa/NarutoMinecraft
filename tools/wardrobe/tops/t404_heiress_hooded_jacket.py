"""Heiress Hooded Jacket: the shy heiress's roomy cream zip jacket with lavender cuffs, a soft
fleece edge round the hood pushed back on the shoulders and a lavender band at the hem."""
from kit import sleeves
from paint import cap, fabric, solid, strip_fabric

META = {
    "name": "Heiress Hooded Jacket",
    "gender": "unisex",
    "description": "Roomy cream zip jacket, lavender cuffs and hem, a fleece-edged hood down on the back.",
    "tags": ["shinobi", "hyuga", "jacket"],
}


def build(g):
    body, jacket = g.part("body"), g.part("jacket")
    strip_fabric(body, "P", "plain", 4721, 2)
    cap(body, "P", texture="plain", seed=4721)
    f = body.front
    f.vline(4, 0, 11, "M3"), f.vline(3, 0, 11, "P1")
    f.vline(1, 3, 9, "P1"), f.vline(6, 4, 9, "P3")
    # A loose lavender band at the hem.
    strip_fabric(jacket, "P", "plain", 4722, 2, 10, 11)
    jacket.front.vline(4, 10, 11, "M3")
    for y in (10, 11):
        jacket.strip.hline(0, jacket.strip.w - 1, y, "A2" if y == 10 else "A1")
    for arm in sleeves(g, "P", "plain", 4723, 2, rows=(0, 10)):
        arm.strip.hline(0, arm.strip.w - 1, 5, "P1")
    for side in ("right", "left"):
        cuff = g.part(f"{side}_sleeve")
        strip_fabric(cuff, "P", "plain", 4724, 2, 2, 7)
        strip_fabric(cuff, "A", "plain", 4725, 2, 8, 10)
        cuff.strip.hline(0, cuff.strip.w - 1, 10, "A1")
    # The hood, down: a deep fold over the shoulders with a pale fleece edge.
    hood = g.piece("hood", "TORSO", (-4.5, 0, -1.5), (9, 4, 3), pivot=(0, -1.2, 3.0), rotation=(24, 0, 0))
    solid(hood, "P", "plain", 4726, 2)
    fabric(hood.top, "A", "plain", 4727, 1)
    hood.top.hline(0, 8, 0, "S4"), hood.top.hline(0, 8, 2, "S4")
    for face in (hood.right, hood.left):
        face.hline(0, face.w - 1, 0, "S4")
    hood.back.vline(4, 0, 3, "P1")
    neck = g.piece("collar", "TORSO", (-4.5, -1.2, -2.7), (9, 2, 5), inflate=.06)
    solid(neck, "P", "plain", 4728, 2)
    for face in neck.sides:
        face.hline(0, face.w - 1, 0, "S4")
    neck.front.vline(4, 0, 1, "M3")
