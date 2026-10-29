"""Matron's Bun: the shop mistress's swept-back hair, puffed out at the sides over the ears and
gathered into a round bun high at the back of the crown with a plain wooden comb set in front."""
from anime import cel_box, ring_shell
from paint import scalp, solid

META = {"name": "Matron's Bun", "gender": "female",
        "description": "Swept back, puffed at the sides, a round bun high at the back with a wooden comb."}


def build(g):
    scalp(g, 36980, side_rows=6, back_rows=8, sideburn=1, part=3)
    ring_shell(g, 36981, side_rows=5, back_rows=7, ring_row=1)
    for side, x in (("right", -5.6), ("left", 4.6)):
        puff = g.piece(f"puff_{side}", "HEAD", (0, 0, 0), (1, 3, 5), pivot=(x, -7.2, -1.6))
        cel_box(puff, 36982 + (x > 0), ring=0, clump=2)
    bun = g.piece("bun", "HEAD", (-2.5, -2, -1.5), (5, 4, 3), pivot=(0, -6.6, 5.6), rotation=(-20, 0, 0))
    cel_box(bun, 36984, base=3, ring=1, clump=2)
    comb = g.piece("bun_comb", "HEAD", (-2.5, -1, -.5), (5, 1, 1), pivot=(0, -8.4, 4.9), rotation=(-20, 0, 0))
    solid(comb, "L", "smooth", 36985, 3, edge=False)
