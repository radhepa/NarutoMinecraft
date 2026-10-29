"""Mito Ceremonial Kimono: after Mito's: a full-length formal kimono with a high collar crossed in red,
long hanging sleeves, a wide dark obi with a red cord and a great bow at the back, and the whirlpool
crest of Uzushiogakure on the back of the obi. One garment with its own floor-length skirt."""
from kit import belt
from kit_uzumaki import crest_patch, wide_sleeves
from paint import cap, solid, strip_fabric

META = {
    "name": "Mito Ceremonial Kimono",
    "gender": "unisex",
    "description": "High-collared formal kimono, long hanging sleeves, dark obi with the whirlpool crest and a back bow.",
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
    high = g.piece("high_collar", "TORSO", (-4.5, -2.0, -2.6), (9, 2, 5), inflate=.08)
    solid(high, "P", "velvet", 2303, 2)
    high.front.vline(4, 0, 1, "A2")
    for face in high.sides:
        face.hline(0, face.w - 1, 0, "A2")
    for i, (x, rz) in enumerate(((-2.4, 30), (2.4, -30))):
        loop = g.piece(f"bow_loop_{i}", "TORSO", (-1.5, -1.5, 0), (3, 3, 2), pivot=(x, 9.4, 2.6), rotation=(0, 0, rz))
        solid(loop, "D", "velvet", 2298 + i, 2)
    knot = g.piece("bow_knot", "TORSO", (-1.5, -1.5, 0), (3, 3, 2), pivot=(0, 9.4, 2.8))
    solid(knot, "D", "velvet", 2300, 2)
    crest_patch(g, "obi_crest", "TORSO", (0, 7.9, 4.85), size=6, ground="D2", ink="A3")
    for i, x in enumerate((-.8, .8)):
        tail = g.piece(f"bow_tail_{i}", "TORSO", (-1, 0, 0), (2, 6, 1), pivot=(x, 10.0, 3.0), motion="sway")
        solid(tail, "D", "velvet", 2301 + i, 2)
