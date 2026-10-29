"""Haragake: the tradesman's bib apron worn over a close-fitting long-sleeved undershirt, dyed deep
with a pale shop mark, a deep pouch pocket across the belly for coins and tallies, and its straps
crossed behind."""
from kit_market import bib, mark, pocket, sleeves
from paint import cap, strip_fabric

META = {
    "name": "Haragake",
    "gender": "unisex",
    "description": "Dark bib apron with a pale shop mark and a deep belly pocket over a fitted long-sleeved undershirt.",
    "tags": ["civilian", "work", "apron"],
    "tucked": True,
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "S", "knit", 36080, 2)
    cap(body, "S", seed=36080)
    body.front.hline(2, 5, 0, "S1")
    sleeves(g, "S", "knit", 36081, rows=(0, 11), base=2, overlay=False)
    for side in ("right", "left"):
        g.part(f"{side}_arm").strip.hline(0, 15, 11, "S1")
    front = bib(g, "haragake", "P", 36083, length=10, width=6, top=1.0, base=2, strap="P1")
    mark(front, "igeta", 1, 1, "S3")
    pouch = pocket(g, "pouch", "P", (0, 7.4, -3.75), size=(6, 3), seed=36085, base=1)
    pouch.front.hline(0, 5, 0, "A2")
