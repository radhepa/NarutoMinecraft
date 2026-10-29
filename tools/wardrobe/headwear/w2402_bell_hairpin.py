"""Bell Hairpin: a sprig of lily of the valley worn above the left ear, three white bells hanging
from an arching green stem with a broad leaf behind, and a smaller sprig tucked in beside it."""
from kit_suzuran import bell_charm

META = {"name": "Bell Hairpin", "gender": "unisex",
        "description": "A sprig of lily of the valley above the left ear, three white bells and a leaf, a second small sprig."}


def build(g):
    bell_charm(g, "sprig", (5.1, -7.4, -2.2), rotation=(0, -90, 18), bells=3)
    bell_charm(g, "small", (5.1, -6.6, -.6), rotation=(0, -90, 34), bells=2)
