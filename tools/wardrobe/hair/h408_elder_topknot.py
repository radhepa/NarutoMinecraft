"""Elder Topknot: an elder's hair combed smoothly back from a high forehead and gathered on the
crown into a bound knot, its short tail folded back over the head and bound with a lavender cord."""
from anime import cel_box, lock
from kit_hyuga import crown, hair_tie

META = {"name": "Elder Topknot", "gender": "unisex",
        "description": "Smooth combed-back hair, a bound knot on the crown with its tail folded back, a clear forehead."}


def build(g):
    crown(g, 4321, side_rows=5, back_rows=8, sideburn=3)
    for i, x in enumerate((-2.6, 0, 2.6)):
        lock(g, f"comb_{i}", (x, -8.9, -3.6), (86, 0, -x * 2), ((3, 4), (3, 2)), 1, 4335 + i, ring=0)
    knot = g.piece("knot", "HEAD", (-1.5, -2.5, -1.5), (3, 3, 3), pivot=(0, -8.6, 1.0))
    cel_box(knot, 4325, ring=0)
    hair_tie(g, "cord", (0, -8.6, 1.0), (0, 0, 0), (4, 1, 4), key="A2", y=-1.4)
    lock(g, "fold", (0, -11.0, .4), (-62, 0, 0), ((3, 3), (2, 1)), 2, 4330, ring=0)
