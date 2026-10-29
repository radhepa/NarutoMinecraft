"""Headband-Swept: hair pushed straight up and back off the forehead the way a tight headband leaves
it, a wall of spikes rising from the hairline and the rest falling back to the nape in layered points."""
from anime import back_fan, lock, ring_shell, spike
from paint import scalp

META = {"name": "Headband-Swept", "gender": "unisex",
        "description": "Hair pushed up and back off the forehead into a wall of spikes, layered points down to the nape."}

WALL = [(-3.0, ((3, 3), (2, 2), (1, 2)), -22, -18), (-1.5, ((3, 4), (2, 3), (1, 2)), -30, -8),
        (0, ((4, 4), (3, 3), (2, 2), (1, 1)), -34, 0), (1.5, ((3, 4), (2, 3), (1, 2)), -30, 8),
        (3.0, ((3, 3), (2, 2), (1, 2)), -22, 18)]
NAPE = [(-2.8, ((3, 3), (2, 2), (1, 2)), 22, 26), (-1.0, ((3, 4), (2, 2), (1, 2)), 8, 30),
        (1.0, ((3, 4), (2, 2), (1, 2)), -8, 30), (2.8, ((3, 3), (2, 2), (1, 2)), -22, 26)]


def build(g):
    scalp(g, 35720, side_rows=5, back_rows=8, sideburn=2, shadow=False)
    ring_shell(g, 35721, side_rows=5, back_rows=7, ring_row=1)
    for i, (x, segs, rx, rz) in enumerate(WALL):
        spike(g, f"wall_{i}", (x, -7.6, -2.6), (rx, 0, rz), segs, 2, 35722 + i * 2)
    for i, (x, z, rx) in enumerate(((-2.0, .6, -52), (2.0, .6, -52), (0, 1.6, -60))):
        spike(g, f"swept_{i}", (x, -7.8, z), (rx, 0, -x * 5), ((3, 3), (2, 2), (1, 1)), 2, 35733 + i)
    back_fan(g, "nape", NAPE, seed=35736)
    for i, (x, rz) in enumerate(((-4.3, 34), (4.3, -34))):
        lock(g, f"side_point_{i}", (x, -6.0, 1.4), (24, 0, rz), ((2, 2), (1, 2)), 2, 35738 + i)
