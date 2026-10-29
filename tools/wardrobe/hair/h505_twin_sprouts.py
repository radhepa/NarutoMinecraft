"""Twin Sprouts: two small spiky pineapple tails tied high on either side of the crown, a short
centre-parted fringe that stops at the brows."""
from anime import bangs
from kit_nara import pineapple, pulled_back

META = {"name": "Twin Sprouts", "gender": "unisex",
        "description": "Two small spiky pineapple tails high on either side of the crown, a short parted fringe."}


def spikes(sign):
    s = ((3, 2), (2, 2), (1, 1))
    return [(s, -22, 14 * sign), (s, -48, 4 * sign), (s, -10, 42 * sign), (s, -34, 46 * sign), (((2, 2), (1, 1)), -4, -6 * sign)]


def build(g):
    pulled_back(g, 5201, side_rows=4, back_rows=7, sideburn=2)
    pineapple(g, "right_tail", (-2.4, -7.6, 1.8), spikes(-1), seed=5210)
    pineapple(g, "left_tail", (2.4, -7.6, 1.8), spikes(1), seed=5230)
    bangs(g, "fringe", [(-2.7, ((2, 2), (1, 1)), 22), (-1.0, ((2, 2),), 14), (1.0, ((2, 2),), -14),
                        (2.7, ((2, 2), (1, 1)), -22)], seed=5250)
