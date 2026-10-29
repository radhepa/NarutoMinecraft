"""Antenna Locks: a short, neat crop with two long, fine locks rising from the crown and curving
back like a beetle's antennae."""
import math

from anime import bangs, ring_shell, spike
from paint import scalp

META = {"name": "Antenna Locks", "gender": "unisex",
        "description": "A short neat crop with two long fine locks curving back from the crown like antennae."}


def build(g):
    scalp(g, 10321, side_rows=3, back_rows=6, sideburn=2)
    ring_shell(g, 10322, side_rows=3, back_rows=6, ring_row=1)
    for side, sign in (("right", -1), ("left", 1)):
        # Each antenna: a fine stem rising from the crown, then a tip bent back from the stem's end.
        stem = (1.4 * sign, -7.8, -1.6)
        spike(g, f"antenna_{side}", stem, (-24, 0, 16 * sign), ((1, 3), (1, 3)), 1, 10330 + (sign > 0))
        end = (stem[0] + 6 * math.sin(math.radians(16)) * math.cos(math.radians(24)) * sign,
               stem[1] - 6 * math.cos(math.radians(16)) * math.cos(math.radians(24)), stem[2] + 6 * math.sin(math.radians(24)))
        spike(g, f"antenna_tip_{side}", end, (-72, 0, 20 * sign), ((1, 2), (1, 2)), 1, 10334 + (sign > 0))
    for i, (x, z) in enumerate(((-2.2, .4), (0, -.6), (2.2, .4), (0, 2.6))):
        spike(g, f"crop_{i}", (x, -7.8, z), (-40, 0, x * 8), ((3, 2), (1, 1)), 3, 10340 + i)
    bangs(g, "fringe", [(-2.2, ((2, 1), (1, 1)), 14), (0, ((2, 1),), 0), (2.2, ((2, 1), (1, 1)), -14)], seed=10350)
