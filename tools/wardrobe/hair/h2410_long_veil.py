"""Long Veil: straight hair to the waist, parted in the centre and hanging in one smooth sheet down
the back, long locks in front of the shoulders and a short split fringe that keeps the brows clear."""
from anime import bangs, curtain, ring_shell, sidelocks
from paint import scalp

META = {"name": "Long Veil", "gender": "unisex",
        "description": "Waist-length straight hair, centre part, long front locks, a short split fringe."}


def build(g):
    scalp(g, 24261, side_rows=8, back_rows=8, sideburn=0, part=3)
    ring_shell(g, 24262, side_rows=7, back_rows=8, ring_row=1)
    curtain(g, "veil", (0, -7.8, 4.6), (4, 0, 0), 10, 14, hem=((0, 3, 2), (3, 4, 3), (7, 3, 2)), seed=24265)
    sidelocks(g, "front", 10, seed=24270, flare=2, x=4.4)
    bangs(g, "fringe", [(-2.6, ((2, 2), (1, 1)), 30), (-1.0, ((2, 2),), 24), (1.0, ((2, 2),), -24),
                        (2.6, ((2, 2), (1, 1)), -30)], seed=24275)
