"""Long White Fang: the White Fang's mane worn loose, a spiky silver crown, ragged bangs to the brows,
long locks framing the face and a sheet of hair down the back that breaks into fang-sharp points."""
from anime import bangs, curtain, ring_shell, sidelocks, spike
from paint import scalp

META = {"name": "Long White Fang", "gender": "unisex",
        "description": "Loose silver mane to the shoulder blades in sharp points, a spiky crown and long framing locks."}

MID = ((3, 2), (2, 2), (1, 1))
CROWN = [(-2.4, -2.2, MID, -20, -18), (.2, -2.4, ((3, 3), (2, 2), (1, 2)), -16, 10), (2.6, -2.0, MID, -16, 30),
         (-2.6, .8, MID, 22, -28), (2.6, .8, MID, 22, 30)]


def build(g):
    scalp(g, 12001, side_rows=8, back_rows=8, sideburn=0)
    ring_shell(g, 12002, side_rows=8, back_rows=8, ring_row=1)
    for i, (x, z, segs, rx, rz) in enumerate(CROWN):
        spike(g, f"crown_spike_{i}", (x, -7.6, z), (rx, 0, rz), segs, 3, 12010 + i)
    bangs(g, "fringe", [(-2.7, ((2, 2), (1, 1)), 20), (-.9, ((2, 2), (1, 1)), 8), (.9, ((2, 2), (1, 1)), -8),
                        (2.7, ((2, 2), (1, 1)), -20)], seed=12030)
    sidelocks(g, "frame", 10, seed=12040, x=4.3, z=-3.3, flare=5, width=2)
    sidelocks(g, "sidelock", 9, seed=12045, x=4.5, z=-.2, flare=9, width=3)
    curtain(g, "mane", (0, -6.6, 4.5), (8, 0, 0), 9, 11, hem=((0, 2, 3), (2, 2, 4), (4, 1, 2), (5, 2, 4), (7, 2, 3)),
            seed=12050)
