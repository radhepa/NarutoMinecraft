"""Guard's Crop: Raido's short dark hair, combed back and cropped close at the sides, the crown
breaking into short stiff points that lean back like spray off a wave, short sideburns, a clear
brow. Flat enough to tie a bandana down over."""
from anime import spike
from paint import scalp
from anime import ring_shell

META = {"name": "Guard's Crop", "gender": "unisex",
        "description": "Short dark hair combed back, close sides, short points leaning back off the crown."}

TUFT = ((3, 2), (2, 1), (1, 1))
# (x, y, z, rx, rz)
POINTS = [(-2.2, -7.8, -.4, -72, -16), (0, -7.9, 0, -76, 0), (2.2, -7.8, -.4, -72, 16),
          (-1.4, -7.6, 2.6, -96, -10), (1.4, -7.6, 2.6, -96, 10)]


def build(g):
    scalp(g, 20011, side_rows=4, back_rows=7, sideburn=3)
    ring_shell(g, 20012, side_rows=4, back_rows=7, ring_row=1)
    for i, (x, y, z, rx, rz) in enumerate(POINTS):
        spike(g, f"point_{i}", (x, y, z), (rx, 0, rz), TUFT, 2, 20015 + i * 3)
