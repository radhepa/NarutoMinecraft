"""Kanzashi Bun: long hair swept back into a low, wide chignon at the nape, pinned through with a
lacquered hairpin whose tassel hangs at one side, with a side-swept fringe and thin face strands."""
from anime import bangs, cel_box, sidelocks
from paint import solid

META = {"name": "Kanzashi Bun", "gender": "female",
        "description": "A low wide chignon pinned with a lacquered kanzashi, side-swept fringe, thin face strands."}


def build(g):
    from kit_hyuga import crown
    crown(g, 4481, side_rows=6, back_rows=8, sideburn=3)
    bun = g.piece("bun", "HEAD", (-2.5, -1.5, 0), (5, 3, 2), pivot=(0, -3.6, 4.2))
    cel_box(bun, 4485, ring=0)
    roll = g.piece("bun_roll", "HEAD", (-1.5, -1, 0), (3, 2, 1), pivot=(0, -3.6, 6.2))
    cel_box(roll, 4487, top_delta=0)
    pin = g.piece("kanzashi", "HEAD", (-4, -.5, -.5), (8, 1, 1), pivot=(0, -4.6, 5.3), rotation=(0, 0, -16))
    solid(pin, "M", "smooth", 4490, 3, edge=False)
    pin.front.set(0, 0, "A3"), pin.back.set(7, 0, "A3")
    for i, (x, length) in enumerate(((3.6, 3), (4.1, 2))):
        tassel = g.piece(f"tassel_{i}", "HEAD", (-.5, 0, -.5), (1, length, 1), pivot=(x, -5.4, 5.3), motion="sway")
        solid(tassel, "A", "weave", 4492 + i, 2)
    bangs(g, "fringe", [(-2.8, ((3, 2), (2, 1), (1, 1)), 30), (-.8, ((3, 1), (2, 1)), 40),
                        (1.4, ((2, 1), (1, 1)), 26), (3.0, ((2, 2), (1, 1)), -14)], seed=4495)
    sidelocks(g, "frame", 7, seed=4499, x=4.3, z=-3.6, flare=2, width=1)
