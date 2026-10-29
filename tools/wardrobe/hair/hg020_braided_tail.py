"""Braided Tail: hair combed back from a short centre-parted fringe and worked into a single braid
from the nape, tied off with a cloth wrap and swinging between the shoulders."""
from anime import bangs, braid, ring_shell, tie
from paint import scalp

META = {"name": "Braided Tail", "gender": "unisex",
        "description": "Combed back from a short parted fringe into a single nape braid tied with a cloth wrap."}


def build(g):
    scalp(g, 32940, side_rows=6, back_rows=8, sideburn=3, part=4)
    ring_shell(g, 32941, side_rows=5, back_rows=8, ring_row=1)
    bangs(g, "fringe", [(-2.8, ((2, 2), (1, 1)), 22), (2.8, ((2, 2), (1, 1)), -22)], seed=32942)
    end = braid(g, "braid", (0, -1.8, 4.8), (10, 0, 0), links=6, width=3, seed=32920)
    tie(g, "wrap", (0, -1.8, 4.8), (10, 0, 0), size=(3, 1, 3), y=end - 2.6, key="D2", motion="sway")
