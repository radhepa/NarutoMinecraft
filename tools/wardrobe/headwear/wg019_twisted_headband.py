"""Twisted Headband: a length of cloth twisted into a thick rope and tied round the forehead, knotted
at the right temple with two short ends sticking out: the fighter's hachimaki, no plate needed."""
from kit_rugged import rope_face
from paint import solid

META = {"name": "Twisted Headband", "gender": "unisex",
        "description": "Cloth twisted into a thick rope round the forehead, knotted at the right temple with two ends."}


def build(g):
    band = g.piece("band", "HEAD", (-4, -7.4, -4), (8, 1, 8), inflate=.62)
    for face in band.faces:
        rope_face(face, "A", 2)
    knot = g.piece("knot", "HEAD", (0, 0, 0), (1, 2, 2), pivot=(-5.0, -8.0, -2.2))
    for face in knot.faces:
        rope_face(face, "A", 3)
    for i, (rx, ry, rz) in enumerate(((0, 0, 50), (0, 0, 80))):
        end = g.piece(f"end_{i}", "HEAD", (-.5, 0, -.5), (1, 3, 1), pivot=(-5.2, -7.2, -1.6 + .9 * i),
                      rotation=(rx, ry, rz), motion="sway")
        solid(end, "A", "weave", 35912 + i, 2)
