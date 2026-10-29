"""Mito Ceremonial Kimono: a full-length formal kimono, collar crossed in red, long hanging sleeves,
a wide dark obi with a red cord and a great bow at the back, and the whirlpool crest on the
shoulders above it. One garment with its own floor-length skirt."""
from kit import belt
from kit_uzumaki import crest_patch, wide_sleeves
from paint import cap, solid, strip_fabric

META = {
    "name": "Mito Ceremonial Kimono",
    "gender": "unisex",
    "description": "Formal kimono with a red-crossed collar, long hanging sleeves, dark obi and back bow.",
    "tags": ["robe", "ceremonial"],
    "covers_waist": True,
    "locked_to": "b205_ceremonial_kimono_skirt",
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "P", "velvet", 2295, 2)
    cap(body, "P", texture="velvet", seed=2295)
    f = body.front
    for y in range(8):
        f.set(y, y, "A2")
        if y + 1 <= 7:
            f.set(y + 1, y, "S3")
    f.set(0, 0, "S3"), f.set(7, 0, "A2")
    for side in ("right", "left"):
        arm = g.part(f"{side}_arm")
        strip_fabric(arm, "P", "velvet", 2296, 2, 0, 8)
    wide_sleeves(g, "P", "velvet", 2297, top=1.0, length=8, drop=5, trim="A2")
    obi = belt(g, "obi", y=6.6, role="D", height=4, buckle=None, inflate=.15)
    for face in obi.sides:
        face.hline(0, face.w - 1, 2, "A2")
    crest_patch(g, "back_crest", "TORSO", (0, .4, 2.05), size=12, ground="P2", ink="A2")
    for i, (x, rz) in enumerate(((-2.4, 30), (2.4, -30))):
        loop = g.piece(f"bow_loop_{i}", "TORSO", (-1.5, -1.5, 0), (3, 3, 2), pivot=(x, 8.4, 2.6), rotation=(0, 0, rz))
        solid(loop, "D", "velvet", 2298 + i, 2)
    knot = g.piece("bow_knot", "TORSO", (-1, -1, 0), (2, 2, 2), pivot=(0, 8.4, 2.8))
    solid(knot, "A", "velvet", 2300, 2)
    for i, x in enumerate((-.8, .8)):
        tail = g.piece(f"bow_tail_{i}", "TORSO", (-1, 0, 0), (2, 6, 1), pivot=(x, 9.0, 3.0), motion="sway")
        solid(tail, "D", "velvet", 2301 + i, 2)
