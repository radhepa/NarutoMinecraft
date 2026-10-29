"""Crossed Pin Bun: long hair coiled into a low round bun at the nape and held by two steel pins
crossed like drawn blades, with soft side-parted bangs and short locks before the ears."""
from anime import bangs, cel_box, ring_shell, sidelocks
from paint import scalp, solid

META = {"name": "Crossed Pin Bun", "gender": "unisex",
        "description": "Low coiled bun at the nape pinned with two crossed steel pins, side-parted bangs."}


def build(g):
    scalp(g, 15380, side_rows=6, back_rows=8, sideburn=3, part=2)
    ring_shell(g, 15381, side_rows=6, back_rows=8, ring_row=1)
    bun = g.piece("bun", "HEAD", (-2.5, -2, 0), (5, 4, 3), pivot=(0, -3.0, 4.2))
    cel_box(bun, 15382, ring=1)
    coil = g.piece("bun_coil", "HEAD", (-1.5, -1.5, 0), (3, 3, 1), pivot=(0, -3.0, 7.0))
    cel_box(coil, 15383, base=3, top_delta=0)
    coil.back.set(1, 1, "H1")
    for i, rz in enumerate((40, -40)):
        pin = g.piece(f"pin_{i}", "HEAD", (-.5, -4, -.5), (1, 8, 1), pivot=(0, -3.0, 6.4), rotation=(0, 0, rz))
        solid(pin, "M", "plain", 15384 + i, 3, edge=False)
        pin.top.fill("M4"), pin.bottom.fill("M1")
    bangs(g, "fringe", [(-2.8, ((3, 2), (2, 1), (1, 1)), 22), (-.8, ((3, 1), (2, 1)), 36), (1.6, ((2, 1),), -24),
                        (3.0, ((2, 2), (1, 1)), -14)], seed=15390)
    sidelocks(g, "frame", 6, seed=15395, x=4.3, z=-3.2, flare=4, width=2)
