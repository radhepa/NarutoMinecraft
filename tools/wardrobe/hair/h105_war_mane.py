"""War Mane: long, untamed hair from the battlefield years, thick locks fanning out over the back
and shoulders to sharp points, a ragged fringe at the brows and heavy locks past the jaw."""
from anime import back_fan, bangs, curtain, ring_shell, sidelocks
from paint import scalp

META = {"name": "War Mane", "gender": "unisex",
        "description": "Long wild hair in thick pointed locks fanning over the back, ragged fringe, heavy side locks."}

LONG = ((3, 5), (3, 4), (2, 3), (1, 2))
MID = ((3, 4), (2, 4), (1, 2))
# (x, segments, splay, tilt out)
FAN = [(-3.4, MID, 20, 12), (-2.0, LONG, 9, 6), (-.6, LONG, 3, 4), (.8, LONG, -4, 5),
       (2.2, LONG, -10, 7), (3.4, MID, -20, 12), (0, MID, 0, 22)]


def build(g):
    scalp(g, 1128, side_rows=7, back_rows=8, sideburn=4)
    ring_shell(g, 1129, side_rows=7, back_rows=8, ring_row=1)
    curtain(g, "curtain", (0, -6.4, 4.6), (-4, 0, 0), 9, 10, seed=1135)
    back_fan(g, "mane", FAN, seed=1133, z=4.9, motion="sway")
    bangs(g, "fringe", [(-2.8, ((2, 2), (1, 1)), 22), (-1.2, ((2, 2), (1, 1)), 6), (.6, ((2, 2), (1, 1)), -14),
                        (2.4, ((2, 2), (1, 1)), -26)], seed=1148)
    sidelocks(g, "frame", 10, seed=1153, x=4.35, z=-3.4, flare=5, width=2)
    sidelocks(g, "flank", 9, seed=1158, x=4.5, z=-.4, flare=9, width=3)
