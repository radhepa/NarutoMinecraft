"""Carpenter's Trousers: narrow dark work trousers with patched knees for kneeling on beams, a
cord at the waist and split-toe jika-tabi laced to mid-calf."""
from kit_market import jika_tabi, patch
from paint import fabric, k, solid, strip_fabric

META = {"name": "Carpenter's Trousers", "gender": "unisex",
        "description": "Narrow dark work trousers with patched knees, a waist cord, jika-tabi to mid-calf.",
        "tags": ["civilian", "trousers", "work"]}


def build(g):
    body = g.part("body")
    strip_fabric(body, "K", "twill", 36770, 3, 9, 11)
    fabric(body.bottom, "K", "twill", 36770, 2)
    for side in ("right", "left"):
        leg = g.part(f"{side}_leg")
        strip_fabric(leg, "K", "twill", 36771 + (side == "left"), 3, 0, 9)
        fabric(leg.top, "K", "twill", 36771, 3)
        patch(leg.front, 0, 3, 4, 2, "K", 4)
    cord = g.piece("waist_cord", "TORSO", (-4.5, 0, -2.5), (9, 1, 5), pivot=(0, 9.0, 0), inflate=.16)
    solid(cord, "A", "weave", 36773, 2, edge=False)
    jika_tabi(g, "D", top=6, seed=36775)
