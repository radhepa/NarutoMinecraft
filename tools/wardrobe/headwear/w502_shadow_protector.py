"""Shadow Protector: the forehead protector on a shadow-black band, its knot tails left long."""
from kit_shinobi import forehead_protector

META = {"name": "Shadow Protector", "gender": "unisex",
        "description": "The leaf forehead protector on a shadow-black band."}


def build(g):
    forehead_protector(g, band="K", seed=5721)
