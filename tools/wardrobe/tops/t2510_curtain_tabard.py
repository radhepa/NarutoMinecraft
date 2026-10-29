"""Curtain Tabard: the Tobari elders' and senior jonin's formal dress, a long tabard hanging front
and back to the knee in pleats like a stage curtain, the crest on the chest, a short pleated mantle
over the shoulders and a dark long-sleeved robe beneath with moon-grey cuffs."""
from kit import flaps, sleeves
from kit_tobari import decal, mantle, pleats, plain_body
from paint import solid

META = {
    "name": "Curtain Tabard",
    "gender": "unisex",
    "description": "Knee-length pleated tabard front and back with the crest, a short shoulder mantle, a dark robe beneath.",
    "tags": ["shinobi", "robe", "jonin"],
    "covers_waist": True,
}


def build(g):
    plain_body(g, "D", "weave", 25570)
    for arm in sleeves(g, "D", "weave", 25571, rows=(0, 11)):
        arm.strip.hline(0, arm.strip.w - 1, 10, "S3"), arm.strip.hline(0, arm.strip.w - 1, 11, "S2")
    for name, z, motion in (("front", -2.75, "none"), ("back", 2.25, "none")):
        panel = g.piece(f"tabard_{name}", "TORSO", (-3, 0, 0), (6, 11, 1), pivot=(0, 0, z), inflate=.05)
        solid(panel, "P", "twill", 25573 + (name == "back"), 2)
        pleats(getattr(panel, name), "P", step=2, start=0)
    for face in flaps(g, "tabard_hem", 6, "P", "twill", 25575, width=6, top=11.0):
        pleats(face, "P", step=2, start=0)
        face.hline(0, face.w - 1, face.h - 2, "A2")
    mantle(g, "mantle", "P", "twill", 25577, length=3, tiers=1, trim=None, hood=False)
    decal(g, "chest_crest", "P2", (0, 4.0, -2.85), face="front")
    sash = g.piece("belt", "TORSO", (-4.5, 0, -2.5), (9, 1, 5), pivot=(0, 9.6, 0), inflate=.2)
    solid(sash, "K", "weave", 25579, 2, edge=False)
