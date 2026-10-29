"""Crown Bun: an invention for the clan's kunoichi. Hair gathered high into a round bun on the crown,
tied with a cloth band, with short spiky points left loose at the brow and over the ears."""
from anime import bangs, cel_box, ring_shell, sidelocks, spike, tie
from paint import k, scalp

META = {"name": "Crown Bun", "gender": "unisex",
        "description": "A round bun tied high on the crown, short spiky points loose at the brow and ears."}


def build(g):
    scalp(g, 9771, side_rows=5, back_rows=8, sideburn=2)
    hat = ring_shell(g, 9772, side_rows=5, back_rows=8, ring_row=1)
    for x in (2, 5):
        hat.top.vline(x, 0, 7, k("H", 1))
    bangs(g, "fringe", [(-2.6, ((2, 2), (1, 1)), 22), (-.6, ((2, 1), (1, 1)), 6), (1.4, ((2, 2), (1, 1)), -14),
                        (3.0, ((1, 2),), -22)], seed=9780)
    sidelocks(g, "frame", 5, seed=9785, x=4.3, z=-3.0, flare=10, width=2)
    pivot = (0, -7.8, 1.6)
    tie(g, "bun_tie", pivot, (-10, 0, 0), (4, 1, 4), y=-1.0, key="A2")
    bun = g.piece("bun", "HEAD", (-2, -4.0, -2), (4, 3, 4), pivot=pivot, rotation=(-10, 0, 0))
    cel_box(bun, 9790, top_delta=1)
    for i, (rx, rz) in enumerate(((-20, -40), (-20, 40), (-60, 0))):
        spike(g, f"bun_tuft_{i}", (0, -11.4, 1.2), (rx, 0, rz), ((2, 2), (1, 1)), 1, 9795 + i)
