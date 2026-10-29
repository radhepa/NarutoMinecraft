"""Nape Tail: short, practical hair close at the sides with a light fringe, and one thin tail left
long at the nape and bound at the root, falling between the shoulder blades."""
from anime import bangs, lock, ring_shell, spike, tie
from paint import scalp

META = {"name": "Nape Tail", "gender": "unisex",
        "description": "Short hair, light fringe, one thin long tail at the nape bound at the root."}

TUFT = ((3, 2), (2, 1))


def build(g):
    scalp(g, 15260, side_rows=4, back_rows=8, sideburn=2)
    ring_shell(g, 15261, side_rows=3, back_rows=7, ring_row=1)
    for i, (x, z, rx, rz) in enumerate(((-2.0, -1.0, -10, -20), (1.0, -1.4, -14, 16), (0, 1.6, 20, 0))):
        spike(g, f"crown_{i}", (x, -7.8, z), (rx, 0, rz), TUFT, 3, 15262 + i)
    bangs(g, "fringe", [(-2.4, ((2, 2), (1, 1)), 20), (0, ((2, 2),), 0), (2.4, ((2, 2), (1, 1)), -20)], seed=15268)
    tie(g, "tail_tie", (0, -.6, 4.5), (-6, 0, 0), size=(2, 1, 2), y=-.5, key="A2")
    lock(g, "tail", (0, -.4, 4.5), (-6, 0, 0), ((2, 4), (1, 4), (1, 2)), 1, 15270, ring=None, motion="sway")
