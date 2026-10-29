"""Tail Skirt: fitted three-quarter trousers with a long open-backed overskirt that hangs only
behind, from hip to calf, swinging as the wearer runs, and open-toe sandals."""
from kit import belt, legs, waistband
from kit_shinobi import sandals
from paint import solid

META = {"name": "Tail Skirt", "gender": "unisex",
        "description": "Fitted three-quarter trousers with a long back overskirt to the calf, sandals.",
        "tags": ["shinobi", "skirt"]}


def build(g):
    waistband(g, "K", "plain", 33760)
    legs(g, "K", "plain", 33761, rows=(0, 8), crease=False)
    sandals(g)
    belt(g, "waist_band", y=9.3, role="A", height=1, buckle=None, inflate=.15)
    tail = g.piece("waist_tail", "TORSO", (-4.5, 0, 0), (9, 10, 1), pivot=(0, 10.0, 1.9), motion="flap_back")
    solid(tail, "P", "weave", 33762, 2)
    tail.back.hline(0, 8, 0, "P3"), tail.back.hline(0, 8, 9, "A2")
    tail.back.vline(0, 1, 9, "P1"), tail.back.vline(8, 1, 9, "P1"), tail.back.vline(4, 2, 9, "P1")
    for name, x in (("right", -5.0), ("left", 4.0)):
        side = g.piece(f"waist_tail_{name}", "TORSO", (0, 0, 0), (1, 6, 2), pivot=(x, 10.0, .2))
        solid(side, "P", "weave", 33763, 2)
