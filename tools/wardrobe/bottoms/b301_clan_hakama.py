"""Clan Hakama: wide pleated dark trousers flaring to the ankle, the waist ties knotted at the front
and white tabi under navy sandals."""
from kit_shinobi import sandals
from paint import fabric, solid, strip_fabric

META = {"name": "Clan Hakama", "gender": "unisex",
        "description": "Wide pleated dark hakama flaring to the ankle, front waist ties, navy sandals.", "tags": ["shinobi"]}


def build(g):
    body = g.part("body")
    strip_fabric(body, "K", "weave", 3950, 2, 9, 11)
    body.strip.hline(0, body.strip.w - 1, 9, "K3")
    fabric(body.bottom, "K", "weave", 3950, 1)
    for side in ("right", "left"):
        leg = g.part(f"{side}_leg")
        strip_fabric(leg, "K", "weave", 3951 + (side == "left"), 2, 0, 9)
        fabric(leg.top, "K", "weave", 3951, 2)
        for x in range(0, leg.strip.w, 2):
            leg.strip.vline(x, 1, 9, "K1")
    sandals(g)
    # The flared lower legs, pleated, swinging with each leg.
    for side, bone in (("right", "RIGHT_LEG"), ("left", "LEFT_LEG")):
        flare = g.piece(f"{side}_flare", bone, (-2.5, 4.0, -2.5), (5, 6, 5), inflate=.15)
        solid(flare, "K", "weave", 3953 + (side == "left"), 2)
        for face in flare.sides:
            for x in range(1, face.w, 2):
                face.vline(x, 0, 5, "K1")
            face.hline(0, face.w - 1, 5, "K3")
    knot = g.piece("waist_tie", "TORSO", (-1, 0, 0), (2, 1, 1), pivot=(0, 9.4, -2.8))
    solid(knot, "S", "weave", 3955, 3)
    for i, (x, rz) in enumerate(((-.6, 8), (.6, -8))):
        end = g.piece(f"waist_tie_end_{i}", "TORSO", (-.5, 0, -.5), (1, 3, 1), pivot=(x, 10.4, -2.8), rotation=(0, 0, rz),
                      motion="sway")
        solid(end, "S", "weave", 3956 + i, 3)
