"""Innkeeper's Kimono: the inn's mistress or master in a full kimono of quiet stripe, a wide obi
with a cord at its middle, the long sleeves hanging and the collar crossed high; one garment with
its own skirt."""
from kit_hyuga import obi
from kit_kurama import kimono_sleeves, wrap_front
from kit_market import stripes
from paint import cap, k, strip_fabric

META = {
    "name": "Innkeeper's Kimono",
    "gender": "unisex",
    "description": "Full kimono in a quiet stripe, wide obi with a centre cord, long hanging sleeves, collar crossed high.",
    "tags": ["civilian", "kimono", "robe", "wrap"],
    "locked_to": "bc025_innkeeper_kimono_skirt",
    "covers_waist": True,
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "P", "weave", 36400, 2)
    cap(body, "P", seed=36400)
    for face in body.sides:
        stripes(face, k("P", 1), 3, offset=1)
    wrap_front(body.front, "S3", "S2", rows=7, start=1)
    for side in ("right", "left"):
        strip_fabric(g.part(f"{side}_arm"), "P", "weave", 36401, 2, 0, 9)
    for sleeve in kimono_sleeves(g, "P", "weave", 36402, length=9, top=-2.3, bell=True):
        for face in sleeve.sides:
            stripes(face, k("P", 1), 3, offset=1, rows=range(1, sleeve.h - 1))
    obi(g, "obi", "A", y=7.0, height=3, knot="back", accent="S3", seed=36405)
