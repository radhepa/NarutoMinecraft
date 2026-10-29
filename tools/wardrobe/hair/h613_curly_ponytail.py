"""Curly Ponytail: curls gathered high on the crown into a big bouncing tail of puffs that tumbles
down the back, curly bangs and a soft curl over each ear."""
from anime import tie
from kit_akimichi import puff
from paint import scalp, shell

META = {"name": "Curly Ponytail", "gender": "unisex",
        "description": "A big tail of curls tied high on the crown, curly bangs and curls over the ears."}

# The tail, top to bottom: (y, z, size)
TAIL = [(-9.0, 4.4, (4, 3, 4)), (-6.6, 6.0, (5, 4, 4)), (-3.6, 6.6, (5, 4, 4)), (-.8, 6.4, (4, 3, 3)), (1.4, 6.0, (3, 2, 3))]


def build(g):
    scalp(g, 6541, side_rows=5, back_rows=7, sideburn=2)
    shell(g, 6541, side_rows=4, back_rows=6)
    tie(g, "tie", (0, -9.0, 2.6), (30, 0, 0), size=(3, 2, 3), key="A2")
    for i, (y, z, size) in enumerate(TAIL):
        puff(g, f"tail_{i}", (0, y, z), size, seed=6547 + i, motion="sway" if i else "none")
    for side, sign in (("right", -1), ("left", 1)):
        puff(g, f"ear_{side}", (4.4 * sign, -5.0, -1.4), (2, 4, 3), seed=6554 + (sign > 0))
    for i, x in enumerate((-2.6, -.4, 2.0)):
        puff(g, f"fringe_{i}", (x, -7.4, -4.1), (3, 2, 1), seed=6561 + i)
