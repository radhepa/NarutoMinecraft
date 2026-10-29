"""Half-Up Bun: the top half of long hair twisted into a small bun at the back of the crown, the
rest left loose to the shoulder blades, a centre-parted fringe drawn back off the forehead."""
from anime import cel_box, curtain, lock, ring_shell, sidelocks
from paint import scalp

META = {"name": "Half-Up Bun", "gender": "unisex",
        "description": "Small bun at the back of the crown, the rest loose to the shoulder blades, open forehead."}


def build(g):
    scalp(g, 19421, side_rows=7, back_rows=8, sideburn=1, part=3)
    ring_shell(g, 19422, side_rows=7, back_rows=8, ring_row=1)
    for i, (x, rz) in enumerate(((-2.7, 44), (2.7, -44))):
        lock(g, f"brow_{i}", (x, -8.55, -4.35), (-10, 0, rz), ((2, 2), (1, 1)), 1, 19425 + i * 7, ring=0)
    sidelocks(g, "frame", 7, seed=19435, x=4.35, flare=3, width=1)
    bun = g.piece("bun", "HEAD", (-1.5, -1.5, -1), (3, 3, 3), pivot=(0, -7.0, 5.4))
    cel_box(bun, 19440, base=2, ring=0)
    curtain(g, "back", (0, -6.0, 4.45), (5, 0, 0), 8, 9, hem=((0, 2, 2), (2, 2, 3), (4, 2, 3), (6, 2, 2)), seed=19445)
