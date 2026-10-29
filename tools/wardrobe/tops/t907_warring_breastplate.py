"""Warring Breastplate: Sasuke Sarutobi in the Warring States. A wrapped top of thick dark cloth, a
red-lacquered breastplate held by leather shoulder straps, a cord belt and gauntlets of leather
scales and thin iron plates."""
from paint import cap, fabric, k, solid, strip_fabric

META = {
    "name": "Warring Breastplate",
    "gender": "unisex",
    "description": "Thick dark wrapped top, red-lacquered breastplate on shoulder straps, scaled gauntlets.",
    "tags": ["shinobi", "armor"],
}


def build(g):
    body, jacket = g.part("body"), g.part("jacket")
    strip_fabric(body, "P", "weave", 9820, 1)
    cap(body, "P", seed=9820, base=1)
    for i in range(5):
        body.front.set(1 + i, i, "P3")
    # The breastplate: lacquer over the chest and belly, a ridge down the centre, laced lower edge.
    strip_fabric(jacket, "A", "smooth", 9821, 2, 1, 8)
    cap(jacket, "A", texture="smooth", seed=9821)
    for face in (jacket.right, jacket.left):
        for y in range(jacket.h):
            for x in range(face.w):
                face.set(x, y, None)
    for face in (jacket.front, jacket.back):
        for x in range(face.w):
            face.set(x, 0, None)
        face.hline(0, 7, 1, "A3"), face.hline(0, 7, 8, "A0")
        face.vline(0, 1, 8, "A1"), face.vline(7, 1, 8, "A1")
        for x in (1, 3, 4, 6):
            face.set(x, 8, "L3")
    jacket.front.vline(3, 2, 7, "A4"), jacket.front.vline(4, 2, 7, "A1")
    jacket.top.fill(None), jacket.bottom.fill(None)
    # Leather shoulder straps over the breastplate.
    for x in (-3.0, 2.0):
        strap = g.piece(f"strap_{'right' if x < 0 else 'left'}", "TORSO", (0, 0, 0), (1, 1, 5), pivot=(x, -.4, -2.5),
                        inflate=.3)
        solid(strap, "L", "leather", 9822, 2)
    # Cord belt.
    body.strip.hline(0, body.strip.w - 1, 9, "S2"), body.strip.hline(0, body.strip.w - 1, 10, "S3")
    body.front.set(3, 10, "S1"), body.front.set(3, 11, "S2")
    for side, bone in (("right", "RIGHT_ARM"), ("left", "LEFT_ARM")):
        arm, sleeve = g.part(f"{side}_arm"), g.part(f"{side}_sleeve")
        strip_fabric(arm, "P", "weave", 9823, 1, 0, 11)
        fabric(arm.top, "P", "weave", 9823, 2), arm.bottom.fill(k("K", 1))
        strip_fabric(sleeve, "L", "leather", 9824, 2, 5, 10)
        for y in range(5, 11):
            for x in range(sleeve.strip.w):
                if (x + (y % 2) * 2) % 4 == 0:
                    sleeve.strip.set(x, y, "M2" if y % 2 else "L1")
        sleeve.strip.hline(0, sleeve.strip.w - 1, 5, "M3")
        plate = g.piece(f"{side}_shoulder_lames", bone, (-3.5 if side == "right" else -.5, -2.6, -2.6), (5, 3, 5),
                        inflate=.05)
        solid(plate, "A", "smooth", 9825, 2)
        for f in plate.sides:
            f.hline(0, f.w - 1, 0, "A3"), f.hline(0, f.w - 1, 2, "L2")
