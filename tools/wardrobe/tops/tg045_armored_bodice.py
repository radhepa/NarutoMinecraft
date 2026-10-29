"""Armored Bodice: a laced leather bodice over a long-sleeved mesh undershirt, a single lacquered
pauldron on the left shoulder and leather bracers: a jonin kunoichi's light armor."""
from kit import arm_x
from kit_shinobi import mesh
from paint import cap, fabric, solid, strip_fabric

META = {
    "name": "Armored Bodice",
    "gender": "unisex",
    "description": "Laced leather bodice over a mesh undershirt, one lacquered pauldron, leather bracers.",
    "tags": ["shinobi", "jonin", "armor"],
}


def build(g):
    body, jacket = g.part("body"), g.part("jacket")
    strip_fabric(body, "K", "plain", 33080, 1)
    mesh(body.strip, 0, 0, body.strip.w - 1, 3, "K3")
    fabric(body.top, "K", "plain", 33080, 2)
    strip_fabric(jacket, "L", "leather", 33081, 2, 3, 10)
    for y in (3, 10):
        jacket.strip.hline(0, jacket.strip.w - 1, y, "L3" if y == 3 else "L1")
    for y in range(4, 10):
        jacket.front.set(3, y, "L0"), jacket.front.set(4, y, "L0")
        if y % 2 == 0:
            jacket.front.set(3, y, "S3"), jacket.front.set(4, y - 1, "S3")
    for face in (jacket.right, jacket.left):
        face.vline(1, 4, 9, "M3")
    for side in ("right", "left"):
        arm = g.part(f"{side}_arm")
        strip_fabric(arm, "K", "plain", 33082, 1, 0, 6)
        mesh(arm.strip, 0, 0, arm.strip.w - 1, 6, "K3")
        fabric(arm.top, "K", "plain", 33082, 2)
        sleeve = g.part(f"{side}_sleeve")
        strip_fabric(sleeve, "L", "leather", 33083, 2, 6, 10)
        sleeve.strip.hline(0, 15, 6, "L3"), sleeve.strip.hline(0, 15, 8, "M3")
    pad = g.piece("pauldron", "LEFT_ARM", (arm_x("left") - .6, -2.6, -2.6), (5, 3, 5))
    solid(pad, "P", "smooth", 33084, 2)
    cap(pad, "P", texture="smooth", seed=33084)
    for face in pad.sides:
        face.hline(0, face.w - 1, 1, "A2")
