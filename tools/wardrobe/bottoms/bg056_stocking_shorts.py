"""Stocking Shorts: loose shorts to mid-thigh with a drawstring waist, long striped stockings to
above the knee and open-toe sandals; the academy-age genin's favourite."""
from kit import stockings, waistband
from kit_shinobi import sandals
from paint import fabric, strip_fabric

META = {"name": "Stocking Shorts", "gender": "unisex",
        "description": "Loose drawstring shorts, long striped stockings above the knee, sandals.",
        "tags": ["shinobi", "genin", "casual"]}


def build(g):
    waistband(g, "P", "weave", 33700)
    body = g.part("body")
    body.front.set(3, 9, "S3"), body.front.set(4, 10, "S3")
    for side in ("right", "left"):
        leg = g.part(f"{side}_leg")
        strip_fabric(leg, "P", "weave", 33701, 2, 0, 2)
        fabric(leg.top, "P", "weave", 33701, 2)
        leg.strip.hline(0, 15, 2, "P1")
    stockings(g, "S", (4, 9), stripe="A2", base=3)
    sandals(g)
