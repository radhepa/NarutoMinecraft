"""Root Trousers: the Foundation's close black trousers, after Sai and Torune: plain dark legs
strapped once at the shin, a holster on the right thigh and open-toe sandals."""
from kit_shinobi import sandals
from paint import fabric, solid, strip_fabric

META = {"name": "Root Trousers", "gender": "unisex",
        "description": "Close black trousers strapped once at the shin, a right thigh holster, sandals.",
        "tags": ["shinobi"]}


def build(g):
    body = g.part("body")
    strip_fabric(body, "K", "twill", 13820, 2, 9, 11)
    body.strip.hline(0, body.strip.w - 1, 9, "K3")
    fabric(body.bottom, "K", "twill", 13820, 1)
    for side in ("right", "left"):
        leg = g.part(f"{side}_leg")
        strip_fabric(leg, "K", "twill", 13821 + (side == "left"), 2, 0, 9)
        fabric(leg.top, "K", "twill", 13821, 2)
        leg.front.vline(1 if side == "right" else 2, 1, 9, "K3")
        leg.strip.hline(0, leg.strip.w - 1, 7, "K0")
    sandals(g)
    strap = g.piece("holster_strap", "RIGHT_LEG", (-2.45, 1.0, -2.45), (5, 1, 5))
    solid(strap, "K", "leather", 13823, 3)
    holster = g.piece("holster", "RIGHT_LEG", (0, 0, 0), (1, 3, 2), pivot=(-3.0, .8, -1.0))
    solid(holster, "K", "leather", 13824, 3)
    holster.right.set(0, 0, "M3")
