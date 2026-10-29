"""Shibi Robe: Shibi's long-skirted robe, collar standing to the nose, belted with a cloth sash,
and the gourd he carries his spare insects in slung across his back."""
from kit import belt
from kit_aburame import high_collar
from paint import cap, fabric, k, solid, strip_fabric

META = {
    "name": "Shibi Robe",
    "gender": "unisex",
    "description": "Mid-thigh robe with a collar to the nose, a cloth sash and an insect gourd on the back.",
    "tags": ["shinobi", "aburame", "robe"],
    "covers_waist": True,
}


def build(g):
    body, jacket = g.part("body"), g.part("jacket")
    strip_fabric(body, "P", "smooth", 10611, 2)
    cap(body, "P", seed=10611)
    strip_fabric(jacket, "P", "smooth", 10612, 2)
    cap(jacket, "P", seed=10612)
    f = jacket.front
    # The overlap of the robe from the right shoulder down to the sash.
    for y in range(9):
        f.set(min(7, 2 + y // 2), y, k("P", 1))
    jacket.back.vline(4, 1, 8, "P1")
    for side in ("right", "left"):
        arm, sleeve = g.part(f"{side}_arm"), g.part(f"{side}_sleeve")
        strip_fabric(arm, "P", "smooth", 10613, 2, 0, 11)
        fabric(arm.top, "P", "smooth", 10613, 3)
        strip_fabric(sleeve, "P", "smooth", 10614 + (side == "left"), 2, 0, 9)
        fabric(sleeve.top, "P", "smooth", 10614, 3)
        sleeve.strip.hline(0, sleeve.strip.w - 1, 9, "P1")
        strip_fabric(arm, "S", "smooth", 10616, 3, 10, 11)   # pale wraps at the wrist
    high_collar(g, "P", "smooth", 10620, front_top=-2.4, back_top=-4.4)
    sash = belt(g, "sash", y=8.6, role="A", height=2, buckle=None)
    sash.front.vline(4, 0, 1, "A1")
    for name, z, motion in (("skirt_front", -2.95, "flap_front"), ("skirt_back", 1.95, "flap_back")):
        skirt = g.piece(name, "TORSO", (-4.6, 0, 0), (9, 6, 1), pivot=(0, 11.4, z), motion=motion)
        solid(skirt, "P", "smooth", 10625 + (z > 0), 2)
        skirt.strip.hline(0, skirt.strip.w - 1, 5, k("P", 1))
        skirt.front.vline(4, 0, 5, k("P", 1))
    for name, x in (("skirt_right", -5.05), ("skirt_left", 4.05)):
        panel = g.piece(name, "TORSO", (0, 0, -2), (1, 5, 4), pivot=(x, 11.4, 0))
        solid(panel, "P", "smooth", 10628, 2)
    # The insect gourd: a big lower bulb, a waist, a small upper bulb and a stopper.
    for i, (w, h, y) in enumerate(((5, 4, 6.2), (3, 1, 5.2), (4, 3, 2.2))):
        part = g.piece(f"gourd_{i}", "TORSO", (-w / 2, 0, 0), (w, h, w - 1), pivot=(1.2, y, 2.3), rotation=(0, 0, -14))
        solid(part, "L", "smooth", 10630 + i, 3)
    stopper = g.piece("gourd_stopper", "TORSO", (-1, 0, 0), (2, 1, 2), pivot=(1.2, 1.2, 2.8), rotation=(0, 0, -14))
    solid(stopper, "S", "plain", 10634, 2)
    cord = g.piece("gourd_cord", "TORSO", (-.5, -6, -.5), (1, 12, 1), pivot=(0, 5.0, 2.25), rotation=(0, 0, -40))
    solid(cord, "A", "smooth", 10635, 2, edge=False)
