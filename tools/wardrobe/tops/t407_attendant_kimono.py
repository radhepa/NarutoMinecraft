"""Attendant Kimono: the household's full-length kimono (top half), a plain wrap with long sleeves
and a wide lavender-banded obi tied in a square bow at the back. One garment with its long skirt."""
from kit_hyuga import kimono_sleeves, obi, wrap_front
from paint import cap, solid, strip_fabric

META = {
    "name": "Attendant Kimono",
    "gender": "unisex",
    "description": "Full-length plain wrap kimono, long sleeves, wide obi with a square bow.",
    "tags": ["hyuga", "kimono"],
    "covers_waist": True,
    "locked_to": "b405_attendant_kimono_skirt",
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "P", "velvet", 4781, 2)
    cap(body, "P", texture="velvet", seed=4781)
    wrap_front(body.front, trim="S3", rows=6, start=2)
    body.front.vline(7, 6, 11, "P1")
    sash = obi(g, "obi", "A", y=6.4, height=4, knot="back", accent="S3", seed=4783)
    sash.front.hline(0, 8, 0, "A3")
    kimono_sleeves(g, "sleeve", "P", "velvet", 4786, top=3.0, length=6, trim="S3", hand_rows=9)
    collar = g.piece("collar", "TORSO", (-4.5, -.9, -2.6), (9, 1, 5), inflate=.06)
    solid(collar, "S", "velvet", 4791, 3)
