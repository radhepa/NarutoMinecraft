"""Kasa Travel Hat: a wide conical sedge hat for the road, woven in rings of straw with a cloth band
and ties under the chin; it sits above the hair, hiding only knots and buns on the crown."""
from paint import k, rnd

META = {"name": "Kasa Travel Hat", "gender": "unisex",
        "description": "Wide conical woven straw hat with a cloth band.",
        "hides_hair": ["knot", "brush", "bun_", "pin_", "crown", "puff_"]}

RINGS = [(14, -8.9), (12, -9.6), (10, -10.3), (7, -11.0), (4, -11.6)]


def build(g):
    for i, (w, y) in enumerate(RINGS):
        ring = g.piece(f"ring_{i}", "HEAD", (-w / 2, y, -w / 2), (w, 1, w))
        for f in ring.faces:
            for yy in range(f.h):
                for xx in range(f.w):
                    s = 3 if (xx + yy + i) % 3 else 2
                    if rnd(xx, yy, 12950 + i) < .08:
                        s -= 1
                    f.set(xx, yy, k("L", s + (1 if f.name == "top" else 0)))
        ring.bottom.fill("L1")
    band = g.piece("band", "HEAD", (-5, -9.9, -5), (10, 1, 10))
    for f in band.faces:
        f.fill("A2")
    for f in band.sides:
        f.hline(0, f.w - 1, 0, "A3")
    for side, x in (("right", -4.3), ("left", 4.3)):
        tie = g.piece(f"tie_{side}", "HEAD", (-.5, 0, -.5), (1, 8, 1), pivot=(x, -8.6, -1.0), scale=(.5, 1, .5))
        for f in tie.faces:
            f.fill("A2")
