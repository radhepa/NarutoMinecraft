"""Field Shirt: the clan's working look for the bug keepers' fields, a khaki short-sleeved shirt open
at the neck with rolled sleeves, a belt and a corked insect jar riding on the hip."""
from kit import belt, neckline, roll
from kit_aburame import BEETLE, glyph
from paint import cap, fabric, k, solid, strip_fabric

META = {
    "name": "Field Shirt",
    "gender": "unisex",
    "description": "Open-necked khaki shirt with rolled sleeves, a belt and an insect jar on the hip.",
    "tags": ["shinobi", "aburame"],
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "P", "weave", 10671, 2)
    cap(body, "P", seed=10671)
    f = body.front
    neckline(f, "v", "P")
    f.vline(4, 4, 8, "P1")
    for y in (5, 7):
        f.set(3, y, "S3")
    f.hline(0, 2, 2, "P3"), f.hline(5, 7, 2, "P3")   # chest pocket flaps
    for side in ("right", "left"):
        arm = g.part(f"{side}_arm")
        strip_fabric(arm, "P", "weave", 10672 + (side == "left"), 2, 0, 3)
        fabric(arm.top, "P", "weave", 10672, 3)
    roll(g, "P", 3.0, prefix="sleeve_roll")
    belt(g, "belt", y=9.6)
    jar = g.piece("insect_jar", "TORSO", (-1, 0, -1), (2, 3, 2), pivot=(-4.6, 9.6, -.5))
    solid(jar, "S", "smooth", 10675, 3)
    for face in jar.sides:
        face.hline(0, 1, 1, "A2")
    cork = g.piece("jar_cork", "TORSO", (-.5, -1, -.5), (1, 1, 1), pivot=(-4.6, 9.6, -.5))
    solid(cork, "L", "plain", 10676, 3, edge=False)
    badge = g.piece("beetle_badge", "TORSO", (0, 0, 0), (8, 8, 1), pivot=(-2.0, 1.6, 2.1), scale=(.5, .5, .5))
    for face in badge.faces:
        fabric(face, "P", "weave", 10677, 2)
    glyph(badge.back, BEETLE, 0, 0, {"#": "A2", "+": "A0"})
