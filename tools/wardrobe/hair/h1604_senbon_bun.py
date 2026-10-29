"""Senbon Bun: everything combed back into a low round bun at the nape, two senbon pushed through
it in a cross, a few wisps escaping at the temples."""
from anime import ring_shell, sidelocks
from kit_senju import bun
from kit_shiranui import senbon
from paint import scalp

META = {"name": "Senbon Bun", "gender": "unisex",
        "description": "Combed back into a low bun at the nape, crossed through with two senbon, temple wisps."}


def build(g):
    scalp(g, 16260, side_rows=4, back_rows=8, sideburn=2)
    ring_shell(g, 16261, side_rows=3, back_rows=7, ring_row=1)
    sidelocks(g, "frame", 4, seed=16262, x=4.3, z=-2.8, flare=5, width=1)
    bun(g, "bun", (0, -3.4, 5.4), size=(4, 3, 3), seed=16270)
    senbon(g, "bun_pin_0", "HEAD", (0, -3.4, 5.6), (0, 0, 58), length=24, y0=-12)
    senbon(g, "bun_pin_1", "HEAD", (0, -3.6, 5.7), (0, 0, -52), length=24, y0=-12)
