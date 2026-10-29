"""Hairband Protector: the forehead protector worn as Sakura wore it, its cloth band tied over the
crown like a hairband with the steel plate sitting on top of the head above the fringe, so the
forehead stays bare."""
from kit_shinobi import protector_plate
from paint import fabric, k, solid

META = {"name": "Hairband Protector", "gender": "unisex",
        "description": "Forehead protector worn as a hairband over the crown, the plate above the fringe, forehead bare."}


def build(g):
    band = g.piece("band", "HEAD", (-4, -8, -1.4), (8, 1, 2), inflate=.66)
    solid(band, "A", "weave", 19910, 2, edge=False)
    for side, x in (("right", -4.66), ("left", 4.66)):
        drop = g.piece(f"band_{side}", "HEAD", (-.5, 0, -1), (1, 5, 2), pivot=(x, -8.0, -.4))
        solid(drop, "A", "weave", 19911 + (x > 0), 2)
        drop.bottom.fill(k("A", 1))
    plate = g.piece("plate", "HEAD", (-9, -4, -2), (18, 8, 2), pivot=(0, -8.7, -3.3), rotation=(-38, 0, 0),
                    scale=(1 / 3, 1 / 3, 1 / 3))
    for face in plate.faces:
        fabric(face, "M", "plain", 19913, 2)
    protector_plate(plate.front)
