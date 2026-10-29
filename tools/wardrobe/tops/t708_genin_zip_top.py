"""Genin Zip Top: the young kunoichi's sleeveless purple top zipped to a soft collar, lavender
panels down the sides, a fitted hip-length hem, and bandages wound round both elbows and forearms."""
from kit import collar
from kit_yamanaka import wrapped
from paint import cap, fabric, strip_fabric

META = {
    "name": "Genin Zip Top",
    "gender": "unisex",
    "description": "Sleeveless purple zip top with lavender side panels, bandaged elbows and forearms.",
    "tags": ["shinobi", "yamanaka", "genin"],
}


def build(g):
    body, jacket = g.part("body"), g.part("jacket")
    strip_fabric(body, "P", "plain", 7850, 2)
    cap(body, "P", seed=7850)
    for face in (body.right, body.left):
        fabric(face, "S", "plain", 7851, 3, 1, 1, 2, 10)
    body.front.vline(4, 0, 10, "M3"), body.front.set(4, 0, "M4"), body.front.vline(3, 1, 10, "P1")
    strip_fabric(jacket, "P", "plain", 7852, 2, 10, 11)
    jacket.strip.hline(0, jacket.strip.w - 1, 10, "S3"), jacket.strip.hline(0, jacket.strip.w - 1, 11, "P1")
    for side in ("right", "left"):
        arm = g.part(f"{side}_arm")
        arm.strip.hline(0, arm.strip.w - 1, 0, "P2"), fabric(arm.top, "P", "plain", 7853, 3)
        wrapped(arm.strip, 0, 4, arm.strip.w - 1, 9)
        arm.strip.hline(0, arm.strip.w - 1, 4, "S2"), arm.strip.hline(0, arm.strip.w - 1, 9, "S2")
    neck = collar(g, "collar", "P", "plain", height=1, y=-.9)
    for face in neck.sides:
        face.hline(0, face.w - 1, 0, "S3")
    neck.front.set(4, 0, "M4")
