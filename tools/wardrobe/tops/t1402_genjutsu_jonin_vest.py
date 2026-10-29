"""Genjutsu Jonin Vest: the Konoha flak vest as Shinku Yuhi and Mirai wore it, over a black long-
sleeved shirt; a crimson thorn stem climbs the right forearm and the right forearm is bound in
bandages for weaving hand signs."""
from kit_shinobi import flak_vest
from kit_yuhi import bandage_turns, thorn_vine
from paint import fabric, strip_fabric

META = {
    "name": "Genjutsu Jonin Vest",
    "gender": "unisex",
    "description": "Flak vest over a black long-sleeved shirt, a thorn stem up the right sleeve, bandaged forearm.",
    "tags": ["shinobi", "vest", "jonin"],
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "K", "weave", 14630, 2)
    fabric(body.top, "K", "weave", 14631, 3), fabric(body.bottom, "K", "weave", 14631, 1)
    for side in ("right", "left"):
        arm = g.part(f"{side}_arm")
        strip_fabric(arm, "K", "weave", 14632 + (side == "left"), 2, 0, 11)
        fabric(arm.top, "K", "weave", 14634, 3), fabric(arm.bottom, "K", "weave", 14634, 1)
        arm.strip.hline(0, arm.strip.w - 1, 11, "K1")
    right = g.part("right_arm")
    thorn_vine(right.front, 1, 4, 6, "A")
    bandage_turns(right.strip, 0, 7, right.strip.w - 1, 10, "S", 3)
    flak_vest(g, shoulder_swirls=True, seed=14635)
