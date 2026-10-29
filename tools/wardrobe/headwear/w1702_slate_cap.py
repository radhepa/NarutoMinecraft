"""Slate Cap: the protector cap in dark slate cloth, the plate on the brow and the long ends of the
knot hanging to the shoulders."""
from kit_morino import head_cloth

META = {"name": "Slate Cap", "gender": "unisex", "hides_hair": ["*"],
        "description": "Dark slate cloth tied over the whole head with the protector plate, long knot ends."}


def build(g):
    head_cloth(g, "D", 17511, plate=True, tails=6, hem="K1")
