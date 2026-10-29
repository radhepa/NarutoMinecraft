"""Bristle Bob: a chin-length bob cut with a knife, its ends kicking out in stiff points, short
spikes on the crown and a choppy fringe at the brows."""
from anime import back_fan, bangs, ring_shell, sidelocks
from kit_hagane import crown
from paint import scalp

META = {"name": "Bristle Bob", "gender": "unisex",
        "description": "A chin-length bob with stiff flicked-out points, short crown spikes, a choppy fringe."}

TOP = ((3, 2), (2, 1), (1, 1))
SPIKES = [(-2.0, -2.0, TOP, 6, -24), (.4, -2.4, TOP, 10, 6), (2.4, -1.8, TOP, 4, 28), (0, .8, TOP, -30, 0)]


def build(g):
    scalp(g, 21440, side_rows=7, back_rows=8, sideburn=1)
    ring_shell(g, 21441, side_rows=7, back_rows=8, ring_row=1)
    crown(g, "spike", SPIKES, 21442)
    back_fan(g, "back", [(-3.0, ((3, 6), (2, 2), (1, 1)), 14, 10), (-1.0, ((3, 6), (2, 2)), 4, 12),
                         (1.0, ((3, 6), (2, 2)), -4, 12), (3.0, ((3, 6), (2, 2), (1, 1)), -14, 10)], seed=21450)
    sidelocks(g, "side", 7, seed=21470, x=4.3, z=-2.6, flare=12, width=3)
    bangs(g, "fringe", [(-2.8, ((2, 3), (1, 1)), 20), (-1.0, ((2, 2), (1, 1)), 8), (1.0, ((2, 2), (1, 1)), -8),
                        (2.8, ((2, 3), (1, 1)), -20)], seed=21480)
