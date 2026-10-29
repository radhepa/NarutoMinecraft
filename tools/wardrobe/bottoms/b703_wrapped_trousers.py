"""Wrapped Trousers: slim purple trousers bound below the knee in bandage wraps that run down to the
ankle, a dark sash at the waist and navy open-toe sandals."""
from kit import belt, legs
from kit_shinobi import sandals
from kit_yamanaka import wrapped
from paint import fabric, strip_fabric

META = {"name": "Wrapped Trousers", "gender": "unisex",
        "description": "Slim purple trousers, bandage wraps from knee to ankle, dark sash, navy sandals.",
        "tags": ["shinobi"]}


def build(g):
    body = g.part("body")
    strip_fabric(body, "P", "twill", 7370, 2, 9, 11)
    fabric(body.bottom, "P", "twill", 7370, 1)
    legs(g, "P", "twill", 7371, 2, rows=(0, 5))
    for side in ("right", "left"):
        leg = g.part(f"{side}_leg")
        wrapped(leg.strip, 0, 6, leg.strip.w - 1, 9)
    belt(g, "waist_sash", y=9.0, role="K", height=1, buckle=None, inflate=.15)
    sandals(g)
