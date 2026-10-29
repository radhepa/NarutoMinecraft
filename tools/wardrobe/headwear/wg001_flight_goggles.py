"""Flight Goggles: a pair of wide rectangular goggles in a steel frame, pushed up on the forehead on a
leather strap: the Academy kid who wants to look ready for anything."""
from paint import fabric, k, solid

META = {"name": "Flight Goggles", "gender": "unisex", "hides_hair": ["fringe"],
        "description": "Wide rectangular goggles in a steel frame pushed up on the forehead, on a leather strap."}


def build(g):
    strap = g.piece("strap", "HEAD", (-4, -7.6, -4), (8, 1, 8), inflate=.64)
    solid(strap, "L", "leather", 31300, 2, edge=False)
    for f in strap.sides:
        f.hline(0, f.w - 1, 0, k("L", 3))
    for side, x in (("right", -1.9), ("left", 1.9)):
        frame = g.piece(f"goggle_{side}", "HEAD", (-1.5, -1, -1), (3, 2, 1), pivot=(x, -7.2, -4.75))
        solid(frame, "M", "plain", 31301, 3, edge=False)
        fabric(frame.front, "A", "plain", 31302, 2)
        frame.front.set(0, 0, k("A", 4)), frame.front.set(1, 0, k("A", 3))
        frame.front.set(2, 1, k("A", 1))
        rim = g.piece(f"rim_{side}", "HEAD", (-2, -1.5, 0), (4, 3, 1), pivot=(x, -7.2, -4.62), scale=(1, 1, .5))
        solid(rim, "M", "plain", 31303, 2, edge=False)
    bridge = g.piece("bridge", "HEAD", (-.5, -.5, 0), (1, 1, 1), pivot=(0, -7.2, -5.0))
    solid(bridge, "M", "plain", 31304, 2, edge=False)
