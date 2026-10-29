"""Blossom Blouse: a young mother's spring blouse, light cotton strewn with small blossoms, puffed
short sleeves, a rounded white collar and a little ribbon bow at the throat."""
from kit_household import arm_cloth, sprigs
from paint import cap, solid, strip_fabric

META = {
    "name": "Blossom Blouse",
    "gender": "female",
    "description": "Blossom-print cotton blouse with puffed short sleeves, a rounded white collar and a ribbon bow.",
    "tags": ["civilian", "casual"],
}


def blossoms(face, rows=None):
    sprigs(face, "A3", "S4", step=4, seed=1, rows=rows)


def build(g):
    body = g.part("body")
    strip_fabric(body, "P", "plain", 37320, 3)
    cap(body, "P", seed=37320, base=3)
    blossoms(body.strip, rows=range(2, 12))
    body.strip.hline(0, body.strip.w - 1, 11, "P2")
    for arm in arm_cloth(g, "P", "plain", 37321, rows=(0, 3), base=3, hem="P2"):
        blossoms(arm.strip, rows=range(0, 3))
    for side, bone, ox in (("right", "RIGHT_ARM", -3.0), ("left", "LEFT_ARM", -1.0)):
        puff = g.piece(f"{side}_puff", bone, (ox - .5, -2.2, -2.5), (5, 3, 5), inflate=.1)
        solid(puff, "P", "plain", 37324 + (side == "left"), 3)
        for face in puff.sides:
            blossoms(face)
            for x in range(0, face.w, 2):
                face.set(x, 2, "P2")
    for side, x in (("right", -1.6), ("left", 1.6)):
        collar = g.piece(f"collar_{side}", "TORSO", (-1.5, 0, 0), (3, 2, 1), pivot=(x, -.3, -2.6))
        solid(collar, "S", "plain", 37327 + (side == "left"), 4, edge=False)
        collar.front.set(0 if side == "left" else 2, 1, "S2")
    bow = g.piece("bow", "TORSO", (-1.5, 0, 0), (3, 1, 1), pivot=(0, 1.2, -2.8))
    solid(bow, "A", "plain", 37330, 2, edge=False)
    bow.front.set(1, 0, "A1")
