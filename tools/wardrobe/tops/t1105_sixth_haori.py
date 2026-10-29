"""Sixth Haori: Kakashi as the Sixth Hokage, the white kage haori burning at the hem with a red 六 (six)
across the back, open over the flak vest and a navy shirt."""
from glyphs import stamp
from kit import collar
from paint import cap, fabric, rnd, solid, strip_fabric

META = {
    "name": "Sixth Haori",
    "gender": "unisex",
    "description": "White haori with a flame hem and a red 六 on the back, open over a flak vest and navy shirt.",
    "tags": ["robe", "kage"],
    "covers_waist": True,
}

SIX = ["....##......",
       ".....##.....",
       "......##....",
       "############",
       "############",
       "............",
       "...##..##...",
       "...##...##..",
       "..##.....##.",
       "..##......##",
       ".##.......##",
       "##.........#",
       "............",
       "............"]


def flames(face, rows: int = 4, seed: int = 0):
    """Flame tongues licking up from the hem: deep red at the hem, bright tips."""
    h = face.h
    for x in range(face.w):
        reach = 1 + int(rnd(x // 2, 3, seed) * rows) if x % 2 == 0 else 1 + int(rnd(x, 9, seed) * (rows - 1))
        for d in range(reach):
            face.set(x, h - 1 - d, "A1" if d == 0 else "A3" if d == reach - 1 and reach > 1 else "A2")


def build(g):
    body, jacket = g.part("body"), g.part("jacket")
    strip_fabric(body, "P", "rib", 11401, 2)
    cap(body, "P", seed=11401)
    for y in (3, 6, 9):
        body.strip.hline(0, body.strip.w - 1, y, "P1")
    body.front.vline(3, 0, 11, "P0"), body.front.vline(4, 0, 11, "P3")
    strip_fabric(jacket, "S", "weave", 11402, 3)
    cap(jacket, "S", seed=11402, base=3)
    f = jacket.front
    for y in range(12):
        for x in range(2, 6):
            f.clear(x, y)
        f.set(1, y, "S2"), f.set(6, y, "S2")
    kanji = g.piece("back_kanji", "TORSO", (-6, 0, 0), (12, 14, 1), pivot=(0, 1.2, 2.3), scale=(.5, .5, .5))
    fabric(kanji.back, "S", "weave", 11403, 3)
    stamp(kanji.back, [row[::-1] for row in SIX], 0, 0, {"#": "A2"})
    for face in (kanji.top, kanji.bottom, kanji.right, kanji.left, kanji.front):
        face.fill("S3")
    flames(jacket.strip, 3, 11404)
    for side in ("right", "left"):
        arm, sleeve = g.part(f"{side}_arm"), g.part(f"{side}_sleeve")
        strip_fabric(arm, "D", "weave", 11405, 2, 0, 10)
        fabric(arm.top, "D", "weave", 11405, 3)
        strip_fabric(sleeve, "S", "weave", 11406, 3, 0, 4)
        fabric(sleeve.top, "S", "weave", 11406, 4)
        bone = "RIGHT_ARM" if side == "right" else "LEFT_ARM"
        ox = -3.0 if side == "right" else -1.0
        cuff = g.piece(f"{side}_haori_sleeve", bone, (ox - .7, 2.5, -2.7), (5, 4, 5), inflate=.15)
        solid(cuff, "S", "weave", 11407, 3)
        for face in cuff.sides:
            face.hline(0, face.w - 1, 3, "A1")
            for x in range(face.w):
                if rnd(x, 1, 11408 + (side == "left")) < .55:
                    face.set(x, 2, "A2")
        cuff.bottom.fill("S1")
    c = collar(g, "vest_collar", "P", "rib", height=2, y=-1.2)
    c.front.hline(3, 5, 0, "P0")
    for name, x in (("right", -3.6), ("left", 2.6)):
        lapel = g.piece(f"lapel_{name}", "TORSO", (0, 0, 0), (1, 11, 1), pivot=(x, .2, -2.75))
        solid(lapel, "S", "weave", 11409, 3)
    for i, x in enumerate((-3.5, 1.5)):
        pocket = g.piece(f"scroll_pocket_{i}", "TORSO", (0, 0, 0), (2, 3, 1), pivot=(x, 4.5, -2.6))
        solid(pocket, "P", "rib", 11410 + i, 2)
        pocket.front.hline(0, 1, 0, "P3")
    for name, x0, w, z, motion in (("skirt_front_right", -4.6, 3, -2.95, "flap_front"),
                                   ("skirt_front_left", 1.6, 3, -2.95, "flap_front"),
                                   ("skirt_back", -4.6, 9, 1.95, "flap_back")):
        skirt = g.piece(name, "TORSO", (0, 0, 0), (w, 9, 1), pivot=(x0, 11.4, z), motion=motion)
        solid(skirt, "S", "weave", 11420 + len(name), 3)
        flames(skirt.strip, 4, len(name))
        skirt.bottom.fill("A1")
    for name, x in (("skirt_right", -5.05), ("skirt_left", 4.05)):
        panel = g.piece(name, "TORSO", (0, 0, -2), (1, 8, 4), pivot=(x, 11.4, 0))
        solid(panel, "S", "weave", 11430, 3)
        flames(panel.strip, 4, 11431 + (x > 0))
        panel.bottom.fill("A1")
