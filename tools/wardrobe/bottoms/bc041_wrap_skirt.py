"""Wrap Skirt: a mid-calf skirt wrapped round and tied at the hip, the overlap edge falling down
the front in a contrasting binding, over plain thong sandals."""
from kit_household import skirt, trouser_legs, waist, zori
from paint import solid

META = {"name": "Wrap Skirt", "gender": "female",
        "description": "Mid-calf wrap skirt tied at the hip, contrasting binding down the overlap, sandals.",
        "tags": ["civilian", "skirt", "wrap"]}


def build(g):
    waist(g, "D", "weave", 37740, band="D3")
    trouser_legs(g, "D", "weave", 37741, rows=(0, 5), base=1)
    zori(g, sock="K2", strap="L2", sole="L3")
    for face in skirt(g, "skirt", 9, "D", "weave", 37743, hem="S3"):
        if face.name == "front":
            face.vline(6, 1, 8, "S3")
    for i, rz in enumerate((8, -10)):
        tie = g.piece(f"waist_tie_{i}", "TORSO", (-.5, 0, -.5), (1, 4 - i, 1), pivot=(2.8 + .6 * i, 10.6, -2.9),
                      rotation=(0, 0, rz), motion="sway")
        solid(tie, "S", "weave", 37745 + i, 3)
