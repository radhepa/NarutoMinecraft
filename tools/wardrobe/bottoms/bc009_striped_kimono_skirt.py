"""Striped Kimono Skirt: the merchant's long kimono in a fine woven stripe falling to the ankle,
the front overlapped, worn with white tabi and wooden geta."""
from kit import flaps, side_panels
from kit_market import geta, stripes
from paint import fabric, k, strip_fabric

META = {"name": "Striped Kimono Skirt", "gender": "unisex",
        "description": "Ankle-length kimono skirt in a fine woven stripe, overlapped front, white tabi and geta.",
        "tags": ["civilian", "skirt", "kimono"]}


def build(g):
    body = g.part("body")
    strip_fabric(body, "P", "weave", 36635, 2, 9, 11)
    fabric(body.bottom, "P", "weave", 36635, 1)
    for side in ("right", "left"):
        leg = g.part(f"{side}_leg")
        strip_fabric(leg, "P", "weave", 36636, 1, 0, 9)
        fabric(leg.top, "P", "weave", 36636, 1)
    for face in flaps(g, "skirt", 10, "P", "weave", 36637, width=9, hem=k("P", 1), top=11.2):
        stripes(face, k("P", 3), 2, rows=range(1, 9))
        if face.name == "front":
            face.vline(5, 1, 9, k("S", 3))
    side_panels(g, "skirt_side", 10, "P", "weave", hem=k("P", 1), top=11.2)
    geta(g, sock="S3")
