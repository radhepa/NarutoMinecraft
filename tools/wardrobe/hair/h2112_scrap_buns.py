"""Scrap Buns: two tight buns high on the head wound with rust cord, their loose ends sticking
out in short spikes, a jagged fringe and a few stray spikes at the nape."""
from anime import bangs, lock, ring_shell, tie
from kit_hagane import crown
from paint import scalp

META = {"name": "Scrap Buns", "gender": "unisex",
        "description": "Two high buns wound in rust cord with spiky loose ends, a jagged fringe."}

STUB = ((2, 2), (1, 1))


def build(g):
    scalp(g, 21640, side_rows=5, back_rows=7, sideburn=2)
    ring_shell(g, 21641, side_rows=5, back_rows=7, ring_row=1)
    for i, (x, rz) in enumerate(((-2.6, -24), (2.6, 24))):
        lock(g, f"bun_{i}", (x, -7.6, 1.0), (180, 0, rz), ((4, 3),), 4, 21642 + i)
        tie(g, f"cord_{i}", (x, -7.6, 1.0), (180, 0, rz), size=(3, 1, 3), key="A2", y=3)
        sx = x + (-1.6 if x < 0 else 1.6)
        crown(g, f"bun_{i}_spike", [(sx, 1.0, STUB, 0, rz * 2.4), (sx, 2.0, STUB, -40, rz * 1.4),
                                    (x * 1.15, -.4, STUB, 30, rz * 1.6)], 21650 + i * 10, depth=1, y=-10.2)
    bangs(g, "fringe", [(-2.7, ((2, 2), (1, 1)), 22), (-.9, ((2, 2), (1, 1)), 8), (.9, ((2, 2), (1, 1)), -8),
                        (2.7, ((2, 2), (1, 1)), -22)], seed=21680)
    for i, (x, rz) in enumerate(((-2.4, 26), (0, 0), (2.4, -26))):
        lock(g, f"nape_{i}", (x, -3.0, 4.3), (40, 0, rz), ((2, 2), (1, 1)), 1, 21690 + i * 5)
