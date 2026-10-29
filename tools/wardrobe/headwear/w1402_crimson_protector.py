"""Crimson Protector: the Konoha forehead protector on a crimson band, the colour of the Yuhi
eyes, tied at the back with two swaying tails."""
from kit_shinobi import forehead_protector

META = {"name": "Crimson Protector", "gender": "unisex",
        "description": "Forehead protector on a crimson band, the steel plate engraved with the leaf."}


def build(g):
    forehead_protector(g, band="A", seed=14970)
