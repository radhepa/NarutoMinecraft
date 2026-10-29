"""Side-Knot Protector: the forehead protector worn a little askew, its band knotted over the left ear
with one short end standing out and one hanging, a style picked up on long missions."""
from kit_shinobi import protector_plate
from paint import fabric, k, solid

META = {"name": "Side-Knot Protector", "gender": "unisex",
        "description": "Forehead protector tilted slightly, the band knotted over the left ear with two ends."}


def build(g):
    band = g.piece("band", "HEAD", (-4, -7.6, -4), (8, 1, 8), inflate=.6, rotation=(0, 0, -3))
    solid(band, "D", "weave", 32994, 2, edge=False)
    plate = g.piece("plate", "HEAD", (-9, -4, -2), (18, 8, 2), pivot=(-.2, -7.0, -4.62), rotation=(0, 0, -3),
                    scale=(1 / 3, 1 / 3, 1 / 3))
    for face in plate.faces:
        fabric(face, "M", "plain", 32995, 2)
    protector_plate(plate.front)
    knot = g.piece("knot", "HEAD", (0, -1, -1), (1, 2, 2), pivot=(4.6, -7.2, 1.2))
    solid(knot, "D", "weave", 32996, 2)
    up = g.piece("end_up", "HEAD", (0, -.5, 0), (3, 1, 1), pivot=(5.4, -7.6, 1.0), rotation=(0, 0, -28))
    solid(up, "D", "weave", 32997, 2)
    down = g.piece("end_down", "HEAD", (-.5, 0, -.5), (1, 4, 1), pivot=(5.0, -6.6, 1.6), rotation=(0, 0, -14), motion="sway")
    solid(down, "D", "weave", 32998, 2)
    down.left.set(0, 3, k("D", 1))
