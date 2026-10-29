"""Long Slit Skirt: a long sleek purple skirt to the shin, slit up the front to the knee over
bandaged legs, a lavender sash at the waist and navy open-toe sandals."""
from kit import belt, flaps
from kit_shinobi import sandals
from kit_yamanaka import wrapped
from paint import fabric, strip_fabric

META = {"name": "Long Slit Skirt", "gender": "unisex",
        "description": "Long purple skirt to the shin slit at the front, bandaged legs, lavender sash, sandals.",
        "tags": ["shinobi", "skirt"]}


def build(g):
    body = g.part("body")
    strip_fabric(body, "P", "smooth", 7570, 2, 9, 11)
    fabric(body.bottom, "P", "smooth", 7570, 1)
    for side in ("right", "left"):
        leg = g.part(f"{side}_leg")
        strip_fabric(leg, "K", "plain", 7571, 2, 0, 1)
        fabric(leg.top, "K", "plain", 7571, 2)
        wrapped(leg.strip, 0, 2, leg.strip.w - 1, 9)
    sandals(g)
    belt(g, "waist_sash", y=9.0, role="S", height=1, buckle=None, inflate=.2)
    for face in flaps(g, "waist_skirt", 10, "P", "smooth", 7572, width=9, hem="P1", top=10.0, front_z=-2.9,
                      back_z=1.9, slit=True):
        face.vline(0, 1, 9, "P1"), face.vline(8, 1, 9, "P3")
