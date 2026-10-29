"""Knit Cardigan: the schoolteacher's and the grandparent's cardigan, a chunky stocking-stitch knit
worn open over a pale collared shirt, ribbed at the cuffs and hem, with two patch pockets and a row
of wooden buttons down the band."""
from kit_household import arm_cloth
from paint import cap, fabric, solid, strip_fabric

META = {
    "name": "Knit Cardigan",
    "gender": "unisex",
    "description": "Open chunky-knit cardigan over a pale collared shirt, ribbed cuffs and hem, patch pockets, wooden buttons.",
    "tags": ["civilian", "casual", "jacket"],
}


def build(g):
    body, jacket = g.part("body"), g.part("jacket")
    strip_fabric(body, "S", "plain", 37040, 3)
    cap(body, "S", seed=37040, base=3)
    f = body.front
    f.set(2, 0, "S4"), f.set(5, 0, "S4"), f.set(3, 0, "S2"), f.set(4, 0, "S2"), f.set(3, 1, "S2")
    for y in (3, 6, 9):
        f.set(4, y, "S1")
    strip_fabric(jacket, "P", "knit", 37041, 2)
    fabric(jacket.top, "P", "knit", 37041, 3)
    for x in (3, 4):
        jacket.front.vline(x, 0, 11, None)
    jacket.front.vline(2, 0, 11, "P3"), jacket.front.vline(5, 0, 11, "P3")
    for y in (2, 5, 8):
        jacket.front.set(2, y, "L3")
    for x0 in (0, 6):
        jacket.front.hline(x0, x0 + 1, 7, "P1")
        jacket.front.rect(x0, 8, 2, 2, "P3")
    jacket.strip.hline(0, jacket.strip.w - 1, 10, "P1"), jacket.strip.hline(0, jacket.strip.w - 1, 11, "P1")
    for x in range(0, jacket.strip.w, 2):
        jacket.strip.set(x, 11, "P0")
    for arm in arm_cloth(g, "P", "knit", 37043, rows=(0, 9), cuff="P1"):
        for x in range(0, arm.strip.w, 2):
            arm.strip.set(x, 10, "P0")
    shirt_collar = g.piece("shirt_collar", "TORSO", (-2.5, 0, 0), (5, 1, 1), pivot=(0, -.2, -2.55))
    solid(shirt_collar, "S", "plain", 37046, 4, edge=False)
