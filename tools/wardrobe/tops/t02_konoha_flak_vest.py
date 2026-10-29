"""Konoha Flak Vest: the green padded vest of chunin and jonin, scroll pockets on the chest, a high
collar and the red Uzumaki swirl on the back and both shoulders, over a navy long-sleeved shirt."""
from kit_shinobi import flak_vest
from paint import cap, fabric, strip_fabric

META = {
    "name": "Konoha Flak Vest",
    "gender": "unisex",
    "description": "Padded green vest with scroll pockets, high collar and red swirls, over a navy shirt.",
    "tags": ["shinobi", "vest"],
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "D", "weave", 51, 2)
    cap(body, "D", seed=51)
    flak_vest(g)
    # Navy sleeves to the wrist.
    for side in ("right", "left"):
        arm = g.part(f"{side}_arm")
        strip_fabric(arm, "D", "weave", 54 + (side == "left"), 2, 0, 10)
        fabric(arm.top, "D", "weave", 54, 3)
        arm.strip.hline(0, arm.strip.w - 1, 10, "D1")
