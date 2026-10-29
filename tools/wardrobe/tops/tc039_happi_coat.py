"""Happi Coat: the festival coat the neighborhood wears to carry the shrine float, bold cloth with a
dark collar band lettered in white, a broad band of white blocks above the hem, elbow sleeves and a
big three-comma crest in a white ring across the back, belted with a twisted sash."""
from glyphs import stamp
from kit_household import collar_band, ichimatsu, robe_skirt, sash, trim, wide_sleeves
from paint import cap, fabric, strip_fabric

META = {
    "name": "Happi Coat",
    "gender": "unisex",
    "description": "Festival coat: lettered collar band, white block band at the hem, elbow sleeves, comma crest on the back.",
    "tags": ["civilian", "jacket", "casual"],
    "covers_waist": True,
}

# Three commas whirling in a ring, the old festival crest, at double resolution.
TOMOE = ["...####...",
         ".##....##.",
         "#..##....#",
         "#.###.#..#",
         "#..#..##.#",
         "#....###.#",
         "#.##..#..#",
         "#.###....#",
         ".##....##.",
         "...####..."]


def build(g):
    body = g.part("body")
    strip_fabric(body, "P", "weave", 37260, 2)
    cap(body, "P", texture="weave", seed=37260)
    f = body.front
    for x in (3, 4):
        f.vline(x, 0, 11, "S3")
    f.vline(2, 0, 11, "P1")
    collar_band(f, "K2", rows=9, width=1)
    for y in range(1, 9, 2):
        f.set(1, y, "S3"), f.set(6, y, "S3")
    ichimatsu(body.strip, "S3", size=2, rows=range(9, 11))
    body.strip.hline(0, body.strip.w - 1, 11, "P1")
    for face in robe_skirt(g, "hem", 3, "P", "weave", 37261, hem="P1", top=10.8):
        ichimatsu(face, "S3", size=1, rows=range(1, 2))
    for box in wide_sleeves(g, "sleeve", "P", "weave", 37263, top=1.6, length=5, hem="K2", arm_rows=4):
        ichimatsu(box.strip, "S3", size=1, rows=range(2, 3))
    crest = g.piece("back_crest", "TORSO", (-5, 0, 0), (10, 10, 1), pivot=(0, 1.4, 2.06), scale=(.5, .5, .5))
    for face in crest.faces:
        fabric(face, "P", "weave", 37268, 2)
    stamp(crest.back, TOMOE, 0, 0, {"#": "S4"})
    belt = sash(g, "sash", "A", y=8.4, height=1, knot="side", seed=37270, inflate=.3)
    trim(belt, 0, "S3")
