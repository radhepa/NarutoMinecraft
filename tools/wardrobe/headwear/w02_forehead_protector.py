"""Forehead Protector: a navy cloth band tied at the back, with a steel plate engraved with the
Hidden Leaf mark. The plate is drawn at triple resolution so the mark reads."""
from kit_shinobi import forehead_protector

META = {"name": "Forehead Protector", "gender": "unisex",
        "description": "Navy band, riveted steel plate with the leaf mark, knot tails at the back."}


def build(g):
    forehead_protector(g)
