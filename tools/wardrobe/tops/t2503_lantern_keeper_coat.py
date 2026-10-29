"""Lantern Keeper Coat: the coat of the families who keep the village's night lanterns lit, knee
length and closed across the chest, a standing collar, moon-grey cuffs, a wide dark sash with the
amber lantern hanging at the front and the night-curtain crest small between the shoulders."""
from kit import collar, flaps, sleeves
from kit_tobari import decal, lantern, sash
from paint import cap, strip_fabric

META = {
    "name": "Lantern Keeper Coat",
    "gender": "unisex",
    "description": "Knee-length closed coat, standing collar, moon-grey cuffs, a wide sash with a paper lantern, the crest.",
    "tags": ["shinobi", "robe"],
    "covers_waist": True,
}


def build(g):
    for layer, seed in (("body", 25360), ("jacket", 25361)):
        box = g.part(layer)
        strip_fabric(box, "P", "twill", seed, 2)
        cap(box, "P", texture="twill", seed=seed)
    jacket = g.part("jacket")
    for y in range(0, 12):
        jacket.front.set(2 + min(y, 5) // 3, y, "P0")
    jacket.front.vline(5, 0, 11, "P3")
    for arm in sleeves(g, "P", "twill", 25362, rows=(0, 11), layer="arm"):
        arm.strip.hline(0, arm.strip.w - 1, 10, "S3"), arm.strip.hline(0, arm.strip.w - 1, 11, "S2")
    col = collar(g, "collar", "P", "twill", height=2, y=-1.4)
    col.front.vline(4, 0, 1, "P0")
    decal(g, "back_crest", "P2", (0, 1.4, 2.35))
    for face in flaps(g, "skirt", 9, "P", "twill", 25364, slit=True):
        face.hline(0, face.w - 1, 8, "P0")
    sash(g, "sash", "D", y=8.6, height=3, knot="right")
    lantern(g, "lantern", pivot=(1.6, 10.8, -3.0))
