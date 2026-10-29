"""Teacher Bun: hair combed up into a neat round bun pinned high on the back of the head, the fringe
parted off the brow and one thin strand left at each temple: tidy for a day at the front of a class."""
from anime import cel_box, sidelocks
from kit_umino import combed_up

META = {"name": "Teacher Bun", "gender": "unisex",
        "description": "Combed up into a neat round bun high on the back of the head, a thin strand at each temple."}


def build(g):
    combed_up(g, 18041, side_rows=4, back_rows=6, sideburn=2)
    base = g.piece("bun_base", "HEAD", (-3, -2, -1), (6, 4, 2), pivot=(0, -6.8, 4.9), rotation=(-30, 0, 0))
    cel_box(base, 18043, base=1)
    bun = g.piece("bun", "HEAD", (-2.5, -2.5, 0), (5, 5, 4), pivot=(0, -7.6, 5.6), rotation=(-30, 0, 0))
    cel_box(bun, 18045, base=2, ring=1)
    for face in bun.sides:
        face.vline(1, 0, 3, "H1")
    sidelocks(g, "strand", 5, seed=18047, x=4.35, z=-3.0, flare=3, width=1)
