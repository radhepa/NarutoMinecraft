"""Fang Crop: the clan's signature short brown mop, cut rough with a knife and left to stand where it
likes: small spikes jutting every way from the crown, a jagged fringe above the brows and a spiky
nape, the way the boy with the white pup wears it."""
from anime import bangs, lock, ring_shell, sidelocks
from kit_inuzuka import burst
from paint import scalp

META = {"name": "Fang Crop", "gender": "unisex",
        "description": "Short messy spikes jutting every way, a jagged fringe and a spiky nape."}

TUFT = ((3, 2), (2, 2), (1, 1))
SMALL = ((2, 2), (1, 1))
CROWN = [(-2.6, -2.6, TUFT, 16, -34), (0, -3.0, TUFT, 26, 4), (2.6, -2.4, TUFT, 12, 36),
         (-1.4, -.6, TUFT, -6, -14), (1.4, -.2, TUFT, -10, 18), (-3.2, 1.0, TUFT, -20, -58),
         (3.2, 1.2, TUFT, -18, 60), (-1.6, 2.6, TUFT, -44, -22), (1.6, 2.8, TUFT, -46, 24), (0, 3.4, SMALL, -70, 0)]


def build(g):
    scalp(g, 8001, side_rows=4, back_rows=7, sideburn=2)
    ring_shell(g, 8002, side_rows=4, back_rows=6, ring_row=1)
    burst(g, "crown_spike", CROWN, 8003)
    bangs(g, "fringe", [(-2.8, ((2, 2), (1, 1)), 26), (-1.0, ((2, 2), (1, 1)), 10), (.8, ((2, 1), (1, 1)), -8),
                        (2.7, ((2, 2), (1, 1)), -28)], seed=8012)
    sidelocks(g, "sidelock", 4, seed=8016, x=4.4, z=-2.0, flare=22, width=2)
    for i, (x, rz, rx) in enumerate(((-3.0, 34, 40), (-1.0, 10, 48), (1.0, -10, 48), (3.0, -34, 40))):
        lock(g, f"nape_{i}", (x, -3.4, 4.3), (rx, 0, rz), ((2, 2), (1, 1)), 1, 8019 + i * 5)
