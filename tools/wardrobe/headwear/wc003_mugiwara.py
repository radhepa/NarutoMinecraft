"""Mugiwara: the farmer's and the fish seller's round straw hat, a domed crown with a cloth band
and a broad flat brim against the sun, sitting above the hair."""
from paint import k, rnd

META = {"name": "Mugiwara Straw Hat", "gender": "unisex",
        "description": "Round straw hat with a domed crown, a cloth band and a broad flat brim.",
        "hides_hair": ["knot", "brush", "bun", "pin_", "crown", "puff_", "spike", "tuft", "top"]}


def straw(face, seed, lift=0):
    for y in range(face.h):
        for x in range(face.w):
            s = 3 if (x + 2 * y) % 4 else 2
            if rnd(x, y, seed) < .07:
                s -= 1
            face.set(x, y, k("L", s + lift))


def build(g):
    brim = g.piece("brim", "HEAD", (-7, -8.8, -7), (14, 1, 14))
    for f in brim.faces:
        straw(f, 36930, 1 if f.name == "top" else 0)
    brim.bottom.paint(lambda x, y, cur: k("L", 1))
    crown = g.piece("crown_dome", "HEAD", (-4.5, -11.4, -4.5), (9, 3, 9))
    for f in crown.faces:
        straw(f, 36931, 1 if f.name == "top" else 0)
    lid = g.piece("crown_lid", "HEAD", (-3.5, -12.2, -3.5), (7, 1, 7))
    for f in lid.faces:
        straw(f, 36932, 1)
    band = g.piece("band", "HEAD", (-4.6, -9.9, -4.6), (9, 1, 9), inflate=.05)
    for f in band.faces:
        f.fill(k("A", 2))
    for f in band.sides:
        f.hline(0, f.w - 1, 0, k("A", 3))
