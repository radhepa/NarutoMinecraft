"""Guard Greaves: plain duty trousers with steel shin guards strapped over the lower legs and heavy
sandals: the gate watch stands all day."""
from kit import legs, waistband
from kit_shinobi import sandals
from paint import solid

META = {"name": "Guard Greaves", "gender": "unisex",
        "description": "Duty trousers with steel shin guards strapped on, heavy sandals.",
        "tags": ["shinobi", "armor"]}


def build(g):
    waistband(g, "D", "twill", 34580)
    legs(g, "D", "twill", 34581, rows=(0, 9))
    sandals(g)
    for side, bone in (("right", "RIGHT_LEG"), ("left", "LEFT_LEG")):
        guard = g.piece(f"{side}_greave", bone, (-2, 5.0, -2.9), (4, 5, 1))
        solid(guard, "M", "plain", 34583 + (side == "left"), 2)
        guard.front.hline(0, 3, 0, "M4"), guard.front.vline(0, 1, 4, "M3")
        guard.front.hline(0, 3, 2, "L2")
        strap = g.piece(f"{side}_greave_strap", bone, (-2.45, 7.0, -2.45), (5, 1, 5))
        solid(strap, "L", "leather", 34585, 2, edge=False)
