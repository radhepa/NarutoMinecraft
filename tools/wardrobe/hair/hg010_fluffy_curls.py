"""Fluffy Curls: a soft round cloud of short curls over the crown and down to the ears, the curls a
little longer at the back, with a few loose ringlets along the brow."""
from paint import curls_box, curls_face, scalp

META = {"name": "Fluffy Curls", "gender": "unisex",
        "description": "A soft round cloud of short curls over the crown and ears, loose ringlets on the brow."}

# Soft range: no bright highlights or black pits, so every hair color keeps the curl shapes.
SOFT = {"H0": "H1", "H4": "H3"}
CLUSTERS = [("crown", (-5, -2, -5), (10, 2, 10), (0, -7.8, 0), (0, 0, 0)),
            ("dome", (-4, -1, -4), (8, 1, 8), (0, -9.8, .2), (0, 0, 0)),
            ("puff_right", (-2, -2, -2), (3, 3, 4), (-3.2, -8.6, .4), (0, 0, -18)),
            ("puff_left", (-1, -2, -2), (3, 3, 4), (3.2, -8.6, .4), (0, 0, 18)),
            ("puff_front", (-2, -2, -1), (4, 2, 2), (0, -9.2, -2.6), (-10, 0, 0)),
            ("back", (-5, 0, -1), (10, 6, 2), (0, -7.6, 4.3), (-4, 0, 0)),
            ("side_right", (-1, 0, -3), (2, 5, 7), (-4.6, -7.6, .8), (0, 0, 6)),
            ("side_left", (-1, 0, -3), (2, 5, 7), (4.6, -7.6, .8), (0, 0, -6))]
BROW = [(-3.0, 12), (-1.0, -4), (1.4, 6), (3.2, -12)]


def soften(box):
    for face in box.faces:
        face.recolor(lambda key, x, y: SOFT.get(key, key))


def build(g):
    scalp(g, 31960, side_rows=6, back_rows=8, sideburn=2)
    hat = g.part("hat")
    for face in (hat.top, hat.back, hat.right, hat.left):
        curls_face(face, 31961 + face.x0)
        face.recolor(lambda key, x, y: SOFT.get(key, key))
    for i, (pid, origin, size, pivot, rot) in enumerate(CLUSTERS):
        box = g.piece(f"curls_{pid}", "HEAD", origin, size, pivot=pivot, rotation=rot)
        curls_box(box, 31962 + i * 3)
        soften(box)
    for i, (x, rz) in enumerate(BROW):
        box = g.piece(f"ringlet_{i}", "HEAD", (-1, 0, -1), (2, 2, 2), pivot=(x, -8.6, -4.0), rotation=(-12, 0, rz))
        curls_box(box, 31990 + i)
        soften(box)
