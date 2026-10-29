"""Pullover Hoodie: a roomy pullover with the hood pushed back, a big kangaroo pocket across the belly,
drawstrings at the neck and ribbed cuffs and hem: the Academy kid who is always cold."""
from kit_academy import drawstrings, hood_down, ribbed, shirt
from paint import strip_fabric

META = {
    "name": "Pullover Hoodie",
    "gender": "unisex",
    "description": "Roomy pullover hoodie, hood down with a contrast lining, a kangaroo pocket and ribbed cuffs.",
    "tags": ["shinobi", "genin"],
}


def build(g):
    body, arms = shirt(g, "P", "plain", 31015, sleeve=10)
    ribbed(body, (10, 11), "P")
    f = body.front
    # The kangaroo pocket: one panel across the belly, open at both sides, a seam along the top.
    for x in range(1, 7):
        f.set(x, 5, "P3")
        for y in (6, 7, 8):
            f.set(x, y, "P2")
    for y in (6, 7, 8):
        f.set(1, y, "P0"), f.set(6, y, "P0")
    f.hline(2, 5, 9, "P1")
    for face in (body.right, body.left):
        face.vline(1, 2, 9, "P1")
    for arm in arms:
        ribbed(arm, (9, 10), "P")
        arm.strip.hline(0, arm.strip.w - 1, 5, "P1")
    jacket = g.part("jacket")
    strip_fabric(jacket, "P", "plain", 31016, 2, 9, 11)
    ribbed(jacket, (10, 11), "P")
    hood_down(g, "P", "A", 31017, depth=2.9, tilt=20)
    drawstrings(g, "S3", 31019)
