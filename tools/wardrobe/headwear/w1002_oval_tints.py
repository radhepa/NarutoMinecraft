"""Oval Tints: wider, flatter tinted glasses in a brown frame, lighter than the clan's black
shades: the eyes are only half hidden behind them."""
from kit_aburame import lenses

META = {"name": "Oval Tints", "gender": "unisex", "covers_face": True,
        "description": "Wide oval glasses with tinted lenses in a brown frame."}


def build(g):
    lenses(g, "D", "L", "oval", y=-3.1)
