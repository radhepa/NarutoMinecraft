"""Runner Wraps: trousers wound in cloth strips from the thigh to the ankle, tied off with a cord
under the knee, over split-toe soft boots: the long-distance runner's legs."""
from kit import footwear, leg_ring, waistband
from kit_shinobi import bandage
from paint import fabric, strip_fabric

META = {"name": "Runner Wraps", "gender": "unisex",
        "description": "Trousers wrapped from thigh to ankle, cord ties under the knee, split-toe soft boots.",
        "tags": ["shinobi", "wrap"]}


def build(g):
    waistband(g, "D", "twill", 34640)
    for side in ("right", "left"):
        leg = g.part(f"{side}_leg")
        strip_fabric(leg, "D", "twill", 34641, 2, 0, 1)
        fabric(leg.top, "D", "twill", 34641, 2)
        bandage(leg.strip, 0, 2, leg.strip.w - 1, 9)
    footwear(g, "boot", top=10, role="D", base=1)
    for side in ("right", "left"):
        g.part(f"{side}_leg").front.vline(1 if side == "right" else 2, 10, 11, "D0")
    leg_ring(g, "knee_cord", 4.0, "A", 2, size=(5, 1, 5), inflate=.02)
