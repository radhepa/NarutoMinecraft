"""Monkey Shorts: Konohamaru's Academy shorts. Loose grey shorts to the knee with a drawstring
waist, sticking plasters on one knee and navy open-toe sandals."""
from kit_shinobi import sandals
from paint import fabric, solid, strip_fabric

META = {"name": "Monkey Shorts", "gender": "unisex",
        "description": "Loose grey knee shorts with a drawstring, a plaster on the knee, navy sandals.",
        "tags": ["shinobi", "genin"]}


def build(g):
    body = g.part("body")
    strip_fabric(body, "S", "twill", 9610, 2, 9, 11)
    body.strip.hline(0, body.strip.w - 1, 9, "S3")
    fabric(body.bottom, "S", "twill", 9610, 1)
    for side in ("right", "left"):
        leg = g.part(f"{side}_leg")
        strip_fabric(leg, "S", "twill", 9611 + (side == "left"), 2, 0, 4)
        fabric(leg.top, "S", "twill", 9611, 2)
        leg.front.vline(1 if side == "right" else 2, 1, 4, "S1")
    for side, bone in (("right", "RIGHT_LEG"), ("left", "LEFT_LEG")):
        hem = g.piece(f"{side}_hem", bone, (-2.5, 3.8, -2.5), (5, 2, 5), inflate=.05)
        solid(hem, "S", "twill", 9613, 2)
        for face in hem.sides:
            face.hline(0, face.w - 1, 0, "S1"), face.hline(0, face.w - 1, 1, "S3")
    # A crossed plaster on the left knee.
    knee = g.part("left_leg").front
    knee.set(1, 6, "S4"), knee.set(2, 6, "S4"), knee.set(1, 7, "S3")
    sandals(g)
    for i, x in enumerate((-.6, .6)):
        cord = g.piece(f"waist_cord_{i}", "TORSO", (-.5, 0, -.5), (1, 2, 1), pivot=(x, 9.6, -2.55),
                       rotation=(0, 0, 10 if i else -10), motion="sway")
        solid(cord, "S", "weave", 9614 + i, 1)
