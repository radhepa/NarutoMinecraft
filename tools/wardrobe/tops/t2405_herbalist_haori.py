"""Herbalist Haori: a short haori printed all over with sprigs of lily of the valley, worn open over
a leaf-green kosode, with white collar bands down the front, broad sleeves to the elbow and a
violet cord tied across the chest."""
from kit_suzuran import bell_print
from paint import cap, fabric, solid, strip_fabric

META = {
    "name": "Herbalist Haori",
    "gender": "unisex",
    "description": "Open haori printed with bell sprigs over a green kosode, white collar bands, a violet chest cord.",
    "tags": ["shinobi", "robe"],
    "covers_waist": True,
}


def build(g):
    body, jacket = g.part("body"), g.part("jacket")
    strip_fabric(body, "D", "weave", 24541, 2)
    cap(body, "D", seed=24541)
    for y in range(4):
        body.front.set(3 - y // 2, y, "S3")
    strip_fabric(jacket, "P", "weave", 24542, 2)
    cap(jacket, "P", seed=24542)
    for face in jacket.sides:
        bell_print(face, "P", 24543 + face.x0)
    for y in range(12):
        for x in range(2, 6):
            jacket.front.clear(x, y)
        jacket.front.set(1, y, "S3"), jacket.front.set(6, y, "S3")
    for i, x in enumerate((-1.6, .6)):
        cord = g.piece(f"himo_{i}", "TORSO", (0, 0, 0), (1, 1, 1), pivot=(x, 5.0, -2.55), scale=(1, .6, .6))
        solid(cord, "A", "smooth", 24544, 3, edge=False)
    for side in ("right", "left"):
        arm = g.part(f"{side}_arm")
        strip_fabric(arm, "D", "weave", 24545, 2, 0, 10)
        fabric(arm.top, "D", "weave", 24545, 3)
        bone = "RIGHT_ARM" if side == "right" else "LEFT_ARM"
        ox = -3.0 if side == "right" else -1.0
        cuff = g.piece(f"{side}_haori_sleeve", bone, (ox - .7, -2.3, -2.7), (5, 8, 5), inflate=.15)
        solid(cuff, "P", "weave", 24546, 2)
        for face in cuff.sides:
            bell_print(face, "P", 24547 + face.x0, rows=(1,))
            face.hline(0, face.w - 1, 7, "S3")
        fabric(cuff.top, "P", "weave", 24546, 3)
        cuff.bottom.fill("P0")
    for name, x, w in (("right", -3.6, 1), ("left", 2.6, 1)):
        lapel = g.piece(f"lapel_{name}", "TORSO", (0, 0, 0), (w, 13, 1), pivot=(x, -.4, -2.75))
        solid(lapel, "S", "weave", 24548, 3)
    for name, x0, w, z, motion, face_name in (("skirt_front_right", -4.6, 3, -2.95, "flap_front", "front"),
                                               ("skirt_front_left", 1.6, 3, -2.95, "flap_front", "front"),
                                               ("skirt_back", -4.6, 9, 1.95, "flap_back", "back")):
        skirt = g.piece(name, "TORSO", (0, 0, 0), (w, 6, 1), pivot=(x0, 11.4, z), motion=motion)
        solid(skirt, "P", "weave", 24549, 2)
        bell_print(getattr(skirt, face_name), "P", 24550 + w, rows=(1,), every=4)
        getattr(skirt, face_name).hline(0, w - 1, 5, "S3")
