"""Ribbon Long: long straight hair worn loose to the shoulder blades, held off the forehead by a
cloth ribbon tied as a headband with a bow above the left temple, like the ribbon Sakura wore as a
girl."""
from anime import curtain, lock, ring_shell, sidelocks
from paint import k, scalp, solid

META = {"name": "Ribbon Long", "gender": "unisex",
        "description": "Long loose hair, a cloth ribbon headband with a bow at the left temple, open forehead."}


def build(g):
    scalp(g, 19151, side_rows=7, back_rows=8, sideburn=1, part=4)
    ring_shell(g, 19152, side_rows=7, back_rows=8, ring_row=2)
    for i, (x, rz) in enumerate(((-3.0, 20), (-1.6, 42), (1.6, -42), (3.0, -20))):
        lock(g, f"fringe_{i}", (x, -8.55, -4.35), (-10, 0, rz), ((2, 1), (1, 1)), 1, 19155 + i * 7, ring=0)
    sidelocks(g, "front", 8, seed=19165, x=4.35, flare=4, width=2)
    curtain(g, "back", (0, -7.2, 4.45), (5, 0, 0), 8, 10, hem=((0, 3, 2), (3, 2, 3), (5, 3, 2)), seed=19170)
    band = g.piece("ribbon", "HEAD", (-4, -7.4, -4), (8, 1, 8), inflate=.68)
    solid(band, "A", "smooth", 19175, 2, edge=False)
    for face in band.sides:
        face.hline(0, face.w - 1, 0, "A3")
    for i, rz in enumerate((-35, 35)):
        loop = g.piece(f"bow_{i}", "HEAD", (-1.5 + 1.5 * i, -1, -.5), (2, 2, 1), pivot=(2.6, -7.6, -4.75), rotation=(0, 0, rz))
        solid(loop, "A", "smooth", 19176 + i, 2, edge=False)
        loop.front.set(1 - i, 0, k("A", 3))
    knot = g.piece("bow_knot", "HEAD", (-.5, -.5, -.5), (1, 1, 1), pivot=(2.6, -7.6, -5.0))
    solid(knot, "A", "smooth", 19178, 3, edge=False)
