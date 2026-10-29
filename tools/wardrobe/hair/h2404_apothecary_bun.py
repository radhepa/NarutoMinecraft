"""Apothecary Bun: everything swept back off the face and twisted into a low bun at the nape, out of
the way of the mortar and the fumes, held by two lacquered pins, with a short side-swept fringe and
one loose strand at the right temple."""
from anime import bangs, cel_box, lock, ring_shell
from paint import k, scalp, solid

META = {"name": "Apothecary Bun", "gender": "unisex",
        "description": "Low bun at the nape held with two pins, short side-swept fringe, one loose temple strand."}


def build(g):
    scalp(g, 24071, side_rows=4, back_rows=8, sideburn=2)
    ring_shell(g, 24072, side_rows=4, back_rows=7, ring_row=1)
    bun = g.piece("bun", "HEAD", (-2.5, -2, -1.5), (5, 4, 3), pivot=(0, -2.8, 5.6))
    cel_box(bun, 24075, ring=1, clump=2)
    twist = g.piece("bun_twist", "HEAD", (-1.5, -1.5, -1), (3, 3, 1), pivot=(0, -2.8, 7.4))
    cel_box(twist, 24076, top_delta=0)
    for f in twist.sides:
        f.set(1, 1, k("H", 0))
    for i, (x, rz) in enumerate(((-1.4, -64), (1.6, -52))):
        pin = g.piece(f"pin_{i}", "HEAD", (-.5, -4, -.5), (1, 8, 1), pivot=(x, -2.6, 6.0), rotation=(0, 0, rz),
                      scale=(.5, .5, .5))
        solid(pin, "K", "smooth", 24077 + i, 2, edge=False)
        pin.top.fill("A3")
    bangs(g, "fringe", [(-2.6, ((2, 2), (1, 1)), 40), (-.6, ((3, 2), (1, 1)), 46), (1.6, ((2, 2), (1, 1)), 40)],
          seed=24080)
    lock(g, "strand", (-4.4, -7.4, -3.2), (0, 0, 6), ((1, 6), (1, 2)), 1, 24085)
