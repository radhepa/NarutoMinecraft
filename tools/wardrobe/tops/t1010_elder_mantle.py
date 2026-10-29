"""Elder Mantle: the clan elders' long dusty coat after Muta, a heavy shoulder mantle over it, the
collar standing to the nose, and a corded insect jar at the hip under the mantle's edge."""
from kit_aburame import high_collar
from paint import cap, fabric, k, solid, strip_fabric

META = {
    "name": "Elder Mantle",
    "gender": "unisex",
    "description": "Long dusty coat under a heavy shoulder mantle, collar to the nose, an insect jar at the hip.",
    "tags": ["shinobi", "aburame", "coat"],
    "covers_waist": True,
}


def build(g):
    body, jacket = g.part("body"), g.part("jacket")
    strip_fabric(body, "P", "smooth", 10691, 2)
    cap(body, "P", seed=10691)
    strip_fabric(jacket, "P", "smooth", 10692, 2)
    cap(jacket, "P", seed=10692)
    jacket.front.vline(4, 0, 11, "P0")
    for y in (6, 8, 10):
        jacket.front.set(3, y, "L3")
    for side in ("right", "left"):
        arm, sleeve = g.part(f"{side}_arm"), g.part(f"{side}_sleeve")
        strip_fabric(arm, "P", "smooth", 10693, 2, 0, 11)
        fabric(arm.top, "P", "smooth", 10693, 3)
        strip_fabric(sleeve, "P", "smooth", 10694 + (side == "left"), 2, 4, 11)
        sleeve.strip.hline(0, sleeve.strip.w - 1, 10, "L2"), sleeve.strip.hline(0, sleeve.strip.w - 1, 11, "L1")
    high_collar(g, "P", "smooth", 10700, front_top=-2.4, back_top=-4.6)
    # The mantle: a cape to the elbow all round, hemmed in leather, closed at the throat.
    mantle = g.piece("mantle", "TORSO", (-5.5, -.4, -3.1), (11, 6, 6))
    solid(mantle, "S", "smooth", 10705, 1)
    for face in mantle.sides:
        for x in range(1, face.w - 1, 3):
            face.vline(x, 1, face.h - 2, k("S", 0))
        face.hline(0, face.w - 1, face.h - 1, "L1")
    mantle.front.vline(5, 0, 5, "S0")
    for name, z, motion in (("skirt_front", -2.95, "flap_front"), ("skirt_back", 1.95, "flap_back")):
        skirt = g.piece(name, "TORSO", (-4.6, 0, 0), (9, 9, 1), pivot=(0, 11.4, z), motion=motion)
        solid(skirt, "P", "smooth", 10706 + (z > 0), 2)
        skirt.strip.hline(0, skirt.strip.w - 1, 8, "L1")
        skirt.front.vline(4, 0, 8, "P0")
    for name, x in (("skirt_right", -5.05), ("skirt_left", 4.05)):
        panel = g.piece(name, "TORSO", (0, 0, -2), (1, 8, 4), pivot=(x, 11.4, 0))
        solid(panel, "P", "smooth", 10708, 2)
    jar = g.piece("insect_jar", "TORSO", (-1, 0, -1), (2, 3, 2), pivot=(4.9, 9.4, -1.0))
    solid(jar, "M", "smooth", 10709, 3)
    cork = g.piece("jar_cork", "TORSO", (-.5, -1, -.5), (1, 1, 1), pivot=(4.9, 9.4, -1.0))
    solid(cork, "L", "plain", 10710, 3, edge=False)
