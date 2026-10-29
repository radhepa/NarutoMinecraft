"""Twin Currents: hair parted down the back and tied in two low tails behind the ears that fall
over the shoulders and curl outward at the ends, a short straight fringe."""
from anime import bangs, ring_shell, tie
from kit_namiashi import wave_lock
from paint import scalp

META = {"name": "Twin Currents", "gender": "unisex",
        "description": "Two low tails tied behind the ears, falling to the shoulders and curling outward."}


def build(g):
    scalp(g, 20291, side_rows=6, back_rows=8, sideburn=2)
    hat = ring_shell(g, 20292, side_rows=6, back_rows=8, ring_row=1)
    hat.back.vline(4, 0, 7, "H0")
    for side, sign in (("right", -1), ("left", 1)):
        pivot = (3.9 * sign, -3.4, 3.2)
        tie(g, f"tie_{side}", pivot, (20, 0, -10 * sign), size=(2, 1, 2), y=-.5, key="K2")
        wave_lock(g, f"tail_{side}", pivot, (20, 0, 4 * sign), [(((2, 4), (2, 2)), 0, 0), (((2, 2),), 0, -22 * sign),
                                                                  (((1, 2),), 0, -26 * sign)],
                  depth=2, seed=20295 + 20 * (sign > 0), motion="sway")
    bangs(g, "fringe", [(-2.8, ((2, 2), (1, 1)), 6), (-1.0, ((2, 2), (1, 1)), 2), (1.0, ((2, 2), (1, 1)), -2),
                        (2.8, ((2, 2), (1, 1)), -6)], seed=20340)
