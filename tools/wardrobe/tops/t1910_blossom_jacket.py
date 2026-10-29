"""Blossom Jacket: a genin's cropped rose jacket wrapped like a kimono with an accent-banded crossed
collar, three-quarter sleeves with turned-back cuffs, worn over a cream undershirt, the circle on
the back."""
from kit import roll
from kit_haruno import back_crest, kimono_trim
from paint import cap, fabric, k, strip_fabric

META = {
    "name": "Blossom Jacket",
    "gender": "unisex",
    "description": "Cropped kimono-wrapped rose jacket, accent-banded collar, three-quarter turned-back sleeves, cream undershirt.",
    "tags": ["shinobi", "genin"],
}

COLLAR = [(0, 5), (1, 5), (2, 4), (3, 4), (4, 3), (5, 3), (6, 2), (7, 2)]


def build(g):
    body, jacket = g.part("body"), g.part("jacket")
    strip_fabric(body, "S", "knit", 19620, 3)
    cap(body, "S", texture="knit", seed=19620, base=3)
    strip_fabric(jacket, "P", "weave", 19621, 2, 0, 7)
    fabric(jacket.top, "P", "weave", 19621, 3)
    kimono_trim(jacket.front, COLLAR, "A", base=2)
    for y in range(0, 2):
        jacket.front.clear(6, y), jacket.front.clear(7, y)
    jacket.strip.hline(0, jacket.strip.w - 1, 7, k("A", 2))
    for side in ("right", "left"):
        arm, sleeve = g.part(f"{side}_arm"), g.part(f"{side}_sleeve")
        strip_fabric(arm, "P", "weave", 19622, 2, 0, 6)
        strip_fabric(sleeve, "P", "weave", 19623 + (side == "left"), 2, 0, 5)
        fabric(sleeve.top, "P", "weave", 19623, 3)
    roll(g, "A", 5.2, base=2, prefix="cuff")
    back_crest(g, "P", texture="weave", seed=19625, size=8, pivot=(0, 1.4, 2.35))
