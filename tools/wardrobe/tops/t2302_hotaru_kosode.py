"""Hotaru Kosode: the clan heir's travelling kosode, bone-pale silk wrapped right over left with a
plum collar band, short loose sleeves, an ochre sash, and on the back the earth spider of the seal
she carries."""
from kit import belt, body, sleeves
from kit_tsuchigumo import spider_crest
from paint import k, solid

META = {
    "name": "Hotaru Kosode",
    "gender": "unisex",
    "description": "Pale wrap-front kosode with a plum collar band, ochre sash and the spider seal on the back.",
    "tags": ["shinobi", "wrap"],
}


def build(g):
    torso = body(g, "S", "weave", 23431)
    jacket = body(g, "S", "weave", 23432, layer="jacket", rows=(0, 9))
    f = jacket.front
    for y in range(9):   # the plum collar band crossing from the right shoulder to the sash
        x = min(7, 1 + y // 2 + y // 3)
        f.set(x, y, "P2"), f.set(max(0, x - 1), y, "P3")
    jacket.back.hline(0, 7, 0, "P2")
    for name in ("right", "left"):
        getattr(jacket, name).hline(0, 3, 0, "P2")
    torso.front.hline(0, 7, 11, k("S", 1))
    for arm in sleeves(g, "S", "weave", 23433, rows=(0, 5), layer="sleeve"):
        for face in arm.sides:
            face.hline(0, face.w - 1, 5, "P2")
    sash = belt(g, "sash", y=8.6, role="A", height=2, buckle=None)
    sash.front.vline(5, 0, 1, "A1")
    knot = g.piece("sash_knot", "TORSO", (-1, 0, -1), (2, 2, 1), pivot=(0, 9.0, 2.9))
    solid(knot, "A", "weave", 23436, 2)
    spider_crest(g, "back_seal", "S", "P1", pivot=(0, 1.6, 2.15))
