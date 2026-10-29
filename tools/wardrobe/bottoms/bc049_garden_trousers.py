"""Garden Trousers: baggy cropped trousers rolled to below the knee for weeding and watering,
a patched knee, a cord belt and straw waraji."""
from kit_household import trouser_legs, waist, waraji
from paint import solid

META = {"name": "Garden Trousers", "gender": "unisex",
        "description": "Baggy cropped trousers rolled below the knee, patched knee, cord belt, straw waraji.",
        "tags": ["civilian", "work", "trousers"]}


def build(g):
    waist(g, "D", "twill", 37868, band="L3")
    trouser_legs(g, "D", "twill", 37869, rows=(0, 6))
    g.part("right_leg").front.rect(1, 3, 2, 2, "L2")
    waraji(g)
    for side, bone in (("right", "RIGHT_LEG"), ("left", "LEFT_LEG")):
        roll = g.piece(f"{side}_roll", bone, (-2.5, 6.2, -2.5), (5, 2, 5), inflate=.08)
        solid(roll, "D", "twill", 37871 + (side == "left"), 3)
        for face in roll.sides:
            face.hline(0, face.w - 1, 1, "D1")
