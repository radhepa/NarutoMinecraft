"""Steel Slacks: straight steel-grey trousers to the ankle with a pressed crease and a dark belt, a
slim needle holster on the left thigh and sandals: the tidy kit of the Hokage's escort."""
from kit import belt, legs
from kit_shinobi import sandals
from kit_shiranui import thigh_holster
from paint import fabric, strip_fabric

META = {"name": "Steel Slacks", "gender": "unisex",
        "description": "Straight steel trousers with a crease, dark belt, a needle holster on the left thigh, sandals.",
        "tags": ["shinobi"]}


def build(g):
    body = g.part("body")
    strip_fabric(body, "P", "twill", 16870, 2, 9, 11)
    fabric(body.bottom, "P", "twill", 16870, 1)
    legs(g, "P", "twill", 16871, rows=(0, 10))
    sandals(g)
    for side in ("right", "left"):
        g.part(f"{side}_leg").strip.hline(0, 15, 9, "P1")
    belt(g, "waist_belt", y=9.2, role="K", buckle="M", height=1)
    thigh_holster(g, "left", seed=16873, needles=2)
