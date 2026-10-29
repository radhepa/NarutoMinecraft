"""Shorts and Knee Socks: long shorts that stop just below the knee, striped socks pulled up to meet
them and low canvas shoes: the tidy student who sits in the front row."""
from kit import footwear
from kit_academy import leg_cloth, stripes, turned_hem, waist

META = {"name": "Shorts and Knee Socks", "gender": "unisex",
        "description": "Below-knee shorts, striped knee socks and low canvas shoes.",
        "tags": ["shinobi", "genin"]}


def build(g):
    waist(g, "K", "twill", 31550)
    leg_cloth(g, "K", "twill", 31551, (0, 5))
    for side in ("right", "left"):
        leg = g.part(f"{side}_leg")
        stripes(leg, range(6, 10), "S3")
        stripes(leg, (6, 8), "P2")
    turned_hem(g, "hem", 5.2, "K", 31553, height=1)
    footwear(g, "shoe", 10, "L", 2, toe="L3", sole="K1")
