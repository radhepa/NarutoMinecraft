"""Council Part: the clan's ordinary office cut, neat and short with a hard side part on the left,
the fringe combed across the brow in one smooth sweep and the sides tapered over the ears."""
from anime import cel_box, lock, ring_shell
from paint import scalp

META = {"name": "Council Part", "gender": "unisex",
        "description": "Neat short cut, a hard side part, the fringe combed across the brow in one sweep."}


def build(g):
    scalp(g, 13231, side_rows=4, back_rows=6, sideburn=2, part=5)
    ring_shell(g, 13232, side_rows=4, back_rows=6, ring_row=1)
    crown = g.piece("crown", "HEAD", (-4.5, -8.5, -4.5), (6, 1, 9))
    cel_box(crown, 13232, ring=0, clump=3)
    low = g.piece("crown_low", "HEAD", (1.5, -8.3, -4.5), (3, 1, 9))
    cel_box(low, 13233, base=1, ring=0, clump=3)
    for i, (x, rz) in enumerate(((-3.2, 64), (-1.6, 70), (0, 74))):
        lock(g, f"sweep_{i}", (x + 1.4, -8.4, -4.4), (-6, 0, rz), ((2, 3), (1, 2)), 1, 13237 + i, ring=0)
