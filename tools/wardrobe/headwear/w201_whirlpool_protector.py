"""Whirlpool Protector: the Hidden Leaf forehead protector on a red cloth band, the colour of the
Uzumaki crest, its tails knotted at the back."""
from kit_shinobi import forehead_protector

META = {"name": "Whirlpool Protector", "gender": "unisex",
        "description": "Leaf forehead protector on a red band, the colour of the Uzumaki crest."}


def build(g):
    forehead_protector(g, band="A", seed=2600)
