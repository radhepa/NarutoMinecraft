"""Twin Tide Tails: hair parted down the middle and tied low behind each ear in red-wrapped tails
that fall behind the shoulders to the chest, with a parted fringe and short side strands."""
from anime import bangs, lock, ring_shell, sidelocks
from kit_uzumaki import wrap_tie
from paint import scalp

META = {"name": "Twin Tide Tails", "gender": "unisex",
        "description": "Low twin tails behind the ears in cloth wraps, middle part, parted fringe."}


def build(g):
    scalp(g, 2170, side_rows=6, back_rows=7, sideburn=3, part=3)
    ring_shell(g, 2171, side_rows=6, back_rows=7, ring_row=1)
    for side, sign in (("right", -1), ("left", 1)):
        pivot, rot = (3.4 * sign, -3.0, 3.4), (16, 0, -5 * sign)
        wrap_tie(g, f"wrap_{side}", pivot, rot, (3, 1, 3), y=-.5, key="A")
        lock(g, f"tail_{side}", pivot, rot, ((3, 3), (3, 3), (2, 3), (1, 2)), 2, 2174 + (sign > 0) * 3, ring=None,
             motion="sway", y0=.5)
    bangs(g, "fringe", [(-2.7, ((2, 2), (1, 1)), 18), (-1.1, ((2, 1), (1, 1)), 34), (1.1, ((2, 1), (1, 1)), -34),
                        (2.7, ((2, 2), (1, 1)), -18)], seed=2180)
    sidelocks(g, "frame", 7, seed=2181, x=4.3, z=-3.6, flare=4, width=1)
