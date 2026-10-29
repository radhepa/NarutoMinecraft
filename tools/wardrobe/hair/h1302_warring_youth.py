"""Warring Youth: Danzo as a boy of the Warring States and a young jonin under the Second Hokage:
the same tousled dark hair grown longer, a heavy ragged fringe to the brows, locks over the ears to
the jaw and a shaggy fall to the collar at the back."""
from anime import back_fan, bangs, ring_shell, sidelocks, spike
from paint import scalp

META = {"name": "Warring Youth", "gender": "unisex",
        "description": "Longer tousled dark hair, a heavy ragged fringe, jaw-length locks, a shaggy fall to the collar."}

TUFT = ((3, 1), (2, 1), (1, 1))
CROWN = [(-2.4, -1.4, -36, -40), (0, -1.8, -42, 0), (2.4, -1.4, -36, 40), (0, 1.8, 44, 0)]


def build(g):
    scalp(g, 13033, side_rows=6, back_rows=8, sideburn=3)
    ring_shell(g, 13034, side_rows=6, back_rows=8, ring_row=1)
    for i, (x, z, rx, rz) in enumerate(CROWN):
        spike(g, f"crown_tuft_{i}", (x, -7.9, z), (rx, 0, rz), TUFT, 3, 13039 + i)
    bangs(g, "fringe", [(-2.9, ((2, 3), (1, 1)), 12), (-1.2, ((2, 2), (1, 1)), 20), (.6, ((2, 2), (1, 1)), -14),
                        (2.6, ((2, 2), (1, 1)), -16)], seed=13045)
    sidelocks(g, "frame", 8, seed=13051, x=4.35, z=-3.2, flare=5, width=2)
    sidelocks(g, "ear", 6, seed=13054, x=4.5, z=-.6, flare=9, width=2)
    back_fan(g, "fall", [(-3.0, ((3, 4), (2, 2), (1, 1)), 12, 6), (-1.0, ((3, 5), (2, 2), (1, 1)), 4, 4),
                         (1.0, ((3, 5), (2, 2), (1, 1)), -4, 4), (3.0, ((3, 4), (2, 2), (1, 1)), -12, 6)],
             seed=13057, z=4.3)
