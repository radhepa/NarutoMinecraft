"""Sealer Hachimaki: a white cloth headband tied round the brow with the red whirlpool on the front,
a paper seal tag tucked under it at one temple and long tails hanging from the knot."""
from kit_uzumaki import crest_patch
from paint import solid

META = {"name": "Sealer Hachimaki", "gender": "unisex",
        "description": "White headband with the red whirlpool on the brow, a seal tag at the temple, long tails."}


def build(g):
    band = g.piece("band", "HEAD", (-4, -7.6, -4), (8, 1, 8), inflate=.62)
    solid(band, "S", "weave", 2610, 3, edge=False)
    crest_patch(g, "crest", "HEAD", (0, -8.6, -4.75), size=6, ground="S3", ink="A2", outward="front")
    tag = g.piece("tag", "HEAD", (0, 0, -.5), (1, 3, 1), pivot=(-4.75, -8.1, -2.2), rotation=(0, 0, 8))
    solid(tag, "S", "plain", 2611, 4, edge=False)
    tag.right.set(0, 1, "K1"), tag.right.set(0, 2, "A2")
    knot = g.piece("knot", "HEAD", (-1, -1, 0), (2, 2, 1), pivot=(0, -7.1, 4.65))
    solid(knot, "S", "weave", 2612, 3)
    for i, (x, rz) in enumerate(((-.6, 16), (.6, -12))):
        tail = g.piece(f"tail_{i}", "HEAD", (-.5, 0, 0), (1, 7, 1), pivot=(x, -6.4, 4.95), rotation=(18, 0, rz),
                       motion="sway")
        solid(tail, "S", "weave", 2613 + i, 3)
        tail.back.set(0, 6, "A2")
