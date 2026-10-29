"""Greaved Hakama: a short split hakama to the knee with dark iron greaves strapped over the shins
and pale tabi in straw sandals: the duelling dress of wandering swordsmen and kickers alike."""
from kit import legs, waistband
from kit_rugged import baggy_legs, shin_guard, straw_sandals, tabi
from paint import solid

META = {"name": "Greaved Hakama", "gender": "unisex",
        "description": "Short split hakama to the knee with iron greaves over the shins, pale tabi, straw sandals.",
        "tags": ["shinobi", "hakama"]}


def build(g):
    waistband(g, "P", "twill", 35490, 2)
    legs(g, "P", "twill", 35491, 2, rows=(0, 5), crease=False)
    baggy_legs(g, "hakama", "P", 35492, top=0.0, length=6, flare=6)
    tabi(g, rows=(6, 11))
    straw_sandals(g)
    shin_guard(g, "greave", "K", 35494, top=6.0, length=4, strap="L2", texture="plain")
    tie = g.piece("waist_tie", "TORSO", (-4.5, 9.3, -2.5), (9, 1, 5), inflate=.2)
    solid(tie, "P", "weave", 35496, 3, edge=False)
