"""Furisode Kimono: the swinging-sleeve kimono for New Year's shrine visits and coming-of-age day,
silk strewn with blossoms that gather thick above the hem of sleeves that hang nearly to the knee,
a broad obi with a raised sash-scarf along its top and a cord tied at the front."""
from kit_household import overlap, sash, sprigs, wide_sleeves
from paint import cap, solid, strip_fabric

META = {
    "name": "Furisode Kimono",
    "gender": "female",
    "description": "Swinging-sleeve silk kimono strewn with blossoms, broad obi with a sash-scarf and a front cord.",
    "tags": ["civilian", "kimono", "wrap", "formal"],
    "tucked": True,
}


def blossoms(face, rows=None):
    sprigs(face, "A3", "S4", step=4, seed=2, rows=rows, chance=.75)


def build(g):
    body = g.part("body")
    strip_fabric(body, "P", "velvet", 37340, 2)
    cap(body, "P", texture="velvet", seed=37340)
    blossoms(body.strip, rows=range(0, 6))
    overlap(body.front, "S4", "P1", rows=6, collar="S4", under="A3")
    for box in wide_sleeves(g, "furisode", "P", "velvet", 37341, top=1.4, length=12, depth=4, arm_rows=9):
        for face in box.sides:
            blossoms(face, rows=range(4, 11))
            face.hline(0, face.w - 1, 11, "P1")
    obi = sash(g, "obi", "S", y=6.0, height=4, knot="bow", seed=37346, base=3)
    for face in obi.sides:
        face.hline(0, face.w - 1, 2, "M3")
    scarf = g.piece("obiage", "TORSO", (-4.5, 0, -2.5), (9, 1, 5), pivot=(0, 5.7, 0), inflate=.22)
    solid(scarf, "A", "velvet", 37352, 3, edge=False)
    cord = g.piece("obijime", "TORSO", (-4.5, 0, -2.5), (9, 1, 5), pivot=(0, 8.0, 0), inflate=.26)
    solid(cord, "A", "weave", 37353, 2, edge=False)
    cord.front.set(4, 0, "A4")
