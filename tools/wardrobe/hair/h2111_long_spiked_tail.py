"""Long Spiked Tail: a crown of short back-swept spikes over long hair tied low at the nape in a
rust cord, the tail hanging to the shoulder blades and ending in ragged points."""
from anime import bangs, lock, ring_shell, sidelocks, tie
from kit_hagane import crown
from paint import scalp

META = {"name": "Long Spiked Tail", "gender": "unisex",
        "description": "Short back-swept crown spikes, a long low tail in a rust cord ending in ragged points."}

MID = ((3, 2), (2, 2), (1, 1))
SPIKES = [(-2.4, -2.6, MID, -24, -26), (0, -3.0, MID, -30, 0), (2.4, -2.6, MID, -24, 26),
          (-1.2, -.2, MID, -50, -10), (1.2, -.2, MID, -50, 10)]


def build(g):
    scalp(g, 21590, side_rows=6, back_rows=8, sideburn=2)
    ring_shell(g, 21591, side_rows=6, back_rows=8, ring_row=1)
    crown(g, "spike", SPIKES, 21592)
    pivot = (0, -2.4, 4.0)
    tie(g, "cord", pivot, (12, 0, 0), size=(3, 1, 3), key="A2")
    lock(g, "tail", pivot, (12, 0, 0), ((3, 5), (3, 3), (2, 2), (1, 2)), 2, 21610, ring=None, motion="sway", y0=1)
    for i, dx in enumerate((-1.0, 1.0)):
        lock(g, f"tail_point_{i}", (dx, -2.4, 4.0), (12, 0, -dx * 14), ((1, 2),), 1, 21615 + i, ring=None,
             motion="sway", y0=10)
    bangs(g, "fringe", [(-2.8, ((2, 2), (1, 1)), 22), (-.8, ((2, 2), (1, 1)), 8), (1.2, ((2, 2), (1, 1)), -10),
                        (2.9, ((2, 2), (1, 1)), -22)], seed=21620)
    sidelocks(g, "frame", 7, seed=21630, x=4.35, z=-3.2, flare=6, width=2)
