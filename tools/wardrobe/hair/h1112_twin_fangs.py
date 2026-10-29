"""Twin Fangs: slanting silver spikes on the crown and the back hair split into two spiky tails tied
low behind the ears, each falling over the shoulder blades like a pair of fangs."""
from anime import bangs, lock, ring_shell, sidelocks, spike, tie
from paint import scalp

META = {"name": "Twin Fangs", "gender": "unisex",
        "description": "Slanting crown spikes, a pointed fringe and two spiky tails tied low behind the ears."}

MID = ((3, 2), (2, 2), (1, 1))
CROWN = [(-2.2, -2.2, MID, -16, 26), (.4, -2.4, ((3, 3), (2, 2), (1, 1)), -12, 36), (2.6, -1.8, MID, -8, 52),
         (-1.6, .8, MID, 18, 30), (1.4, 1.0, MID, 20, 44)]


def build(g):
    scalp(g, 12101, side_rows=6, back_rows=8, sideburn=2)
    ring_shell(g, 12102, side_rows=6, back_rows=7, ring_row=1)
    for i, (x, z, segs, rx, rz) in enumerate(CROWN):
        spike(g, f"crown_spike_{i}", (x, -7.6, z), (rx, 0, rz), segs, 3, 12110 + i)
    bangs(g, "fringe", [(-2.6, ((2, 2), (1, 1)), 22), (-.8, ((2, 2), (1, 1)), 14), (1.0, ((2, 2), (1, 1)), 4),
                        (2.7, ((2, 2), (1, 1)), -12)], seed=12130)
    sidelocks(g, "frame", 7, seed=12140, x=4.3, z=-3.4, flare=6, width=1)
    for side, sign in (("right", -1), ("left", 1)):
        pivot = (3.0 * sign, -4.0, 3.6)
        tie(g, f"tie_{side}", pivot, (16, 0, -10 * sign), size=(2, 1, 2))
        lock(g, f"tail_{side}", pivot, (16, 0, -10 * sign), ((3, 3), (2, 3), (2, 2), (1, 2)), 2, 12150 + (sign > 0) * 9,
             ring=None, y0=1.0, motion="sway")
