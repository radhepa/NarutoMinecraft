"""Medic Trousers: slim leaf-green trousers bound from knee to ankle in white wraps so nothing
catches in the brambles, a white sash at the waist and open-toe sandals."""
from kit import belt, legs
from kit_shinobi import sandals, wraps
from paint import fabric, strip_fabric

META = {"name": "Medic Trousers", "gender": "unisex",
        "description": "Slim green trousers wrapped white from knee to ankle, white sash, sandals.",
        "tags": ["shinobi"]}


def build(g):
    body = g.part("body")
    strip_fabric(body, "D", "twill", 24701, 2, 9, 11)
    fabric(body.bottom, "D", "twill", 24701, 1)
    legs(g, "D", "twill", 24702, 2, rows=(0, 6))
    wraps(g, 6, 9)
    belt(g, "waist_sash", y=9.0, role="S", height=1, buckle=None, inflate=.15)
    sandals(g)
