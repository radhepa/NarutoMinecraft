"""Wrapped Tank: a ribbed tank top with contrast binding at the neck and armholes, bandages wound
from the elbow to the knuckles and a cloth band knotted round the left arm: the taijutsu student."""
from kit_academy import forearm_wraps
from paint import cap, k, solid, strip_fabric

META = {
    "name": "Wrapped Tank",
    "gender": "unisex",
    "description": "Ribbed tank top with contrast binding, bandaged forearms and a cloth band on the left arm.",
    "tags": ["shinobi", "genin"],
    "tucked": True,
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "P", "rib", 31045, 2)
    cap(body, "P", texture="rib", seed=31045)
    f, b = body.front, body.back
    for face in (f, b):
        face.clear(0, 0), face.clear(7, 0)
        face.hline(1, 6, 0, "S3")
    f.clear(3, 0), f.clear(4, 0), f.hline(3, 4, 1, "S3"), f.set(2, 1, "S2"), f.set(5, 1, "S2")
    for face in (body.right, body.left):
        face.hline(0, face.w - 1, 0, "S3"), face.hline(0, face.w - 1, 1, "S2")
    body.top.fill(None)
    for x in (0, 7):
        for y in range(4):
            body.top.set(x, y, "S3")
    forearm_wraps(g, 5, 10)
    band = g.piece("arm_band", "LEFT_ARM", (-1.5, 1.2, -2.5), (5, 1, 5))
    solid(band, "A", "weave", 31046, 2, edge=False)
    for face in band.sides:
        face.hline(0, face.w - 1, 0, "A3")
    knot = g.piece("arm_band_knot", "LEFT_ARM", (0, 0, 0), (1, 1, 1), pivot=(3.5, 1.2, -.5))
    solid(knot, "A", "weave", 31047, 3, edge=False)
    tail = g.piece("arm_band_tail", "LEFT_ARM", (0, 0, 0), (1, 3, 1), pivot=(3.6, 2.0, -.2), rotation=(0, 0, -14),
                   motion="sway")
    solid(tail, "A", "weave", 31048, 2)
    tail.left.set(0, 2, k("A", 1))
