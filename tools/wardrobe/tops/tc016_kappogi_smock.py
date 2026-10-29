"""Kappogi Smock: the cook's and stallholder's white over-smock that covers a kimono whole, long
sleeves gathered at the wrist, a round collar tied at the back, two front pockets and a skirt to
the hip."""
from kit import flaps
from kit_market import pocket, sleeves
from paint import cap, k, solid, strip_fabric

META = {
    "name": "Kappogi Smock",
    "gender": "unisex",
    "description": "White over-smock with long sleeves gathered at the wrist, round collar, two pockets, skirt to the hip.",
    "tags": ["civilian", "apron", "work"],
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "S", "weave", 36320, 3)
    cap(body, "S", seed=36320, base=3)
    body.front.hline(2, 5, 0, k("P", 2)), body.front.hline(3, 4, 1, k("P", 1))
    body.front.hline(1, 6, 1, "S4"), body.front.set(2, 1, k("P", 2)), body.front.set(5, 1, k("P", 2))
    sleeves(g, "S", "weave", 36321, rows=(0, 9), base=3)
    for side in ("right", "left"):
        cuff = g.piece(f"{side}_gathered_cuff", "RIGHT_ARM" if side == "right" else "LEFT_ARM",
                       (-3.5 if side == "right" else -1.5, 7.2, -2.5), (5, 1, 5), inflate=.08)
        solid(cuff, "S", "rib", 36323 + (side == "left"), 2, edge=False)
        for face in cuff.sides:
            face.paint(lambda x, y, cur: "S2" if x % 2 else "S3")
    for i, x in enumerate((-2.0, 2.0)):
        pocket(g, f"pocket_{i}", "S", (x, 9.4, -2.95), size=(3, 2), seed=36325 + i, base=3)
    for face in flaps(g, "smock_hem", 3, "S", "weave", 36327, width=9, top=11.0, front_z=-3.0, back_z=2.0, base=3):
        face.hline(0, 8, 2, "S2")
    knot = g.piece("collar_tie", "TORSO", (-1, 0, 0), (2, 2, 1), pivot=(0, .2, 2.3))
    solid(knot, "S", "weave", 36329, 3)
