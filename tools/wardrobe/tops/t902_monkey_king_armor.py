"""Monkey King Armor: the Third Hokage's battle dress. A black combat suit under a dark plated
cuirass with a high collar, layered steel pauldrons, long steel forearm guards and the face of
Enma, the Monkey King, on the back plate."""
from kit_sarutobi import monkey, pauldron
from paint import cap, fabric, k, solid, strip_fabric

META = {
    "name": "Monkey King Armor",
    "gender": "unisex",
    "description": "Black combat suit, plated cuirass and high collar, steel pauldrons and arm guards, Enma on the back.",
    "tags": ["shinobi", "armor", "kage"],
}


def build(g):
    body, jacket = g.part("body"), g.part("jacket")
    strip_fabric(body, "K", "plain", 9740, 2)
    cap(body, "K", seed=9740)
    # The cuirass: horizontal lames over the chest and belly, a seam down the centre.
    strip_fabric(jacket, "P", "smooth", 9741, 2, 0, 9)
    cap(jacket, "P", texture="smooth", seed=9741)
    for y in (3, 6, 9):
        jacket.strip.hline(0, jacket.strip.w - 1, y - 1, "P0")
        jacket.strip.hline(0, jacket.strip.w - 1, y, "P3")
    jacket.strip.hline(0, jacket.strip.w - 1, 0, "P3")
    jacket.front.vline(4, 1, 9, "P1")
    for face in (jacket.right, jacket.left):
        face.vline(1, 0, 9, "K1"), face.vline(2, 0, 9, "K2")
    # Rivets on the lames.
    for y in (1, 4, 7):
        jacket.front.set(1, y, "M3"), jacket.front.set(6, y, "M3")
    # The belt of the suit.
    body.strip.hline(0, body.strip.w - 1, 10, "A2"), body.strip.hline(0, body.strip.w - 1, 11, "A1")
    plate = g.piece("back_monkey", "TORSO", (-6, 0, 0), (12, 11, 1), pivot=(0, 1.4, 2.3), scale=(.5, .5, .5))
    for face in plate.faces:
        fabric(face, "P", "smooth", 9742, 2)
    monkey(plate.back, 0, 0, k("A", 2))
    collar = g.piece("collar", "TORSO", (-4.5, -2.0, -2.7), (9, 2, 5), inflate=.1)
    solid(collar, "P", "smooth", 9743, 2)
    for face in collar.sides:
        face.hline(0, face.w - 1, 0, "P3")
    collar.front.vline(4, 0, 1, "P0")
    for side, bone in (("right", "RIGHT_ARM"), ("left", "LEFT_ARM")):
        arm = g.part(f"{side}_arm")
        strip_fabric(arm, "K", "plain", 9744 + (side == "left"), 2)
        fabric(arm.top, "K", "plain", 9744, 3), arm.bottom.fill("K1")
        pauldron(g, side, "P", 9746, trim=k("A", 2), tiers=1)
        # Forearm guards: steel splints on the outside and top of the forearm over the black sleeve.
        guard = g.part(f"{side}_sleeve")
        outer = guard.right if side == "right" else guard.left
        for face in (outer, guard.front):
            fabric(face, "M", "smooth", 9748, 1, 0, 5, face.w, 4)
            face.hline(0, face.w - 1, 5, "M3"), face.hline(0, face.w - 1, 8, "M0")
            face.vline(face.w // 2, 6, 7, "M2")
