"""Bolero Tunic: a short-sleeved bolero ending under the bust, worn over a long sleeveless tunic
that falls to the hip with side vents, belted low with a pouch on the right."""
from kit import belt, pouch, sleeves
from paint import cap, strip_fabric

META = {
    "name": "Bolero Tunic",
    "gender": "unisex",
    "description": "Short-sleeved bolero over a hip-length vented tunic, a low belt with a pouch.",
    "tags": ["shinobi", "genin", "tunic"],
}


def build(g):
    body, jacket = g.part("body"), g.part("jacket")
    strip_fabric(body, "S", "weave", 33200, 2)
    cap(body, "S", texture="weave", seed=33200)
    for face in (body.right, body.left):
        face.vline(1, 9, 11, "S0")
    body.front.hline(2, 5, 0, "S1")
    strip_fabric(jacket, "P", "plain", 33201, 2, 0, 4)
    jacket.top.fill("P3")
    for y in range(5):
        jacket.front.clear(3, y), jacket.front.clear(4, y)
    jacket.front.vline(2, 0, 4, "A2"), jacket.front.vline(5, 0, 4, "A2")
    jacket.strip.hline(0, jacket.strip.w - 1, 4, "P1")
    sleeves(g, "P", "plain", 33202, rows=(0, 3), layer="sleeve", cuff="A2")
    belt(g, "belt", y=9.8, role="L", height=1, buckle="M")
    pouch(g, "pouch", (-3.0, 10.2, -2.6), size=(2, 2, 1), role="L", flap="L3")
