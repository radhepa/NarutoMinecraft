"""Nagato Fringe: straight hair to the jaw all round with a long fringe swept to one side; a long
lock falls past the right eye to the chin, outside the face, and the back hangs to the collar."""
from anime import cel_box, lock, ring_shell
from paint import scalp

META = {"name": "Nagato Fringe", "gender": "unisex",
        "description": "Jaw-length straight hair, a long side-swept fringe and a lock falling past one eye."}


def build(g):
    scalp(g, 2030, side_rows=8, back_rows=8, sideburn=0)
    ring_shell(g, 2031, side_rows=8, back_rows=8, ring_row=1)
    back = g.piece("back", "HEAD", (-4.5, 0, -.5), (9, 10, 1), pivot=(0, -7.2, 4.6), rotation=(-4, 0, 0), motion="sway")
    cel_box(back, 2032, ring=1)
    for i, x in enumerate((-3, 0, 3)):
        lock(g, f"back_tip_{i}", (x, 2.6, 4.55), (-4, 0, 0), ((3, 1), (1, 1)), 1, 2033 + i, ring=None, motion="sway")
    for side, sign in (("right", -1), ("left", 1)):
        panel = g.piece(f"side_{side}", "HEAD", (-.5, 0, -3.6), (1, 9, 8), pivot=(4.6 * sign, -7.6, .2))
        cel_box(panel, 2036 + (sign > 0), ring=1)
    # The swept fringe: every lock leans to the character's right, the deepest stopping at the brow.
    for i, (x, segs, rz) in enumerate(((3.0, ((2, 2), (1, 1)), 34), (1.6, ((2, 2), (1, 1)), 36), (.2, ((2, 2), (1, 1)), 38),
                                      (-1.2, ((2, 2), (1, 1)), 40), (-2.6, ((2, 1), (1, 1)), 30))):
        lock(g, f"fringe_{i}", (x, -8.55, -4.35), (-10, 0, rz), segs, 1, 2040 + i * 13, ring=0)
    # The long lock past the right eye, hung outside the eye line, down to the jaw.
    lock(g, "veil", (-4.1, -7.8, -4.0), (-4, 0, 2), ((2, 5), (2, 2), (1, 2)), 1, 2049, ring=1)
    lock(g, "frame_left", (4.3, -7.6, -3.4), (0, 0, -3), ((2, 7), (1, 2)), 1, 2050, ring=1)
