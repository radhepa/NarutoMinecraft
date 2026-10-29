"""Student Hakama: the skirt-cut andon hakama of the girls' and boys' writing school, deep pleats
falling to mid-shin, a stripe above the hem and lace-up leather boots beneath."""
from kit_household import skirt, trouser_legs, waist
from kit import footwear
from paint import solid

META = {"name": "Student Hakama", "gender": "unisex",
        "description": "Skirt-cut pleated andon hakama to mid-shin with a hem stripe, lace-up leather boots.",
        "tags": ["civilian", "hakama", "skirt"]}


def pleats(face, rows=None):
    for y in rows or range(face.h):
        for x in range(1, face.w, 2):
            face.set(x, y, "D1")
        face.set(0, y, "D1")


def build(g):
    waist(g, "D", "twill", 37804, band="D3")
    trouser_legs(g, "D", "twill", 37805, rows=(0, 6), base=1)
    footwear(g, "boot", top=6, role="L", base=2)
    for side in ("right", "left"):
        leg = g.part(f"{side}_leg")
        for y in range(7, 10):
            leg.front.set(1 + (y % 2), y, "S3")
    for face in skirt(g, "hakama", 9, "D", "twill", 37807, hem="D0", pattern=pleats):
        face.hline(0, face.w - 1, 7, "S3")
    tie = g.piece("waist_tie", "TORSO", (-4.5, 0, -2.5), (9, 1, 5), pivot=(0, 9.3, 0), inflate=.2)
    solid(tie, "D", "weave", 37810, 3, edge=False)
