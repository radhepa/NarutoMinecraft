"""Nape Braid: a close, short crop over the crown with one thin braid left long at the nape and
hanging down between the shoulders."""
from anime import braid
from paint import scalp, shell

META = {"name": "Nape Braid", "gender": "unisex",
        "description": "Close short crop with one thin braid left long at the nape."}


def build(g):
    scalp(g, 17131, side_rows=4, back_rows=7, sideburn=1)
    shell(g, 17132, side_rows=3, back_rows=6, sheen=1, front=[(1, 1), (2, 1), (5, 1), (6, 1)])
    braid(g, "braid", (0, -1.4, 4.4), (10, 0, 0), links=4, width=2, seed=17133)
