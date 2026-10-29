"""Lantern Festival Skirt: a long kimono-style skirt for the summer festival, plain above and
dyed near the hem with a band of overlapping waves, over bare feet in red-thonged geta."""
from kit_household import geta, skirt, trouser_legs, waist

META = {"name": "Lantern Festival Skirt", "gender": "unisex",
        "description": "Long kimono-style skirt with a band of overlapping waves near the hem, red-thonged geta.",
        "tags": ["civilian", "kimono", "skirt"]}

WAVE = [".##.", "#..#", "...."]


def waves(face, rows=None):
    for y in range(7, 10):
        for x in range(face.w):
            if WAVE[(y - 7) % 3][(x + face.x0) % 4] == "#":
                face.set(x, y, "S3")


def build(g):
    waist(g, "P", "plain", 37884)
    trouser_legs(g, "P", "plain", 37885, rows=(0, 9), base=1)
    geta(g, strap="A2")
    for face in skirt(g, "skirt", 11, "P", "plain", 37887, hem="D2"):
        waves(face)
        if face.name == "front":
            face.vline(3, 1, 6, "P1")
