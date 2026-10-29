"""Layered Shag: shoulder-length hair cut in short layers, choppy over the crown and flicking out at
the ends, a split fringe falling to the brows on either side of the forehead."""
from anime import back_fan, lock, ring_shell, sidelocks
from paint import scalp

META = {"name": "Layered Shag", "gender": "unisex",
        "description": "Shoulder-length choppy layers flicking out at the ends, a split fringe to the brows."}

FRINGE = [(-2.8, ((2, 2), (1, 1)), 18), (-1.2, ((2, 2), (1, 1)), 48), (1.2, ((2, 2), (1, 1)), -48), (2.8, ((2, 2), (1, 1)), -18)]
BACK = [(-3.0, ((2, 5), (1, 2)), 18, 14), (-1.0, ((3, 6), (1, 2)), 6, 12), (1.0, ((3, 6), (1, 2)), -6, 12),
        (3.0, ((2, 5), (1, 2)), -18, 14)]


def build(g):
    scalp(g, 19351, side_rows=7, back_rows=8, sideburn=1, part=3)
    ring_shell(g, 19352, side_rows=6, back_rows=8, ring_row=1)
    for i, (x, segs, rz) in enumerate(FRINGE):
        lock(g, f"fringe_{i}", (x, -8.55, -4.35), (-10, 0, rz), segs, 1, 19355 + i * 7, ring=0)
    sidelocks(g, "frame", 7, seed=19385, x=4.4, flare=10, width=2)
    for side, sign in (("right", -1), ("left", 1)):
        lock(g, f"layer_{side}", (4.5 * sign, -6.8, .8), (0, 0, -18 * sign), ((2, 4), (1, 2)), 3, 19388 + (sign > 0))
    back_fan(g, "back", BACK, seed=19390, motion="sway")
