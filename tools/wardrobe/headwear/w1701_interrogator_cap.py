"""Interrogator Cap: Ibiki Morino's forehead protector worn as a cap, a black cloth tied over the
whole head with the steel plate on the brow and the ends knotted at the nape."""
from kit_morino import head_cloth

META = {"name": "Interrogator Cap", "gender": "unisex", "hides_hair": ["*"],
        "description": "Black cloth tied over the whole head, the protector plate on the brow, knotted at the nape."}


def build(g):
    head_cloth(g, "K", 17501, plate=True, tails=4)
