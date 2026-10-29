"""Knee-Guard Trousers: field trousers with padded, steel-faced guards strapped over the knees, the
legs bloused low into short shin wraps above open-toe sandals."""
from kit_field import blouse, knee_guards, trousers
from kit_shinobi import sandals, wraps

META = {"name": "Knee-Guard Trousers", "gender": "unisex",
        "description": "Trousers with steel-faced knee guards, bloused low into short shin wraps, sandals.",
        "tags": ["shinobi"]}


def build(g):
    trousers(g, "D", 32480, length=7)
    wraps(g, 8, 9)
    sandals(g)
    blouse(g, "D", 32483, y=6.8)
    knee_guards(g, 32485, y=3.4)
