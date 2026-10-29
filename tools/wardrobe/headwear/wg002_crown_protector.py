"""Crown Protector: the forehead protector worn high as a hair band, the cloth arching over the crown
from ear to ear and the steel plate sitting on top of the head at the hairline: the new genin's
proud look."""
from kit_shinobi import protector_plate
from paint import fabric, k, solid

META = {"name": "Crown Protector", "gender": "unisex",
        "description": "Forehead protector worn high as a hair band, arching over the crown, the plate at the hairline."}


def build(g):
    arch = g.piece("band", "HEAD", (-4, -8, -2.6), (8, 1, 2), inflate=.66)
    solid(arch, "D", "weave", 31310, 2, edge=False)
    for side, x in (("right", -4.0), ("left", 3.0)):
        drop = g.piece(f"band_{side}", "HEAD", (x, -7.6, -2.6), (1, 6, 2), inflate=.66)
        solid(drop, "D", "weave", 31311 + (x > 0), 2)
        for f in drop.sides:
            f.hline(0, f.w - 1, 5, k("D", 1))
    plate = g.piece("plate", "HEAD", (-9, -4, -2), (18, 8, 2), pivot=(0, -8.3, -3.2), rotation=(-58, 0, 0),
                    scale=(1 / 3, 1 / 3, 1 / 3))
    for face in plate.faces:
        fabric(face, "M", "plain", 31313, 2)
    protector_plate(plate.front)
