"""Mouth Senbon: a single steel senbon held in the teeth like a toothpick, tilted down and out,
the family habit that keeps a weapon ready without anyone noticing."""
from kit_shiranui import mouth_senbon

META = {"name": "Mouth Senbon", "gender": "unisex", "covers_mouth": True,
        "description": "A single senbon held in the corner of the mouth like a toothpick."}


def build(g):
    mouth_senbon(g)
