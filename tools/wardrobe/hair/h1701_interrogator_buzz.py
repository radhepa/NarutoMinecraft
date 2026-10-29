"""Interrogator Buzz: clipped to dark stubble all over, the way the head interrogator keeps it under
his cloth cap: nothing to grab, nothing to hide behind."""
from kit_morino import clipped

META = {"name": "Interrogator Buzz", "gender": "unisex",
        "description": "Clipped to dark stubble all over, close to the scalp."}


def build(g):
    clipped(g, 17001, side_rows=3, back_rows=5)
