"""Kizashi Bloom: the Haruno father's hair, cropped at the sides and swept up on the crown into five
broad petals that open like a cherry blossom seen from above."""
from anime import ring_shell, spike
from paint import scalp

META = {"name": "Kizashi Bloom", "gender": "unisex",
        "description": "Short sides, five broad petal spikes on the crown opening like a cherry blossom."}

PETAL = ((5, 3), (4, 1), (3, 1), (1, 1))
# Five petals tilted out from the crown and turned round it a fifth of a circle apart, one to the front.
TILT = 42


def build(g):
    scalp(g, 19081, side_rows=3, back_rows=5, sideburn=2)
    ring_shell(g, 19082, side_rows=2, back_rows=4, ring_row=1)
    for i in range(5):
        spike(g, f"petal_{i}", (0, -7.4, .4), (TILT, 72 * i, 0), PETAL, 1, 19085 + i * 5)
    spike(g, "heart", (0, -7.8, .4), (0, 0, 0), ((4, 1), (2, 1)), 4, 19110, base=3)
