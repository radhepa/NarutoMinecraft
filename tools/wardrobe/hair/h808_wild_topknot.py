"""Wild Topknot: shaggy sides and back, the top gathered into a knot on the crown with a red cord
and left to burst into a spray of spikes, rough bangs at the brows."""
from anime import back_fan, bangs, ring_shell, sidelocks, tie
from kit_inuzuka import burst
from paint import scalp

META = {"name": "Wild Topknot", "gender": "unisex",
        "description": "Shaggy sides, a topknot tied with red cord bursting into a spray of spikes."}

SPRAY = ((2, 3), (2, 2), (1, 1))
KNOT = [(-.8, .2, SPRAY, -8, -40), (.8, .2, SPRAY, -8, 40), (0, -.6, SPRAY, 26, 0), (0, 1.0, SPRAY, -40, 0),
        (-.6, .6, ((2, 3), (1, 2), (1, 1)), -26, -14), (.6, .6, ((2, 3), (1, 2), (1, 1)), -26, 14)]


def build(g):
    scalp(g, 8211, side_rows=6, back_rows=8, sideburn=3)
    ring_shell(g, 8212, side_rows=6, back_rows=8, ring_row=1)
    tie(g, "crown_cord", (0, -8.0, .4), size=(3, 2, 3), y=-1.4, key="A2")
    burst(g, "crown_spray", KNOT, 8213, y=-10.0)
    back_fan(g, "nape", [(-3.0, ((2, 3), (1, 2)), 22, 20), (-1.0, ((3, 4), (2, 2), (1, 1)), 6, 14),
                         (1.0, ((3, 4), (2, 2), (1, 1)), -6, 14), (3.0, ((2, 3), (1, 2)), -22, 20)], seed=8219)
    bangs(g, "fringe", [(-2.6, ((2, 3), (1, 1)), 18), (-.8, ((2, 2), (1, 1)), 8), (1.0, ((2, 2), (1, 1)), -10),
                        (2.7, ((2, 3), (1, 1)), -20)], seed=8222)
    sidelocks(g, "sidelock", 6, seed=8226, x=4.4, z=-2.4, flare=14, width=2)
