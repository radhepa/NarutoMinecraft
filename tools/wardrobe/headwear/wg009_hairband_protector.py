"""Hairband Protector: the forehead protector worn as a hairband, its cloth running over the crown
from ear to ear and the plate set high at the hairline, so the fringe falls free beneath it."""
from kit_shinobi import protector_plate
from paint import fabric, solid

META = {"name": "Hairband Protector", "gender": "unisex",
        "description": "Forehead protector worn as a hairband over the crown, the plate high at the hairline."}


def build(g):
    band = g.piece("band", "HEAD", (-4, -8, -2.6), (8, 1, 2), inflate=.62)
    solid(band, "D", "weave", 33990, 2, edge=False)
    for name, x in (("right", -4.0), ("left", 3.0)):
        strap = g.piece(f"band_{name}", "HEAD", (x, -8, -2.6), (1, 4, 2), inflate=.62)
        solid(strap, "D", "weave", 33991, 2, edge=False)
    plate = g.piece("plate", "HEAD", (-9, -4, -2), (18, 8, 2), pivot=(0, -8.6, -2.6), rotation=(-62, 0, 0),
                    scale=(1 / 3, 1 / 3, 1 / 3))
    for face in plate.faces:
        fabric(face, "M", "plain", 33992, 2)
    protector_plate(plate.front)
