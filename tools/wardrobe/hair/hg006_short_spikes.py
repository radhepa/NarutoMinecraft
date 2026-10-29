"""Short Spikes: short hair that stands straight up in a dense brush of stubby spikes, the sides trimmed
and a row of short points along the brow."""
from anime import bangs, ring_shell, spike
from paint import scalp

META = {"name": "Short Spikes", "gender": "unisex",
        "description": "A dense brush of short upright spikes, trimmed sides, short points along the brow."}

SPIKE = ((2, 2), (1, 1))


def build(g):
    scalp(g, 31830, side_rows=3, back_rows=6, sideburn=1)
    ring_shell(g, 31831, side_rows=3, back_rows=6, ring_row=1)
    n = 0
    for z, rx in ((-2.8, -14), (-.9, -4), (1.0, 6), (2.9, 18)):
        for x in (-3.0, -1.0, 1.0, 3.0):
            jitter = ((n * 7) % 5 - 2) * 3
            spike(g, f"spike_{n}", (x + (.5 if z > 0 else 0), -7.8, z), (rx + jitter, 0, x * 5 - jitter),
                  ((3, 2), (2, 1), (1, 1)) if n % 3 == 0 else SPIKE, 2, 31832 + n)
            n += 1
    bangs(g, "fringe", [(-2.6, ((2, 1), (1, 1)), 10), (-.9, ((2, 1), (1, 1)), 0), (.9, ((2, 1), (1, 1)), 0),
                        (2.6, ((2, 1), (1, 1)), -10)], seed=31850)
