"""Wave-hem Tunic: the young guard's tunic. Short-sleeved, deep teal, a pale wave trim round the
hem and the sleeve ends, a dark cloth belt, forearms bound for the grip and the kokuto at the left
hip where a right hand draws it."""
from kit import belt
from kit_namiashi import hip_kokuto, wave_band
from kit_shinobi import bandage
from paint import cap, fabric, strip_fabric

META = {
    "name": "Wave-hem Tunic",
    "gender": "unisex",
    "description": "Short-sleeved teal tunic with a pale wave hem and cuffs, dark belt, bound forearms, kokuto at the hip.",
    "tags": ["shinobi", "genin"],
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "P", "weave", 20211, 2)
    cap(body, "P", seed=20211)
    for x, y in ((2, 0), (3, 0), (4, 0), (5, 0), (3, 1), (4, 1)):
        body.front.set(x, y, "D1")
    wave_band(body.strip, 10, "S", 2)
    belt(g, "belt", y=8.4, role="D", height=1, buckle=None, inflate=.1)
    for side in ("right", "left"):
        arm = g.part(f"{side}_arm")
        strip_fabric(arm, "P", "weave", 20212 + (side == "left"), 2, 0, 3)
        fabric(arm.top, "P", "weave", 20212, 3)
        wave_band(arm.strip, 3, "S", 2, phase=1)
        bandage(arm.strip, 0, 6, arm.strip.w - 1, 10)
    hip_kokuto(g)
