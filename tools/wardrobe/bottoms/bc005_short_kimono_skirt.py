"""Short Kimono Skirt: the lower half of a plain everyday kimono worn to the knee for work, the
front panels overlapping, white tabi and wooden geta."""
from kit import flaps, side_panels
from kit_market import geta
from paint import fabric, k, strip_fabric

META = {"name": "Short Kimono Skirt", "gender": "unisex",
        "description": "Knee-length plain kimono skirt with overlapping front panels, white tabi and geta.",
        "tags": ["civilian", "skirt", "kimono"]}


def build(g):
    body = g.part("body")
    strip_fabric(body, "P", "weave", 36575, 2, 9, 11)
    fabric(body.bottom, "P", "weave", 36575, 1)
    for side in ("right", "left"):
        leg = g.part(f"{side}_leg")
        strip_fabric(leg, "P", "weave", 36576, 1, 0, 5)
        fabric(leg.top, "P", "weave", 36576, 1)
    for face in flaps(g, "skirt", 7, "P", "weave", 36577, width=9, hem=k("P", 1), top=11.2):
        if face.name == "front":
            face.vline(5, 1, 6, k("P", 3)), face.vline(6, 1, 6, k("P", 1))
    side_panels(g, "skirt_side", 7, "P", "weave", hem=k("P", 1), top=11.2)
    geta(g, sock="S3")
