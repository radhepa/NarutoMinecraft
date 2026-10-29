"""Branch Crop: a branch-house guard's practical cut, close at the sides and nape with the top
combed straight back in short flat locks, so nothing hides the forehead or the cursed seal."""
from anime import lock
from kit_hyuga import crown

META = {"name": "Branch Crop", "gender": "unisex",
        "description": "Close sides and nape, short flat locks combed straight back, forehead clear."}

TOP = [(-2.6, 0, 4), (0, 0, 0), (2.6, 0, -4)]


def build(g):
    crown(g, 4241, side_rows=4, back_rows=7, sideburn=2)
    for i, (x, rx, rz) in enumerate(TOP):
        lock(g, f"comb_{i}", (x, -8.9, -3.6), (86, 0, rz), ((3, 4), (3, 2)), 1, 4245 + i, ring=0)
    for i, x in enumerate((-2.5, 0, 2.5)):
        lock(g, f"nape_{i}", (x, -3.0, 4.6), (8, 0, -x * 4), ((3, 2), (1, 1)), 1, 4255 + i, ring=None)
