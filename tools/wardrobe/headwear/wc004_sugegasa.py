"""Sugegasa: a shallow peaked sedge hat, wide and low for rain and sun in the rice fields and on
the road, a dark lacquered rim, a red cord ring inside and ties under the chin."""
from paint import k, rnd

META = {"name": "Sugegasa", "gender": "unisex",
        "description": "Wide, low peaked sedge hat with a dark rim, a red cord ring and chin ties.",
        "hides_hair": ["knot", "brush", "bun", "pin_", "crown", "puff_", "spike", "tuft", "top"]}

RINGS = [(16, -8.7), (13, -9.3), (10, -9.9), (7, -10.5), (4, -11.0), (2, -11.5)]


def build(g):
    for i, (w, y) in enumerate(RINGS):
        ring = g.piece(f"ring_{i}", "HEAD", (-w / 2, y, -w / 2), (w, 1, w))
        for f in ring.faces:
            for yy in range(f.h):
                for xx in range(f.w):
                    s = 3 if (xx - yy + 2 * i) % 4 else 2
                    if rnd(xx, yy, 36940 + i) < .06:
                        s -= 1
                    f.set(xx, yy, k("L", s + (1 if f.name == "top" else 0)) if i < 5 else k("K", 3))
        ring.bottom.fill(k("L", 1) if i < 5 else "K2")
        if i == 0:
            for f in ring.sides:
                f.fill(k("K", 3))
    cord = g.piece("cord_ring", "HEAD", (-4.8, -8.9, -4.8), (9, 1, 9))
    for f in cord.faces:
        f.fill(k("A", 2))
    for side, x in (("right", -4.3), ("left", 4.3)):
        tie = g.piece(f"tie_{side}", "HEAD", (-.5, 0, -.5), (1, 8, 1), pivot=(x, -8.6, -1.0), scale=(.5, 1, .5))
        for f in tie.faces:
            f.fill(k("A", 2))
