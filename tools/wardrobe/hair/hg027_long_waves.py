"""Long Waves: thick waves loose to the middle of the back, each length rippling as it falls, a deep
side part with the fringe swept toward the right, and wavy locks framing the face."""
from anime import bangs, cel_box, ring_shell
from kit_kunoichi import wave_lock
from paint import scalp

META = {"name": "Long Waves", "gender": "unisex",
        "description": "Thick waves to mid-back, a deep side part, a swept fringe, wavy framing locks."}

BACK = [(-3.2, 0, ((3, 3), (3, 3), (3, 3), (2, 2), (1, 1))), (-1.1, 1, ((3, 3), (3, 3), (3, 4), (2, 2), (1, 1))),
        (1.1, 0, ((3, 3), (3, 3), (3, 3), (2, 2), (1, 1))), (3.2, 1, ((3, 3), (3, 4), (3, 3), (2, 2), (1, 1)))]


def build(g):
    scalp(g, 33910, side_rows=7, back_rows=8, sideburn=2, part=2)
    ring_shell(g, 33911, side_rows=7, back_rows=8, ring_row=1)
    for i, (x, phase, segs) in enumerate(BACK):
        wave_lock(g, f"wave_{i}", (x, -6.4, 4.4), (-6, 0, -x * 2), segs, 2, 33912 + i * 3, phase=phase)
    for side, sign in (("right", -1), ("left", 1)):
        panel = g.piece(f"side_{side}", "HEAD", (-.5, 0, -2.5), (1, 8, 6), pivot=(4.6 * sign, -7.2, .8))
        cel_box(panel, 33925 + (sign > 0), ring=1)
        wave_lock(g, f"frame_{side}", (4.4 * sign, -7.5, -3.2), (0, 0, -3 * sign), ((2, 4), (2, 3), (2, 3), (1, 1)), 1,
                  33927 + (sign > 0), amp=.3, phase=sign > 0, motion="none")
    bangs(g, "fringe", [(-2.8, ((2, 2), (1, 1)), 34), (-1.0, ((3, 2), (2, 2)), 54), (1.0, ((3, 2), (2, 2), (1, 1)), 60),
                        (2.9, ((2, 2), (1, 1)), 40)], seed=33930)
