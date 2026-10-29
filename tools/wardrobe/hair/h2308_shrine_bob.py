"""Shrine Bob: the shrine maiden's cut, straight and blunt: a heavy fringe cut level at the brows
and the sides falling in two square panels to the jaw."""
from anime import cel_box, ring_shell
from paint import k, scalp

META = {"name": "Shrine Bob", "gender": "unisex",
        "description": "Straight blunt bob: a level fringe at the brows, square side panels to the jaw."}


def build(g):
    scalp(g, 23161, side_rows=8, back_rows=8, sideburn=0)
    hat = ring_shell(g, 23162, side_rows=8, back_rows=8, ring_row=1)
    for x in range(8):   # the blunt fringe, cut level across the brows
        hat.front.set(x, 0, k("H", 2)), hat.front.set(x, 1, k("H", 2 if x % 3 else 1))
        hat.front.set(x, 2, k("H", 1))
    for side, sign in (("right", -1), ("left", 1)):
        panel = g.piece(f"side_{side}", "HEAD", (-.5, 0, -4.2), (1, 8, 8), pivot=(4.55 * sign, -8.2, 0))
        cel_box(panel, 23165 + (sign > 0), ring=1)
        for f in panel.sides:
            f.hline(0, f.w - 1, f.h - 1, k("H", 1))
    back = g.piece("back_panel", "HEAD", (-4.5, 0, -.5), (9, 8, 1), pivot=(0, -8.2, 4.55))
    cel_box(back, 23168, ring=1)
