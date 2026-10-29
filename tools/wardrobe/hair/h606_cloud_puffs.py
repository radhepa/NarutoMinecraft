"""Cloud Puffs: a short, round crop of tight curls hugging the head in soft puffs, a little fuller at
the crown, with a curly edge along the brow."""
from kit_akimichi import puff
from paint import scalp, shell

META = {"name": "Cloud Puffs", "gender": "unisex", "description": "A short round crop of tight curls, fuller at the crown."}

PUFFS = [(-3.0, -8.4, -1.6, (3, 2, 3)), (0, -8.8, -.4, (4, 2, 4)), (3.0, -8.4, -1.6, (3, 2, 3)),
         (-2.0, -8.6, 2.2, (4, 2, 4)), (2.0, -8.6, 2.2, (4, 2, 4)), (-4.3, -6.0, .6, (2, 4, 5)),
         (4.3, -6.0, .6, (2, 4, 5)), (0, -5.4, 4.4, (6, 4, 2)), (-2.6, -2.8, 4.3, (3, 3, 2)), (2.6, -2.8, 4.3, (3, 3, 2))]


def build(g):
    scalp(g, 6501, side_rows=5, back_rows=8, sideburn=1)
    shell(g, 6502, side_rows=4, back_rows=7)
    for i, (x, y, z, size) in enumerate(PUFFS):
        puff(g, f"puff_{i}", (x, y, z), size, seed=6510 + i)
    for i, x in enumerate((-2.6, 0, 2.6)):
        puff(g, f"fringe_{i}", (x, -7.6, -4.1), (3, 1, 1), seed=6530 + i)
