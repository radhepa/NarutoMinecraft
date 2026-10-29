"""Shoulder Braid: hair gathered behind the left ear into one thick braid that falls forward over the
shoulder, tied off with a scrap of indigo cloth, and a long side-swept fringe kept off the eyes."""
from anime import bangs, braid, cel_box, ring_shell, tie
from paint import scalp

META = {"name": "Shoulder Braid", "gender": "unisex",
        "description": "One thick braid behind the left ear falling forward over the shoulder, an indigo tie."}

PIVOT, TILT = (4.4, -3.2, 1.0), (-22, 0, 10)


def build(g):
    scalp(g, 22181, side_rows=6, back_rows=8, sideburn=2, part=2)
    ring_shell(g, 22182, side_rows=6, back_rows=8, ring_row=1)
    gather = g.piece("gather", "HEAD", (-1.5, -2, -1.5), (3, 3, 3), pivot=PIVOT, rotation=TILT)
    cel_box(gather, 22183, ring=1)
    end = braid(g, "braid", PIVOT, TILT, links=5, width=3, seed=22184, y0=1)
    tie(g, "tie", PIVOT, TILT, (3, 1, 3), y=end - 2.5, key="D2", motion="sway")
    bangs(g, "fringe", [(-2.8, ((2, 2), (1, 1)), -30), (-1.0, ((3, 2), (2, 1)), -50), (1.0, ((3, 2), (1, 1)), -48),
                        (2.8, ((2, 2), (1, 1)), -24)], seed=22190)
