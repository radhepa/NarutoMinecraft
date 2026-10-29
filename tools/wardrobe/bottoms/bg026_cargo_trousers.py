"""Cargo Trousers: full-length trousers with a flapped cargo pocket on each thigh and a second on the
right shin, tucked into laced leather field boots."""
from kit import footwear
from kit_field import cargo, pocket, trousers
from kit_shinobi import wraps

META = {"name": "Cargo Trousers", "gender": "unisex",
        "description": "Full-length trousers with thigh and shin cargo pockets, tucked into leather boots.",
        "tags": ["shinobi"]}


def build(g):
    trousers(g, "D", 32500, length=8)
    wraps(g, 8, 8)
    footwear(g, "boot", top=9)
    for side in ("right", "left"):
        cargo(g, side, 32503 + (side == "left"), y=1.4, size=(3, 4, 1), scale=.9)
    pocket(g, "right_shin_pocket", (-2.25, 5.0, 0), (3, 3, 1), "D", 32506, bone="RIGHT_LEG", rotation=(0, 90, 0),
           scale=.75, texture="twill")
