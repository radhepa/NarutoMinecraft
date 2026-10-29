"""Chocho Volume: a huge cloud of curls standing out round the head, two round buns tied on top
and short curly bangs that stop at the brows: the young Akimichi's big, unmissable hair."""
from anime import tie
from kit_akimichi import puff
from paint import scalp, shell

META = {"name": "Chocho Volume", "gender": "unisex",
        "description": "A huge cloud of curls round the head, two round buns tied on top, short curly bangs."}

# The cloud, built from overlapping puffs so its outline stays lumpy: (x, y, z, size)
CLOUD = [(-5.0, -6.2, -.6, (3, 4, 4)), (-5.4, -3.6, 1.0, (4, 4, 4)), (-4.6, -1.0, 2.2, (3, 3, 4)),
         (-4.0, -7.6, 2.4, (4, 3, 4)), (-3.2, -4.4, 4.6, (4, 5, 3)), (0, -5.6, 5.2, (5, 5, 3)),
         (0, -2.4, 4.8, (4, 3, 3)), (0, -8.6, 1.4, (6, 2, 6)), (-2.4, -8.4, -2.0, (3, 2, 3))]


def build(g):
    scalp(g, 6091, side_rows=7, back_rows=8, sideburn=1)
    shell(g, 6091, side_rows=6, back_rows=8)
    for i, (x, y, z, size) in enumerate(CLOUD):
        puff(g, f"cloud_{i}", (x, y, z), size, seed=6097 + i)
        if x:
            puff(g, f"cloud_{i}_mirror", (-x, y, z), size, seed=6111 + i)
    for side, sign in (("right", -1), ("left", 1)):
        puff(g, f"bun_{side}", (2.6 * sign, -10.4, .4), (3, 3, 3), seed=6125 + (sign > 0))
        tie(g, f"bun_tie_{side}", (2.6 * sign, -8.9, .4), size=(2, 1, 2), key="A2")
    for i, x in enumerate((-2.4, 0, 2.4)):
        puff(g, f"fringe_{i}", (x, -7.3, -4.1), (3, 2, 1), seed=6132 + i)
