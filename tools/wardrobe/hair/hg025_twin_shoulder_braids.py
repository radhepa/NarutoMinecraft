"""Twin Shoulder Braids: hair parted in the middle and plaited into two braids from behind the ears
that fall forward over the shoulders, tied off with cloth, a light parted fringe."""
from anime import bangs, braid, cel_box, ring_shell, tie
from paint import scalp

META = {"name": "Twin Shoulder Braids", "gender": "unisex",
        "description": "Two braids from behind the ears over the shoulders, cloth ties, a parted fringe."}


def build(g):
    scalp(g, 33870, side_rows=7, back_rows=8, sideburn=2, part=3)
    ring_shell(g, 33871, side_rows=7, back_rows=8, ring_row=1)
    for side, sign in (("right", -1), ("left", 1)):
        pivot, tilt = (4.1 * sign, -3.4, -.4), (-28, 0, -4 * sign)
        gather = g.piece(f"gather_{side}", "HEAD", (-1.5, -2, -1.5), (3, 3, 3), pivot=pivot, rotation=tilt)
        cel_box(gather, 33872 + (sign > 0), ring=1)
        end = braid(g, f"braid_{side}", pivot, tilt, links=4, width=3, seed=33874 + (sign > 0) * 9, y0=1)
        tie(g, f"tie_{side}", pivot, tilt, (3, 1, 3), y=end - 2.5, key="A2", motion="sway")
    bangs(g, "fringe", [(-2.7, ((2, 2), (1, 1)), 24), (-1.0, ((2, 1), (1, 1)), 36), (1.0, ((2, 1), (1, 1)), -36),
                        (2.7, ((2, 2), (1, 1)), -24)], seed=33893)
