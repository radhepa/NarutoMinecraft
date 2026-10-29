"""Shinku Shag: after Shinku Yuhi, Kurenai's father, a genjutsu jonin with the clan's untamed black
hair worn short and shaggy: ragged spikes swept back off the crown, a rough fringe, wild tufts over
the ears and a shaggy nape."""
from anime import bangs, spike
from kit_yuhi import wave_fan, wave_lock, wave_shell
from paint import scalp

META = {"name": "Shinku Shag", "gender": "unisex",
        "description": "Short shaggy wild hair, ragged spikes swept back, rough fringe, tufts over the ears."}

NAPE = [(-3.0, ((3, 2), (2, 2), (1, 1)), 16, 14), (-1.0, ((3, 3), (2, 1), (1, 1)), 4, 12), (1.0, ((3, 3), (2, 1), (1, 1)), -4, 12),
        (3.0, ((3, 2), (2, 2), (1, 1)), -16, 14)]


def build(g):
    scalp(g, 14081, side_rows=5, back_rows=8, sideburn=2)
    wave_shell(g, 14082, side_rows=5, back_rows=8, ring_row=1)
    bangs(g, "fringe", [(-2.9, ((2, 2), (1, 1)), 24), (-1.2, ((2, 1), (1, 1)), 6), (.6, ((2, 2), (1, 1)), -10),
                        (2.6, ((2, 1), (1, 1)), -28)], seed=14090)
    for i, (x, z, rx, rz) in enumerate(((-2.6, -2.2, -84, -22), (0, -2.6, -86, 4), (2.6, -2.2, -84, 24), (-1.4, .6, -96, -14),
                                        (1.4, .6, -98, 16), (0, 2.8, -110, 0))):
        spike(g, f"crown_{i}", (x, -7.9, z), (rx, 0, rz), ((3, 2), (2, 1), (1, 1)), 3, 14100 + i)
    for side, sign in (("right", -1), ("left", 1)):
        wave_lock(g, f"tuft_{side}", (4.4 * sign, -7.4, -.6), (0, 0, -24 * sign), ((2, 3), (2, 2), (1, 1)), 4,
                  14110 + (sign > 0), amp=.35, flip=sign > 0)
    wave_fan(g, "nape", NAPE, seed=14120, y=-6.2, z=4.4, motion="none", amp=.3)
