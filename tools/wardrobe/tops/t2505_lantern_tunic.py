"""Lantern Tunic: an academy pupil's short-sleeved tunic in the clan's grey, a small knitted scarf
knotted at the throat with its ends down the chest, a plain belt and the first paper-lantern charm
a Tobari child is given, tied at the hip."""
from kit import belt, sleeves
from kit_tobari import lantern, muffler, plain_body
from paint import fabric

META = {
    "name": "Lantern Tunic",
    "gender": "unisex",
    "description": "Short-sleeved grey tunic, a small knitted scarf knotted at the throat, a belt and a paper-lantern charm.",
    "tags": ["shinobi", "genin"],
}


def build(g):
    body = plain_body(g, "P", "weave", 25420)
    body.strip.hline(0, body.strip.w - 1, 11, "P1")
    body.front.vline(5, 1, 8, "P1")
    for arm in sleeves(g, "P", "weave", 25421, rows=(0, 4), cuff="P1"):
        fabric(arm.top, "P", "weave", 25421, 3)
    muffler(g, "scarf", "S", "knit", 25423, tails="front")
    belt(g, "belt", y=9.6, role="L", height=1)
    lantern(g, "lantern", pivot=(-2.6, 10.2, -2.9))
