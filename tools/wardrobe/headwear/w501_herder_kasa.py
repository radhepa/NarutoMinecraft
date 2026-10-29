"""Herder Kasa: a broad, shallow woven hat for long days in the deer paddocks, tied under the knot
of the hair with a cord. It sits over the whole head and hides the hairstyle."""
from paint import fabric, solid

META = {"name": "Herder Kasa", "gender": "unisex", "hides_hair": ["*"],
        "description": "A broad shallow woven hat for the deer paddocks."}


def build(g):
    crown = g.piece("crown", "HEAD", (-4, -9, -4), (8, 2, 8), inflate=.62)
    solid(crown, "L", "weave", 5701, 3, edge=False)
    for i, (w, y, base) in enumerate(((14, -8.0, 2), (10, -9.0, 3), (6, -10.0, 3), (2, -10.6, 4))):
        ring = g.piece(f"brim_{i}", "HEAD", (-w / 2, y, -w / 2), (w, 1, w))
        solid(ring, "L", "weave", 5702 + i, base, edge=False)
        fabric(ring.top, "L", "weave", 5706 + i, base + 1)
        for face in ring.sides:
            for x in range(0, face.w, 2):
                face.set(x, 0, "L1")
    band = g.piece("band", "HEAD", (-4, -8, -4), (8, 1, 8), inflate=.7)
    solid(band, "K", "weave", 5710, 2, edge=False)
