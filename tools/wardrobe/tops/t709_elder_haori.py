"""Elder Haori: a clan elder's purple haori to the thigh over a pale kimono shirt, the haori open at
the front with a braided cord tie, wide long sleeves and a blossom crest across the back."""
from glyphs import stamp
from kit import arm_x
from paint import cap, fabric, solid, strip_fabric

META = {
    "name": "Elder Haori",
    "gender": "unisex",
    "description": "Thigh-length purple haori over a pale kimono, cord tie, wide sleeves, blossom crest.",
    "tags": ["yamanaka", "robe", "jonin"],
    "covers_waist": True,
}

# The Yamanaka blossom: five petals round a bright heart, drawn at double resolution.
BLOSSOM = ["...##...",
           "..#aa#..",
           ".##aa##.",
           "#aa##aa#",
           "#aaooaa#",
           ".#a##a#.",
           ".#a#.#a.",
           "..#...#."]


def build(g):
    body, jacket = g.part("body"), g.part("jacket")
    strip_fabric(body, "S", "weave", 7950, 3)
    cap(body, "S", texture="weave", seed=7950, base=3)
    for i in range(7):
        body.front.set(1 + i, i, "S1")
    strip_fabric(jacket, "P", "velvet", 7951, 2)
    cap(jacket, "P", texture="velvet", seed=7951)
    for x in range(2, 6):
        for y in range(12):
            jacket.front.clear(x, y)
    jacket.front.vline(1, 0, 11, "P0"), jacket.front.vline(6, 0, 11, "P0")
    cord = g.piece("cord", "TORSO", (-1.5, 0, 0), (3, 1, 1), pivot=(0, 5.0, -2.85))
    solid(cord, "A", "plain", 7952, 3)
    crest = g.piece("back_crest", "TORSO", (-4, 0, 0), (8, 8, 1), pivot=(0, 2.0, 2.15), scale=(.5, .5, .5))
    for face in crest.faces:
        fabric(face, "P", "velvet", 7953, 2)
    stamp(crest.back, BLOSSOM, 0, 0, {"#": "S3", "a": "A3", "o": "A4"})
    for name, z, motion in (("front", -3.0, "flap_front"), ("back", 1.95, "flap_back")):
        if name == "back":
            panel = g.piece("haori_back", "TORSO", (-4.5, 0, 0), (9, 5, 1), pivot=(0, 11.2, z), motion=motion)
            solid(panel, "P", "velvet", 7954, 2)
            continue
        for i, x in enumerate((-4.5, 2.5)):
            panel = g.piece(f"haori_front_{i}", "TORSO", (0, 0, 0), (2, 5, 1), pivot=(x, 11.2, z), motion=motion)
            solid(panel, "P", "velvet", 7955 + i, 2)
    for side, bone in (("right", "RIGHT_ARM"), ("left", "LEFT_ARM")):
        arm = g.part(f"{side}_arm")
        strip_fabric(arm, "S", "weave", 7957, 3, 0, 9)
        fabric(arm.top, "P", "velvet", 7957, 3)
        sleeve = g.piece(f"{side}_wide_sleeve", bone, (arm_x(side) - .6, -1.8, -2.6), (5, 9, 5), inflate=.1)
        solid(sleeve, "P", "velvet", 7958 + (side == "left"), 2)
        for face in sleeve.sides:
            face.hline(0, face.w - 1, 8, "P0")
