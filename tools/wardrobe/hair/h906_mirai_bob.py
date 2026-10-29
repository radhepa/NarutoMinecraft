"""Mirai Bob: Mirai Sarutobi's short dark hair, cut blunt at the chin all the way round, the fringe
cut straight at the brows and the sides falling just past the cheeks."""
from anime import back_fan, bangs, ring_shell, sidelocks
from paint import scalp

META = {"name": "Mirai Bob", "gender": "unisex",
        "description": "A blunt chin-length bob all the way round with a straight fringe at the brows."}


def build(g):
    scalp(g, 9311, side_rows=8, back_rows=8, sideburn=0)
    ring_shell(g, 9312, side_rows=8, back_rows=8, ring_row=1)
    bangs(g, "fringe", [(-2.7, ((2, 3),), 4), (-1.0, ((2, 2),), 0), (1.0, ((2, 2),), 0), (2.7, ((2, 3),), -4)],
          seed=9320)
    sidelocks(g, "frame", 8, seed=9330, x=4.4, z=-3.3, flare=4, width=2, taper=False)
    sidelocks(g, "frame_mid", 8, seed=9335, x=4.5, z=-.8, flare=6, width=3, taper=False)
    back_fan(g, "back", [(-3.0, ((3, 8),), 10, 10), (0.0, ((3, 8),), 0, 12), (3.0, ((3, 8),), -10, 10)], seed=9340)
