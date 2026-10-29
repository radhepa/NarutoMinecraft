"""Magaki Spikes: the rough mane of the Magaki faction, who wanted the forbidden jutsu for war: hard
spikes thrown back off the brow and jutting out behind, a few ragged points over the temples."""
from anime import ring_shell, spike
from paint import scalp

META = {"name": "Magaki Spikes", "gender": "unisex",
        "description": "Hard spikes thrown back off the brow and jutting out behind, ragged at the temples."}

SPIKES = [(-2.4, -2.6, ((3, 3), (2, 2), (1, 2)), -38, -34), (0, -2.8, ((3, 3), (2, 3), (1, 2)), -42, 0),
          (2.4, -2.6, ((3, 3), (2, 2), (1, 2)), -38, 34),
          (-2.6, .6, ((3, 3), (2, 3), (1, 2)), -66, -40), (0, .4, ((4, 3), (3, 3), (1, 2)), -70, 0),
          (2.6, .6, ((3, 3), (2, 3), (1, 2)), -66, 40),
          (-1.6, 3.2, ((3, 3), (2, 2), (1, 2)), -96, -24), (1.6, 3.2, ((3, 3), (2, 2), (1, 2)), -96, 24),
          (-3.6, -1.0, ((2, 2), (1, 2)), -20, -70), (3.6, -1.0, ((2, 2), (1, 2)), -20, 70)]


def build(g):
    scalp(g, 23141, side_rows=4, back_rows=7, sideburn=2)
    ring_shell(g, 23142, side_rows=3, back_rows=6, ring_row=1)
    for i, (x, z, segs, rx, rz) in enumerate(SPIKES):
        spike(g, f"crown_spike_{i}", (x, -7.6, z), (rx, 0, rz), segs, 3, 23145 + i)
