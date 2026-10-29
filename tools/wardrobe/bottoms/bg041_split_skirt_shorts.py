"""Split Skirt Shorts: fitted shorts under a short skirt split up the front and back into four
panels, a holster on the right thigh and open-toe sandals: the genin kunoichi's running skirt."""
from kit import belt, flaps
from kit_kunoichi import thigh_holster
from kit_shinobi import sandals
from paint import fabric, strip_fabric

META = {"name": "Split Skirt Shorts", "gender": "unisex",
        "description": "Fitted shorts under a short skirt split front and back, a thigh holster, sandals.",
        "tags": ["shinobi", "skirt"]}


def build(g):
    body = g.part("body")
    strip_fabric(body, "K", "plain", 33400, 2, 9, 11)
    fabric(body.bottom, "K", "plain", 33400, 1)
    for side in ("right", "left"):
        leg = g.part(f"{side}_leg")
        strip_fabric(leg, "K", "plain", 33401, 2, 0, 2)
        fabric(leg.top, "K", "plain", 33401, 2)
        leg.strip.hline(0, 15, 2, "K1")
    sandals(g)
    thigh_holster(g, side="right", y=2.6, seed=33402)
    belt(g, "waist_band", y=9.4, role="P", height=1, buckle=None, inflate=.15)
    for face in flaps(g, "waist_skirt", 5, "P", "weave", 33404, width=9, hem="A2", top=10.2, front_z=-2.9, back_z=1.9,
                      slit=True):
        face.vline(0, 1, 4, "P1"), face.vline(8, 1, 4, "P3")
