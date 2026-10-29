"""Balding Crown: an older man's bare crown with the hair left in a short thick horseshoe round the
sides and the back of the head, bushier over the ears."""
from paint import hair_face, k, rnd
from anime import cel_box

META = {"name": "Balding Crown", "gender": "male",
        "description": "Bare crown, a short thick horseshoe of hair round the sides and back, bushier over the ears."}


def build(g):
    head, hat = g.part("head"), g.part("hat")
    for face, rows in ((head.right, range(2, 6)), (head.left, range(2, 6)), (head.back, range(1, 7))):
        hair_face(face, 36970 + face.x0, 2, rows=rows)
    head.right.set(7, 6, "H1"), head.left.set(0, 6, "H1")
    # The rim of the crown at the back and sides, thinning to nothing at the front.
    for x in range(8):
        head.top.set(x, 0, k("H", 2 if rnd(x, 0, 36971) < .7 else 1))
    for y in range(4):
        head.top.set(0, y, "H2"), head.top.set(7, y, "H2")
    for face, rows in ((hat.right, range(3, 5)), (hat.left, range(3, 5)), (hat.back, range(2, 6))):
        hair_face(face, 36972 + face.x0, 2, rows=rows)
    for side, x in (("right", -4.75), ("left", 3.75)):
        tuft = g.piece(f"ear_tuft_{side}", "HEAD", (0, 0, 0), (1, 2, 3), pivot=(x, -5.4, -.2))
        cel_box(tuft, 36974 + (x > 0), clump=2)
