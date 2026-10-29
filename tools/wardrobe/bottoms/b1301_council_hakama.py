"""Council Hakama: wide charcoal hakama to the ankle, pressed in pleats, the waist cords tied in
front, the hems flaring over the feet into open-toe sandals: the dress of Danzo and the council."""
from kit_shinobi import sandals
from paint import fabric, k, solid, strip_fabric

META = {"name": "Council Hakama", "gender": "unisex",
        "description": "Wide pleated charcoal hakama to the ankle, tied waist cords, flaring hems, sandals.",
        "tags": ["shinobi"]}


def build(g):
    body = g.part("body")
    strip_fabric(body, "D", "twill", 13800, 2, 9, 11)
    body.strip.hline(0, body.strip.w - 1, 9, "D3")
    fabric(body.bottom, "D", "twill", 13800, 1)
    for side in ("right", "left"):
        leg, pants = g.part(f"{side}_leg"), g.part(f"{side}_pants")
        strip_fabric(leg, "D", "twill", 13801 + (side == "left"), 2, 0, 9)
        fabric(leg.top, "D", "twill", 13801, 2)
        strip_fabric(pants, "D", "twill", 13803 + (side == "left"), 2, 0, 8)
        fabric(pants.top, "D", "twill", 13803, 2)
        for x in range(0, pants.strip.w, 2):
            pants.strip.vline(x, 1, 8, "D1")
    sandals(g)
    for side, bone in (("right", "RIGHT_LEG"), ("left", "LEFT_LEG")):
        hem = g.piece(f"{side}_hem", bone, (-2.5, 8.4, -2.5), (5, 1, 5), inflate=.25)
        solid(hem, "D", "twill", 13805, 2, edge=False)
        for face in hem.sides:
            for x in range(0, face.w, 2):
                face.set(x, 0, "D1")
    knot = g.piece("waist_cord_knot", "TORSO", (-1, 0, 0), (2, 1, 1), pivot=(0, 9.6, -2.75))
    solid(knot, "D", "twill", 13806, 3, edge=False)
    for i, x in enumerate((-.5, .5)):
        end = g.piece(f"waist_cord_{i}", "TORSO", (-.5, 0, 0), (1, 3, 1), pivot=(x, 10.4, -2.8), motion="sway")
        solid(end, "D", "twill", 13807 + i, 3)
        end.front.set(0, 2, k("D", 1))
