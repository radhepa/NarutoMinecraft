"""Striped Sweater: an autumn pullover in a rib knit with broad horizontal stripes, a rolled
turtleneck and deep ribbed cuffs and hem: the chilly-evening sweater of students and mothers."""
from kit_household import arm_cloth, bands
from paint import cap, solid, strip_fabric

META = {
    "name": "Striped Sweater",
    "gender": "unisex",
    "description": "Rib-knit pullover in broad stripes with a rolled turtleneck and deep ribbed cuffs and hem.",
    "tags": ["civilian", "casual"],
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "P", "rib", 37280, 2)
    cap(body, "P", texture="plain", seed=37280)
    bands(body.strip, "S3", every=4, offset=2, rows=range(1, 10))
    body.strip.hline(0, body.strip.w - 1, 10, "P1")
    strip_fabric(body, "P", "rib", 37281, 2, 10, 11)
    for arm in arm_cloth(g, "P", "rib", 37282, rows=(0, 10)):
        bands(arm.strip, "S3", every=4, offset=2, rows=range(1, 9))
        strip_fabric(arm, "P", "rib", 37285, 1, 9, 10)
    neck = g.piece("turtleneck", "TORSO", (-3, 0, -2), (6, 2, 4), pivot=(0, -1.6, 0), inflate=.2)
    solid(neck, "P", "rib", 37286, 2, edge=False)
    neck.top.fill("P0")
