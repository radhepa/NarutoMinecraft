"""Stubby Ponytail: hair scraped back into a short stubby ponytail at the back of the crown that sticks
straight out like a brush, with loose short strands escaping over the brow and at the temples."""
from anime import bangs, lock, ring_shell, sidelocks, spike, tie
from paint import scalp

META = {"name": "Stubby Ponytail", "gender": "unisex",
        "description": "Short brush-like ponytail sticking out at the back of the crown, loose strands at the brow."}


def build(g):
    scalp(g, 31940, side_rows=5, back_rows=8, sideburn=2)
    hat = ring_shell(g, 31941, side_rows=4, back_rows=7, ring_row=1)
    for x in (1, 3, 5, 7):
        hat.back.vline(x, 1, 5, "H1")
    bangs(g, "fringe", [(-2.4, ((2, 2), (1, 1)), 22), (1.0, ((2, 1), (1, 1)), -14), (2.8, ((1, 2), (1, 1)), -24)],
          seed=31942)
    sidelocks(g, "temple", 4, seed=31945, x=4.3, z=-3.0, flare=8, width=1)
    pivot = (0, -6.4, 4.4)
    tie(g, "tie", pivot, (-70, 0, 0), (3, 1, 3), y=-.6)
    for i, (rx, rz) in enumerate(((-96, 0), (-80, 16), (-82, -16), (-108, 10), (-104, -12))):
        spike(g, f"tail_{i}", pivot, (rx, 0, rz), ((3, 2), (2, 2), (1, 1)) if i == 0 else ((2, 2), (2, 1), (1, 1)), 2,
              31948 + i * 2)
    lock(g, "nape_wisp", (-1.6, -3.0, 4.2), (24, 0, 14), ((1, 2),), 1, 31958)
