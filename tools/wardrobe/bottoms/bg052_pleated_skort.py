"""Pleated Skort: a short pleated skirt sewn over shorts, pleats crisp all round, with knee-high
socks banded at the top and open-toe sandals."""
from kit import flaps, side_panels, stockings
from kit_shinobi import sandals
from paint import fabric, strip_fabric

META = {"name": "Pleated Skort", "gender": "female",
        "description": "Short pleated skirt over shorts, banded knee-high socks, sandals.",
        "tags": ["shinobi", "skirt"]}


def build(g):
    body = g.part("body")
    strip_fabric(body, "P", "rib", 33620, 2, 9, 11)
    fabric(body.bottom, "P", "rib", 33620, 1)
    for side in ("right", "left"):
        leg = g.part(f"{side}_leg")
        strip_fabric(leg, "P", "plain", 33621, 1, 0, 1)
        fabric(leg.top, "P", "plain", 33621, 1)
    stockings(g, "S", (5, 9), base=3)
    for side in ("right", "left"):
        g.part(f"{side}_leg").strip.hline(0, 15, 5, "A2")
    sandals(g)
    for face in flaps(g, "waist_skirt", 4, "P", "rib", 33622, width=9, hem="P1", top=10.6, front_z=-2.9, back_z=1.9):
        face.hline(0, 8, 0, "P3")
    side_panels(g, "waist_skirt_side", 4, "P", "rib", hem="P1", top=10.6)
