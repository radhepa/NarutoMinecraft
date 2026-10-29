"""Eight Legs: eight long tapered locks raked back from the crown and fanning out behind the head,
four to a side, bending down at the tips like the legs of the earth spider."""
from anime import lock, ring_shell
from paint import scalp

META = {"name": "Eight Legs", "gender": "unisex",
        "description": "Eight long tapered locks fanning back from the crown, four to a side, like spider legs."}

# (x, y, z, tilt back, splay): the inner pairs ride high on the crown, the outer pairs low and wide.
LEGS = [(-1.6, -8.0, -1.4, 58, 22), (-2.6, -7.6, .4, 66, 32), (-3.3, -6.8, 2.2, 52, 40), (-3.6, -5.6, 3.6, 34, 36)]


def build(g):
    scalp(g, 23081, side_rows=5, back_rows=8, sideburn=2)
    ring_shell(g, 23082, side_rows=4, back_rows=8, ring_row=1)
    for i, (x, y, z, rx, rz) in enumerate(LEGS):
        for side, sign in (("right", 1), ("left", -1)):
            lock(g, f"leg_{side}_{i}", (x * sign, y, z), (rx, 0, rz * sign), ((2, 4), (2, 3), (1, 3)), 2,
                 23085 + i * 3 + (sign < 0))
