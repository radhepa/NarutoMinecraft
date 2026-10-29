"""Jinbei Top: the summer house jacket of fathers and children, light crepe in a narrow stripe,
crossed over the chest and tied with two small cloth ties at the side instead of an obi, short
sleeves joined to the body with open lattice stitching, and a broad collar band."""
from kit_household import arm_cloth, overlap, stripes
from paint import cap, solid, strip_fabric

META = {
    "name": "Jinbei Top",
    "gender": "unisex",
    "description": "Striped summer crepe jacket crossed and tied at the side, short sleeves with lattice stitching.",
    "tags": ["civilian", "casual", "wrap"],
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "P", "plain", 37080, 2)
    cap(body, "P", seed=37080)
    stripes(body.strip, "P3", every=3)
    overlap(body.front, "P0", None, rows=12)
    body.strip.hline(0, body.strip.w - 1, 11, "P1")
    for arm in arm_cloth(g, "P", "plain", 37081, rows=(0, 4), hem="P1"):
        stripes(arm.strip, "P3", every=3, rows=range(0, 4))
        for x in range(0, arm.strip.w, 2):
            arm.strip.set(x, 0, "S3")
    for i, y in enumerate((4.2, 7.6)):
        tie = g.piece(f"tie_{i}", "TORSO", (-.5, 0, -.5), (1, 2, 1), pivot=(-2.6, y, -2.75), rotation=(0, 0, 12),
                      motion="sway")
        solid(tie, "P", "plain", 37084 + i, 1)
