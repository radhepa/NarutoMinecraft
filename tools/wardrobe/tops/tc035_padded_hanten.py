"""Padded Hanten: the elders' winter jacket, quilted cotton padding in diamond stitching, a dark
satin collar band running round the neck and down both lapels, worn open over a striped inner
kimono and tied at the chest with two short cloth ties; square sleeves to the wrist."""
from kit_household import arm_cloth, collar_band, overlap, robe_skirt, stripes
from paint import cap, fabric, solid, strip_fabric

META = {
    "name": "Padded Hanten",
    "gender": "unisex",
    "description": "Quilted winter jacket with a dark satin collar band, open over a striped kimono, chest ties.",
    "tags": ["civilian", "jacket", "kimono"],
    "covers_waist": True,
}


def build(g):
    body, jacket = g.part("body"), g.part("jacket")
    strip_fabric(body, "D", "weave", 37180, 2)
    cap(body, "D", texture="weave", seed=37180)
    stripes(body.strip, "D3", every=3)
    overlap(body.front, "S3", "D1", rows=9)
    strip_fabric(jacket, "P", "quilt", 37181, 2)
    fabric(jacket.top, "P", "quilt", 37181, 3)
    for x in range(2, 6):
        jacket.front.vline(x, 0, 11, None)
    collar_band(jacket.front, "K2", rows=12)
    jacket.front.vline(6, 0, 11, "K3")
    jacket.back.hline(1, 6, 0, "K2")
    for i, y in enumerate((3.4, 6.4)):
        for j, x in enumerate((-1.2, .4)):
            tie = g.piece(f"tie_{i}_{j}", "TORSO", (0, 0, 0), (1, 1, 1), pivot=(x, y, -2.85))
            solid(tie, "K", "weave", 37183 + i, 2, edge=False)
    robe_skirt(g, "hem", 2, "P", "quilt", 37185, hem="P1", top=11.0)
    arm_cloth(g, "P", "quilt", 37187, rows=(0, 9), hem="P1")
    for side, bone, ox in (("right", "RIGHT_ARM", -3.0), ("left", "LEFT_ARM", -1.0)):
        cuff = g.piece(f"{side}_cuff", bone, (ox - .4, 7.0, -2.4), (5, 2, 5))
        solid(cuff, "P", "quilt", 37190 + (side == "left"), 2)
        for face in cuff.sides:
            face.hline(0, face.w - 1, 1, "K2")
