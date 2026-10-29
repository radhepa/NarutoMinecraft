"""Maekake Trousers: the shop counter's wear, easy brown trousers tied at the ankle over sandals,
with a merchant's maekake apron in the accent colour tied over the front, the white circle of the
Haruno shop printed on it."""
from kit import belt, leg_ring, legs
from kit_haruno import chest_crest
from kit_shinobi import sandals
from paint import fabric, k, solid, strip_fabric

META = {"name": "Maekake Trousers", "gender": "unisex",
        "description": "Easy brown trousers tied at the ankle, a merchant's front apron with the circle crest, sandals.",
        "tags": ["shinobi"]}


def build(g):
    body = g.part("body")
    strip_fabric(body, "L", "weave", 19730, 2, 9, 11)
    fabric(body.bottom, "L", "weave", 19730, 1)
    legs(g, "L", "weave", 19731, 2, rows=(0, 9))
    for ring in leg_ring(g, "ankle_tie", 8.6, "S", 3, (5, 1, 5), "weave", inflate=.1):
        for face in ring.sides:
            face.set(2, 0, k("S", 1))
    sandals(g)
    belt(g, "waist_cord", y=9.0, role="S", height=1, buckle=None, inflate=.25)
    apron = g.piece("waist_apron", "TORSO", (-4, 0, 0), (8, 9, 1), pivot=(0, 9.8, -2.95), motion="flap_front")
    solid(apron, "A", "weave", 19732, 2)
    apron.front.hline(0, 7, 0, k("A", 3))
    apron.front.hline(0, 7, 8, k("A", 1))
    chest_crest(g, "waist_apron_crest", 0, y=11.4, z=-3.15, role="A", seed=19733)
