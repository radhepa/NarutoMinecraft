"""Pup Tufts: a short scruffy crop with two tall pointed tufts standing up at the corners of the
crown like a puppy's pricked ears, and a short spiky fringe: the youngest Inuzuka's look."""
from anime import bangs, ring_shell, spike
from kit_inuzuka import burst
from paint import scalp

META = {"name": "Pup Tufts", "gender": "unisex",
        "description": "A short scruffy crop with two tall tufts pricked up like a puppy's ears."}

TUFT = ((2, 2), (1, 1))
CROWN = [(-.8, -2.2, TUFT, 20, -8), (1.0, -1.6, TUFT, 16, 12), (0, 1.2, TUFT, -28, 0), (-2.0, 2.6, TUFT, -50, -20),
         (2.0, 2.6, TUFT, -50, 20)]


def build(g):
    scalp(g, 8151, side_rows=4, back_rows=6, sideburn=2)
    ring_shell(g, 8152, side_rows=3, back_rows=5, ring_row=1)
    burst(g, "crown_tuft", CROWN, 8153)
    for i, (x, rz) in enumerate(((-2.6, -16), (2.6, 16))):
        spike(g, f"crown_ear_{i}", (x, -7.6, -.6), (-6, 0, rz), ((4, 2), (3, 2), (2, 2), (1, 1)), 2, 8159 + i * 4)
    bangs(g, "fringe", [(-2.4, ((2, 2), (1, 1)), 20), (-.4, ((2, 1), (1, 1)), 4), (1.6, ((2, 2), (1, 1)), -16)], seed=8162)
