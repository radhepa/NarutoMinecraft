"""Hakama Skirt: a pleated hakama cut short and full as a skirt, its stiff back board showing above
the ties, worn over dark leggings with tabi boots."""
from kit import flaps, side_panels
from kit_kunoichi import tabi_boots
from paint import fabric, solid, strip_fabric

META = {"name": "Hakama Skirt", "gender": "unisex",
        "description": "Short pleated hakama skirt with a back board and ties, dark leggings, tabi boots.",
        "tags": ["shinobi", "skirt", "hakama"]}


def build(g):
    body = g.part("body")
    strip_fabric(body, "P", "twill", 33480, 2, 9, 11)
    fabric(body.bottom, "P", "twill", 33480, 1)
    for side in ("right", "left"):
        leg = g.part(f"{side}_leg")
        strip_fabric(leg, "K", "smooth", 33481, 2, 0, 9)
        fabric(leg.top, "K", "smooth", 33481, 2)
    tabi_boots(g, top=8, seed=33482)
    for face in flaps(g, "waist_hakama", 7, "P", "twill", 33484, width=9, hem="P1", top=10.0, front_z=-2.95, back_z=1.95):
        for x in (1, 3, 5, 7):
            face.vline(x, 1, 6, "P1")
        for x in (2, 6):
            face.vline(x, 1, 6, "P3")
    side_panels(g, "waist_hakama_side", 6, "P", "twill", hem="P1", top=10.0)
    board = g.piece("waist_koshiita", "TORSO", (-2.5, 0, 0), (5, 2, 1), pivot=(0, 8.6, 2.0))
    solid(board, "P", "twill", 33487, 2)
    tie = g.piece("waist_himo", "TORSO", (-4.6, 0, -2.6), (9, 1, 5), pivot=(0, 9.4, 0), inflate=.12)
    solid(tie, "S", "weave", 33488, 3, edge=False)
