"""Weathered Protector: a forehead protector worn for years on the road, the steel plate dulled and
cut by a long scratch, the cloth band faded and frayed into three long tails at the back."""
from kit_shinobi import protector_plate
from paint import fabric, line, solid

META = {"name": "Weathered Protector", "gender": "unisex",
        "description": "Dulled, scratched protector plate on a faded band with three long frayed tails."}


def build(g):
    band = g.piece("band", "HEAD", (-4, -7.6, -4), (8, 1, 8), inflate=.6)
    solid(band, "S", "weave", 35870, 1, edge=False)
    for face in band.sides:
        for x in range(0, face.w, 3):
            face.set(x, 0, "S0")
    plate = g.piece("plate", "HEAD", (-9, -4, -2), (18, 8, 2), pivot=(0, -7.0, -4.62), scale=(1 / 3, 1 / 3, 1 / 3))
    for face in plate.faces:
        fabric(face, "M", "plain", 35871, 1)
    protector_plate(plate.front)
    # Dull the plate and cut a scratch across it, corner to corner.
    for y in range(8):
        for x in range(18):
            if plate.front.get(x, y) == "M3":
                plate.front.set(x, y, "M2")
    line(plate.front, 3, 1, 14, 6, "M0"), line(plate.front, 4, 1, 15, 6, "M4")
    knot = g.piece("knot", "HEAD", (-1, -1, 0), (2, 2, 1), pivot=(0, -7.1, 4.6))
    solid(knot, "S", "weave", 35872, 1)
    for i, (x, rz, n) in enumerate(((-.8, 16, 7), (0, 0, 9), (.8, -14, 6))):
        tail = g.piece(f"tail_{i}", "HEAD", (-.5, 0, 0), (1, n, 1), pivot=(x, -6.4, 4.9), rotation=(20, 0, rz),
                       motion="sway")
        solid(tail, "S", "weave", 35873 + i, 1)
        tail.back.set(0, n - 1, "S0"), tail.front.set(0, n - 1, "S0")
