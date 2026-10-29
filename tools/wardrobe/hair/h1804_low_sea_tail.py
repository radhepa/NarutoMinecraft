"""Low Sea Tail: hair parted in the middle and pulled back loosely to a low tail at the nape that
falls straight to the shoulder blades, the fringe parted into two points at the brows and a long lock
left in front of each ear."""
from anime import bangs, sidelocks, tie
from kit_umino import combed_up, falling_tail

META = {"name": "Low Sea Tail", "gender": "unisex",
        "description": "Centre-parted and tied in a low tail at the nape, two fringe points and long side locks."}


def build(g):
    combed_up(g, 18061, side_rows=6, back_rows=8, sideburn=1, streaks=False)
    g.part("head").top.vline(3, 0, 7, "H0")
    bangs(g, "fringe", [(-2.2, ((3, 2), (2, 1)), 26), (2.2, ((3, 2), (2, 1)), -26)], seed=18063)
    sidelocks(g, "side", 8, seed=18065, x=4.35, z=-2.9, flare=3, width=2)
    tie(g, "tie", (0, -2.6, 4.5), size=(3, 1, 2))
    falling_tail(g, "tail", (0, -2.2, 4.7), ((3, 3), (3, 3), (2, 2), (1, 2)), rx=8, seed=18067, depth=2)
