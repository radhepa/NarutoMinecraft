"""Wolf Tail: a short spiky crop with one long thin tail grown from the nape, bound in three red
cords down its length: an old tracker's habit, so the tail never snags in brush."""
from anime import bangs, lock, ring_shell, sidelocks, tie
from kit_inuzuka import burst
from paint import scalp

META = {"name": "Wolf Tail", "gender": "unisex",
        "description": "A short spiky crop with one long thin nape tail bound in red cords."}

TUFT = ((3, 2), (2, 2), (1, 1))
CROWN = [(-2.4, -2.4, TUFT, 16, -30), (0, -2.8, TUFT, 22, 4), (2.4, -2.2, TUFT, 12, 32), (-2.4, .8, TUFT, -24, -40),
         (0, .6, TUFT, -20, 0), (2.4, .8, TUFT, -24, 40), (0, 2.8, TUFT, -56, 0)]
TAIL = dict(pivot=(0, -2.6, 4.4), rotation=(8, 0, 0), motion="sway")


def build(g):
    scalp(g, 8390, side_rows=4, back_rows=7, sideburn=2)
    ring_shell(g, 8391, side_rows=4, back_rows=6, ring_row=1)
    burst(g, "crown_spike", CROWN, 8393)
    lock(g, "nape_tail", TAIL["pivot"], TAIL["rotation"], ((2, 4), (2, 4), (2, 4), (1, 2)), 2, 8402, ring=None,
         motion="sway")
    for i, y in enumerate((.6, 4.6, 8.6)):
        tie(g, f"nape_cord_{i}", TAIL["pivot"], TAIL["rotation"], size=(3, 1, 3), y=y - .5, key="A2", motion="sway")
    bangs(g, "fringe", [(-2.6, ((2, 2), (1, 1)), 22), (-.6, ((2, 2), (1, 1)), 6), (1.4, ((2, 2), (1, 1)), -14),
                        (2.9, ((2, 2), (1, 1)), -26)], seed=8406)
    sidelocks(g, "sidelock", 5, seed=8410, x=4.4, z=-2.4, flare=16, width=2)
