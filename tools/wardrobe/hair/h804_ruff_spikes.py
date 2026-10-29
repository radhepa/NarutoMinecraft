"""Ruff Spikes: a short top with a wolf's ruff, thick spikes jutting straight out from the sides and
back of the head at ear height, so the head looks bigger from every side."""
from anime import bangs, ring_shell
from kit_inuzuka import burst
from paint import scalp

META = {"name": "Ruff Spikes", "gender": "unisex",
        "description": "A short top and a ruff of thick spikes jutting out from the sides and back."}

RUFF = ((3, 3), (2, 2), (1, 1))
TOP = ((3, 2), (2, 1), (1, 1))
CROWN = [(-1.8, -2.0, TOP, 18, -16), (.6, -2.4, TOP, 22, 10), (-.4, .6, TOP, -12, -4), (2.0, .4, TOP, -10, 22)]
# The ruff hangs lower on the head: (x, y, z, segments, tilt x, tilt z)
SIDE = [(-3.6, -5.6, -1.6, RUFF, 10, -86), (-3.6, -5.2, 1.2, RUFF, -20, -80), (3.6, -5.6, -1.6, RUFF, 10, 86),
        (3.6, -5.2, 1.2, RUFF, -20, 80), (-2.2, -5.0, 3.6, RUFF, -84, -34), (2.2, -5.0, 3.6, RUFF, -84, 34),
        (0, -6.0, 3.6, RUFF, -76, 0), (0, -3.6, 3.6, ((2, 2), (1, 1)), -104, 0)]


def build(g):
    scalp(g, 8091, side_rows=5, back_rows=8, sideburn=2)
    ring_shell(g, 8092, side_rows=5, back_rows=7, ring_row=1)
    burst(g, "crown_tuft", CROWN, 8093)
    from anime import spike
    for i, (x, y, z, segs, rx, rz) in enumerate(SIDE):
        spike(g, f"ruff_{i}", (x, y, z), (rx, 0, rz), segs, 3, 8096 + i * 3)
    bangs(g, "fringe", [(-2.4, ((2, 2), (1, 1)), 20), (0, ((2, 1), (1, 1)), 0), (2.4, ((2, 2), (1, 1)), -20)], seed=8106)
