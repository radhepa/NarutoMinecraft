"""Tide Protector: the leaf forehead protector on a sea-blue band, its knot tails left long."""
from kit_shinobi import forehead_protector

META = {"name": "Tide Protector", "gender": "unisex",
        "description": "The leaf forehead protector on a sea-blue band."}


def build(g):
    forehead_protector(g, band="A", seed=18801)
