"""Will of Fire: an invention in the clan's spirit. Hair swept up off the forehead and streaming
back over the crown in long tongues like a flame in the wind, the longest at the centre."""
from anime import ring_shell, sidelocks, spike
from paint import scalp

META = {"name": "Will of Fire", "gender": "unisex",
        "description": "Hair swept up and streaming back over the crown in long flame tongues."}

LONG = ((4, 3), (3, 3), (2, 2), (1, 2))
MID = ((3, 3), (2, 2), (1, 2))
SHORT = ((3, 2), (2, 2), (1, 1))
FLAMES = [(0.0, -8.0, -3.0, LONG, -52, 0), (-2.4, -8.0, -2.6, MID, -54, -14), (2.4, -8.0, -2.6, MID, -54, 14),
          (-1.2, -8.0, -.2, LONG, -66, -6), (1.2, -8.0, -.2, LONG, -66, 6),
          (-3.4, -7.2, -.6, SHORT, -60, -40), (3.4, -7.2, -.6, SHORT, -60, 40),
          (-2.2, -7.0, 2.8, MID, -84, -22), (2.2, -7.0, 2.8, MID, -84, 22), (0.0, -6.2, 3.8, SHORT, -104, 0)]


def build(g):
    scalp(g, 9511, side_rows=5, back_rows=7, sideburn=2)
    ring_shell(g, 9512, side_rows=5, back_rows=7, ring_row=1)
    for i, (x, y, z, segs, rx, rz) in enumerate(FLAMES):
        spike(g, f"crown_{i}", (x, y, z), (rx, 0, rz), segs, 2, 9520 + i * 3)
    sidelocks(g, "frame", 4, seed=9570, x=4.3, z=-3.0, flare=12, width=2)
