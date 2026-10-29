"""Young Scarecrow: Kakashi as a boy, a smaller rounder shock of spikes leaning to the wearer's left,
a fuller fringe of points to the brows and short tufts over the ears."""
from anime import bangs, lock, ring_shell, sidelocks, spike
from paint import scalp

META = {"name": "Young Scarecrow", "gender": "unisex",
        "description": "A short round shock of spikes leaning to one side, a full pointed fringe, tufts over the ears."}

MID = ((3, 2), (2, 2), (1, 1))
SMALL = ((3, 2), (2, 1), (1, 1))
CROWN = [(-2.6, -2.4, MID, -24, 20), (0, -2.8, ((4, 2), (3, 2), (2, 1), (1, 1)), -22, 30), (2.6, -2.2, MID, -18, 52),
         (-2.8, .6, MID, 8, 18), (0, .6, ((4, 2), (3, 2), (2, 1), (1, 1)), 10, 32), (2.8, .8, SMALL, 10, 60),
         (-1.4, 3.0, SMALL, 40, 24), (1.4, 3.0, SMALL, 40, 44)]


def build(g):
    scalp(g, 11201, side_rows=5, back_rows=8, sideburn=1)
    ring_shell(g, 11202, side_rows=5, back_rows=7, ring_row=1)
    for i, (x, z, segs, rx, rz) in enumerate(CROWN):
        spike(g, f"crown_spike_{i}", (x, -7.6, z), (rx, 0, rz), segs, 3, 11210 + i)
    bangs(g, "fringe", [(-2.8, ((2, 2), (1, 1)), 24), (-1.2, ((2, 2), (1, 1)), 16), (.6, ((2, 2), (1, 1)), 12),
                        (2.4, ((2, 1), (1, 1)), 4)], seed=11230)
    sidelocks(g, "tuft", 4, seed=11240, x=4.4, z=-2.0, flare=18, width=2)
    for i, (x, rz, rx) in enumerate(((-2.4, 22, 36), (0, 0, 44), (2.4, -22, 36))):
        lock(g, f"nape_{i}", (x, -3.4, 4.3), (rx, 0, rz), ((2, 1), (1, 2)), 1, 11250 + i * 5)
