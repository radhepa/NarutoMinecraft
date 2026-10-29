"""Oxblood Kerchief: a plain oxblood cloth tied close over the head with no plate, the edge turned
in black, the knot at the nape: worn off duty and by the clan's young."""
from kit_morino import head_cloth

META = {"name": "Oxblood Kerchief", "gender": "unisex", "hides_hair": ["*"],
        "description": "Plain oxblood cloth tied close over the head, black-edged, knotted at the nape."}


def build(g):
    head_cloth(g, "A", 17521, plate=False, tails=3, hem="K1", base=1)
