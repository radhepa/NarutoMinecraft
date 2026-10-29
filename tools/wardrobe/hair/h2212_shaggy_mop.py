"""Shaggy Mop: a thick shaggy mop grown out between haircuts, ragged locks over the ears and down to
the collar at the back, the fringe pushed aside in uneven points that stop at the brows."""
from anime import back_fan, bangs, ring_shell, sidelocks, spike
from paint import scalp

META = {"name": "Shaggy Mop", "gender": "unisex",
        "description": "Thick grown-out shag, ragged locks over the ears and to the collar, uneven fringe."}


def build(g):
    scalp(g, 22221, side_rows=7, back_rows=8, sideburn=2)
    ring_shell(g, 22222, side_rows=6, back_rows=8, ring_row=1)
    for i, (x, z, rx, rz) in enumerate(((-2.4, -1.8, -14, -30), (.6, -2.2, -16, 18), (-.8, 1.0, 12, -10),
                                        (2.4, 1.4, 14, 30))):
        spike(g, f"crown_{i}", (x, -7.8, z), (rx, 0, rz), ((3, 2), (2, 1), (1, 1)), 2, 22224 + i)
    back_fan(g, "nape", [(-3.0, ((3, 4), (2, 2), (1, 1)), 18, 12), (-1.0, ((3, 5), (2, 2), (1, 1)), 6, 14),
                         (1.0, ((3, 5), (2, 2), (1, 1)), -8, 14), (3.0, ((3, 4), (2, 2), (1, 1)), -20, 12)], seed=22230)
    sidelocks(g, "ear", 6, seed=22236, x=4.4, z=-1.4, flare=16, width=3)
    bangs(g, "fringe", [(-2.8, ((2, 2), (1, 1)), 34), (-1.0, ((2, 2), (1, 1)), 44), (1.0, ((2, 1), (1, 1)), 30),
                        (2.8, ((2, 2), (1, 1)), -16)], seed=22240)
