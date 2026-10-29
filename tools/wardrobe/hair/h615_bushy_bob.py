"""Bushy Bob: a thick chin-length bob that puffs out wide at the sides in curling points, heavy
layered bangs to the brow and a full rounded back."""
from anime import back_fan, bangs, ring_shell
from kit_akimichi import puff
from paint import scalp

META = {"name": "Bushy Bob", "gender": "unisex",
        "description": "A thick chin-length bob puffed wide at the sides, layered bangs, a rounded back."}


def build(g):
    scalp(g, 7401, side_rows=8, back_rows=8, sideburn=0)
    ring_shell(g, 7402, side_rows=8, back_rows=8, ring_row=1)
    for side, sign in (("right", -1), ("left", 1)):
        puff(g, f"side_{side}", (4.8 * sign, -5.0, .6), (3, 5, 6), seed=7410 + (sign > 0))
        puff(g, f"side_{side}_low", (5.2 * sign, -1.6, -.4), (3, 4, 4), seed=7412 + (sign > 0))
        puff(g, f"side_{side}_back", (3.6 * sign, -2.4, 3.6), (3, 4, 4), seed=7416 + (sign > 0))
        puff(g, f"crown_{side}", (2.2 * sign, -8.4, .8), (4, 2, 6), seed=7418 + (sign > 0))
    puff(g, "back", (0, -5.0, 4.8), (6, 6, 3), seed=7414)
    back_fan(g, "nape", [(-2.6, ((3, 2), (1, 1)), 24, 26), (0, ((3, 2), (1, 1)), 0, 30), (2.6, ((3, 2), (1, 1)), -24, 26)],
             seed=7420, z=5.6)
    bangs(g, "fringe", [(-2.8, ((2, 2), (1, 1)), 14), (-1.0, ((2, 2), (1, 1)), 8), (1.0, ((2, 2), (1, 1)), -8),
                        (2.8, ((2, 2), (1, 1)), -14)], seed=7430)
