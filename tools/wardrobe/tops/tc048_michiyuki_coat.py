"""Michiyuki Coat: the winter coat worn over a kimono to go out, velvet to the knee, its square
neckline framed by a stitched panel so the kimono collar shows, closed with cloth-covered buttons,
with broad sleeves to the wrist."""
from kit_household import robe_skirt, wide_sleeves
from paint import cap, strip_fabric

META = {
    "name": "Michiyuki Coat",
    "gender": "unisex",
    "description": "Knee-length velvet coat with a framed square neckline over the kimono collar, covered buttons.",
    "tags": ["civilian", "coat", "kimono"],
    "covers_waist": True,
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "P", "velvet", 37440, 2)
    cap(body, "P", texture="velvet", seed=37440)
    f = body.front
    f.rect(2, 0, 4, 3, "P3")
    f.rect(3, 0, 2, 2, "S3"), f.set(3, 0, "A2"), f.set(4, 1, "D2")
    f.hline(1, 6, 3, "P1"), f.vline(1, 0, 3, "P1"), f.vline(6, 0, 3, "P1")
    f.vline(4, 4, 11, "P1")
    for y in (5, 8):
        f.set(3, y, "P4")
    robe_skirt(g, "coat", 7, "P", "velvet", 37441, hem="P1", overlap_key="P1")
    wide_sleeves(g, "sleeve", "P", "velvet", 37443, top=2.0, length=8, hem="P1", arm_rows=9)
