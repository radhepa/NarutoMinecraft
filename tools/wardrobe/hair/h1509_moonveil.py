"""Moonveil: hair parted in the centre, long straight locks hanging in front of the shoulders to the
chest like a veil drawn back from the face, the rest cut level at the shoulders behind."""
from anime import cel_box, lock, ring_shell
from paint import scalp

META = {"name": "Moonveil", "gender": "unisex",
        "description": "Centre part, long locks hanging before the shoulders to the chest, shoulder-length back."}


def build(g):
    scalp(g, 15230, side_rows=8, back_rows=8, sideburn=0, part=3)
    ring_shell(g, 15231, side_rows=8, back_rows=8, ring_row=1)
    back = g.piece("back", "HEAD", (-4.5, 0, -.5), (9, 10, 1), pivot=(0, -7.6, 4.6), motion="sway")
    cel_box(back, 15232, ring=1)
    for side, sign in (("right", -1), ("left", 1)):
        panel = g.piece(f"side_{side}", "HEAD", (-.5, 0, -1), (1, 9, 6), pivot=(4.6 * sign, -7.6, 0))
        cel_box(panel, 15234 + (sign > 0), ring=1)
        # The veil: a long flat lock from the temple, over the collarbone to the chest.
        lock(g, f"veil_{side}", (4.6 * sign, -7.8, -3.2), (-6, 0, -2 * sign), ((2, 8), (2, 4), (2, 2), (1, 1)), 1,
             15238 + (sign > 0) * 9, motion="sway")
    for i, (x, rz) in enumerate(((-1.6, 30), (1.6, -30))):
        lock(g, f"part_{i}", (x, -8.55, -4.35), (-10, 0, rz), ((2, 2), (1, 1)), 1, 15250 + i, ring=0)
