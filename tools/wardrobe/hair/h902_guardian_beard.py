"""Guardian Beard: Asuma's look. Short dark hair brushed up and back in stiff spikes off a square
hairline, sideburns running down into a short full beard along the jaw and under the chin."""
from anime import ring_shell, spike
from kit_sarutobi import beard
from paint import scalp

META = {"name": "Guardian Beard", "gender": "male",
        "description": "Short spikes brushed up and back, sideburns into a short beard along the jaw."}

CROWN = [(-2.6, -7.6, -2.6, ((3, 2), (2, 1), (1, 1)), 24, -18),
         (0.0, -7.8, -2.8, ((4, 2), (2, 2), (1, 1)), 26, 0),
         (2.6, -7.6, -2.6, ((3, 2), (2, 1), (1, 1)), 24, 18),
         (-1.6, -8.0, -.2, ((3, 2), (2, 2), (1, 1)), -30, -10),
         (1.6, -8.0, -.2, ((3, 2), (2, 2), (1, 1)), -30, 10),
         (-2.6, -7.4, 2.4, ((3, 2), (2, 2), (1, 1)), -64, -24),
         (0.0, -7.6, 2.6, ((3, 2), (2, 2), (1, 1)), -62, 0),
         (2.6, -7.4, 2.4, ((3, 2), (2, 2), (1, 1)), -64, 24),
         (0.0, -5.4, 3.8, ((3, 2), (2, 1)), -96, 0)]


def build(g):
    scalp(g, 9061, side_rows=5, back_rows=7, sideburn=3)
    ring_shell(g, 9062, side_rows=5, back_rows=7, ring_row=1)
    for i, (x, y, z, segs, rx, rz) in enumerate(CROWN):
        spike(g, f"crown_{i}", (x, y, z), (rx, 0, rz), segs, 2, 9070 + i * 3)
    beard(g, 9100)
