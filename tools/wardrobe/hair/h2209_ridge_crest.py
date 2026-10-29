"""Ridge Crest: a ridge of spikes standing up along the middle of the head from brow to crown,
like the ridge beam of a roof, the sides swept back flat and close to the head."""
from anime import ring_shell, spike
from paint import k, scalp

META = {"name": "Ridge Crest", "gender": "unisex",
        "description": "A ridge of spikes standing up along the middle from brow to crown, flat swept sides."}


def build(g):
    scalp(g, 22161, side_rows=4, back_rows=7, sideburn=2)
    hat = ring_shell(g, 22162, side_rows=4, back_rows=7, ring_row=1)
    for x in (0, 1, 6, 7):
        hat.top.vline(x, 0, 7, k("H", 1 if x in (0, 7) else 3))
    for i, (z, rx) in enumerate(((-3.0, -64), (-1.5, -32), (0, 0), (1.5, 32), (3.0, 64))):
        spike(g, f"ridge_{i}", (0, -7.8, z), (rx, 0, 0), ((2, 3), (1, 2)), 2, 22164 + i * 3)
    for side, sign in (("right", -1), ("left", 1)):
        for i, z in enumerate((-1.6, 1.6)):
            spike(g, f"swept_{side}_{i}", (2.6 * sign, -7.6, z), (-70, 0, -30 * sign), ((2, 2), (1, 1)), 1,
                  22178 + i + (sign > 0) * 2)
