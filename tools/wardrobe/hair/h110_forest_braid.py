"""Forest Braid: hair drawn back from a centre parting into one thick braid that falls from the nape
to the waist, with short locks left loose in front of the ears."""
from anime import bangs, braid, ring_shell, sidelocks, tie
from paint import scalp

META = {"name": "Forest Braid", "gender": "unisex",
        "description": "Centre parting, hair drawn back into one thick braid to the waist, loose locks at the ears."}

PIVOT, TILT = (0, -2.0, 4.6), (-6, 0, 0)


def build(g):
    scalp(g, 1288, side_rows=5, back_rows=8, sideburn=3, part=3)
    ring_shell(g, 1289, side_rows=5, back_rows=8, ring_row=1)
    bangs(g, "fringe", [(-2.6, ((2, 2), (1, 1)), 24), (2.6, ((2, 2), (1, 1)), -24)], seed=1303)
    sidelocks(g, "frame", 7, seed=1308, x=4.3, z=-3.3, flare=4, width=1)
    tie(g, "braid_tie", PIVOT, TILT, (3, 1, 3), y=-.5)
    end = braid(g, "braid", PIVOT, TILT, links=7, width=3, seed=1313, y0=.5)
    tie(g, "braid_end_tie", PIVOT, TILT, (2, 1, 2), y=end - 2.5, key="A2", motion="sway")
