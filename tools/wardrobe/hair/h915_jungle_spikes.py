"""Jungle Spikes: an invention, a wild-grown Sarutobi mane. Long spiky hair falling past the nape
in jagged points, spikes kicked up over the crown and a messy fringe, untamed like the forest."""
from anime import back_fan, bangs, ring_shell, sidelocks, spike
from paint import scalp

META = {"name": "Jungle Spikes", "gender": "unisex",
        "description": "Long jagged spikes falling past the nape, spikes kicked up over the crown, messy fringe."}

CROWN = [(-2.2, -8.0, -1.0, ((3, 3), (2, 2), (1, 1)), -24, -26), (2.2, -8.0, -1.0, ((3, 3), (2, 2), (1, 1)), -24, 26),
         (0.0, -8.0, .6, ((3, 3), (2, 2), (1, 1)), -40, 0), (-3.4, -7.0, 1.2, ((3, 2), (2, 2), (1, 1)), -40, -56),
         (3.4, -7.0, 1.2, ((3, 2), (2, 2), (1, 1)), -40, 56)]


def build(g):
    scalp(g, 9811, side_rows=7, back_rows=8, sideburn=1)
    ring_shell(g, 9812, side_rows=7, back_rows=8, ring_row=1)
    for i, (x, y, z, segs, rx, rz) in enumerate(CROWN):
        spike(g, f"crown_{i}", (x, y, z), (rx, 0, rz), segs, 2, 9820 + i * 3)
    bangs(g, "fringe", [(-2.8, ((2, 2), (1, 2)), 26), (-1.0, ((2, 2), (1, 1)), 12), (1.2, ((2, 2), (1, 1)), -16),
                        (2.8, ((2, 2), (1, 2)), -28)], seed=9840)
    sidelocks(g, "frame", 8, seed=9850, x=4.4, z=-2.8, flare=16, width=2)
    back_fan(g, "back", [(-3.2, ((3, 5), (2, 2), (1, 2)), 34, 20), (-1.2, ((3, 6), (2, 3), (1, 2)), 12, 24),
                         (1.2, ((3, 6), (2, 3), (1, 2)), -12, 24), (3.2, ((3, 5), (2, 2), (1, 2)), -34, 20)],
             seed=9860, motion="sway")
