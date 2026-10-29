"""Crescent Dancer: the Dance of the Crescent Moon's fitted jacket: a high crossed collar trimmed in
silver, a silver crescent on the left breast, close sleeves with silver cuffs, a sash at the waist and
a katana thrust through it on the left hip."""
from kit import belt, collar
from kit_gekko import crescent, hip_katana
from paint import cap, fabric, strip_fabric

META = {
    "name": "Crescent Dancer",
    "gender": "unisex",
    "description": "Fitted jacket with a silver-trimmed crossed collar, a crescent on the breast, a katana at the hip.",
    "tags": ["shinobi"],
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "P", "twill", 15750, 2)
    cap(body, "P", texture="twill", seed=15750)
    f = body.front
    # Crossed front: the left panel over the right, its edge trimmed in silver.
    for x, y in ((2, 0), (3, 1), (4, 0), (4, 1)):
        f.set(x, y, "S3")
    f.vline(4, 2, 8, "S3"), f.vline(5, 1, 8, "P1")
    for side in ("right", "left"):
        arm = g.part(f"{side}_arm")
        strip_fabric(arm, "P", "twill", 15752 + (side == "left"), 2, 0, 10)
        fabric(arm.top, "P", "twill", 15752, 3)
        arm.strip.hline(0, arm.strip.w - 1, 9, "S3"), arm.strip.hline(0, arm.strip.w - 1, 10, "S2")
    collar(g, "collar", "P", texture="twill", height=2, y=-1.4)
    belt(g, "sash", y=8.8, role="D", buckle=None, height=2, inflate=.12)
    crescent(g, "breast_crescent", (-2.2, 3.4, -2.32), role="P", mark="S4", face="front", flip=True)
    hip_katana(g, side="left")
