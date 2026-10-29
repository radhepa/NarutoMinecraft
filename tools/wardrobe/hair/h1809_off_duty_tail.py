"""Off-Duty Tail: the Iruka tail tied a little lower and looser at the end of the day, a shorter brush
standing out behind the head, a few locks pulled free at the temples and over the brow."""
from anime import bangs, lock
from kit_umino import brush_tail, combed_up, knot

META = {"name": "Off-Duty Tail", "gender": "unisex",
        "description": "A looser, lower brush of a tail, locks pulled free at the temples and over the brow."}

MID = ((3, 3), (2, 2), (1, 2))
LOCKS = [(MID, 62, 0), (MID, 56, -26), (MID, 56, 26), (((2, 2), (1, 2)), 40, -10), (((2, 2), (1, 2)), 84, 12)]


def build(g):
    combed_up(g, 18161, side_rows=5, back_rows=7, sideburn=2)
    bangs(g, "fringe", [(-2.4, ((2, 2), (1, 1)), 30), (2.8, ((1, 2), (1, 1)), -20)], seed=18163)
    for side, sign in (("right", -1), ("left", 1)):
        lock(g, f"loose_{side}", (4.3 * sign, -7.6, -2.4), (0, 0, -10 * sign), ((2, 3), (1, 2)), 1, 18165 + (sign > 0))
    knot(g, "tail", (0, -5.6, 4.5), rx=-10)
    brush_tail(g, "tail", (0, -5.8, 6.0), LOCKS, seed=18170)
