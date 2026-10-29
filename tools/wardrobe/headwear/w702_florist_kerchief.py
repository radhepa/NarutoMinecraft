"""Florist Kerchief: a cotton kerchief tied over the hair for work in the flower shop, knotted at
the nape with two short ends, a blossom tucked in at the side."""
from kit_yamanaka import flower, petal_fabric
from paint import fabric, solid

META = {"name": "Florist Kerchief", "gender": "unisex", "hides_hair": ["*"],
        "description": "Blossom-print kerchief tied over the hair, knotted at the nape, a flower tucked at the side."}


def build(g):
    cap = g.piece("kerchief", "HEAD", (-4, -8, -4), (8, 2, 8), inflate=.62)
    for face in cap.sides:
        petal_fabric(face, "S", 7720 + face.x0, 3, motif="P")
    fabric(cap.top, "S", "plain", 7720, 4), cap.bottom.fill("S1")
    back = g.piece("kerchief_back", "HEAD", (-4, -6, 3), (8, 3, 1), inflate=.62)
    for face in back.faces:
        petal_fabric(face, "S", 7721, 3, motif="P")
    knot = g.piece("knot", "HEAD", (-1, -1, 0), (2, 2, 1), pivot=(0, -3.0, 4.7))
    solid(knot, "S", "weave", 7722, 2)
    for i, (x, rz) in enumerate(((-.6, 22), (.6, -18))):
        end = g.piece(f"kerchief_end_{i}", "HEAD", (-.5, 0, 0), (1, 3, 1), pivot=(x, -2.4, 4.9), rotation=(18, 0, rz),
                      motion="sway")
        solid(end, "S", "weave", 7723 + i, 3)
    flower(g, "tucked", (-4.75, -6.2, -1.5), rotation=(0, 90, 0), size=5)
