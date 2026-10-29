"""Field Vest: the jonin flak vest over a charcoal shirt with the sleeves rolled to the elbow,
bandaged forearms and a kunai pouch strapped to the right arm: a jonin back from a long mission."""
from kit import roll
from kit_shinobi import bandage, flak_vest
from paint import fabric, solid, strip_fabric

META = {
    "name": "Field Vest",
    "gender": "unisex",
    "description": "Flak vest over a charcoal shirt with rolled sleeves, bandaged forearms and an arm pouch.",
    "tags": ["shinobi", "vest", "jonin"],
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "D", "weave", 381, 2)
    fabric(body.top, "D", "weave", 381, 3), fabric(body.bottom, "D", "weave", 382, 1)
    flak_vest(g, seed=383)
    for side in ("right", "left"):
        arm = g.part(f"{side}_arm")
        strip_fabric(arm, "D", "weave", 390 + (side == "left"), 2, 0, 4)
        fabric(arm.top, "D", "weave", 390, 3)
        bandage(arm.strip, 0, 6, arm.strip.w - 1, 10)
    roll(g, "D", 3.6)
    strap = g.piece("arm_pouch_strap", "RIGHT_ARM", (-3.45, 1.6, -2.45), (5, 1, 5))
    solid(strap, "L", "leather", 392, 2, edge=False)
    pouch = g.piece("arm_pouch", "RIGHT_ARM", (0, 0, -1), (1, 2, 2), pivot=(-4.0, 1.4, 0))
    solid(pouch, "L", "leather", 393, 2)
    pouch.right.hline(0, 1, 0, "L3")
