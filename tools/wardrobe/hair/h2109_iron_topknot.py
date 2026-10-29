"""Iron Topknot: hair dragged up from every side into a knot on the crown, bound in rust cord,
its ends bursting out of the tie in a fist of spikes; short bristles at the temples."""
from anime import bangs, lock, ring_shell, tie
from kit_hagane import crown
from paint import scalp

META = {"name": "Iron Topknot", "gender": "unisex",
        "description": "A knot on the crown bound in rust cord, its ends bursting out in a fist of spikes."}

BURST = ((2, 2), (1, 2))
SPIKES = [(0, .4, BURST, rx, rz) for rx, rz in ((0, -40), (0, 40), (24, 0), (-24, 0), (14, -20), (-14, 20), (0, 0))]


def build(g):
    scalp(g, 21490, side_rows=4, back_rows=7, sideburn=2)
    ring_shell(g, 21491, side_rows=4, back_rows=7, ring_row=1)
    lock(g, "knot", (0, -8.2, .4), (180, 0, 0), ((3, 2),), 3, 21492)
    tie(g, "cord", (0, -10.2, .4), (0, 0, 0), size=(3, 1, 3), key="A2")
    crown(g, "burst", SPIKES, 21494, y=-10.6)
    bangs(g, "fringe", [(-2.6, ((2, 2), (1, 1)), 22), (2.6, ((2, 2), (1, 1)), -22)], seed=21520)
