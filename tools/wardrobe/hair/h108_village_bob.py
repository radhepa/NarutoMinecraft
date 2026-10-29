"""Village Bob: straight hair cut level at the shoulders all the way round, a blunt fringe at the
brows, the calm everyday cut of the clan's townsfolk."""
from anime import bangs, curtain, ring_shell
from kit_senju import side_panels
from paint import scalp

META = {"name": "Village Bob", "gender": "unisex",
        "description": "Straight hair cut level at the shoulders, a blunt fringe at the brows."}


def build(g):
    scalp(g, 1224, side_rows=7, back_rows=8, sideburn=1)
    ring_shell(g, 1225, side_rows=7, back_rows=8, ring_row=1)
    curtain(g, "curtain", (0, -6.4, 4.6), (-2, 0, 0), 9, 8, hem=[(0, 9, 1)], seed=1229)
    side_panels(g, "side", 8, 1234, depth=7)
    bangs(g, "fringe", [(-3.0, ((2, 3),), 0), (-1.5, ((2, 2),), 0), (0, ((2, 2),), 0), (1.5, ((2, 2),), 0),
                        (3.0, ((2, 3),), 0)], seed=1239)
    for side, sign in (("right", -1), ("left", 1)):
        bangs(g, f"cheek_{side}", [(3.9 * sign, ((1, 7),), 0)], seed=1244 + (sign > 0))
