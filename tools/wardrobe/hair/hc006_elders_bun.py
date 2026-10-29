"""Elder's Bun: thinning hair combed straight back from a high forehead and twisted into a small
tight bun high on the back of the crown, held by a plain wooden pin, with short wisps at the
temples: the grandparent's knot."""
from anime import lock, ring_shell
from kit_household import topknot
from paint import scalp, solid

META = {"name": "Elder's Bun", "gender": "unisex",
        "description": "Thinning hair combed back from a high forehead into a small tight bun on the crown, wooden pin."}


def build(g):
    scalp(g, 37950, side_rows=5, back_rows=7, sideburn=1, shadow=False)
    hat = ring_shell(g, 37951, side_rows=4, back_rows=6, ring_row=1)
    hat.front.hline(0, 7, 0, "H1")
    topknot(g, "bun", (0, -8.6, 2.0), (3, 2, 3), seed=37952)
    pin = g.piece("bun_pin", "HEAD", (-3, -.5, -.5), (6, 1, 1), pivot=(0, -8.6, 2.0), rotation=(0, 20, 8))
    solid(pin, "L", "smooth", 37955, 3, edge=False)
    for side, sign in (("right", -1), ("left", 1)):
        lock(g, f"wisp_{side}", (4.3 * sign, -6.6, -3.2), (0, 0, -6 * sign), ((1, 2), (1, 1)), 1, 37956 + (sign > 0))
