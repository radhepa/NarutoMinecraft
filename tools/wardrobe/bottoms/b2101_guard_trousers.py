"""Guard Trousers: dark gunmetal trousers for long days standing at the gate, steel shin guards
strapped from knee to ankle, a kunai holster on the right thigh and open-toe sandals."""
from kit import legs, waistband
from kit_hagane import shin_guards
from kit_shinobi import sandals
from paint import solid

META = {"name": "Guard Trousers", "gender": "unisex",
        "description": "Dark gunmetal trousers, riveted steel shin guards, a thigh holster, sandals.",
        "tags": ["shinobi"]}


def build(g):
    waistband(g, "D", "twill", 21980, 2)
    legs(g, "D", "twill", 21981, 2, rows=(0, 9))
    sandals(g)
    shin_guards(g, top=5.0, height=5, seed=21982)
    strap = g.piece("holster_strap", "RIGHT_LEG", (-2.45, 1.0, -2.45), (5, 1, 5))
    solid(strap, "L", "leather", 21983, 2)
    holster = g.piece("holster", "RIGHT_LEG", (0, 0, 0), (1, 3, 2), pivot=(-3.0, .8, -1.0))
    solid(holster, "K", "leather", 21984, 2)
