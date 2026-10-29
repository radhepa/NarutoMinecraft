"""Bandana and Senbon: the backward bandana with a senbon held idly in the corner of the mouth, the
full off-hand look of the Hokage's bodyguard on a quiet watch."""
from kit_shiranui import backward_bandana, mouth_senbon

META = {"name": "Bandana and Senbon", "gender": "unisex", "hides_hair": ["crown", "fringe"], "covers_mouth": True,
        "description": "The backward bandana protector, a senbon held in the corner of the mouth."}


def build(g):
    backward_bandana(g, "D", seed=16894)
    mouth_senbon(g)
