"""Scholar Split Skirt: a long wrapped skirt in the coat colour, open in a deep front split over dark
leggings, a sash at the waist with a brush case hanging from it, and split-toe socks with sandals."""
from kit import belt, flaps
from kit_hyuga import tabi
from kit_specialist import scroll_tube
from paint import fabric, strip_fabric

META = {"name": "Scholar Split Skirt", "gender": "unisex",
        "description": "Long wrapped skirt with a deep front split over dark leggings, sash with a brush case, tabi.",
        "tags": ["shinobi", "skirt"]}


def build(g):
    body = g.part("body")
    strip_fabric(body, "P", "weave", 34740, 2, 9, 11)
    fabric(body.bottom, "P", "weave", 34740, 1)
    for side in ("right", "left"):
        leg = g.part(f"{side}_leg")
        strip_fabric(leg, "K", "plain", 34741, 2, 0, 8)
        fabric(leg.top, "K", "plain", 34741, 2)
    tabi(g, "S", "K1", "K2")
    belt(g, "waist_sash", y=9.0, role="S", height=1, buckle=None, inflate=.15)
    for face in flaps(g, "waist_skirt", 11, "P", "weave", 34742, width=9, hem="P1", top=10.0, front_z=-2.9,
                      back_z=1.9, slit=True):
        face.vline(3, 1, 10, "P1")
    scroll_tube(g, "waist_brush_case", (3.6, 9.6, -2.6), (0, 0, -6), length=4, role="L", seed=34745, width=1)
