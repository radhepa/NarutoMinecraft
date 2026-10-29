"""Wave Shorts: knee-length teal shorts, the cuffs rolled with the pale wave, bare shins and dark
open-toe sandals, a dark cloth belt."""
from kit import SIDES
from kit_namiashi import wave_band
from kit_shinobi import sandals
from paint import fabric, strip_fabric

META = {"name": "Wave Shorts", "gender": "unisex",
        "description": "Knee-length teal shorts with wave-rolled cuffs, bare shins, dark sandals.",
        "tags": ["shinobi"]}


def build(g):
    body = g.part("body")
    strip_fabric(body, "P", "twill", 20611, 2, 9, 11)
    body.strip.hline(0, body.strip.w - 1, 9, "D2"), body.strip.hline(0, body.strip.w - 1, 10, "D1")
    fabric(body.bottom, "P", "twill", 20611, 1)
    for side in SIDES:
        leg = g.part(f"{side}_leg")
        strip_fabric(leg, "P", "twill", 20612 + (side == "left"), 2, 0, 5)
        fabric(leg.top, "P", "twill", 20612, 2)
        wave_band(leg.strip, 4, "S", 2)
    sandals(g)
