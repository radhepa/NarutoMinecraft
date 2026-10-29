"""Crest Spikes: short hair standing up off the crown in thick spikes that all lean back and curl
over at the tips, a row of wave crests running front to back. Clear brow, close sides."""
from anime import ring_shell
from kit_namiashi import wave_lock
from paint import scalp

META = {"name": "Crest Spikes", "gender": "unisex",
        "description": "Thick spikes standing off the crown, leaning back and curling over at the tips like crests."}

SEG = (((3, 2), (2, 1)), 0, 0)
TIP = (((1, 2),), -40, 0)
# (x, z, rz)
CRESTS = [(-2.2, -3.0, -10), (0.2, -3.2, 4), (2.4, -2.8, 14), (-1.0, .2, -6), (1.4, .4, 8), (0, 3.0, 0)]


def build(g):
    scalp(g, 20071, side_rows=4, back_rows=7, sideburn=2)
    ring_shell(g, 20072, side_rows=4, back_rows=7, ring_row=1)
    for i, (x, z, rz) in enumerate(CRESTS):
        wave_lock(g, f"crest_{i}", (x, -7.6, z), (196, 0, rz), [SEG, TIP], depth=2, seed=20075 + i * 7)
