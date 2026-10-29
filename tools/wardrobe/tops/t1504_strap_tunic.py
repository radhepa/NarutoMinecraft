"""Sword-Strap Tunic: a slate tunic with short sleeves and a stand collar, a wide leather sword
strap across the chest and back carrying a katana, forearms wrapped for grip, a cloth belt."""
from kit import belt
from kit_gekko import katana, sword_strap
from kit_shinobi import bandage
from paint import cap, fabric, strip_fabric
from kit import collar

META = {
    "name": "Sword-Strap Tunic",
    "gender": "unisex",
    "description": "Slate tunic with short sleeves and a stand collar, a wide sword strap, a katana, wrapped forearms.",
    "tags": ["shinobi", "genin"],
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "P", "weave", 15740, 2)
    cap(body, "P", seed=15740)
    body.front.vline(5, 0, 8, "P1")
    sword_strap(body.front, "L", rows=11)
    sword_strap(body.back, "L", rows=11, mirror=True)
    belt(g, "belt", y=9.4, role="D", buckle=None, inflate=.1)
    collar(g, "collar", "P", height=1, y=-.9)
    for side in ("right", "left"):
        arm = g.part(f"{side}_arm")
        strip_fabric(arm, "P", "weave", 15742 + (side == "left"), 2, 0, 3)
        fabric(arm.top, "P", "weave", 15742, 3)
        arm.strip.hline(0, arm.strip.w - 1, 3, "P1")
        bandage(arm.strip, 0, 6, arm.strip.w - 1, 10)
    katana(g, pivot=(-1.4, 2.4, 2.75))
