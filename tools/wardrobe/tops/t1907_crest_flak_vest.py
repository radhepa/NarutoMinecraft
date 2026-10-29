"""Crest Flak Vest: the Konoha flak vest of a Haruno jonin over a long-sleeved rose shirt, with the
family's white circle patched on the left shoulder and rose fingerless gloves."""
from kit import sleeves
from kit_haruno import arm_crest
from kit_shinobi import flak_vest
from paint import cap, k, strip_fabric

META = {
    "name": "Crest Flak Vest",
    "gender": "unisex",
    "description": "Konoha flak vest over a long-sleeved rose shirt, circle patch on the left shoulder, rose gloves.",
    "tags": ["shinobi", "vest", "jonin"],
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "A", "weave", 19570, 1)
    cap(body, "A", texture="weave", seed=19570, base=1)
    flak_vest(g, shoulder_swirls=False, seed=19571)
    for box in sleeves(g, "A", "weave", 19580, 1, rows=(0, 11)):
        box.strip.hline(0, box.strip.w - 1, 8, k("A", 3))
        for y in (9, 10, 11):
            box.strip.hline(0, box.strip.w - 1, y, k("A", 2))
    arm_crest(g, "left", "A", seed=19582, base=1)
