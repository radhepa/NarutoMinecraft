"""Scruff Tails: shaggy shoulder-length hair caught into two low tails behind the ears with leather
ties, their ends left bristling, a choppy fringe and short wild spikes on the crown."""
from anime import bangs, lock, ring_shell, sidelocks, tie
from kit_inuzuka import burst
from paint import scalp

META = {"name": "Scruff Tails", "gender": "unisex",
        "description": "Two low bristling tails behind the ears, a choppy fringe, short wild crown spikes."}

TOP = ((3, 2), (2, 1), (1, 1))
CROWN = [(-2.0, -1.8, TOP, 10, -30), (.4, -2.2, TOP, 14, 6), (2.4, -1.6, TOP, 8, 30), (0, 1.4, TOP, -36, 0)]


def build(g):
    scalp(g, 8420, side_rows=6, back_rows=8, sideburn=3, part=4)
    ring_shell(g, 8421, side_rows=6, back_rows=8, ring_row=1)
    burst(g, "crown_tuft", CROWN, 8423)
    for i, (x, rz) in enumerate(((-3.2, 6), (3.2, -6))):
        pivot = (x, -2.6, 3.8)
        tie(g, f"tie_{i}", pivot, (18, 0, rz), size=(3, 1, 3), key="L2")
        lock(g, f"tail_{i}", pivot, (18, 0, rz), ((3, 3), (3, 3), (2, 2), (1, 2)), 3, 8427 + i, ring=None, motion="sway",
             y0=1)
        for j, dx in enumerate((-.6, .6)):
            lock(g, f"tail_{i}_bristle_{j}", (x + dx, -2.6, 3.8), (18, 0, rz), ((1, 2),), 2, 8429 + i + j, ring=None,
                 motion="sway", y0=10)
    bangs(g, "fringe", [(-2.8, ((2, 3), (1, 1)), 20), (-1.0, ((2, 2), (1, 1)), 10), (.8, ((2, 2), (1, 1)), -8),
                        (2.7, ((2, 3), (1, 1)), -20)], seed=8433)
    sidelocks(g, "frame", 8, seed=8437, x=4.35, z=-3.4, flare=4, width=2)
