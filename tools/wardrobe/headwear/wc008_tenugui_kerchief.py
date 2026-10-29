"""Tenugui Kerchief: a striped cotton towel laid over the hair for cleaning day and the garden,
its front edge folded back at the hairline and its end tucked at the nape so a tail hangs down."""
from kit_household import stripes
from paint import fabric, solid

META = {"name": "Tenugui Kerchief", "gender": "unisex", "hides_hair": ["*"],
        "description": "Striped cotton towel over the hair, edge folded at the hairline, tail hanging at the nape."}


def towel(face, rows=None):
    stripes(face, "D2", every=4, rows=rows)


def build(g):
    cap = g.piece("kerchief", "HEAD", (-4, -8, -4), (8, 2, 8), inflate=.64)
    for face in cap.sides:
        fabric(face, "S", "plain", 37920 + face.x0, 3)
        towel(face)
    fabric(cap.top, "S", "plain", 37920, 4)
    towel(cap.top)
    cap.bottom.fill("S1")
    fold = g.piece("kerchief_fold", "HEAD", (-4, 0, -4), (8, 1, 8), pivot=(0, -7.3, 0), inflate=.74)
    solid(fold, "S", "plain", 37921, 4, edge=False)
    fold.bottom.fill("S1")
    back = g.piece("kerchief_back", "HEAD", (-4, 0, 0), (8, 3, 1), pivot=(0, -5.6, 3.3), inflate=.64)
    for face in back.faces:
        fabric(face, "S", "plain", 37922, 3)
        towel(face)
    tail = g.piece("kerchief_tail", "HEAD", (-1.5, 0, 0), (3, 4, 1), pivot=(.6, -3.4, 4.6), rotation=(14, 0, -4), motion="sway")
    solid(tail, "S", "plain", 37923, 3)
    towel(tail.back)
    tail.back.hline(0, 2, 3, "D1")
