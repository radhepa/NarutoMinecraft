"""Scarecrow Spikes: Kakashi's silver hair that defies gravity, a tall shock of thick spikes standing
up and slanting to the wearer's left, a few ragged points over the brow and spiky locks over the ears."""
from anime import bangs, lock, ring_shell, sidelocks, spike
from paint import scalp

META = {"name": "Scarecrow Spikes", "gender": "unisex",
        "description": "Tall silver spikes standing up and slanting to one side, ragged brow points, spiky sides."}

TALL = ((4, 3), (3, 3), (2, 3), (1, 2))
BIG = ((4, 3), (3, 2), (2, 2), (1, 2))
MID = ((3, 2), (2, 2), (1, 2))
# (x, z, segments, rx, rz): thick spikes all leaning to the wearer's left (+x), the back row tipping back.
CROWN = [(-2.4, -2.4, BIG, -16, 26), (.2, -2.6, TALL, -14, 34), (2.8, -2.0, MID, -10, 52),
         (-2.6, .4, TALL, 2, 24), (.2, .6, TALL, 4, 32), (2.8, .8, BIG, 6, 46),
         (-1.4, 3.0, BIG, 30, 30), (1.6, 3.0, MID, 32, 44)]


def build(g):
    scalp(g, 11001, side_rows=5, back_rows=8, sideburn=2)
    ring_shell(g, 11002, side_rows=5, back_rows=7, ring_row=1)
    for i, (x, z, segs, rx, rz) in enumerate(CROWN):
        spike(g, f"crown_spike_{i}", (x, -7.6, z), (rx, 0, rz), segs, 3, 11010 + i)
    bangs(g, "fringe", [(-2.6, ((2, 2), (1, 1)), 22), (-.6, ((2, 2), (1, 1)), 18), (1.6, ((2, 1), (1, 1)), 10)],
          seed=11030)
    sidelocks(g, "sidelock", 5, seed=11040, x=4.4, z=-2.4, flare=14, width=2)
    for i, (x, rz, rx) in enumerate(((-3.0, 26, 32), (-1.0, 8, 40), (1.0, -8, 40), (3.0, -26, 32))):
        lock(g, f"nape_{i}", (x, -3.6, 4.3), (rx, 0, rz), ((2, 2), (1, 2)), 1, 11050 + i * 5)
