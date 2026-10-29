"""Flower Kanzashi: a hairpin of folded-silk blossoms for festivals and visits, three flowers of
graded size pinned above the left ear, with two strings of tiny metal petals swinging below."""
from kit_household import HALF, blossom
from paint import solid

META = {"name": "Flower Kanzashi", "gender": "unisex",
        "description": "Three folded-silk blossoms pinned above the left ear with two swinging strings of metal petals."}

FACE_OUT = (0, -90, 0)


def build(g):
    blossom(g, "bloom_big", (5.4, -6.6, -1.4), FACE_OUT, petal="A3", heart="M4", size=5)
    blossom(g, "bloom_mid", (5.35, -7.6, .4), FACE_OUT, petal="S3", heart="A3", size=3)
    blossom(g, "bloom_small", (5.35, -5.6, .2), FACE_OUT, petal="A2", heart="S4", size=3)
    for i, z in enumerate((-1.8, -.9)):
        string = g.piece(f"bira_{i}", "HEAD", (-.5, 0, -.5), (1, 5, 1), pivot=(5.45, -5.4, z), scale=HALF, motion="sway")
        solid(string, "M", "smooth", 37910 + i, 3, edge=False)
        string.right.set(0, 4, "A3"), string.left.set(0, 4, "A3")
    pin = g.piece("pin", "HEAD", (-.5, -.5, 0), (1, 1, 6), pivot=(5.1, -6.6, -1.0), rotation=(-12, 0, 0), scale=HALF)
    solid(pin, "K", "smooth", 37912, 2, edge=False)
