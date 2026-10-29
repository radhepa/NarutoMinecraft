"""Market Kerchief: a square of cream cotton dotted in colour folded into a triangle and tied over the hair, the
knot at the nape and the point hanging down the back of the neck, for the counter and the stall."""
from kit_market import dots
from paint import fabric, k, solid

META = {"name": "Market Kerchief", "gender": "unisex", "hides_hair": ["*"],
        "description": "Dotted cotton kerchief folded in a triangle, knotted at the nape, the point down the back."}


def build(g):
    cap = g.piece("kerchief", "HEAD", (-4, -8, -4), (8, 2, 8), inflate=.62)
    for face in cap.sides:
        fabric(face, "S", "weave", 36950 + face.x0, 3)
        dots(face, k("A", 2), 3)
        face.hline(0, face.w - 1, 1, k("A", 2))
    fabric(cap.top, "S", "weave", 36951, 4)
    dots(cap.top, k("A", 2), 3)
    cap.bottom.fill(k("S", 1))
    back = g.piece("kerchief_back", "HEAD", (-4, -6, 3), (8, 3, 1), inflate=.62)
    for face in back.faces:
        fabric(face, "S", "weave", 36952, 3)
        dots(face, k("A", 2), 3, offset=1)
    for i, w in enumerate((4, 2)):
        tip = g.piece(f"point_{i}", "HEAD", (-w / 2, 0, 0), (w, 1, 1), pivot=(0, -2.4 + i, 4.75), motion="sway")
        solid(tip, "S", "weave", 36953 + i, 3)
    knot = g.piece("knot", "HEAD", (-1, -1, 0), (2, 2, 1), pivot=(0, -3.6, 4.9))
    solid(knot, "S", "weave", 36955, 3)
