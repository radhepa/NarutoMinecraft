"""Side Braid: straight hair parted in the middle and gathered behind the left ear into one long
braid laid forward over the shoulder, a short loose fall left over the right ear."""
from anime import bangs, braid, ring_shell, sidelocks, tie
from paint import scalp

META = {"name": "Side Braid", "gender": "unisex",
        "description": "Parted in the middle, gathered into one braid over the left shoulder, a loose right lock."}


def build(g):
    scalp(g, 16720, side_rows=6, back_rows=8, sideburn=1, part=3)
    ring_shell(g, 16721, side_rows=6, back_rows=8, ring_row=1)
    bangs(g, "fringe", [(-2.9, ((2, 3), (1, 1)), 18), (-1.3, ((2, 2),), 26), (1.3, ((2, 2),), -26),
                        (2.9, ((2, 3), (1, 1)), -18)], seed=16722)
    sidelocks(g, "frame", 6, seed=16730, x=4.3, z=-3.0, flare=4, width=2)
    tie(g, "braid_tie", (4.6, -3.0, -1.0), (-24, 0, -4), size=(3, 1, 3), y=0, key="D2")
    braid(g, "braid", (4.6, -3.0, -1.0), (-24, 0, -4), links=6, width=3, seed=16740, y0=1)
