"""Work Shorts: an apprentice's knee-length indigo work shorts with a patched knee, cream knee socks
and black jika-tabi."""
from kit import waistband
from kit_kinoshita import tabi
from paint import fabric, strip_fabric

META = {"name": "Work Shorts", "gender": "unisex",
        "description": "Knee-length indigo shorts with a patched knee, cream socks and black jika-tabi.",
        "tags": ["shinobi", "kinoshita"]}


def build(g):
    waistband(g, "D", "twill", 22681)
    for side in ("right", "left"):
        leg = g.part(f"{side}_leg")
        strip_fabric(leg, "D", "twill", 22682 + (side == "left"), 2, 0, 4)
        fabric(leg.top, "D", "twill", 22682, 2)
        leg.strip.hline(0, leg.strip.w - 1, 4, "D1")
        fabric(leg.strip, "S", "knit", 22684, 3, 0, 7, leg.strip.w, 2)
        leg.strip.hline(0, leg.strip.w - 1, 7, "S4")
    patch = g.part("left_leg").front
    patch.hline(0, 2, 2, "A2"), patch.hline(0, 2, 3, "A1")
    tabi(g, top=9)
