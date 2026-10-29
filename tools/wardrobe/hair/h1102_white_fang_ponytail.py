"""White Fang Ponytail: Sakumo's long silver hair, a crown of spikes standing up and back, ragged bangs
falling over the forehead protector to the brows, long spiky locks framing the face and the length
gathered at the nape into a thick spiky tail down to the middle of the back."""
from anime import bangs, lock, ring_shell, sidelocks, spike, tie
from paint import scalp

META = {"name": "White Fang Ponytail", "gender": "unisex",
        "description": "Spiky crown, ragged bangs, long framing locks and a thick spiky ponytail to mid-back."}

MID = ((3, 3), (2, 2), (1, 2))
# (x, z, segments, rx, rz): spikes standing up and tipping back, the front ones a little forward.
CROWN = [(-2.4, -2.2, MID, -18, -22), (.2, -2.6, ((4, 3), (3, 2), (2, 2), (1, 1)), -14, 6), (2.6, -2.0, MID, -16, 30),
         (-2.8, .8, MID, 18, -34), (0, .8, MID, 22, 0), (2.8, .8, MID, 18, 34)]
# The tail: (x, rz, segments) locks fanned from the tie, the middle one longest.
TAIL = [(-.9, 10, ((3, 4), (3, 4), (2, 3), (1, 2))), (.9, -10, ((3, 4), (3, 4), (2, 3), (1, 2))),
        (0, 0, ((3, 5), (3, 4), (2, 4), (1, 3))), (-1.4, 22, ((2, 4), (2, 3), (1, 2))), (1.4, -22, ((2, 4), (2, 3), (1, 2)))]


def build(g):
    scalp(g, 11101, side_rows=6, back_rows=8, sideburn=3)
    ring_shell(g, 11102, side_rows=6, back_rows=8, ring_row=1)
    for i, (x, z, segs, rx, rz) in enumerate(CROWN):
        spike(g, f"crown_spike_{i}", (x, -7.6, z), (rx, 0, rz), segs, 3, 11110 + i)
    bangs(g, "fringe", [(-2.7, ((2, 2), (1, 1)), 20), (-1.0, ((2, 2), (1, 1)), 8), (.8, ((2, 2), (1, 1)), -8),
                        (2.6, ((2, 2), (1, 1)), -20)], seed=11130)
    sidelocks(g, "frame", 8, seed=11140, x=4.35, z=-3.4, flare=8, width=2)
    sidelocks(g, "sidelock", 6, seed=11145, x=4.45, z=-.8, flare=14, width=2)
    tie(g, "tie", (0, -4.4, 4.3), (12, 0, 0), size=(4, 2, 2))
    for i, (x, rz, segs) in enumerate(TAIL):
        lock(g, f"ponytail_{i}", (x, -4.2, 5.0), (12, 0, rz), segs, 2, 11150 + i * 7, ring=None, motion="sway")
