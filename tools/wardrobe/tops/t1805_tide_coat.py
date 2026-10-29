"""Tide Coat: a senior instructor's knee-length navy coat over the flak vest's undershirt, sand
lapels crossing at the chest, a sand sash and a deep hem printed with rolling sea-blue waves."""
from kit import belt, flaps
from kit_umino import waves
from paint import cap, fabric, strip_fabric

META = {
    "name": "Tide Coat",
    "gender": "unisex",
    "description": "Knee-length navy coat with sand lapels and sash, its hem printed with rolling sea-blue waves.",
    "tags": ["shinobi", "jonin", "coat"],
    "covers_waist": True,
}


def build(g):
    body, jacket = g.part("body"), g.part("jacket")
    strip_fabric(body, "K", "weave", 18481, 2)
    cap(body, "K", seed=18481)
    strip_fabric(jacket, "D", "twill", 18482, 2)
    cap(jacket, "D", texture="twill", seed=18482)
    f = jacket.front
    for i in range(6):
        f.set(1 + i, i, "S3"), f.set(6 - i, i, "S2") if i < 3 else None
    f.vline(4, 3, 11, "D1")
    belt(g, "sash", y=7.6, role="S", height=2, buckle=None, inflate=.1)
    for face in flaps(g, "coat_skirt", 8, "D", "twill", 18483, width=9, top=9.4, front_z=-2.8, back_z=1.8):
        waves(face, 4, "A3")
        waves(face, 6, "A2", phase=2)
        face.hline(0, face.w - 1, face.h - 1, "D0")
    for side in ("right", "left"):
        arm, sleeve = g.part(f"{side}_arm"), g.part(f"{side}_sleeve")
        strip_fabric(arm, "D", "twill", 18484, 2, 0, 11)
        fabric(arm.top, "D", "twill", 18484, 3)
        strip_fabric(sleeve, "D", "twill", 18485 + (side == "left"), 2, 0, 10)
        fabric(sleeve.top, "D", "twill", 18485, 3)
        waves(sleeve.strip, 8, "A3")
        sleeve.strip.hline(0, sleeve.strip.w - 1, 10, "S3")
