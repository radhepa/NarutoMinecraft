"""Shorts and Thigh Wraps: snug shorts with a rolled cuff, bandages wound round both thighs above
the knee, a holster on the left thigh, and shin-high sandals with wrapped ankles."""
from kit_kunoichi import thigh_holster
from kit_shinobi import bandage, sandals
from paint import fabric, strip_fabric

META = {"name": "Shorts and Thigh Wraps", "gender": "unisex",
        "description": "Snug cuffed shorts, bandaged thighs, a left thigh holster, sandals with ankle wraps.",
        "tags": ["shinobi"]}


def build(g):
    body = g.part("body")
    strip_fabric(body, "P", "twill", 33520, 2, 9, 11)
    fabric(body.bottom, "P", "twill", 33520, 1)
    body.strip.hline(0, body.strip.w - 1, 9, "P3")
    for side in ("right", "left"):
        leg = g.part(f"{side}_leg")
        strip_fabric(leg, "P", "twill", 33521, 2, 0, 1)
        fabric(leg.top, "P", "twill", 33521, 2)
        leg.strip.hline(0, 15, 1, "P3")
        bandage(leg.strip, 0, 3, 15, 4)
        bandage(leg.strip, 0, 8, 15, 9)
    sandals(g)
    thigh_holster(g, side="left", y=2.0, seed=33522)
