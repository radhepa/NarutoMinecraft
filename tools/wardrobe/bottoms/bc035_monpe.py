"""Monpe: roomy country work trousers in kasuri-flecked cotton, gathered at the waist and caught in
at the ankle so the legs balloon, worn with white tabi and zori for the garden and the rice field."""
from kit_household import kasuri, trouser_legs, waist, zori
from paint import solid

META = {"name": "Monpe", "gender": "unisex",
        "description": "Roomy kasuri-flecked work trousers gathered at waist and ankle, white tabi and zori.",
        "tags": ["civilian", "work", "trousers"]}


def build(g):
    body = waist(g, "D", "weave", 37644, band="D1")
    kasuri(body.strip, "D3", step=3, rows=range(10, 12))
    for leg in trouser_legs(g, "D", "weave", 37645, rows=(0, 9)):
        kasuri(leg.strip, "D3", step=3, seed=1, rows=range(0, 10))
    zori(g, strap="D1")
    for side, bone in (("right", "RIGHT_LEG"), ("left", "LEFT_LEG")):
        puff = g.piece(f"{side}_balloon", bone, (-2.5, 1.0, -2.5), (5, 7, 5), inflate=.18)
        solid(puff, "D", "weave", 37647 + (side == "left"), 2)
        for face in puff.sides:
            kasuri(face, "D3", step=3, seed=2)
            face.hline(0, face.w - 1, 6, "D1")
        cuff = g.piece(f"{side}_ankle", bone, (-2.5, 8.2, -2.5), (5, 1, 5))
        solid(cuff, "D", "weave", 37650, 1, edge=False)
