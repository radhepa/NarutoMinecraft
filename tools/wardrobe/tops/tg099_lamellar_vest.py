"""Lamellar Vest: rows of small hardened-leather plates laced together into a vest over a
long-sleeved shirt, shoulder plates tied over the upper arms and a cord belt: old armor from the
border wars, still the best a clanless jonin can afford."""
from kit import arm_bone, arm_x, sleeves
from paint import fabric, k, solid, strip_fabric

META = {
    "name": "Lamellar Vest",
    "gender": "unisex",
    "description": "Laced rows of small leather plates over long sleeves, tied shoulder plates and a cord belt.",
    "tags": ["shinobi", "armor", "vest", "jonin"],
}


def lamellae(face, y0, y1, role="L"):
    """Small plates in staggered rows: each plate 2 texels wide and 2 tall with a shaded edge, a dark
    lacing row with pale cord stitches under every row."""
    for y in range(y0, y1 + 1):
        r, row = (y - y0) % 3, (y - y0) // 3
        for x in range(face.w):
            if r == 2:
                face.set(x, y, "S2" if (x + row) % 2 == 0 else k(role, 0))
            elif (x + row) % 2 == 1:
                face.set(x, y, k(role, 1))
            else:
                face.set(x, y, k(role, 3 if r == 0 else 2))


def build(g):
    body, jacket = g.part("body"), g.part("jacket")
    strip_fabric(body, "P", "weave", 35190, 2, 0, 10)
    fabric(body.top, "P", "weave", 35190, 3)
    sleeves(g, "P", "weave", 35191, 2, rows=(0, 10), cuff="P1", cuff_row=10)
    lamellae(jacket.strip, 1, 9)
    jacket.strip.hline(0, jacket.strip.w - 1, 10, "L1")
    fabric(jacket.top, "L", "leather", 35192, 2)
    jacket.strip.hline(0, jacket.strip.w - 1, 1, "L1")
    jacket.front.vline(4, 1, 9, "L0")
    for side in ("right", "left"):
        plate = g.piece(f"{side}_shoulder_plate", arm_bone(side), (arm_x(side) - .6, -2.4, -2.6), (5, 4, 5), inflate=.05)
        solid(plate, "L", "leather", 35193 + (side == "left"), 2)
        for face in plate.sides:
            lamellae(face, 1, 3)
            face.hline(0, face.w - 1, 3, "L1")
            face.hline(0, face.w - 1, 0, "L3")
    belt = g.piece("cord_belt", "TORSO", (-4.5, 9.6, -2.5), (9, 1, 5), inflate=.12)
    for face in belt.faces:
        for x in range(face.w):
            for y in range(face.h):
                face.set(x, y, "A3" if (x + y) % 2 else "A1")
