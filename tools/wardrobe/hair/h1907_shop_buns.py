"""Shop Buns: two round buns pinned high on either side of the crown for a busy day behind the
counter, a short blunt fringe cut above the brows and loose wisps at the temples."""
from anime import bangs, cel_box, lock, ring_shell
from paint import scalp

META = {"name": "Shop Buns", "gender": "unisex",
        "description": "Two round buns high on the crown, a short blunt fringe, loose wisps at the temples."}


def build(g):
    scalp(g, 19181, side_rows=5, back_rows=7, sideburn=2)
    ring_shell(g, 19182, side_rows=5, back_rows=6, ring_row=1)
    bangs(g, "fringe", [(-2.8, ((2, 2),), 6), (-1.0, ((2, 2),), 2), (1.0, ((2, 2),), -2), (2.8, ((2, 2),), -6)], seed=19185)
    for side, sign in (("right", -1), ("left", 1)):
        bun = g.piece(f"bun_{side}", "HEAD", (-1.5, -3, -1.5), (3, 3, 3), pivot=(2.3 * sign, -8.3, .9), rotation=(0, 0, 12 * sign))
        cel_box(bun, 19195 + (sign > 0), base=2, ring=0)
        wrap = g.piece(f"bun_{side}_base", "HEAD", (-2, -.5, -2), (4, 1, 4), pivot=(2.3 * sign, -8.3, .9), rotation=(0, 0, 12 * sign))
        cel_box(wrap, 19197 + (sign > 0), base=1, top_delta=0)
        lock(g, f"wisp_{side}", (4.3 * sign, -7.4, -3.2), (0, 0, -6 * sign), ((1, 4), (1, 1)), 1, 19199 + (sign > 0))
