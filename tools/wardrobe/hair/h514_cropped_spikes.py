"""Cropped Spikes: the tail cut off. Short dark hair combed back in stiff spikes that all point to
the back of the head, close at the sides, nothing over the brow."""
from anime import spike
from kit_nara import pulled_back

META = {"name": "Cropped Spikes", "gender": "unisex",
        "description": "Short hair combed back into stiff spikes all pointing behind the head, close sides."}

TUFT = ((3, 2), (2, 2), (1, 1))
# (x, z, rx, rz)
CROWN = [(-2.4, -2.6, -70, -10), (0, -2.8, -72, 0), (2.4, -2.6, -70, 10), (-2.6, .2, -80, -16), (0, 0, -82, 0),
         (2.6, .2, -80, 16), (-1.4, 2.8, -96, -12), (1.4, 2.8, -96, 12)]


def build(g):
    pulled_back(g, 5851, side_rows=3, back_rows=6, sideburn=2)
    for i, (x, z, rx, rz) in enumerate(CROWN):
        spike(g, f"crown_{i}", (x, -7.8, z), (rx, 0, rz), TUFT, 2, 5860 + i * 3)
