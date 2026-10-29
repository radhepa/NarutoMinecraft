"""Flicker Curls: Shisui's thick mop of tight black curls, piled high on the crown, bunched over the
ears and down to the nape, with a row of short curls along the brow."""
from paint import curls_box, curls_face, scalp

META = {"name": "Flicker Curls", "gender": "unisex", "description": "A thick mop of tight curls over the crown, ears and nape, short curls on the brow."}

# Curl clusters: (id, origin, size, pivot, rotation)
CLUSTERS = [("crown", (-5, -2, -5), (10, 3, 10), (0, -7.6, 0), (0, 0, 0)),
            ("crown_top", (-4, -1, -4), (8, 1, 8), (0, -9.6, .4), (0, 0, 0)),
            ("lump_right", (-2, -2, -2), (3, 3, 3), (-3.4, -9.0, -1.6), (0, 0, -14)),
            ("lump_left", (-1, -2, -2), (3, 3, 3), (3.4, -9.0, -.4), (0, 0, 14)),
            ("lump_back", (-2, -2, -1), (4, 3, 3), (.6, -8.8, 3.4), (16, 0, 0)),
            ("back", (-5, 0, -1), (10, 7, 2), (0, -7.6, 4.4), (-6, 0, 0)),
            ("nape", (-4, 0, -1), (8, 2, 2), (0, -1.0, 4.6), (10, 0, 0)),
            ("side_right", (-1, 0, -4), (2, 6, 8), (-4.6, -7.4, .6), (0, 0, 4)),
            ("side_left", (-1, 0, -4), (2, 6, 8), (4.6, -7.4, .6), (0, 0, -4))]
BROW = [(-3.2, 14), (-1.1, 4), (1.1, -4), (3.2, -14)]


def build(g):
    scalp(g, 3201, side_rows=6, back_rows=8, sideburn=2)
    hat = g.part("hat")
    for face in (hat.top, hat.back, hat.right, hat.left):
        curls_face(face, 3202 + face.x0, base=1)
    for i, (pid, origin, size, pivot, rot) in enumerate(CLUSTERS):
        box = g.piece(f"curls_{pid}", "HEAD", origin, size, pivot=pivot, rotation=rot)
        curls_box(box, 3210 + i * 7, base=1)
    for i, (x, rz) in enumerate(BROW):
        box = g.piece(f"fringe_curl_{i}", "HEAD", (-1, 0, -1), (2, 2, 2), pivot=(x, -8.4, -4.0), rotation=(-12, 0, rz))
        curls_box(box, 3260 + i * 5, base=1)
