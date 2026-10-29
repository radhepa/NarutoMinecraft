"""Innkeeper's Kimono Skirt: the lower half of the Innkeeper's Kimono, falling straight to the
ankle in the same quiet stripe with the front panels overlapping, white tabi and zori."""
from kit import flaps, side_panels
from kit_hyuga import tabi
from kit_market import stripes
from paint import fabric, k, strip_fabric

META = {"name": "Innkeeper's Kimono Skirt", "gender": "unisex",
        "description": "Ankle-length striped kimono skirt with overlapping front panels, white tabi and zori.",
        "tags": ["civilian", "kimono", "robe"], "locked_to": "tc020_innkeeper_kimono"}


def build(g):
    body = g.part("body")
    strip_fabric(body, "P", "weave", 36875, 2, 9, 11)
    fabric(body.bottom, "P", "weave", 36875, 1)
    for side in ("right", "left"):
        leg = g.part(f"{side}_leg")
        strip_fabric(leg, "P", "weave", 36876, 1, 0, 8)
        fabric(leg.top, "P", "weave", 36876, 1)
    for face in flaps(g, "kimono", 11, "P", "weave", 36877, width=9, hem="S3", top=11.2, front_z=-2.75, back_z=1.75):
        stripes(face, k("P", 1), 3, offset=1, rows=range(1, 10))
        if face.name == "front":
            face.vline(5, 1, 10, "S3"), face.vline(6, 1, 10, k("P", 0))
    side_panels(g, "kimono_side", 11, "P", "weave", hem="S3", top=11.2)
    tabi(g, strap="A2")
