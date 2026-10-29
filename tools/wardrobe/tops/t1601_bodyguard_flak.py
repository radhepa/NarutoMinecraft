"""Bodyguard Flak: the jonin flak vest zipped over a dark long-sleeved shirt, the sleeves pushed to
the forearm where a leather cuff carries a row of senbon on the left wrist: the Hokage's guard on
duty, relaxed but never unarmed."""
from kit_shinobi import flak_vest
from kit_shiranui import wrist_holster
from paint import cap, fabric, strip_fabric

META = {
    "name": "Bodyguard Flak",
    "gender": "unisex",
    "description": "Jonin flak vest over a dark shirt, a senbon cuff on the left wrist.",
    "tags": ["shinobi", "jonin", "vest"],
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "D", "weave", 16760, 2)
    cap(body, "D", seed=16760)
    flak_vest(g, seed=16761)
    for side in ("right", "left"):
        arm = g.part(f"{side}_arm")
        strip_fabric(arm, "D", "weave", 16762 + (side == "left"), 2, 0, 11)
        fabric(arm.top, "D", "weave", 16762, 3)
        arm.strip.hline(0, arm.strip.w - 1, 6, "D3"), arm.strip.hline(0, arm.strip.w - 1, 7, "D1")
    wrist_holster(g, "left", seed=16764, y=7.6)
