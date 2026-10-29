"""Short Hime: a blunt fringe cut straight at the brows, long square sidelocks to the collarbone
held by metal rings, and the back cut short and level at the nape."""
from anime import cel_box, lock, ring_shell
from paint import scalp

META = {"name": "Short Hime", "gender": "female",
        "description": "Blunt fringe at the brows, ringed square sidelocks to the collarbone, short level back."}


def build(g):
    scalp(g, 33895, side_rows=8, back_rows=8, sideburn=0)
    ring_shell(g, 33896, side_rows=8, back_rows=8, ring_row=1)
    back = g.piece("back", "HEAD", (-4.5, 0, -.5), (9, 8, 1), pivot=(0, -7.8, 4.6), rotation=(-3, 0, 0))
    cel_box(back, 33897, ring=1)
    for side, sign in (("right", -1), ("left", 1)):
        panel = g.piece(f"side_{side}", "HEAD", (-.5, 0, -1), (1, 8, 5), pivot=(4.6 * sign, -7.8, 1.0))
        cel_box(panel, 33898 + (sign > 0), ring=1)
        lock(g, f"hime_{side}", (4.3 * sign, -7.8, -3.4), (0, 0, 0), ((2, 11),), 1, 33900 + (sign > 0), ring=1)
        ring = g.piece(f"hime_{side}_ring", "HEAD", (-1, 0, -1), (2, 1, 2), pivot=(4.3 * sign, -1.4, -3.4))
        for f in ring.faces:
            f.fill("H4")
        for f in ring.sides:
            f.set(0, 0, "H3")
    for i, x in enumerate((-3.0, -1.0, 1.0, 3.0)):
        cut = g.piece(f"fringe_{i}", "HEAD", (-1, 0, -.5), (2, 3, 1), pivot=(x, -8.5, -4.35), rotation=(-8, 0, 0))
        cel_box(cut, 33903 + i, ring=0)
