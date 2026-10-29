"""Kunoichi Greaves: fitted leggings with steel shin greaves strapped over them from knee to ankle,
a short wrap at the hip and open-toe sandals: armor light enough to run in."""
from kit import belt
from kit_shinobi import sandals
from paint import fabric, solid, strip_fabric

META = {"name": "Kunoichi Greaves", "gender": "unisex",
        "description": "Fitted leggings, steel shin greaves strapped knee to ankle, a hip wrap, sandals.",
        "tags": ["shinobi", "armor"]}


def build(g):
    body = g.part("body")
    strip_fabric(body, "K", "plain", 33780, 2, 9, 11)
    fabric(body.bottom, "K", "plain", 33780, 1)
    for side in ("right", "left"):
        leg = g.part(f"{side}_leg")
        strip_fabric(leg, "K", "plain", 33781, 2, 0, 9)
        fabric(leg.top, "K", "plain", 33781, 2)
    sandals(g)
    for side, bone in (("right", "RIGHT_LEG"), ("left", "LEFT_LEG")):
        plate = g.piece(f"{side}_greave", bone, (-2.2, 0, -.6), (4, 5, 1), pivot=(0, 5.0, -2.0), inflate=.1)
        solid(plate, "M", "plain", 33782, 3)
        plate.front.hline(0, 3, 0, "M4"), plate.front.vline(2, 1, 4, "M2")
        plate.front.set(0, 2, "L2"), plate.front.set(3, 2, "L2")
    belt(g, "waist_wrap", y=9.3, role="P", height=2, buckle=None, inflate=.15)
