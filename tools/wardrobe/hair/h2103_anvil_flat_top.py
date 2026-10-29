"""Anvil Flat Top: spikes cut level across the top so the head reads square as an anvil, the
sides kept close and a blunt short fringe: the smith's practical crop."""
from anime import bangs, ring_shell
from kit_hagane import crown
from paint import scalp

META = {"name": "Anvil Flat Top", "gender": "unisex",
        "description": "Upright spikes cut level into a square flat top, close sides, a blunt fringe."}

POST = ((3, 2), (2, 1))
SPIKES = [(x, z, POST, 0, 0) for z in (-2.6, -.4, 1.8) for x in (-2.6, 0, 2.6)] + \
         [(-2.6, 3.4, POST, -30, 0), (0, 3.4, POST, -30, 0), (2.6, 3.4, POST, -30, 0)]


def build(g):
    scalp(g, 21220, side_rows=2, back_rows=5, sideburn=2)
    ring_shell(g, 21221, side_rows=2, back_rows=5, ring_row=1)
    crown(g, "post", SPIKES, 21222)
    bangs(g, "fringe", [(-2.2, ((3, 1),), 8), (0, ((2, 1),), 0), (2.2, ((3, 1),), -8)], seed=21260)
