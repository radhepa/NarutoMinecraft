"""Hokage Haori: the white kage cloak with a burning flame hem, worn open over the jonin flak vest."""
from glyphs import FIRE, stamp
from kit import collar
from paint import cap, fabric, grid, k, rnd, solid, strip_fabric

META = {
    "name": "Hokage Haori",
    "gender": "unisex",
    "description": "White haori with a flame hem and 火 on the back, open over a green flak vest and navy shirt.",
    "tags": ["robe", "kage"],
    "covers_waist": True,
}

def flames(face, rows: int = 4, seed: int = 0):
    """Flame tongues licking up from the hem: deep red at the hem, bright tips."""
    h = face.h
    for x in range(face.w):
        reach = 1 + int(rnd(x // 2, 3, seed) * rows) if x % 2 == 0 else 1 + int(rnd(x, 9, seed) * (rows - 1))
        for d in range(reach):
            y = h - 1 - d
            face.set(x, y, "A1" if d == 0 else "A3" if d == reach - 1 and reach > 1 else "A2")


def build(g):
    body, jacket = g.part("body"), g.part("jacket")
    # Under-layer: the flak vest's green ribbing over the navy shirt.
    strip_fabric(body, "P", "rib", 11, 2)
    cap(body, "P", seed=11)
    for y in (3, 6, 9):
        body.strip.hline(0, body.strip.w - 1, y, "P1")
    body.front.vline(3, 0, 11, "P0"), body.front.vline(4, 0, 11, "P3")
    # The haori overlay: white everywhere but the open front.
    strip_fabric(jacket, "S", "weave", 12, 3)
    cap(jacket, "S", seed=12, base=3)
    f, b = jacket.front, jacket.back
    for y in range(12):
        for x in range(2, 6):
            f.clear(x, y)
        f.set(1, y, "S2"), f.set(6, y, "S2")
    # 火 (fire) across the shoulders at double resolution.
    kanji = g.piece("back_kanji", "TORSO", (-6, 0, 0), (12, 14, 1), pivot=(0, 1.2, 2.3), scale=(.5, .5, .5))
    fabric(kanji.back, "S", "weave", 21, 3)
    stamp(kanji.back, [row[::-1] for row in FIRE], 0, 0, {"#": "A2"})
    for face in (kanji.top, kanji.bottom, kanji.right, kanji.left, kanji.front):
        face.fill("S3")
    flames(jacket.strip, 3, 13)
    # Navy shirt sleeves with skin hands; wide white haori sleeves to the elbow.
    for side in ("right", "left"):
        arm, sleeve = g.part(f"{side}_arm"), g.part(f"{side}_sleeve")
        strip_fabric(arm, "D", "weave", 14, 2, 0, 10)
        fabric(arm.top, "D", "weave", 14, 3)
        strip_fabric(sleeve, "S", "weave", 15, 3, 0, 4)
        fabric(sleeve.top, "S", "weave", 15, 4)
        bone = "RIGHT_ARM" if side == "right" else "LEFT_ARM"
        ox = -3.0 if side == "right" else -1.0
        cuff = g.piece(f"{side}_haori_sleeve", bone, (ox - .7, 2.5, -2.7), (5, 4, 5), inflate=.15)
        solid(cuff, "S", "weave", 16, 3)
        for face in cuff.sides:
            face.hline(0, face.w - 1, 3, "A1")
            for x in range(face.w):
                if rnd(x, 1, 17 + (side == "left")) < .55:
                    face.set(x, 2, "A2")
        cuff.bottom.fill("S1")
    # Vest collar and the haori's standing lapels.
    c = collar(g, "vest_collar", "P", "rib", height=2, y=-1.2)
    c.front.hline(3, 5, 0, "P0")
    for name, x in (("right", -3.6), ("left", 2.6)):
        lapel = g.piece(f"lapel_{name}", "TORSO", (0, 0, 0), (1, 11, 1), pivot=(x, .2, -2.75))
        solid(lapel, "S", "weave", 18, 3)
    # Scroll pockets on the vest.
    for i, x in enumerate((-3.5, 1.5)):
        pocket = g.piece(f"scroll_pocket_{i}", "TORSO", (0, 0, 0), (2, 3, 1), pivot=(x, 4.5, -2.6))
        solid(pocket, "P", "rib", 19 + i, 2)
        pocket.front.hline(0, 1, 0, "P3")
    # Long skirts: the open front halves and the back, each burning at the hem.
    for name, x0, w, z, motion, face_name in (("skirt_front_right", -4.6, 3, -2.95, "flap_front", "front"),
                                               ("skirt_front_left", 1.6, 3, -2.95, "flap_front", "front"),
                                               ("skirt_back", -4.6, 9, 1.95, "flap_back", "back")):
        skirt = g.piece(name, "TORSO", (0, 0, 0), (w, 10, 1), pivot=(x0, 11.4, z), motion=motion)
        solid(skirt, "S", "weave", 20 + len(name), 3)
        flames(skirt.strip, 4, len(name))
        skirt.bottom.fill("A1")
    for name, x in (("skirt_right", -5.05), ("skirt_left", 4.05)):
        panel = g.piece(name, "TORSO", (0, 0, -2), (1, 9, 4), pivot=(x, 11.4, 0))
        solid(panel, "S", "weave", 30, 3)
        flames(panel.strip, 4, 31 + (x > 0))
        panel.bottom.fill("A1")
