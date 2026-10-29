"""Taped Trousers: straight field trousers taped flat at the knee and the ankle so nothing snags, a
holster tied to the left thigh and open-toe sandals."""
from kit_field import holster, tape, trousers
from kit_shinobi import sandals

META = {"name": "Taped Trousers", "gender": "unisex",
        "description": "Straight trousers taped at the knee and ankle, a tied holster on the left thigh, sandals.",
        "tags": ["shinobi"]}


def build(g):
    trousers(g, "D", 32400, length=9, crease=True)
    for side in ("right", "left"):
        tape(g.part(f"{side}_leg"), (5, 8, 9))
    holster(g, "left", 32404, tied=True)
    sandals(g)
