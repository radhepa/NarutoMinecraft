"""Little Brother: Izuna's spiky black hair, a short shock of spikes on the crown, a long jagged
fringe parted to the sides, and a spiky tail tied at the nape falling to the shoulder blades."""
from anime import bangs, lock, ring_shell, sidelocks, spike, tie
from paint import scalp

META = {"name": "Little Brother", "gender": "unisex",
        "description": "A spiky crown, jagged side-parted fringe and a spiky tail tied at the nape."}

CROWN = [(-2.4, -1.6, -10, -30), (0, -1.8, -6, 0), (2.4, -1.6, -10, 30), (-1.6, 1.2, 20, -26), (1.6, 1.2, 20, 26)]


def build(g):
    scalp(g, 3321, side_rows=5, back_rows=8, sideburn=3)
    ring_shell(g, 3322, side_rows=5, back_rows=8, ring_row=1)
    for i, (x, z, rx, rz) in enumerate(CROWN):
        spike(g, f"crown_spike_{i}", (x, -7.8, z), (rx, 0, rz), ((3, 2), (2, 2), (1, 1)), 2, 3330 + i)
    bangs(g, "fringe", [(-2.6, ((2, 2), (1, 1)), 28), (-.9, ((2, 2), (1, 1)), 14), (.9, ((2, 2), (1, 1)), -14),
                        (2.6, ((2, 2), (1, 1)), -28)], seed=3340)
    sidelocks(g, "frame", 9, seed=3345, x=4.35, z=-3.4, flare=8, width=2)
    tie(g, "tie", (0, -1.6, 4.6), size=(3, 1, 2))
    for i, (x, rz, segs) in enumerate(((-.7, 8, ((2, 4), (1, 3))), (.7, -8, ((2, 4), (1, 3))),
                                      (0, 0, ((3, 4), (2, 4), (1, 3))))):
        lock(g, f"tail_{i}", (x, -1.0, 4.9), (10, 0, rz), segs, 2, 3350 + i * 4, ring=None, motion="sway")
