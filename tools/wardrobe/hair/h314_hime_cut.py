"""Hime Cut: a court kunoichi's cut, a blunt fringe level with the brows, blunt cheek locks cut
straight at the jaw and straight hair hanging level to the shoulder blades."""
from anime import cel_box, lock, ring_shell
from paint import scalp

META = {"name": "Hime Cut", "gender": "female", "description": "A blunt brow-level fringe, blunt jaw-length cheek locks, straight hair to the shoulder blades."}


def build(g):
    scalp(g, 3661, side_rows=7, back_rows=8, sideburn=1)
    ring_shell(g, 3662, side_rows=7, back_rows=8, ring_row=1)
    sheet = g.piece("curtain", "HEAD", (-4.5, 0, -.5), (9, 12, 1), pivot=(0, -6.2, 4.6), rotation=(-6, 0, 0), motion="sway")
    cel_box(sheet, 3665, ring=1)
    for side, sign in (("right", -1), ("left", 1)):
        panel = g.piece(f"side_{side}", "HEAD", (-.5, 0, -3), (1, 11, 6), pivot=(4.6 * sign, -7, 1.4))
        cel_box(panel, 3670 + (sign > 0), ring=1)
        lock(g, f"cheek_{side}", (4.3 * sign, -7.6, -3.4), (0, 0, 0), ((2, 8),), 1, 3675 + (sign > 0), ring=1)
    for i, x in enumerate((-2.5, -.5, 1.5)):
        lock(g, f"fringe_{i}", (x + .5, -8.55, -4.35), (-10, 0, 0), ((2, 3),), 1, 3680 + i * 3, ring=0)
