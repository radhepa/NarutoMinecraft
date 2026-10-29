"""Web Braid: hair drawn smoothly back from a middle part and plaited into one long braid down the
spine, the end bound with thread."""
from anime import braid, ring_shell, sidelocks, tie
from paint import scalp

META = {"name": "Web Braid", "gender": "unisex",
        "description": "Middle-parted hair drawn back into one long braid down the spine, thread-bound at the end."}

PIVOT, TILT = (0, -3.0, 4.6), (12, 0, 0)


def build(g):
    scalp(g, 23121, side_rows=6, back_rows=8, sideburn=2, part=3)
    ring_shell(g, 23122, side_rows=5, back_rows=8, ring_row=1)
    tie(g, "braid_root", PIVOT, TILT, size=(3, 1, 3), y=-.6, key="A2", motion="sway")
    end = braid(g, "braid", PIVOT, TILT, links=6, width=3, seed=23125, y0=.4)
    tie(g, "braid_end_tie", PIVOT, TILT, (2, 1, 2), y=end - 2.5, key="A2", motion="sway")
    sidelocks(g, "frame", 5, seed=23130, x=4.35, z=-3.0, flare=3, width=1)
