"""Painted Band Protector: the Hidden Leaf forehead protector on a band dyed in the clan accent, the
way Kurama shinobi wear it."""
from kit_shinobi import forehead_protector

META = {"name": "Painted Band Protector", "gender": "unisex",
        "description": "Forehead protector on an accent-dyed band, knot tails at the back."}


def build(g):
    forehead_protector(g, band="A", seed=12955)
