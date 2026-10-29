"""Field Leggings: fitted dark leggings with a beige wrap of cloth tied round the hips and knotted at
the side, rose ties under the knee and tall black shinobi boots."""
from kit import footwear, legs, leg_ring
from paint import fabric, k, solid, strip_fabric

META = {"name": "Field Leggings", "gender": "unisex",
        "description": "Fitted dark leggings, a beige hip wrap knotted at the side, rose knee ties, tall black boots.",
        "tags": ["shinobi"]}


def build(g):
    body = g.part("body")
    strip_fabric(body, "S", "weave", 19760, 2, 9, 11)
    fabric(body.bottom, "S", "weave", 19760, 1)
    body.strip.hline(0, body.strip.w - 1, 9, k("S", 3))
    legs(g, "K", "smooth", 19761, 3, rows=(0, 9), crease=False)
    for side in ("right", "left"):
        leg = g.part(f"{side}_leg")
        strip_fabric(leg, "S", "weave", 19762, 2, 0, 1)
    footwear(g, "boot", top=6, role="K", base=2, sole="K0")
    for ring in leg_ring(g, "knee_tie", 5.2, "A", 2, (5, 1, 5), "weave", inflate=.3):
        ring.front.set(1, 0, k("A", 4))
    knot = g.piece("waist_knot", "TORSO", (-1, 0, -1), (2, 2, 2), pivot=(4.2, 10.0, -.5))
    solid(knot, "S", "weave", 19763, 3)
    end = g.piece("waist_end", "TORSO", (-.5, 0, -.5), (1, 4, 1), pivot=(4.4, 11.4, -.8), motion="sway")
    solid(end, "S", "weave", 19764, 2)
