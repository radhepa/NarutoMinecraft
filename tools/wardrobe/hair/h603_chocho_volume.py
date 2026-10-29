"""Chocho Volume: Chocho's big hair, two spiky ponytails bursting up from bands on top of the head,
the rest left loose in a wide spiky mass down the back, with bangs swept across to her left."""
from anime import back_fan, bangs, curtain, ring_shell, sidelocks, spike, tie
from paint import scalp

META = {"name": "Chocho Volume", "gender": "unisex",
        "description": "Two spiky ponytails bursting up from bands on top, a wide spiky mass down the back."}

# The loose back: (x, segments, splay z, tilt x)
FAN = [(-4.2, ((2, 4), (2, 3), (1, 2)), 30, 20), (4.2, ((2, 4), (2, 3), (1, 2)), -30, 20),
       (-2.6, ((3, 5), (2, 3), (1, 2)), 14, 16), (2.6, ((3, 5), (2, 3), (1, 2)), -14, 16)]


def build(g):
    scalp(g, 6091, side_rows=7, back_rows=8, sideburn=1)
    ring_shell(g, 6092, side_rows=7, back_rows=8, ring_row=1)
    curtain(g, "back", (0, -6.4, 4.7), (-8, 0, 0), 8, 9, hem=((0, 2, 3), (2, 2, 4), (4, 2, 3), (6, 2, 4)), seed=6093,
            depth=2)
    back_fan(g, "fan", FAN, seed=6097, z=4.4, motion="sway")
    # The two ponytails: bands on the crown, spikes bursting up and out of each.
    for side, sign in (("right", -1), ("left", 1)):
        tie(g, f"band_{side}", (2.4 * sign, -8.4, .6), (0, 0, 20 * sign), size=(3, 1, 3), key="A2")
        for i, (rz, rx, segs) in enumerate(((26, -10, ((3, 3), (2, 2), (1, 2))), (54, 0, ((3, 3), (2, 2), (1, 1))),
                                            (34, 30, ((2, 3), (2, 2), (1, 1))))):
            spike(g, f"tail_{side}_{i}", (2.4 * sign, -8.9, .6), (rx, 0, rz * sign), segs, 2, 6111 + i + (sign > 0) * 4)
    bangs(g, "fringe", [(-2.6, ((2, 2), (1, 1)), 26), (-.8, ((2, 2), (1, 1)), 30), (1.0, ((3, 2), (2, 1)), 34),
                        (3.0, ((2, 2), (1, 1)), 10)], seed=6121)
    sidelocks(g, "frame", 8, seed=6127, x=4.4, z=-3.0, flare=8, width=2)
