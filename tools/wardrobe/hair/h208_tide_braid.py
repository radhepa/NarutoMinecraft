"""Tide Braid: a single thick braid from the crown down the back to the waist, tied off in a cloth
wrap with a paper seal tag; a soft parted fringe and long face-framing locks."""
from anime import bangs, braid, cel_box, ring_shell, sidelocks
from kit_uzumaki import wrap_tie
from paint import scalp

META = {"name": "Tide Braid", "gender": "unisex",
        "description": "One thick braid to the waist tied with a seal tag, parted fringe, long face locks."}

PIVOT, TILT = (0, -3.4, 4.7), (8, 0, 0)


def build(g):
    scalp(g, 2120, side_rows=6, back_rows=8, sideburn=4)
    ring_shell(g, 2121, side_rows=6, back_rows=8, ring_row=1)
    gather = g.piece("gather", "HEAD", (-2, -4, -1), (4, 4, 2), pivot=PIVOT, rotation=TILT)
    cel_box(gather, 2122, ring=1)
    end = braid(g, "braid", PIVOT, TILT, links=7, width=3, seed=2123)
    wrap_tie(g, "wrap", PIVOT, TILT, (3, 1, 3), y=end - 2.6, key="A", tag=True)
    bangs(g, "fringe", [(-2.7, ((2, 2), (1, 1)), 18), (-1.2, ((2, 1), (1, 1)), 30), (1.2, ((2, 1), (1, 1)), -30),
                        (2.7, ((2, 2), (1, 1)), -18)], seed=2124)
    sidelocks(g, "frame", 12, seed=2125, x=4.3, z=-3.4, flare=3, width=2)
