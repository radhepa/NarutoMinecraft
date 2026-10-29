"""Scarf Tee: a plain tee with a long cloth scarf wound twice round the neck, its two ends streaming
out behind: the genin who saw it in a picture book and never took it off."""
from kit_academy import shirt
from paint import k, solid

META = {
    "name": "Scarf Tee",
    "gender": "unisex",
    "description": "Plain tee with a long scarf wound round the neck, its two ends streaming out behind.",
    "tags": ["shinobi", "genin"],
}


def build(g):
    body, arms = shirt(g, "S", "plain", 31210, sleeve=3, trim="S1")
    for face in (body.right, body.left):
        face.vline(1, 2, 10, "S1")
    body.strip.hline(0, body.strip.w - 1, 11, "S1")
    wrap = g.piece("scarf", "TORSO", (-4.5, -1.8, -2.7), (9, 3, 5), inflate=.1)
    solid(wrap, "A", "weave", 31211, 2)
    for face in wrap.sides:
        face.hline(0, face.w - 1, 0, "A3"), face.hline(0, face.w - 1, 1, "A1")
    for i, (x, rz, n) in enumerate(((-1.6, 10, 9), (.6, -6, 7))):
        end = g.piece(f"scarf_end_{i}", "TORSO", (-1, 0, 0), (2, n, 1), pivot=(x, .4, 2.6), rotation=(18, 0, rz),
                      motion="flap_back")
        solid(end, "A", "weave", 31212 + i, 2)
        end.back.hline(0, 1, n - 1, k("S", 3))
        end.back.hline(0, 1, n - 2, k("A", 1))
