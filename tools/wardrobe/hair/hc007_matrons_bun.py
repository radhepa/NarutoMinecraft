"""Matron's Bun: long hair parted in the centre, swept back in soft rolls over the ears and wound
into a broad round bun low at the nape, pinned with a lacquered comb; the forehead clear."""
from anime import cel_box, ring_shell
from kit_household import topknot
from paint import scalp, solid

META = {"name": "Matron's Bun", "gender": "female",
        "description": "Centre parting, soft rolls over the ears, a broad low bun at the nape with a lacquered comb."}


def build(g):
    scalp(g, 37960, side_rows=6, back_rows=8, sideburn=2, part=3)
    ring_shell(g, 37961, side_rows=6, back_rows=8, ring_row=1)
    for side, sign in (("right", -1), ("left", 1)):
        roll = g.piece(f"roll_{side}", "HEAD", (-.5, 0, -3), (1, 3, 6), pivot=(4.65 * sign, -7.2, .8))
        cel_box(roll, 37962 + (sign > 0), ring=0)
    topknot(g, "bun", (0, -3.4, 5.0), (5, 4, 3), seed=37964)
    comb = g.piece("comb", "HEAD", (-2.5, -.5, -.5), (5, 1, 1), pivot=(0, -5.6, 5.0), rotation=(-10, 0, 0))
    solid(comb, "K", "smooth", 37967, 2, edge=False)
    comb.top.hline(0, 4, 0, "A3")
