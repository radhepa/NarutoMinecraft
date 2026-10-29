"""Heko-obi Kimono: a child's summer kimono in dotted cotton, short sleeves, tied with a soft gauzy
heko obi wound twice and knotted at the back in a big fluffy bow with long trailing ends."""
from kit_household import dots, overlap, sash, wide_sleeves
from paint import cap, strip_fabric

META = {
    "name": "Heko-obi Kimono",
    "gender": "unisex",
    "description": "Child's dotted summer kimono with short sleeves and a soft heko obi in a big fluffy bow.",
    "tags": ["civilian", "kimono", "wrap"],
    "tucked": True,
}


def spots(face, rows=None):
    dots(face, "S4", step=4, seed=1, rows=rows)


def build(g):
    body = g.part("body")
    strip_fabric(body, "P", "plain", 37460, 2)
    cap(body, "P", seed=37460)
    spots(body.strip)
    overlap(body.front, "P0", "P1", rows=8, under="S4")
    wide_sleeves(g, "sleeve", "P", "plain", 37461, top=1.4, length=5, pattern=spots, arm_rows=3)
    sash(g, "heko_obi", "A", y=7.2, height=3, knot="bow", seed=37466, base=3)
