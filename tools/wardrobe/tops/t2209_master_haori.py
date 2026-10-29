"""Master's Haori: the toryo, the master builder, in a long indigo haori to the knee over a cream
kimono, the collar band lettered down both edges in the guild's marks, a cedar-red lining at the
cuffs, the crest large and white on the back and the steel square tucked through the obi."""
from kit import belt
from kit_kinoshita import back_crest, square
from paint import cap, fabric, solid, strip_fabric

META = {
    "name": "Master's Haori",
    "gender": "unisex",
    "description": "Knee-length indigo haori with lettered collar bands, cedar lining, white crest; a square in the obi.",
    "tags": ["shinobi", "kinoshita", "robe", "jonin"],
    "covers_waist": True,
}


def build(g):
    body, jacket = g.part("body"), g.part("jacket")
    strip_fabric(body, "S", "weave", 22461, 3)
    cap(body, "S", base=3, seed=22461)
    f = body.front
    for i in range(6):
        f.set(2 + i // 2 + (i % 2), i, "S1")
    belt(g, "obi", y=8.2, role="D", height=2, buckle=None, inflate=.1)
    square(g, "square", (-1.6, 7.0, -2.8), (0, 0, 0), long=7, short=6)
    # The haori, open down the front, the collar band lettered in the guild's marks.
    strip_fabric(jacket, "P", "weave", 22462, 2)
    cap(jacket, "P", seed=22462)
    for y in range(12):
        for x in range(2, 6):
            jacket.front.clear(x, y)
    for name, x in (("right", -3.6), ("left", 2.6)):
        band = g.piece(f"collar_band_{name}", "TORSO", (0, 0, 0), (1, 18, 1), pivot=(x, -.4, -2.75))
        solid(band, "K", "weave", 22463, 2, edge=False)
        for y in range(1, 17, 3):
            band.front.set(0, y, "S3"), band.front.set(0, y + 1, "S2")
    back_crest(g, "P", "S4", 22464, y=1.0)
    for side, bone, ox in (("right", "RIGHT_ARM", -3.0), ("left", "LEFT_ARM", -1.0)):
        arm, sleeve = g.part(f"{side}_arm"), g.part(f"{side}_sleeve")
        strip_fabric(arm, "S", "weave", 22465, 3, 0, 10)
        fabric(arm.top, "S", "weave", 22465, 4)
        strip_fabric(sleeve, "P", "weave", 22466, 2, 0, 3)
        fabric(sleeve.top, "P", "weave", 22466, 3)
        wide = g.piece(f"{side}_haori_sleeve", bone, (ox - .7, 1.5, -2.8), (5, 6, 6), inflate=.12)
        solid(wide, "P", "weave", 22467, 2)
        for face in wide.sides:
            face.hline(0, face.w - 1, 5, "A2")
        wide.bottom.fill("A1")
    for name, x0, w, z, motion in (("skirt_front_right", -4.6, 3, -2.95, "flap_front"),
                                   ("skirt_front_left", 1.6, 3, -2.95, "flap_front"),
                                   ("skirt_back", -4.6, 9, 1.95, "flap_back")):
        skirt = g.piece(name, "TORSO", (0, 0, 0), (w, 7, 1), pivot=(x0, 11.4, z), motion=motion)
        solid(skirt, "P", "weave", 22468, 2)
        (skirt.front if z < 0 else skirt.back).hline(0, w - 1, 6, "A2")
    for name, x in (("skirt_right", -5.05), ("skirt_left", 4.05)):
        panel = g.piece(name, "TORSO", (0, 0, -2), (1, 6, 4), pivot=(x, 11.4, 0))
        solid(panel, "P", "weave", 22469, 2)
