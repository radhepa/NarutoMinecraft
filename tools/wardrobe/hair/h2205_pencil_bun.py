"""Pencil Bun: hair twisted up into a round bun at the back of the crown and skewered through with a
carpenter's pencil, a few short wisps loose at the nape and a light side-swept fringe."""
from anime import bangs, cel_box, lock, ring_shell
from kit_kinoshita import pencil
from paint import scalp

META = {"name": "Pencil Bun", "gender": "unisex",
        "description": "A round twisted bun at the back of the crown skewered with a carpenter's pencil."}


def build(g):
    scalp(g, 22081, side_rows=5, back_rows=8, sideburn=2, part=5)
    ring_shell(g, 22082, side_rows=5, back_rows=8, ring_row=1)
    bun = g.piece("bun", "HEAD", (-2.5, -2.5, -2), (5, 5, 4), pivot=(0, -7.4, 5.2), rotation=(-30, 0, 0))
    cel_box(bun, 22083, ring=1)
    twist = g.piece("bun_twist", "HEAD", (-1.5, -1.5, 0), (3, 3, 1), pivot=(0, -7.4, 7.1), rotation=(-30, 0, 0))
    cel_box(twist, 22084, base=1)
    pencil(g, "bun_pencil", (0, -7.6, 6.2), (-30, 0, 74), length=14)
    for i, (x, rz) in enumerate(((-1.8, 14), (1.6, -18))):
        lock(g, f"wisp_{i}", (x, -3.6, 4.2), (16, 0, rz), ((1, 2), (1, 1)), 1, 22086 + i, ring=None)
    bangs(g, "fringe", [(-2.8, ((2, 2), (1, 1)), 36), (-1.0, ((3, 1), (2, 1)), 52), (1.2, ((3, 1), (1, 1)), 54),
                        (3.0, ((2, 2), (1, 1)), 24)], seed=22090)
