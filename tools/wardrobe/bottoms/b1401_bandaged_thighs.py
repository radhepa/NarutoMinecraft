"""Bandaged Thighs: Kurenai's legs under her wrap dress: snug dark shorts, the upper thighs bound
in broad bandage turns, bare shins and navy open-toe sandals."""
from kit_shinobi import sandals
from kit_yuhi import bandage_turns
from paint import fabric, strip_fabric

META = {"name": "Bandaged Thighs", "gender": "female",
        "description": "Dark shorts, broad bandages round the upper thighs, bare shins, navy sandals.",
        "tags": ["shinobi", "wrap"]}


def build(g):
    body = g.part("body")
    strip_fabric(body, "K", "plain", 14900, 2, 9, 11)
    fabric(body.bottom, "K", "plain", 14900, 1)
    for side in ("right", "left"):
        leg = g.part(f"{side}_leg")
        strip_fabric(leg, "K", "plain", 14901, 2, 0, 1)
        fabric(leg.top, "K", "plain", 14901, 2)
        bandage_turns(leg.strip, 0, 2, leg.strip.w - 1, 5, "S", 3, lean=1 if side == "right" else -1)
        leg.strip.hline(0, leg.strip.w - 1, 5, "S2")
    sandals(g)
