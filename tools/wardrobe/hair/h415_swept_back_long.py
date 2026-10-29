"""Swept-Back Long: long straight hair combed straight back off a bare forehead, with no fringe at
all, two fine strands slipping loose at the temples and the length past the shoulder blades."""
from anime import lock
from kit_hyuga import back_sheet, crown, ear_panels

META = {"name": "Swept-Back Long", "gender": "unisex",
        "description": "Combed straight back off a bare forehead, two loose temple strands, length past the shoulder blades."}


def build(g):
    crown(g, 4601, side_rows=6, back_rows=8, sideburn=2)
    back_sheet(g, "length", 12, 4605, tilt=-5)
    ear_panels(g, "side", 7, 4610, z0=-1.5, depth=6)
    for i, x in enumerate((-2.6, 0, 2.6)):
        lock(g, f"comb_{i}", (x, -8.9, -3.6), (86, 0, -x * 2), ((3, 5), (3, 2)), 1, 4615 + i, ring=0)
    for side, sign in (("right", -1), ("left", 1)):
        lock(g, f"strand_{side}", (3.9 * sign, -7.8, -3.9), (-6, 0, -6 * sign), ((1, 5), (1, 2)), 1, 4620 + (sign > 0), ring=1)
