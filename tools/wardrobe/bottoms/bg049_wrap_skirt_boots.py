"""Wrap Skirt Boots: a short wrap skirt fastened at the left hip with its edge falling on a slant,
fitted shorts beneath and tall soft boots to just below the knee."""
from kit import flaps, footwear
from paint import fabric, solid, strip_fabric

META = {"name": "Wrap Skirt Boots", "gender": "female",
        "description": "Short wrap skirt fastened at the left hip, shorts beneath, tall soft boots.",
        "tags": ["shinobi", "skirt", "wrap"]}


def build(g):
    body = g.part("body")
    strip_fabric(body, "P", "weave", 33560, 2, 9, 11)
    fabric(body.bottom, "P", "weave", 33560, 1)
    for side in ("right", "left"):
        leg = g.part(f"{side}_leg")
        strip_fabric(leg, "K", "plain", 33561, 2, 0, 1)
        fabric(leg.top, "K", "plain", 33561, 2)
    footwear(g, "boot", top=4, role="L", base=2)
    front, back = flaps(g, "waist_skirt", 5, "P", "weave", 33562, width=9, hem="P1", top=10.2, front_z=-2.9, back_z=1.9)
    # The wrapped edge: a lit fold falling from the left hip toward the right hem.
    for y in range(5):
        front.set(6 - y, y, "P3"), front.set(7 - y, y, "P1")
    knot = g.piece("waist_knot", "TORSO", (-.5, -.5, -.5), (1, 1, 1), pivot=(3.0, 10.4, -3.2))
    solid(knot, "A", "weave", 33563, 3)
