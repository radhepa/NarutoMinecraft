"""Summer Yukata Hem: the skirt of the Summer Yukata, straight to the ankle in the same broad check
with the overlap running down the front, over bare feet in wooden geta."""
from kit_household import checks, geta, skirt, trouser_legs, waist

META = {"name": "Summer Yukata Hem", "gender": "unisex",
        "description": "The yukata's checked skirt falling straight to the ankle, wooden geta.",
        "tags": ["civilian", "kimono"], "locked_to": "tc032_summer_yukata"}


def igeta(face, rows=None):
    checks(face, "S3", every=4, offset=1, cross="S4", rows=rows)


def build(g):
    body = waist(g, "P", "plain", 37548, base=1)
    igeta(body.strip, rows=range(9, 12))
    for leg in trouser_legs(g, "P", "plain", 37549, rows=(0, 9), base=1):
        igeta(leg.strip, rows=range(0, 10))
    geta(g, strap="K1")
    for face in skirt(g, "yukata", 11, "P", "plain", 37551, hem="P0", base=1, pattern=igeta):
        if face.name == "front":
            face.vline(3, 1, 10, "P0")
