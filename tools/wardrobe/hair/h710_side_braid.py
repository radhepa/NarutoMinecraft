"""Side Braid: hair drawn smoothly over the right ear into one long braid that rests forward on the
shoulder, finished with a blossom tie, a side-swept fringe and a short framing lock on the left."""
from anime import bangs, braid, cel_box, lock, ring_shell, tie
from kit_yamanaka import flower
from paint import scalp

META = {"name": "Side Braid", "gender": "unisex",
        "description": "One long braid over the right shoulder with a blossom tie, side-swept fringe."}

PIVOT, TILT = (-4.4, -3.4, -1.4), (-14, 0, -8)


def build(g):
    scalp(g, 7901, side_rows=6, back_rows=8, sideburn=2, part=5)
    ring_shell(g, 7902, side_rows=6, back_rows=8, ring_row=1)
    gather = g.piece("gather", "HEAD", (-1.5, -2, -1.5), (3, 3, 3), pivot=PIVOT, rotation=TILT)
    cel_box(gather, 7910, ring=1)
    end = braid(g, "braid", PIVOT, TILT, links=5, width=3, seed=7920, y0=1)
    tie(g, "tie", PIVOT, TILT, (3, 1, 3), y=end - 2.5, key="A2")
    flower(g, "bloom", PIVOT, rotation=TILT, at=(0, end - 2, -1.6))
    bangs(g, "fringe", [(-2.8, ((2, 2), (1, 1)), 30), (-1.0, ((3, 2), (2, 1)), 46), (1.0, ((3, 2), (1, 1)), 50),
                        (2.8, ((2, 2), (1, 1)), 28)], seed=7930)
    lock(g, "frame_left", (4.5, -7.6, -3.3), (0, 0, -3), ((2, 5), (1, 2)), 1, 7940)
