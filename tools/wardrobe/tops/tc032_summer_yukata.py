"""Summer Yukata: a full men's-style yukata to the ankle, indigo-dyed cotton in a broad well-curb
check, short wide sleeves and a stiff narrow kaku obi knotted low at the back. One garment with its
skirt, the Summer Yukata Hem."""
from kit_household import checks, overlap, sash, wide_sleeves
from paint import cap, strip_fabric

META = {
    "name": "Summer Yukata",
    "gender": "unisex",
    "description": "Full ankle-length yukata in a broad check, short wide sleeves, a narrow kaku obi low at the back.",
    "tags": ["civilian", "kimono", "wrap"],
    "covers_waist": True,
    "locked_to": "bc029_summer_yukata_hem",
}


def igeta(face, rows=None):
    checks(face, "S3", every=4, offset=1, cross="S4", rows=rows)


def build(g):
    body = g.part("body")
    strip_fabric(body, "P", "plain", 37120, 1)
    cap(body, "P", seed=37120, base=1)
    igeta(body.strip)
    overlap(body.front, "P0", "P0", rows=12, under="S4")
    wide_sleeves(g, "sleeve", "P", "plain", 37121, top=2.2, length=6, base=1, pattern=igeta, arm_rows=8)
    sash(g, "obi", "K", y=8.8, height=2, knot="back", seed=37126, stripe="L2")
