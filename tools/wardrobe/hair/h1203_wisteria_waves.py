"""Wisteria Waves: long, soft light-brown waves loose down the back, parted at the side with the
fringe swept over the brow. Each length ripples on its own, like the hanging sprays of wisteria the
clan paints; two wavy locks frame the face to the collarbone."""
from anime import cel_box, ring_shell
from kit_kurama import part_line, side_fringe, wave_lock
from paint import scalp

META = {"name": "Wisteria Waves", "gender": "unisex",
        "description": "Long loose waves down the back, a side part and a swept fringe, wavy face-framing locks."}

# Waves down the back: (x, phase, segments).
BACK = [(-3.3, 0, ((3, 4), (3, 3), (3, 3), (2, 2), (1, 1))), (-1.1, 1, ((3, 4), (3, 3), (3, 4), (2, 2), (1, 1))),
        (1.1, 0, ((3, 4), (3, 3), (3, 4), (2, 2), (1, 1))), (3.3, 1, ((3, 4), (3, 3), (3, 3), (2, 2), (1, 1)))]


def build(g):
    scalp(g, 12080, side_rows=7, back_rows=8, sideburn=1, part=5)
    ring_shell(g, 12081, side_rows=7, back_rows=8, ring_row=1)
    part_line(g, 5)
    for i, (x, phase, segs) in enumerate(BACK):
        wave_lock(g, f"wave_{i}", (x, -6.6, 4.5), (-6, 0, -x * 1.5), segs, 2, 12084 + i * 9, phase=phase, motion="sway")
    for side, sign in (("right", -1), ("left", 1)):
        panel = g.piece(f"side_{side}", "HEAD", (-.5, 0, -3), (1, 8, 7), pivot=(4.6 * sign, -7.2, .8))
        cel_box(panel, 12100 + (sign > 0), ring=1)
        wave_lock(g, f"frame_{side}", (4.35 * sign, -7.5, -3.0), (0, 0, -3 * sign), ((2, 5), (2, 3), (2, 2), (1, 1)), 2,
                  12104 + (sign > 0) * 7, amp=.3, phase=sign > 0)
    side_fringe(g, "fringe", 12112, side=-1)
