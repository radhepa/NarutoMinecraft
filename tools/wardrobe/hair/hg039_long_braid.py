"""Long Braid: hair parted to one side, the fringe swept clear of the eyes, and the length plaited
into one long braid down the back, tied off with a cord: a sensor's or an archivist's braid."""
from anime import braid, ring_shell, tie
from kit_kurama import part_line, side_fringe
from paint import scalp

META = {"name": "Long Braid", "gender": "unisex",
        "description": "Side-parted hair, fringe swept clear, one long braid down the back tied with a cord."}


def build(g):
    scalp(g, 34910, side_rows=6, back_rows=8, sideburn=3, part=5)
    ring_shell(g, 34911, side_rows=5, back_rows=8, ring_row=1)
    part_line(g, 5)
    side_fringe(g, "fringe", 34912, side=-1, specs=[(-2.8, ((2, 1),), 52), (-.9, ((3, 1), (2, 1)), 62),
                                                    (1.1, ((2, 1), (1, 1)), 66)])
    tie(g, "braid_tie", (0, -1.6, 4.7), (12, 0, 0), (3, 1, 3), y=0, key="K1")
    braid(g, "braid", (0, -1.0, 4.8), (12, 0, 0), links=7, width=3, seed=34920)
