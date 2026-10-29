"""Side-Swept Bob: a jaw-length bob parted at the side, the long fringe swept across the forehead above
the brows, the heavier side tucked forward along the cheek."""
from anime import cel_box, lock, ring_shell
from paint import scalp

META = {"name": "Side-Swept Bob", "gender": "unisex",
        "description": "Jaw-length bob parted at the side, a long fringe swept across above the brows."}


def build(g):
    scalp(g, 31860, side_rows=7, back_rows=8, sideburn=1, part=5)
    ring_shell(g, 31861, side_rows=7, back_rows=8, ring_row=1)
    for side, sign, n in (("right", -1, 8), ("left", 1, 7)):
        panel = g.piece(f"side_{side}", "HEAD", (-.5, 0, -3.5), (1, n, 7), pivot=(4.5 * sign, -7.6, .2),
                        rotation=(0, 0, -5 * sign))
        cel_box(panel, 31862 + (sign > 0), ring=1)
    back = g.piece("back_panel", "HEAD", (-4.5, 0, -.5), (9, 7, 1), pivot=(0, -7.2, 4.6), rotation=(5, 0, 0))
    cel_box(back, 31864, ring=1)
    # The swept fringe: long locks lying almost flat across the brow from the side parting.
    for i, (x, rz, segs) in enumerate(((1.8, 62, ((3, 2), (2, 2), (1, 1))), (.2, 70, ((3, 2), (2, 2), (1, 1))),
                                       (-1.6, 64, ((2, 2), (1, 1))))):
        lock(g, f"fringe_{i}", (x, -8.5, -4.35), (-8, 0, rz), segs, 1, 31866 + i * 3, ring=0)
    lock(g, "cheek_lock", (-4.3, -6.8, -3.4), (0, 0, 6), ((2, 4), (1, 2)), 1, 31876, ring=1)
