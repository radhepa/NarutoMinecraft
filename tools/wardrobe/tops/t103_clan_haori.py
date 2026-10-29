"""Clan Haori: a forest-green haori to mid-thigh worn open over a dark kimono and a cream obi, wide
sleeves to the elbow, a braided cord tied across the chest and the Senju crest large on the back."""
from kit import belt
from kit_senju import crest
from paint import cap, fabric, solid, strip_fabric

META = {
    "name": "Clan Haori",
    "gender": "unisex",
    "description": "Open green haori over a dark kimono, elbow sleeves, chest cord, large Senju crest on the back.",
    "tags": ["shinobi", "senju", "robe"],
    "covers_waist": True,
}


def build(g):
    body, jacket = g.part("body"), g.part("jacket")
    # The kimono beneath: dark, wrapped left over right with a cream collar edge.
    strip_fabric(body, "D", "weave", 1530, 2)
    cap(body, "D", seed=1530)
    f = body.front
    for i in range(6):
        f.set(2 + i // 2 + (i % 2), i, "S3")
    belt(g, "obi", y=8.4, role="S", height=2, buckle=None, inflate=.1)
    # The haori: open front, a dark lining showing on the edges.
    strip_fabric(jacket, "P", "weave", 1531, 2)
    cap(jacket, "P", seed=1531)
    for y in range(12):
        for x in range(2, 6):
            jacket.front.clear(x, y)
        jacket.front.set(1, y, "P1"), jacket.front.set(6, y, "P1")
    jacket.strip.hline(0, jacket.strip.w - 1, 11, "P1")
    for name, x in (("right", -3.6), ("left", 2.6)):
        lapel = g.piece(f"lapel_{name}", "TORSO", (0, 0, 0), (1, 11, 1), pivot=(x, -.4, -2.75))
        solid(lapel, "P", "weave", 1532, 2)
        lapel.front.vline(0, 0, 10, "P3")
    cord = g.piece("chest_cord", "TORSO", (-1.5, 0, 0), (3, 1, 1), pivot=(0, 4.6, -2.9))
    solid(cord, "A", "plain", 1533, 3, edge=False)
    knot = g.piece("chest_cord_knot", "TORSO", (-.5, 0, 0), (1, 2, 1), pivot=(0, 4.6, -3.1))
    solid(knot, "A", "plain", 1534, 2, edge=False)
    back = g.piece("back_crest", "TORSO", (-4, 0, 0), (8, 8, 1), pivot=(0, 1.4, 2.3))
    for face in back.faces:
        fabric(face, "P", "weave", 1535, 2)
    crest(back.back, 0, 0, "S3", bar="P0")
    # Sleeves: dark kimono to the wrist, the haori's wide sleeve to the elbow.
    for side, bone, ox in (("right", "RIGHT_ARM", -3.0), ("left", "LEFT_ARM", -1.0)):
        arm, sleeve = g.part(f"{side}_arm"), g.part(f"{side}_sleeve")
        strip_fabric(arm, "D", "weave", 1536, 2, 0, 10)
        fabric(arm.top, "D", "weave", 1536, 3)
        strip_fabric(sleeve, "P", "weave", 1537, 2, 0, 3)
        fabric(sleeve.top, "P", "weave", 1537, 3)
        wide = g.piece(f"{side}_haori_sleeve", bone, (ox - .7, 1.5, -2.8), (5, 5, 6), inflate=.12)
        solid(wide, "P", "weave", 1538, 2)
        for face in wide.sides:
            face.hline(0, face.w - 1, 4, "P1")
        wide.bottom.fill("D1")
    # Skirts to mid-thigh: open front halves and the back.
    for name, x0, w, z, motion in (("skirt_front_right", -4.6, 3, -2.95, "flap_front"),
                                   ("skirt_front_left", 1.6, 3, -2.95, "flap_front"),
                                   ("skirt_back", -4.6, 9, 1.95, "flap_back")):
        skirt = g.piece(name, "TORSO", (0, 0, 0), (w, 6, 1), pivot=(x0, 11.4, z), motion=motion)
        solid(skirt, "P", "weave", 1539 + len(name) % 3, 2)
    for name, x in (("skirt_right", -5.05), ("skirt_left", 4.05)):
        panel = g.piece(name, "TORSO", (0, 0, -2), (1, 5, 4), pivot=(x, 11.4, 0))
        solid(panel, "P", "weave", 1542, 2)
