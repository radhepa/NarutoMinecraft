"""Cloud Haori: a short haori jacket painted with ink-wash clouds, worn open over a dark kosode. The
cream collar band runs down both front edges, a braided cord ties across the chest, the sleeves are
broad to the elbow and the Kurama crest is painted on the back."""
from kit_kurama import back_crest, ink_clouds
from paint import cap, fabric, solid, strip_fabric

META = {
    "name": "Cloud Haori",
    "gender": "unisex",
    "description": "Open haori painted with ink-wash clouds over a dark kosode, cream collar bands, chest cord, crest.",
    "tags": ["shinobi", "robe"],
    "covers_waist": True,
}


def build(g):
    body, jacket = g.part("body"), g.part("jacket")
    strip_fabric(body, "D", "weave", 12675, 2)
    cap(body, "D", seed=12675)
    body.front.vline(3, 0, 11, "D1")
    strip_fabric(jacket, "P", "weave", 12676, 2)
    cap(jacket, "P", seed=12676)
    for face in jacket.sides:
        ink_clouds(face, "P", 12677, density=.7)
    f = jacket.front
    for y in range(12):
        for x in range(2, 6):
            f.clear(x, y)
        f.set(1, y, "S3"), f.set(6, y, "S3")
    # The cord tied across the chest, with a tassel.
    for i, x in enumerate((-1.6, .6)):
        cord = g.piece(f"himo_{i}", "TORSO", (0, 0, 0), (1, 1, 1), pivot=(x, 5.0, -2.55), scale=(1, .6, .6))
        solid(cord, "A", "smooth", 12678, 3, edge=False)
    tassel = g.piece("himo_tassel", "TORSO", (-.5, 0, -.5), (1, 2, 1), pivot=(-.2, 5.4, -2.6), motion="sway",
                     scale=(.6, 1, .6))
    solid(tassel, "A", "smooth", 12679, 2)
    for side in ("right", "left"):
        arm, sleeve = g.part(f"{side}_arm"), g.part(f"{side}_sleeve")
        strip_fabric(arm, "D", "weave", 12680, 2, 0, 10)
        fabric(arm.top, "D", "weave", 12680, 3)
        bone = "RIGHT_ARM" if side == "right" else "LEFT_ARM"
        ox = -3.0 if side == "right" else -1.0
        cuff = g.piece(f"{side}_haori_sleeve", bone, (ox - .7, -2.3, -2.7), (5, 8, 5), inflate=.15)
        solid(cuff, "P", "weave", 12681, 2)
        for face in cuff.sides:
            ink_clouds(face, "P", 12682 + (side == "left"), density=.7)
            face.hline(0, face.w - 1, 7, "S3")
        fabric(cuff.top, "P", "weave", 12681, 3)
        cuff.bottom.fill("P0")
        fabric(sleeve.top, "P", "weave", 12684, 3)
    # Lapels standing proud of the open front, and the skirt of the haori to mid-thigh.
    for name, x in (("right", -3.6), ("left", 2.6)):
        lapel = g.piece(f"lapel_{name}", "TORSO", (0, 0, 0), (1, 13, 1), pivot=(x, -.4, -2.75))
        solid(lapel, "S", "weave", 12685, 3)
    for name, x0, w, z, motion, face_name in (("skirt_front_right", -4.6, 3, -2.95, "flap_front", "front"),
                                               ("skirt_front_left", 1.6, 3, -2.95, "flap_front", "front"),
                                               ("skirt_back", -4.6, 9, 1.95, "flap_back", "back")):
        skirt = g.piece(name, "TORSO", (0, 0, 0), (w, 7, 1), pivot=(x0, 11.4, z), motion=motion)
        solid(skirt, "P", "weave", 12686 + len(name), 2)
        ink_clouds(getattr(skirt, face_name), "P", 12690 + len(name), density=.7)
        getattr(skirt, face_name).hline(0, w - 1, 6, "S3")
    back_crest(g, role="P", ink="K2", pivot=(0, 1.4, 2.32))
