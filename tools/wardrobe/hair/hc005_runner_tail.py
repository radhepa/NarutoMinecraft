"""Runner's Tail: a short ragged crop pulled back into a stub of a tail at the nape, a few short
tufts falling to the brow, for the delivery runners and errand children."""
from anime import bangs, lock, ring_shell, tie
from paint import scalp

META = {"name": "Runner's Tail", "gender": "unisex",
        "description": "Short ragged crop with a stub of a tail at the nape and short tufts at the brow."}


def build(g):
    scalp(g, 36992, side_rows=4, back_rows=7, sideburn=2)
    ring_shell(g, 36993, side_rows=3, back_rows=6, ring_row=1)
    lock(g, "nape_tail", (0, -3.6, 4.5), (20, 0, 0), ((2, 2), (2, 1), (1, 1)), 2, 36994)
    tie(g, "nape_tie", (0, -3.6, 4.5), (20, 0, 0), (3, 1, 3), y=0, key="A2")
    bangs(g, "fringe", [(-2.4, ((2, 1), (1, 1)), 22), (0, ((2, 1),), -6), (2.3, ((2, 1), (1, 1)), -24)], seed=36996)
