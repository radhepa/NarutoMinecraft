"""Shrine Kosode: the white kosode of the shrine attendants, crisp white cloth with the red
under-collar showing in a fine line at the throat, deep white sleeves gathered at the hem with red
sleeve cords. It uses the white and the red of the palette, so it is shrine white-and-red in any
outfit. Tucked, to sit under the vermilion hakama or anything else."""
from kit_household import overlap, wide_sleeves
from paint import cap, solid, strip_fabric

META = {
    "name": "Shrine Kosode",
    "gender": "unisex",
    "description": "White kosode with a red under-collar line, deep white sleeves with red sleeve cords at the hem.",
    "tags": ["civilian", "kimono", "wrap"],
    "tucked": True,
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "S", "weave", 37160, 3)
    cap(body, "S", texture="weave", seed=37160, base=3)
    f = body.front
    overlap(f, "S4", "S1", rows=9, collar="S4", under="A2")
    f.set(4, 2, "A2"), f.set(5, 2, "S2")
    for face in (body.right, body.left):
        face.vline(1, 0, 11, "S2")
    for box in wide_sleeves(g, "sleeve", "S", "weave", 37161, top=2.0, length=8, base=3, arm_rows=9):
        for face in box.sides:
            face.hline(0, face.w - 1, 7, "S1")
        for x, side_face in ((1, box.front), (3, box.back)):
            side_face.set(x, 7, "A2")
    for side, bone, x in (("right", "RIGHT_ARM", -1.0), ("left", "LEFT_ARM", 1.0)):
        cord = g.piece(f"{side}_sleeve_cord", bone, (-.5, 0, -.5), (1, 2, 1), pivot=(x, 9.9, -2.9), motion="sway")
        solid(cord, "A", "weave", 37166 + (side == "left"), 2)
