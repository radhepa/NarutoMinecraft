"""Little Pleated Skirt: a girl's short pleated skirt for play and school, with knee socks and
strapped cloth shoes."""
from kit_household import cloth_shoes, skirt, socks, waist

META = {"name": "Little Pleated Skirt", "gender": "female",
        "description": "Short pleated skirt with knee socks and strapped cloth shoes.",
        "tags": ["civilian", "skirt"]}


def pleats(face, rows=None):
    for y in rows or range(face.h):
        for x in range(0, face.w, 2):
            face.set(x, y, "D1")


def build(g):
    waist(g, "D", "plain", 37788, band="D3")
    socks(g, "S3", rows=(4, 9))
    cloth_shoes(g, "A", 2, strap="A3")
    skirt(g, "skirt", 4, "D", "plain", 37790, hem="D1", pattern=pleats)
