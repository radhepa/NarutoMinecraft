"""Wave Crop: short at the back and sides, with a thick quiff on top that swells up from the crown
and breaks forward over the brow like the crest of a wave."""
from anime import lock, ring_shell, spike
from paint import scalp

META = {"name": "Wave Crop", "gender": "unisex",
        "description": "Short back and sides, a quiff swelling from the crown and breaking forward like a wave."}

# Spikes from the back of the crown to the front, leaning ever further forward: the swell and the crest.
WAVE = [(-1.6, 2.4, ((4, 2), (3, 1), (1, 1)), -10, -8), (1.6, 2.4, ((4, 2), (3, 1), (1, 1)), -10, 8),
        (-1.4, .2, ((4, 2), (3, 2), (2, 1)), 14, -6), (1.4, .2, ((4, 2), (3, 2), (2, 1)), 14, 6),
        (0, -2.0, ((5, 2), (4, 2), (2, 1)), 42, 0), (-2.2, -2.4, ((3, 2), (2, 1)), 50, -14),
        (2.2, -2.4, ((3, 2), (2, 1)), 50, 14)]


def build(g):
    scalp(g, 2160, side_rows=3, back_rows=6, sideburn=2)
    ring_shell(g, 2161, side_rows=3, back_rows=5, ring_row=1)
    for i, (x, z, segs, rx, rz) in enumerate(WAVE):
        spike(g, f"wave_{i}", (x, -7.8, z), (rx, 0, rz), segs, 3, 2162 + i)
    for i, (x, rz) in enumerate(((-2.4, 20), (0, 0), (2.4, -20))):
        lock(g, f"nape_{i}", (x, -2.2, 4.3), (30, 0, rz), ((2, 1), (1, 1)), 1, 2170 + i, ring=None)
