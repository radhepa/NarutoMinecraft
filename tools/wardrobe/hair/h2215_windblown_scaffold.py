"""Windblown: medium hair blown sideways by the wind up on the scaffold, every lock streaming to the
right in long points over the ear and the back, the fringe swept the same way clear of the eyes."""
from anime import back_fan, bangs, lock, ring_shell, spike
from paint import scalp

META = {"name": "Windblown", "gender": "unisex",
        "description": "Medium hair streaming sideways to the right in long points, fringe swept clear."}


def build(g):
    scalp(g, 22801, side_rows=6, back_rows=8, sideburn=2)
    ring_shell(g, 22802, side_rows=6, back_rows=8, ring_row=1)
    for i, (x, z) in enumerate(((1.6, -2.2), (-.6, -.4), (1.4, 1.8), (-1.8, 2.4))):
        spike(g, f"stream_{i}", (x, -7.8, z), (-50, 0, 34), ((3, 2), (2, 2), (1, 1)), 2, 22804 + i)
    for i, (y, z) in enumerate(((-6.6, -1.4), (-5.0, .8), (-3.6, 2.6))):
        lock(g, f"side_{i}", (-4.3, y, z), (0, 0, 26), ((2, 3), (1, 2)), 2, 22810 + i, ring=None)
    back_fan(g, "back", [(-2.4, ((3, 4), (2, 2), (1, 1)), 24, 10), (0, ((3, 4), (2, 2), (1, 1)), 22, 10),
                         (2.4, ((3, 3), (2, 2), (1, 1)), 18, 10)], seed=22814)
    bangs(g, "fringe", [(2.8, ((2, 2), (1, 1)), -50), (1.0, ((3, 1), (2, 1)), -66), (-1.0, ((2, 1), (1, 1)), -70)],
          seed=22820)
