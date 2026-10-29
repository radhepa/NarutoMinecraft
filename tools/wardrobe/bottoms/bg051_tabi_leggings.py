"""Tabi Leggings: close-fitting leggings with a seam down the outside, split-toe tabi boots to
mid-shin with clasps at the back, and a plain belt with a scroll case at the back."""
from kit import belt
from kit_kunoichi import tabi_boots
from paint import fabric, solid, strip_fabric

META = {"name": "Tabi Leggings", "gender": "unisex",
        "description": "Close leggings with an outer seam, split-toe tabi boots, a belt with a scroll case.",
        "tags": ["shinobi"]}


def build(g):
    body = g.part("body")
    strip_fabric(body, "P", "smooth", 33600, 2, 9, 11)
    fabric(body.bottom, "P", "smooth", 33600, 1)
    for side in ("right", "left"):
        leg = g.part(f"{side}_leg")
        strip_fabric(leg, "P", "smooth", 33601, 2, 0, 11)
        fabric(leg.top, "P", "smooth", 33601, 2)
        outer = leg.right if side == "right" else leg.left
        outer.vline(2, 0, 8, "P1")
    tabi_boots(g, top=7, seed=33602)
    belt(g, "waist_belt", y=9.4, role="L", height=1, buckle="M")
    case = g.piece("waist_scroll", "TORSO", (-3, -.5, -.5), (6, 1, 1), pivot=(0, 10.2, 2.7))
    solid(case, "S", "plain", 33604, 3)
    case.back.set(0, 0, "A2"), case.back.set(5, 0, "A2")
