"""Windblown: a scruffy mid-length cut that the wind has pushed hard to one side, every spike
leaning the same way, the fringe swept across the brow and the far side flaring out."""
from anime import bangs, lock, ring_shell, sidelocks
from kit_inuzuka import burst
from paint import scalp

META = {"name": "Windblown", "gender": "unisex",
        "description": "Scruffy hair pushed hard to one side, every spike leaning the same way."}

MID = ((3, 3), (2, 2), (1, 1))
CROWN = [(-2.6, -2.2, MID, 10, 40), (-.2, -2.4, MID, 12, 46), (2.4, -2.0, ((3, 3), (2, 2), (2, 1), (1, 1)), 6, 64),
         (-2.0, .8, MID, -28, 44), (.6, 1.0, MID, -24, 54), (3.0, .6, ((3, 3), (2, 2), (1, 2)), -16, 76),
         (-.8, 3.0, MID, -60, 36), (1.8, 3.0, MID, -56, 50)]


def build(g):
    scalp(g, 8330, side_rows=5, back_rows=8, sideburn=2, part=2)
    ring_shell(g, 8331, side_rows=5, back_rows=7, ring_row=1)
    burst(g, "crown_spike", CROWN, 8333)
    bangs(g, "fringe", [(-2.8, ((3, 2), (2, 1)), -36), (-.8, ((3, 2), (2, 1), (1, 1)), -40),
                        (1.4, ((2, 2), (1, 1)), -44), (3.0, ((2, 3), (1, 1)), -30)], seed=8350)
    sidelocks(g, "sidelock", 6, seed=8355, x=4.4, z=-2.4, flare=10, width=2)
    for i, (x, rz) in enumerate(((-2.0, -30), (0, -40), (2.0, -50))):
        lock(g, f"nape_{i}", (x, -3.6, 4.3), (40, 0, rz), ((2, 2), (1, 2)), 1, 8357 + i)
