"""Shaving Curls: a loose mop of springy curls like the ribbons that peel off a plane, curling out
over the crown, the ears and the nape, and a curled fringe resting on the brows."""
from anime import ring_shell
from paint import curls_box, scalp

META = {"name": "Shaving Curls", "gender": "unisex",
        "description": "A loose mop of springy plane-shaving curls over the crown, ears and nape, curled fringe."}


def curl(g, pid, pivot, rotation, size, seed):
    w, h, d = size
    box = g.piece(pid, "HEAD", (-w / 2, -h / 2, -d / 2), size, pivot=pivot, rotation=rotation)
    curls_box(box, seed)


def build(g):
    scalp(g, 22101, side_rows=5, back_rows=8, sideburn=2)
    ring_shell(g, 22102, side_rows=5, back_rows=8, ring_row=1)
    for i, (pivot, rot, size) in enumerate((((-2.2, -8.4, -1.8), (0, 0, -14), (4, 3, 4)),
                                            ((1.8, -8.6, -1.4), (0, 0, 12), (4, 3, 4)),
                                            ((0, -8.6, 1.6), (10, 0, 0), (5, 3, 4)),
                                            ((-3.6, -6.4, 1.0), (0, 0, -20), (3, 4, 5)),
                                            ((3.6, -6.4, 1.0), (0, 0, 20), (3, 4, 5)),
                                            ((0, -4.4, 3.8), (16, 0, 0), (6, 4, 3)),
                                            ((-2.4, -2.8, 3.4), (20, 0, -10), (3, 3, 3)),
                                            ((2.4, -2.8, 3.4), (20, 0, 10), (3, 3, 3)))):
        curl(g, f"curl_{i}", pivot, rot, size, 22104 + i)
    for i, x in enumerate((-2.6, -.4, 1.8)):
        curl(g, f"fringe_{i}", (x, -7.5, -3.8), (-10, 0, 0), (3, 2, 2), 22113 + i)
