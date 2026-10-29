"""Crossed Wrap Top: a short-sleeved top wrapped left over right and tied with a narrow sash at the
side, the lapel edged in the accent, forearms wound in bandages: the everyday genin kunoichi's top."""
from kit import sleeves
from kit_kunoichi import obi, wrap_front
from kit_shinobi import bandage
from paint import cap, strip_fabric

META = {
    "name": "Crossed Wrap Top",
    "gender": "unisex",
    "description": "Short-sleeved wrap top crossed left over right, a side-tied sash, bandaged forearms.",
    "tags": ["shinobi", "genin", "wrap"],
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "P", "weave", 33000, 2, 0, 10)
    cap(body, "P", texture="weave", seed=33000)
    wrap_front(body.front, "P", rows=8)
    for y in range(8):
        body.front.set(min(7, 2 + y * 5 // 7), y, "A2")
    body.front.hline(0, 7, 10, "P1")
    for side in sleeves(g, "P", "weave", 33001, rows=(0, 3), cuff="A2"):
        bandage(side.strip, 0, 6, side.strip.w - 1, 10)
    obi(g, "sash", y=8.4, role="A", height=1, knot="side", seed=33004)
