"""Quilted Trousers: padded trousers stitched in diamonds for cold postings, bloused into shin wraps,
with a pocket on the right thigh and open-toe sandals."""
from kit_field import blouse, cargo, trousers
from kit_shinobi import sandals, wraps

META = {"name": "Quilted Trousers", "gender": "unisex",
        "description": "Diamond-quilted padded trousers bloused into shin wraps, a thigh pocket and sandals.",
        "tags": ["shinobi"]}


def build(g):
    trousers(g, "D", 32680, texture="quilt")
    wraps(g)
    sandals(g)
    blouse(g, "D", 32683, texture="quilt")
    cargo(g, "right", 32685, y=1.4, scale=.8)
