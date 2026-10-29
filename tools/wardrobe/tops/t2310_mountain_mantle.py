"""Mountain Mantle: a short umber shoulder cape against the mountain wind, pinned at the throat with
an ochre clasp and fringed in web-line trim, over a plain plum shirt: the academy children's
winter kit."""
from kit import body, neckline, sleeves
from kit_tsuchigumo import web_hem
from paint import k, solid

META = {
    "name": "Mountain Mantle",
    "gender": "unisex",
    "description": "Short umber shoulder cape with an ochre clasp and web-line trim over a plum shirt.",
    "tags": ["shinobi", "genin"],
}


def build(g):
    shirt = body(g, "P", "weave", 23671)
    neckline(shirt.front, "round", "P")
    shirt.strip.hline(0, shirt.strip.w - 1, 11, k("P", 1))
    sleeves(g, "P", "weave", 23672, rows=(0, 9), cuff="P3")
    cape = g.piece("mantle", "TORSO", (-5, -.4, -3), (10, 5, 6), inflate=.15)
    solid(cape, "L", "tweed", 23675, 2)
    cape.top.fill(k("L", 3))
    for face in cape.sides:
        web_hem(face, 4, "A2", "A1")
    for side, x in (("right", -6.4), ("left", 5.4)):
        drape = g.piece(f"mantle_{side}", "TORSO", (0, 0, -3), (1, 4, 6), pivot=(x, .4, 0), inflate=.15)
        solid(drape, "L", "tweed", 23677, 2)
        for face in drape.sides:
            face.hline(0, face.w - 1, 3, "A2")
    clasp = g.piece("clasp", "TORSO", (-1, -1, -.5), (2, 2, 1), pivot=(0, .8, -3.3))
    solid(clasp, "A", "smooth", 23679, 3, edge=False)
