"""Hooded Longcoat: Shino's Shippuden coat, olive and closed to the knee, its collar standing to the
nose, the deep hood thrown back on the shoulders and a satchel strap across the chest."""
from kit_aburame import BEETLE, glyph, high_collar, hood_down
from paint import cap, fabric, k, solid, strip_fabric

META = {
    "name": "Hooded Longcoat",
    "gender": "unisex",
    "description": "Knee-length olive coat, collar to the nose, hood down on the shoulders, satchel strap.",
    "tags": ["shinobi", "aburame", "coat"],
    "covers_waist": True,
}

SLING = dict(pivot=(0, 5.0, -2.7), rotation=(0, 0, 34))


def build(g):
    body, jacket = g.part("body"), g.part("jacket")
    strip_fabric(body, "P", "smooth", 10531, 2)
    cap(body, "P", seed=10531)
    strip_fabric(jacket, "P", "smooth", 10532, 2)
    cap(jacket, "P", seed=10532)
    f = jacket.front
    f.vline(4, 0, 11, "P0"), f.vline(3, 0, 11, "P3")
    for y in (2, 5, 8):
        f.set(5, y, "M3")
    jacket.back.vline(4, 2, 11, "P1")
    for side in ("right", "left"):
        arm, sleeve = g.part(f"{side}_arm"), g.part(f"{side}_sleeve")
        strip_fabric(arm, "P", "smooth", 10533, 2, 0, 11)
        fabric(arm.top, "P", "smooth", 10533, 3)
        strip_fabric(sleeve, "P", "smooth", 10534 + (side == "left"), 2, 0, 11)
        fabric(sleeve.top, "P", "smooth", 10534, 3)
        sleeve.strip.hline(0, sleeve.strip.w - 1, 10, "P1"), sleeve.strip.hline(0, sleeve.strip.w - 1, 11, "P0")
        (sleeve.right if side == "right" else sleeve.left).vline(1, 2, 9, "P1")
    high_collar(g, "P", "smooth", 10540)
    hood_down(g, "P", "smooth", 10545)
    # The skirts of the coat: closed at the front with an overlap seam, slit behind.
    for name, z, motion, face in (("skirt_front", -2.95, "flap_front", "front"), ("skirt_back", 1.95, "flap_back", "back")):
        skirt = g.piece(name, "TORSO", (-4.6, 0, 0), (9, 8, 1), pivot=(0, 11.4, z), motion=motion)
        solid(skirt, "P", "smooth", 10550 + (z > 0), 2)
        side_face = getattr(skirt, face)
        side_face.hline(0, 8, 0, k("P", 3))
        side_face.vline(4, 1, 7, k("P", 0 if z < 0 else 1))
        skirt.strip.hline(0, skirt.strip.w - 1, 7, k("P", 1))
    for name, x in (("skirt_right", -5.05), ("skirt_left", 4.05)):
        panel = g.piece(name, "TORSO", (0, 0, -2), (1, 7, 4), pivot=(x, 11.4, 0))
        solid(panel, "P", "smooth", 10553, 2)
    strap = g.piece("sling", "TORSO", (-.5, -7, -.5), (1, 14, 1), **SLING)
    solid(strap, "L", "leather", 10555, 2, edge=False)
    bag = g.piece("satchel", "TORSO", (-1.5, 0, -1), (3, 3, 2), pivot=(3.4, 9.0, -1.0))
    solid(bag, "L", "leather", 10556, 2)
    bag.front.hline(0, 2, 0, "L3"), bag.front.set(1, 1, "M3")
    badge = g.piece("beetle_badge", "TORSO", (0, 0, 0), (8, 8, 1), pivot=(-1.2, 4.6, 2.3), scale=(.5, .5, .5))
    for face in badge.faces:
        fabric(face, "P", "smooth", 10557, 2)
    glyph(badge.back, BEETLE, 0, 0, {"#": "A2", "+": "A0"})
