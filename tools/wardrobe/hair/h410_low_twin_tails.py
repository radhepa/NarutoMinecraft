"""Low Twin Tails: a middle part, a soft blunt fringe and two tails tied low behind the ears with
cloth bands, hanging down the back past the shoulders."""
from anime import lock
from kit_hyuga import blunt_fringe, crown, hair_tie

META = {"name": "Low Twin Tails", "gender": "female",
        "description": "Middle part, soft fringe, two tails tied low behind the ears with cloth bands."}


def build(g):
    crown(g, 4401, side_rows=7, back_rows=8, sideburn=3, part=3)
    blunt_fringe(g, "fringe", 4405, length=1, xs=(-2.6, -.8, 1.0, 2.8))
    for side, sign in (("right", -1), ("left", 1)):
        pivot, rot = (3.0 * sign, -3.4, 3.9), (4, 0, -3 * sign)
        hair_tie(g, f"tie_{side}", pivot, rot, (3, 1, 3), key="A2")
        lock(g, f"tail_{side}", pivot, rot, ((3, 4), (3, 4), (2, 3), (1, 2)), 2, 4410 + (sign > 0) * 9, ring=None,
             motion="sway", y0=1)
