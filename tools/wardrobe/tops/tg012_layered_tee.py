"""Layered Tee: a short-sleeved tee worn over a striped long-sleeved undershirt, with a big swirl
printed across the back: the genin who dresses in whatever is clean."""
from glyphs import SWIRL
from kit_academy import back_crest, shirt, stripes
from paint import fabric, strip_fabric

META = {
    "name": "Layered Tee",
    "gender": "unisex",
    "description": "Short-sleeved tee over a striped long-sleeved undershirt, a swirl printed on the back.",
    "tags": ["shinobi", "genin"],
}


def build(g):
    body, arms = shirt(g, "P", "plain", 31165, sleeve=11, sleeve_role="S")
    for arm in arms:
        stripes(arm, (5, 7, 9), "K2")
        arm.strip.hline(0, arm.strip.w - 1, 11, "S1")
    for side in ("right", "left"):
        sleeve = g.part(f"{side}_sleeve")
        strip_fabric(sleeve, "P", "plain", 31166 + (side == "left"), 2, 0, 3)
        fabric(sleeve.top, "P", "plain", 31166, 3)
        sleeve.strip.hline(0, sleeve.strip.w - 1, 3, "P1")
    f = body.front
    f.hline(2, 5, 0, "S2"), f.hline(3, 4, 1, "S2"), f.set(2, 1, "P1"), f.set(5, 1, "P1")
    body.strip.hline(0, body.strip.w - 1, 11, "P1")
    back_crest(g, "P", "A2", 31168, y=2.4, rows=SWIRL)
