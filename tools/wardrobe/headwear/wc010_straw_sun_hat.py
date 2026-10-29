"""Straw Sun Hat: a broad woven straw hat for summer errands, the riverbank and the rice paddies,
a round crown ringed with a ribbon whose two ends trail at the back."""
from paint import k, solid

META = {"name": "Straw Sun Hat", "gender": "unisex", "hides_hair": ["*"],
        "description": "Broad woven straw hat with a ribbon round the crown and two trailing ribbon ends."}


def weave(face):
    for y in range(face.h):
        for x in range(face.w):
            face.set(x, y, "L4" if (x + y) % 2 else "L3")


def build(g):
    brim = g.piece("brim", "HEAD", (-7, 0, -7), (14, 1, 14), pivot=(0, -7.9, 0))
    for f in brim.faces:
        weave(f)
    for f in brim.sides:
        f.hline(0, f.w - 1, 0, "L2")
    brim.bottom.fill("L2")
    crown = g.piece("crown", "HEAD", (-4, -10.6, -4), (8, 3, 8), inflate=.64)
    for f in crown.faces:
        weave(f)
    for f in crown.sides:
        f.hline(0, f.w - 1, 2, "A2")
    for i, (x, rz) in enumerate(((-.8, 8), (.6, -10))):
        end = g.piece(f"ribbon_{i}", "HEAD", (-.5, 0, 0), (1, 4 - i, 1), pivot=(x, -8.0, 4.7), rotation=(10, 0, rz),
                      motion="sway")
        solid(end, "A", "weave", 37940 + i, 2)
        end.back.set(0, end.back.h - 1, k("A", 1))
