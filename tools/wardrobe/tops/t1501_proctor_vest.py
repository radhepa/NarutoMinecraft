"""Proctor Vest: Hayate Gekko as the Chunin Exam proctor: the Konoha flak vest over a navy
long-sleeved shirt, a sword strap across the chest and his katana on the back, the hilt over the
right shoulder."""
from kit_gekko import katana, sword_strap
from kit_shinobi import flak_vest
from paint import cap, fabric, strip_fabric

META = {
    "name": "Proctor Vest",
    "gender": "unisex",
    "description": "Flak vest over a navy shirt, a sword strap across the chest, a katana on the back.",
    "tags": ["shinobi", "vest", "jonin"],
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "D", "weave", 15700, 2)
    cap(body, "D", seed=15700)
    flak_vest(g, seed=15701)
    jacket = g.part("jacket")
    sword_strap(jacket.front, "L", rows=10)
    sword_strap(jacket.back, "L", rows=10, mirror=True)
    for side in ("right", "left"):
        arm = g.part(f"{side}_arm")
        strip_fabric(arm, "D", "weave", 15710 + (side == "left"), 2, 0, 10)
        fabric(arm.top, "D", "weave", 15710, 3)
        arm.strip.hline(0, arm.strip.w - 1, 10, "D1")
    katana(g, pivot=(-1.4, 2.2, 3.1))
