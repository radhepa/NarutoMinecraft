"""Long Braid: hair parted in the middle with short swept bangs at the temples, the length drawn back
into one tight three-strand braid that hangs from the nape to below the shoulder blades."""
from anime import braid, sidelocks
from kit_hyuga import crown, hair_tie, parted_fringe

META = {"name": "Long Braid", "gender": "unisex",
        "description": "Middle part, swept temple bangs, one tight braid from the nape down the back."}


def build(g):
    crown(g, 4281, side_rows=6, back_rows=8, sideburn=3, part=3)
    parted_fringe(g, "fringe", 4285, reach=1)
    sidelocks(g, "frame", 6, seed=4290, x=4.3, z=-3.5, flare=2, width=1)
    pivot, rot = (0, -2.6, 4.6), (-3, 0, 0)
    hair_tie(g, "braid_tie_top", pivot, rot, (3, 1, 3), key="D2")
    braid(g, "braid", pivot, rot, links=7, width=3, seed=4295, y0=1)
    hair_tie(g, "braid_tie_end", pivot, rot, (2, 1, 2), key="D2", motion="sway", y=13)
