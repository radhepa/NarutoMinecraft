"""Balding Elder: the old man's crown gone bare and shining, a fringe of cropped hair left round
the back and sides, combed into two bushy tufts above the ears."""
from anime import lock
from paint import hair_face, k

META = {"name": "Balding Elder", "gender": "male",
        "description": "Bare crown, a ring of cropped hair round the back and sides, bushy tufts above the ears."}


def build(g):
    head, hat = g.part("head"), g.part("hat")
    hair_face(head.back, 37990, rows=range(2, 7))
    hair_face(head.right, 37991, rows=range(2, 6), cols=range(0, 6))
    hair_face(head.left, 37992, rows=range(2, 6), cols=range(2, 8))
    for face, rows, cols in ((hat.back, range(2, 6), range(8)), (hat.right, range(2, 5), range(0, 6)),
                             (hat.left, range(2, 5), range(2, 8))):
        hair_face(face, 37993 + face.x0, rows=rows, cols=cols)
        for x in cols:
            face.set(x, rows[-1] + 1, k("H", 1))
    for side, sign in (("right", -1), ("left", 1)):
        for i, z in enumerate((-1.2, .8)):
            lock(g, f"tuft_{side}_{i}", (4.4 * sign, -5.8, z), (0, 0, -40 * sign), ((2, 2), (1, 1)), 2, 37995 + i + (sign > 0) * 2)
