"""Academy Tuft: a child's soft round cut, a parted fringe that keeps falling forward, short points
over the ears and a stubborn cowlick sticking up at the crown."""
from anime import back_fan, bangs, ring_shell, sidelocks, spike
from paint import scalp

META = {"name": "Academy Tuft", "gender": "unisex",
        "description": "Soft round cut, parted fringe, short points over the ears, a cowlick at the crown."}


def build(g):
    scalp(g, 16640, side_rows=6, back_rows=8, sideburn=1, part=3)
    ring_shell(g, 16641, side_rows=6, back_rows=7, ring_row=1)
    bangs(g, "fringe", [(-2.9, ((2, 3),), 14), (-1.3, ((2, 3),), 8), (0.8, ((2, 3),), -10), (2.6, ((2, 3),), -16)],
          seed=16642)
    sidelocks(g, "frame", 5, seed=16650, x=4.3, z=-3.0, flare=8, width=2)
    back_fan(g, "nape", [(-2.4, ((3, 3), (2, 1)), 12, 8), (0, ((3, 3), (2, 1)), 0, 8), (2.4, ((3, 3), (2, 1)), -12, 8)],
             seed=16655)
    spike(g, "crown_cowlick", (.6, -8.2, 1.2), (-30, 0, -24), ((2, 2), (1, 2)), depth=1, seed=16660)
    spike(g, "crown_cowlick_b", (-.4, -8.2, 1.8), (-44, 0, 20), ((1, 2), (1, 1)), depth=1, seed=16664)
