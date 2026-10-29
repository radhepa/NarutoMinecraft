"""Swept Tail: hair swept straight back off the forehead and tied in a short, tidy tail at the nape
that stops above the collar: a patrol leader's or courier's practical cut."""
from anime import lock, tie
from kit_nara import pulled_back

META = {"name": "Swept Tail", "gender": "unisex",
        "description": "Hair swept back off the forehead into a short tidy tail at the nape."}


def build(g):
    pulled_back(g, 34890, side_rows=5, back_rows=8, sideburn=2)
    for i, x in enumerate((-2.0, 0, 2.0)):
        lock(g, f"swept_{i}", (x, -8.55, -3.2), (94, 0, 0), ((2, 4), (2, 3)), 1, 34892 + i * 3, ring=0)
    tie(g, "nape_tie", (0, -2.2, 4.6), (10, 0, 0), (3, 1, 2), y=0, key="K1")
    lock(g, "tail", (0, -1.8, 4.7), (14, 0, 0), ((3, 3), (2, 2), (1, 1)), 2, 34897, ring=None, motion="sway")
