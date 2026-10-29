"""Wave Hachimaki: a pale cloth headband for the sword hall, printed round with an accent wave,
knotted on the left side of the head with two short ends."""
from kit_namiashi import wave_band
from paint import solid

META = {"name": "Wave Hachimaki", "gender": "unisex",
        "description": "Pale headband printed with an accent wave, knotted at the left side, two short ends."}


def build(g):
    band = g.piece("band", "HEAD", (-4, -7.8, -4), (8, 2, 8), inflate=.7)
    solid(band, "S", "weave", 20811, 3, edge=False)
    for face in band.sides:
        wave_band(face, 0, "A", 2, ground="S3")
    knot = g.piece("knot", "HEAD", (0, -1, -1), (1, 2, 2), pivot=(4.7, -6.9, 1.6))
    solid(knot, "S", "weave", 20812, 2)
    for i, (z, rx) in enumerate(((1.2, 18), (2.1, 34))):
        end = g.piece(f"end_{i}", "HEAD", (0, 0, -.5), (1, 4, 1), pivot=(4.9, -6.6, z), rotation=(rx, 0, -12), motion="sway")
        solid(end, "S", "weave", 20813 + i, 2)
        end.left.set(0, 3, "A2")
