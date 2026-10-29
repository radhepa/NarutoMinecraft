"""Tousled Shag: Hayate's hair without the bandana, after a sleepless week: layered and uneven,
tufts standing up on the crown, ragged locks over the ears and the nape to the collar."""
from anime import back_fan, bangs, ring_shell, sidelocks, spike
from paint import scalp

META = {"name": "Tousled Shag", "gender": "unisex",
        "description": "Messy layered hair, crown tufts, ragged locks over the ears, nape to the collar."}

TUFT = ((3, 2), (2, 1), (1, 1))
CROWN = [(-1.8, -1.2, TUFT, -14, -22), (1.6, .4, TUFT, 8, 24)]


def build(g):
    scalp(g, 15170, side_rows=6, back_rows=8, sideburn=3)
    ring_shell(g, 15171, side_rows=6, back_rows=8, ring_row=1)
    for i, (x, z, segs, rx, rz) in enumerate(CROWN):
        spike(g, f"crown_tuft_{i}", (x, -7.8, z), (rx, 0, rz), segs, 3, 15175 + i)
    bangs(g, "fringe", [(-3.0, ((2, 3), (1, 1)), 22), (-1.2, ((2, 2), (1, 1)), -6), (0.8, ((2, 2),), 14),
                        (2.6, ((2, 3), (1, 1)), -22)], seed=15180)
    sidelocks(g, "ear", 6, seed=15190, x=4.4, z=-1.4, flare=6, width=2)
    back_fan(g, "nape", [(-3.0, ((3, 3), (2, 1), (1, 1)), 22, 14), (-.8, ((2, 4), (1, 1)), 6, 8),
                         (1.2, ((3, 3), (1, 2)), -10, 10), (3.1, ((2, 3), (1, 1)), -24, 16)], seed=15195)
