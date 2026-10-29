"""Tenugui Cap: the noodle cook's white towel tied flat over the crown and knotted at the nape, a
band of indigo print at its edge, keeping the hair out of the pot."""
from paint import fabric, k, solid

META = {"name": "Tenugui Cap", "gender": "unisex", "hides_hair": ["*"],
        "description": "White towel tied flat over the crown with an indigo print edge, knotted at the nape."}


def build(g):
    cap = g.piece("cap", "HEAD", (-4, -8, -4), (8, 2, 8), inflate=.62)
    for face in cap.sides:
        fabric(face, "S", "weave", 36920 + face.x0, 3)
        face.hline(0, face.w - 1, 1, k("D", 2))
        for x in range(0, face.w, 2):
            face.set(x, 1, k("S", 3))
    fabric(cap.top, "S", "weave", 36921, 4), cap.bottom.fill("S1")
    back = g.piece("cap_back", "HEAD", (-4, -6, 3), (8, 2, 1), inflate=.62)
    for face in back.faces:
        fabric(face, "S", "weave", 36922, 3)
    knot = g.piece("knot", "HEAD", (-1, -1, 0), (2, 2, 1), pivot=(0, -4.4, 4.7))
    solid(knot, "S", "weave", 36923, 3)
    for i, (x, rz) in enumerate(((-.6, 24), (.6, -20))):
        end = g.piece(f"end_{i}", "HEAD", (-.5, 0, 0), (1, 3, 1), pivot=(x, -3.8, 4.9), rotation=(16, 0, rz), motion="sway")
        solid(end, "S", "weave", 36924 + i, 3)
        end.back.set(0, 2, k("D", 2))
