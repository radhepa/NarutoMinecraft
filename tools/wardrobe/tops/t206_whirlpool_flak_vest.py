"""Whirlpool Flak Vest: the Konoha flak vest whose red swirl is the Uzumaki crest, worn by the clan's
jonin over a long-sleeved shirt with the swirl patches on both shoulders and wave-banded cuffs."""
from kit_shinobi import flak_vest
from kit_uzumaki import waves
from paint import cap, fabric, strip_fabric

META = {
    "name": "Whirlpool Flak Vest",
    "gender": "unisex",
    "description": "Konoha flak vest with the Uzumaki swirl, swirl shoulder patches, wave-banded cuffs.",
    "tags": ["shinobi", "vest", "jonin"],
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "D", "weave", 2260, 2)
    cap(body, "D", seed=2260)
    for side in ("right", "left"):
        arm = g.part(f"{side}_arm")
        strip_fabric(arm, "D", "weave", 2261 + (side == "left"), 2, 0, 10)
        fabric(arm.top, "D", "weave", 2261, 3)
        waves(arm.strip, 8, "A", 2)
        arm.strip.hline(0, arm.strip.w - 1, 10, "D1")
    flak_vest(g, seed=2263)
