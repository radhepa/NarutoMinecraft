"""Guardian Vest: Asuma Sarutobi. The green jonin flak vest over a navy shirt, the sash of the
Twelve Guardian Ninja knotted at the waist with the kanji for fire on its right hip, black
fingerless gloves and a chakra trench knife on the right fist."""
from kit_sarutobi import guardian_sash, trench_knife
from kit_shinobi import flak_vest
from paint import fabric, strip_fabric

META = {
    "name": "Guardian Vest",
    "gender": "unisex",
    "description": "Flak vest over a navy shirt, the Guardian Ninja sash with the fire kanji, a trench knife.",
    "tags": ["shinobi", "vest", "jonin"],
    "covers_waist": True,
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "D", "weave", 9701, 2)
    fabric(body.top, "D", "weave", 9701, 3), fabric(body.bottom, "D", "weave", 9702, 1)
    flak_vest(g, seed=9703)
    for side in ("right", "left"):
        arm = g.part(f"{side}_arm")
        strip_fabric(arm, "D", "weave", 9710 + (side == "left"), 2, 0, 8)
        fabric(arm.top, "D", "weave", 9710, 3)
        arm.strip.hline(0, arm.strip.w - 1, 8, "D1")
        strip_fabric(arm, "K", "smooth", 9712, 2, 9, 11)
        arm.strip.hline(0, arm.strip.w - 1, 9, "K3")
        arm.bottom.fill("K1")
    guardian_sash(g, "S", "K1", 9720)
    trench_knife(g, "right", 9730)
