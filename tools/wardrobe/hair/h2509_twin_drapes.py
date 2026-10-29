"""Twin Drapes: shoulder-length hair with two long locks hanging before the ears to the chest, each
bound in three small dark rings like the cords of a drawn curtain, a soft side fringe."""
from anime import back_fan, bangs, lock, ring_shell, tie
from paint import scalp

META = {"name": "Twin Drapes", "gender": "unisex",
        "description": "Shoulder-length hair, two long front locks bound in dark rings, a soft side fringe."}


def build(g):
    scalp(g, 25160, side_rows=7, back_rows=8, sideburn=3, part=-2)
    ring_shell(g, 25161, side_rows=7, back_rows=8, ring_row=1)
    for side, sign in (("right", -1), ("left", 1)):
        pivot = (4.5 * sign, -6.6, -2.6)
        lock(g, f"drape_{side}", pivot, (0, 0, -2 * sign), ((2, 9), (2, 2), (1, 1)), 2, 25162 + (sign > 0), ring=1,
             motion="sway")
        for i, y in enumerate((3.0, 5.5, 8.0)):
            tie(g, f"drape_{side}_ring_{i}", pivot, (0, 0, -2 * sign), size=(3, 1, 3), y=y, key="K2", motion="sway")
    bangs(g, "fringe", [(-2.8, ((2, 2), (1, 1)), 16), (-.8, ((3, 1), (2, 1)), -36), (1.6, ((3, 2), (2, 1)), -30),
                        (3.0, ((2, 2), (1, 1)), -18)], seed=25170)
    back_fan(g, "nape", [(-3.0, ((3, 7), (2, 1)), 6, 8), (0, ((3, 7), (2, 1)), 0, 8), (3.0, ((3, 7), (2, 1)), -6, 8)],
             seed=25175)
