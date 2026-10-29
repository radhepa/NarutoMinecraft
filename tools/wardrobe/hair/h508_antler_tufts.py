"""Antler Tufts: for the deer keepers of the Nara forest. Two stiff tufts tied up at either side of
the crown and sweeping back, each forking into points like a young buck's antlers."""
from anime import bangs, spike, tie
from kit_nara import pulled_back

META = {"name": "Antler Tufts", "gender": "unisex",
        "description": "Two tufts tied high at the sides of the crown, sweeping back and forking like antlers."}


def build(g):
    pulled_back(g, 5401, side_rows=4, back_rows=7, sideburn=2)
    for side, sign in (("right", -1), ("left", 1)):
        pivot = (2.6 * sign, -7.8, .6)
        tie(g, f"{side}_tie", pivot, (-40, 0, 20 * sign), (2, 1, 2))
        # The beam sweeps back and out, then tines fork off it.
        spike(g, f"{side}_beam", pivot, (-52, 0, 26 * sign), ((2, 3), (2, 3), (1, 2)), 2, 5410 + (sign > 0) * 20)
        spike(g, f"{side}_brow_tine", pivot, (-14, 0, 22 * sign), ((2, 2), (1, 2)), 2, 5420 + (sign > 0) * 20)
        spike(g, f"{side}_tine", (2.9 * sign, -11.2, 3.6), (-24, 0, 34 * sign), ((1, 2), (1, 1)), 1, 5425 + (sign > 0) * 20)
    bangs(g, "fringe", [(-2.8, ((2, 2), (1, 1)), 20), (0, ((2, 1),), 0), (2.8, ((2, 2), (1, 1)), -20)], seed=5460)
