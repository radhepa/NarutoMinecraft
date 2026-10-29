"""Kitchen Trousers: the cook's pale cotton trousers, straight and loose so they stay cool by the
stove, a drawstring at the waist and wooden geta to keep the feet off the wet floor."""
from kit_market import geta
from paint import fabric, k, solid, strip_fabric

META = {"name": "Kitchen Trousers", "gender": "unisex",
        "description": "Straight pale cotton trousers with a drawstring waist, wooden geta.",
        "tags": ["civilian", "trousers", "work"]}


def build(g):
    body = g.part("body")
    strip_fabric(body, "S", "weave", 36605, 2, 9, 11)
    body.strip.hline(0, body.strip.w - 1, 9, "S3")
    fabric(body.bottom, "S", "weave", 36605, 1)
    for side in ("right", "left"):
        leg = g.part(f"{side}_leg")
        strip_fabric(leg, "S", "weave", 36606 + (side == "left"), 2, 0, 9)
        fabric(leg.top, "S", "weave", 36606, 2)
        leg.front.vline(1 if side == "right" else 2, 1, 9, "S3")
        leg.strip.hline(0, leg.strip.w - 1, 9, "S1")
    for i, x in enumerate((-.6, .6)):
        cord = g.piece(f"waist_string_{i}", "TORSO", (-.5, 0, -.5), (1, 3, 1), pivot=(x, 9.4, -2.5), rotation=(0, 0, 12 - 24 * i),
                       scale=(.5, 1, .5), motion="sway")
        solid(cord, "S", "weave", 36608 + i, 3)
    geta(g, strap=k("K", 2))
