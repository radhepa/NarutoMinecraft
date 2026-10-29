"""Kasuri Kimono Skirt: the skirt of a well-worn everyday kimono in splash-dyed kasuri, the front
overlap running to the ankle, over bare feet in wooden geta with a cloth thong."""
from kit_household import geta, kasuri, skirt, trouser_legs, waist

META = {"name": "Kasuri Kimono Skirt", "gender": "unisex",
        "description": "Ankle-length kasuri kimono skirt with the overlap at the front, wooden geta.",
        "tags": ["civilian", "kimono", "skirt"]}


def flecks(face, rows=None):
    kasuri(face, "P3", step=3, seed=1, rows=rows)


def build(g):
    waist(g, "P", "weave", 37676)
    trouser_legs(g, "P", "weave", 37677, rows=(0, 9), base=1)
    geta(g, strap="D2")
    for face in skirt(g, "kimono", 11, "P", "weave", 37679, hem="P0", pattern=flecks):
        if face.name == "front":
            face.vline(3, 1, 10, "P0")
