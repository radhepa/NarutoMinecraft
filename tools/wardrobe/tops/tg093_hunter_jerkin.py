"""Hunter's Jerkin: a sleeveless leather jerkin laced up the front over a long-sleeved shirt, laced
leather bracers on the forearms and a short blade worn across the small of the back: for the trackers
and trappers of the deep forest."""
from kit import arm_bone, arm_x, sleeves
from kit_shinobi import tanto
from paint import fabric, solid, strip_fabric

META = {
    "name": "Hunter's Jerkin",
    "gender": "unisex",
    "description": "Sleeveless leather jerkin laced up the front over long sleeves, laced bracers, a blade at the back.",
    "tags": ["shinobi", "vest", "chunin"],
}


def build(g):
    body, jacket = g.part("body"), g.part("jacket")
    strip_fabric(body, "P", "weave", 35130, 2, 0, 10)
    fabric(body.top, "P", "weave", 35130, 3)
    sleeves(g, "P", "weave", 35131, 2, rows=(0, 10))
    strip_fabric(jacket, "L", "leather", 35132, 2, 1, 10)
    fabric(jacket.top, "L", "leather", 35132, 3)
    f = jacket.front
    f.vline(3, 1, 10, "L0"), f.vline(4, 1, 10, "L0")
    for y in range(2, 10, 2):
        f.set(3, y, "S3"), f.set(4, y + 1, "S3")
    f.set(3, 1, None), f.set(4, 1, None)
    jacket.strip.hline(0, jacket.strip.w - 1, 1, "L3")
    jacket.strip.hline(0, jacket.strip.w - 1, 10, "L1")
    for face in (jacket.right, jacket.left):
        face.vline(face.w // 2, 2, 9, "L1")
    for side in ("right", "left"):
        bracer = g.piece(f"{side}_bracer", arm_bone(side), (arm_x(side) - .3, 4.4, -2.3), (4, 4, 4), inflate=.1)
        solid(bracer, "L", "leather", 35133 + (side == "left"), 2)
        outer = bracer.right if side == "right" else bracer.left
        for y in range(0, 4, 2):
            outer.set(1, y, "S3"), outer.set(2, y + 1, "S3")
        for face in bracer.sides:
            face.hline(0, face.w - 1, 0, "L3")
    tanto(g, "back_blade", pivot=(-2.2, 9.0, 2.9), rotation=(0, 0, -78), length=7, wrap="L3")
