"""Karin Asymmetric: the right side cut short and spiky, the left side left long and straight to
the chest, a choppy fringe and a messy nape: two haircuts on one head."""
from anime import bangs, cel_box, lock, ring_shell
from paint import scalp

META = {"name": "Karin Asymmetric", "gender": "unisex",
        "description": "Short spiky right side, long straight left side to the chest, choppy fringe."}


def build(g):
    scalp(g, 2020, side_rows=5, back_rows=8, sideburn=2)
    ring_shell(g, 2021, side_rows=4, back_rows=7, ring_row=1)
    # The short side: stiff points flicking out above the right ear.
    for i, (y, z, rz, rx) in enumerate(((-7.4, -2.6, 64, 0), (-6.2, -1.0, 74, 10), (-5.0, .8, 70, 22),
                                        (-7.2, 1.6, 52, 30))):
        lock(g, f"short_{i}", (-4.3, y, z), (rx, 0, rz), ((2, 2), (1, 1)), 1, 2022 + i * 3, ring=0)
    # The long side: a sheet over the left ear and long straight locks to the chest.
    panel = g.piece("side_left", "HEAD", (-.5, 0, -3), (1, 10, 6), pivot=(4.6, -7.2, .9), motion="sway")
    cel_box(panel, 2023, ring=1)
    for i, (z, n, rz) in enumerate(((-3.4, 13, -3), (-2.2, 12, -5))):
        lock(g, f"long_{i}", (4.3, -7.6, z), (0, 0, rz), ((2, n - 2), (1, 2)), 1, 2024 + i * 5, ring=1)
    # Choppy fringe swept toward the long side.
    bangs(g, "fringe", [(-2.9, ((2, 2), (1, 1)), 28), (-1.4, ((2, 1), (1, 1)), 18), (.2, ((2, 2), (1, 1)), -6),
                        (1.8, ((2, 2), (1, 1)), -18), (3.1, ((2, 2), (1, 1)), -12)], seed=2025)
    # A messy nape, longer on the left.
    for i, (x, n, rz, rx) in enumerate(((-2.6, 3, 24, 30), (-.6, 4, 6, 24), (1.4, 5, -6, 16), (3.2, 7, -12, 10))):
        lock(g, f"nape_{i}", (x, -4.2, 4.3), (rx, 0, rz), ((2, n - 1), (1, 1)), 1, 2027 + i * 7, ring=None)
