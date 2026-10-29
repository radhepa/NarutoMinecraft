"""Haori over Kimono: the head of the household's going-out dress. A dark striped kimono under a
hip-length haori jacket worn open, its lapels a band of the jacket cloth, tied across the chest with
a pale braided cord ending in two tassels, and broad haori sleeves to the wrist."""
from kit_household import collar_band, overlap, robe_skirt, stripes, wide_sleeves
from paint import cap, fabric, solid, strip_fabric

META = {
    "name": "Haori over Kimono",
    "gender": "unisex",
    "description": "Striped dark kimono under an open hip-length haori with a tasselled cord and broad sleeves.",
    "tags": ["civilian", "kimono", "haori", "wrap"],
    "covers_waist": True,
}


def build(g):
    body, jacket = g.part("body"), g.part("jacket")
    # The kimono beneath: dark cloth with a fine stripe, showing between the open lapels.
    strip_fabric(body, "D", "weave", 37020, 2)
    cap(body, "D", texture="weave", seed=37020)
    stripes(body.strip, "D1", every=2)
    overlap(body.front, "S3", "D0", rows=8)
    # The haori: the jacket overlay all round, open down the front between two lapel bands.
    strip_fabric(jacket, "P", "twill", 37021, 2)
    fabric(jacket.top, "P", "twill", 37021, 3)
    for x in range(2, 6):
        jacket.front.vline(x, 0, 11, None)
    collar_band(jacket.front, "P1", rows=12)
    jacket.front.vline(1, 0, 11, "P3"), jacket.front.vline(6, 0, 11, "P1")
    jacket.back.vline(3, 0, 11, "P1")
    # The cord tied across the chest, with its two tassels.
    knot = g.piece("cord_knot", "TORSO", (-1, 0, 0), (2, 1, 1), pivot=(0, 5.0, -2.75))
    solid(knot, "S", "weave", 37022, 3, edge=False)
    for i, x in enumerate((-.9, .4)):
        tassel = g.piece(f"cord_tassel_{i}", "TORSO", (0, 0, 0), (1, 2, 1), pivot=(x, 5.8, -2.85), motion="sway")
        solid(tassel, "S", "weave", 37023 + i, 3)
    robe_skirt(g, "haori", 3, "P", "twill", 37025, hem="P1", top=10.8)
    wide_sleeves(g, "sleeve", "P", "twill", 37027, top=2.4, length=8, hem="P1", arm_rows=9)
