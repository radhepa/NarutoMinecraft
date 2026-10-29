"""Guard Pixie: Mirai grown up, the Hokage's bodyguard. A short pixie cut, the fringe swept to one
side across the brow, ears half covered and the nape cut close in short points."""
from anime import back_fan, bangs, ring_shell, sidelocks, spike
from paint import scalp

META = {"name": "Guard Pixie", "gender": "unisex",
        "description": "A short pixie with a fringe swept to one side and the nape cut close in points."}


def build(g):
    scalp(g, 9661, side_rows=6, back_rows=8, sideburn=1)
    ring_shell(g, 9662, side_rows=6, back_rows=8, ring_row=1)
    bangs(g, "fringe", [(-3.0, ((2, 3), (1, 1)), 34), (-1.4, ((2, 2), (1, 1)), 40), (0.4, ((2, 2), (1, 1)), 46),
                        (2.4, ((2, 2), (1, 1)), 30)], seed=9670)
    sidelocks(g, "frame", 6, seed=9680, x=4.3, z=-3.0, flare=5, width=2)
    back_fan(g, "back", [(-2.6, ((3, 3), (1, 1)), 12, 8), (0.0, ((3, 4), (1, 1)), 0, 8), (2.6, ((3, 3), (1, 1)), -12, 8)],
             seed=9690)
    spike(g, "crown_0", (-.8, -8.0, 1.2), (-40, 0, -10), ((3, 2), (2, 1), (1, 1)), 2, 9695)
