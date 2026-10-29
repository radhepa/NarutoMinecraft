"""Vest Over Tee: a simple open cloth vest with two patch pockets worn over a long-sleeved tee, the
sleeves pushed up to the elbow: the genin's first proper mission kit."""
from kit_academy import shirt
from paint import fabric, k, strip_fabric

META = {
    "name": "Vest Over Tee",
    "gender": "unisex",
    "description": "Open cloth vest with patch pockets over a long-sleeved tee, sleeves pushed to the elbow.",
    "tags": ["shinobi", "genin", "vest"],
}


def build(g):
    body, arms = shirt(g, "S", "plain", 31075, sleeve=6)
    for arm in arms:
        arm.strip.hline(0, arm.strip.w - 1, 5, "S3"), arm.strip.hline(0, arm.strip.w - 1, 6, "S1")
    body.front.hline(3, 4, 0, "S1")
    jacket = g.part("jacket")
    strip_fabric(jacket, "P", "twill", 31076, 2)
    fabric(jacket.top, "P", "twill", 31076, 3)
    f = jacket.front
    for y in range(12):
        for x in (3, 4):
            f.clear(x, y)
    for y in range(3):
        f.clear(2, y), f.clear(5, y)
    f.vline(2, 3, 11, k("A", 2)), f.vline(5, 3, 11, k("A", 2))
    for y in range(3):
        f.set(1, y, "A2"), f.set(6, y, "A2")
    jacket.top.rect(2, 0, 4, 4, None)
    for face in jacket.sides:
        face.hline(0, face.w - 1, 11, "P1")
    # Two patch pockets, a flap seam and a button on each.
    for x0 in (0, 6):
        for y in (6, 7, 8):
            for x in (x0, x0 + 1) if x0 == 0 else (x0, x0 + 1):
                f.set(x, y, "P3" if y == 6 else "P2")
        f.set(x0 + (1 if x0 == 0 else 0), 6, "M3")
    for face in (jacket.right, jacket.left):
        face.vline(1, 1, 10, "P1")
