"""Spiked Tail: the clan's upswept spikes on top and the long back gathered low into a short,
stiff tail that points down between the shoulders."""
from anime import lock, ring_shell, spike, tie
from paint import scalp

META = {"name": "Spiked Tail", "gender": "unisex",
        "description": "Upswept spikes on top, the back gathered low into a short stiff tail."}

SPIKES = [(-2.4, -2.4, -24, -22), (0, -2.6, -30, 0), (2.4, -2.4, -24, 22), (-1.4, .6, -52, -12), (1.4, .6, -52, 12)]


def build(g):
    scalp(g, 10291, side_rows=5, back_rows=8, sideburn=2)
    ring_shell(g, 10292, side_rows=4, back_rows=8, ring_row=1)
    for i, (x, z, rx, rz) in enumerate(SPIKES):
        spike(g, f"crown_spike_{i}", (x, -7.8, z), (rx, 0, rz), ((3, 3), (2, 2), (1, 1)), 3, 10300 + i)
    tie(g, "tail_tie", (0, -2.2, 4.7), (14, 0, 0), size=(3, 1, 2))
    lock(g, "tail", (0, -1.4, 4.8), (14, 0, 0), ((3, 3), (2, 3), (1, 2)), 2, 10310, ring=None, motion="sway")
