"""Festival Updo: hair swept up all round into a high rounded knot with two soft loops at the back
like folded wings, a short side-swept fringe that stops at the brows and two curled tendrils left
by the ears, done up for the summer festival and New Year visits."""
from anime import bangs, cel_box, lock, ring_shell
from kit_household import topknot
from paint import scalp

META = {"name": "Festival Updo", "gender": "female",
        "description": "High rounded knot with two folded loops at the back, a short side-swept fringe, curled tendrils."}


def build(g):
    scalp(g, 37970, side_rows=6, back_rows=8, sideburn=2)
    ring_shell(g, 37971, side_rows=5, back_rows=8, ring_row=1)
    topknot(g, "knot", (0, -9.0, .8), (4, 3, 4), seed=37972)
    for side, sign in (("right", -1), ("left", 1)):
        loop = g.piece(f"loop_{side}", "HEAD", (-1.5, -1.5, -1), (3, 3, 2), pivot=(2.2 * sign, -6.6, 4.6),
                       rotation=(0, 0, 20 * sign))
        cel_box(loop, 37975 + (sign > 0), ring=0)
        lock(g, f"tendril_{side}", (4.3 * sign, -6.4, -3.2), (0, 0, -4 * sign), ((1, 3), (1, 1)), 1, 37977 + (sign > 0))
    bangs(g, "fringe", [(-2.6, ((2, 2), (1, 1)), 22), (-.8, ((3, 1), (2, 1)), 34), (1.4, ((2, 1),), 30)], seed=37980)
