"""Night Braid: hair combed back under a short side fringe and plaited from the nape into one thick
braid over the shoulder blades, its root bound in dark cord and its tail in a single amber thread."""
from anime import bangs, braid, ring_shell, sidelocks, tie
from paint import scalp

META = {"name": "Night Braid", "gender": "unisex",
        "description": "Short side fringe, one thick braid from the nape, dark cord at the root, amber thread at the tail."}

PIVOT, TILT = (0, -3.0, 4.7), (-4, 0, 0)


def build(g):
    scalp(g, 25180, side_rows=6, back_rows=8, sideburn=3, part=-2)
    ring_shell(g, 25181, side_rows=6, back_rows=8, ring_row=1)
    tie(g, "root_tie", PIVOT, TILT, size=(4, 1, 4), y=-.2, key="K2")
    end = braid(g, "braid", PIVOT, TILT, links=5, width=4, seed=25182, y0=.8)
    tie(g, "tail_tie", PIVOT, TILT, size=(3, 1, 3), y=end - 2.6, key="A2", motion="sway")
    bangs(g, "fringe", [(-2.8, ((3, 2), (2, 1)), -14), (-.6, ((3, 1), (2, 1)), -36), (1.8, ((3, 2), (2, 1)), -26)],
          seed=25190)
    sidelocks(g, "frame", 6, seed=25195, x=4.35, z=-3.2, flare=4, width=1)
