"""Hound Wrap Skirt: a navy wrap skirt split at the front over dark leggings, a slate sash with a
small white paw at the hip, white shin wraps and navy open-toe sandals."""
from kit import flaps
from kit_shinobi import sandals, wraps
from paint import fabric, solid, strip_fabric

META = {"name": "Hound Wrap Skirt", "gender": "unisex",
        "description": "Navy split wrap skirt over dark leggings, white shin wraps, navy sandals.",
        "tags": ["shinobi"]}


def build(g):
    body = g.part("body")
    strip_fabric(body, "D", "weave", 11301, 2, 9, 11)
    body.strip.hline(0, body.strip.w - 1, 9, "D3")
    fabric(body.bottom, "D", "weave", 11301, 1)
    for side in ("right", "left"):
        leg = g.part(f"{side}_leg")
        strip_fabric(leg, "K", "plain", 11302 + (side == "left"), 3, 0, 6)
        fabric(leg.top, "K", "plain", 11302, 3)
    wraps(g, 7, 9)
    sandals(g)
    for face in flaps(g, "waist_skirt", 6, "D", "weave", 11304, top=10.6, slit=True):
        face.hline(0, face.w - 1, 5, "D1")
