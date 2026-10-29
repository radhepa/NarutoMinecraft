"""Wave Curtain: long straight hair worn loose to the shoulder blades, the hem cut in a rolling line
of points, temple locks tucked behind the ears and a centre-parted fringe."""
from anime import bangs, curtain, ring_shell, sidelocks
from paint import scalp

META = {"name": "Wave Curtain", "gender": "unisex",
        "description": "Long straight loose hair to the shoulder blades, a rolling hem of points, parted fringe."}


def build(g):
    scalp(g, 20201, side_rows=8, back_rows=8, sideburn=0, part=4)
    ring_shell(g, 20202, side_rows=8, back_rows=8, ring_row=1)
    curtain(g, "curtain", (0, -7.4, 4.7), (8, 0, 0), 9, 13, hem=[(0, 2, 2), (2, 3, 3), (5, 2, 2), (7, 2, 3)], seed=20203)
    sidelocks(g, "side", 9, seed=20210, x=4.4, z=-1.6, flare=3, width=2)
    bangs(g, "fringe", [(-2.9, ((2, 3), (1, 1)), 18), (-1.2, ((2, 2), (1, 1)), 24), (1.2, ((2, 2), (1, 1)), -24),
                        (2.9, ((2, 3), (1, 1)), -18)], seed=20215)
