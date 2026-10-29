"""Merchant Happi: Kizashi's shop coat, a short beige happi worn open over a cream undershirt, its
front bands in the accent colour running from the collar to the hem, wide sleeves to the elbow and
a large white circle on the back for the family shop."""
from kit import arm_bone, arm_x, flaps
from kit_haruno import back_crest
from paint import cap, fabric, k, solid, strip_fabric

META = {
    "name": "Merchant Happi",
    "gender": "unisex",
    "description": "Short open beige happi coat with accent front bands, wide elbow sleeves, a large circle on the back.",
    "tags": ["shinobi", "coat"],
}


def build(g):
    body, jacket = g.part("body"), g.part("jacket")
    strip_fabric(body, "S", "weave", 19550, 2)
    cap(body, "S", texture="weave", seed=19550)
    strip_fabric(jacket, "P", "weave", 19551, 2)
    cap(jacket, "P", texture="weave", seed=19551)
    f = jacket.front
    for y in range(12):
        f.clear(3, y), f.clear(4, y)
        f.set(2, y, k("A", 2)), f.set(5, y, k("A", 2))
        f.set(1, y, k("A", 3)) if y < 3 else None
        f.set(6, y, k("A", 1)) if y < 3 else None
    for y in (5, 8):
        f.set(2, y, k("S", 4)), f.set(5, y, k("S", 4))
    jacket.strip.hline(0, jacket.strip.w - 1, 11, k("P", 1))
    for side in ("right", "left"):
        arm, sleeve = g.part(f"{side}_arm"), g.part(f"{side}_sleeve")
        strip_fabric(arm, "S", "weave", 19552, 2, 0, 6)
        strip_fabric(sleeve, "P", "weave", 19553 + (side == "left"), 2, 0, 5)
        fabric(sleeve.top, "P", "weave", 19553, 3)
        cuff = g.piece(f"{side}_sleeve_mouth", arm_bone(side), (arm_x(side) - .6, 2.5, -2.6), (5, 3, 5), inflate=.1, motion="sway")
        solid(cuff, "P", "weave", 19555 + (side == "left"), 2)
        for face in cuff.sides:
            face.hline(0, face.w - 1, 2, k("A", 2))
        cuff.bottom.fill(k("P", 0))
    back_crest(g, "P", texture="weave", seed=19557, size=12, pivot=(0, 1.2, 2.35))
    for face in flaps(g, "happi_hem", 2, "P", "weave", 19558, width=9, hem=k("A", 2), top=11.8, front_z=-2.9, back_z=2.0):
        face.vline(4, 0, 1, k("P", 0))
