"""Infiltration Top: a dark fitted long-sleeved top with a cowl neck, seams that curve to the
waist, a narrow sash and gloves with steel knuckle plates: night work."""
from kit import belt, collar
from paint import cap, strip_fabric

META = {
    "name": "Infiltration Top",
    "gender": "unisex",
    "description": "Dark fitted long-sleeved top, cowl neck, shaped seams, narrow sash, plated gloves.",
    "tags": ["shinobi", "chunin"],
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "K", "smooth", 33160, 3)
    cap(body, "K", texture="smooth", seed=33160, base=3)
    f = body.front
    for y in range(3, 9):
        f.set(1, y, "K2"), f.set(6, y, "K4")
    for face in (body.right, body.left):
        face.vline(1, 2, 11, "K2")
    for side in ("right", "left"):
        arm = g.part(f"{side}_arm")
        strip_fabric(arm, "K", "smooth", 33161, 3, 0, 9)
        cap(arm, "K", texture="smooth", seed=33161, base=3)
        strip_fabric(arm, "K", "leather", 33162, 1, 10, 11)
        arm.front.hline(0, 3, 10, "M3")
    sash = belt(g, "sash", y=9.4, role="P", height=1, buckle=None, inflate=.1)
    sash.front.set(2, 0, "P4")
    cowl = collar(g, "cowl", "K", "smooth", base=3, height=2, y=-1.2, inflate=.3)
    for face in cowl.sides:
        face.hline(0, face.w - 1, 1, "K2")
