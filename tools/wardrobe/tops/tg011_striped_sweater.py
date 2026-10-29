"""Striped Sweater: a chunky knit sweater banded in broad stripes, the sleeves shoved up past the elbow
in a thick roll, with ribbed collar and hem: the Academy kid in a hand-me-down."""
from kit_academy import ribbed, sleeve_roll, stripes
from paint import cap, fabric, strip_fabric

META = {
    "name": "Striped Sweater",
    "gender": "unisex",
    "description": "Chunky knit sweater in broad stripes, sleeves shoved past the elbow, ribbed collar and hem.",
    "tags": ["shinobi", "genin"],
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "P", "knit", 31150, 2)
    cap(body, "P", texture="knit", seed=31150)
    stripes(body, (3, 4, 7, 8), "S2")
    ribbed(body, (10, 11), "P")
    body.front.hline(2, 5, 0, "S3"), body.front.hline(3, 4, 1, "S3"), body.back.hline(2, 5, 0, "S3")
    for side in ("right", "left"):
        arm = g.part(f"{side}_arm")
        strip_fabric(arm, "P", "knit", 31151 + (side == "left"), 2, 0, 5)
        fabric(arm.top, "P", "knit", 31151, 3)
        stripes(arm, (3, 4), "S2")
    sleeve_roll(g, "P", 3.6, 31153)
