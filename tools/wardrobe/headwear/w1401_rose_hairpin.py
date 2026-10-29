"""Rose Hairpin: a crimson rose pinned above the left ear with a dark lacquered pin through the
hair, the clan's flower worn on the head."""
from kit_yuhi import rose
from paint import solid

META = {"name": "Rose Hairpin", "gender": "unisex",
        "description": "A crimson rose pinned above the left ear with a dark lacquered pin."}


def build(g):
    rose(g, "rose", (4.95, -6.2, -1.2), rotation=(0, -90, 0), petal="A", base=2)
    pin = g.piece("pin", "HEAD", (-.5, -.5, -2), (1, 1, 4), pivot=(4.75, -5.6, .6), rotation=(-20, 0, 0), scale=(.5, .5, 1))
    solid(pin, "K", "smooth", 14960, 2, edge=False)
    pin.back.fill("A3")
