"""Guard's Trousers: straight dark trousers bloused into pale shin wraps topped with the wave, a
black kunai holster on the right thigh and dark open-toe sandals."""
from kit import SIDES, leg_bone
from kit_namiashi import wave_band
from kit_shinobi import sandals, wraps
from paint import fabric, solid, strip_fabric

META = {"name": "Guard's Trousers", "gender": "unisex",
        "description": "Straight dark trousers into pale shin wraps edged with the wave, thigh holster, sandals.",
        "tags": ["shinobi"]}


def build(g):
    body = g.part("body")
    strip_fabric(body, "D", "twill", 20601, 2, 9, 11)
    body.strip.hline(0, body.strip.w - 1, 9, "D1")
    fabric(body.bottom, "D", "twill", 20601, 1)
    for side in SIDES:
        leg = g.part(f"{side}_leg")
        strip_fabric(leg, "D", "twill", 20602 + (side == "left"), 2, 0, 9)
        fabric(leg.top, "D", "twill", 20602, 2)
        leg.front.vline(1 if side == "right" else 2, 1, 5, "D3")
    wraps(g, 7, 9)
    for side in SIDES:
        wave_band(g.part(f"{side}_leg").strip, 6, "S", 2, ground="D2")
    sandals(g)
    strap = g.piece("holster_strap", "RIGHT_LEG", (-2.45, 1.0, -2.45), (5, 1, 5))
    solid(strap, "K", "leather", 20604, 2)
    holster = g.piece("holster", "RIGHT_LEG", (0, 0, 0), (1, 3, 2), pivot=(-3.0, .8, -1.0))
    solid(holster, "K", "leather", 20605, 2)
    holster.right.set(0, 0, "M3")
