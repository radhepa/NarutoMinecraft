"""Ledger Tail: hair combed straight back off the brow and gathered in a low tail at the nape, tied
with a cloth band the way a merchant keeps it out of the accounts, two short locks at the temples."""
from anime import lock, ring_shell, tie
from paint import scalp

META = {"name": "Ledger Tail", "gender": "unisex",
        "description": "Combed-back hair in a low tail at the nape tied with cloth, short temple locks."}

TAIL = ((3, 3), (3, 3), (2, 3), (1, 2))


def build(g):
    scalp(g, 19211, side_rows=5, back_rows=8, sideburn=2)
    ring_shell(g, 19212, side_rows=5, back_rows=7, ring_row=1)
    hat = g.part("hat")
    for x in range(8):
        hat.front.set(x, 0, "H3" if x % 3 else "H2")
    for side, sign in (("right", -1), ("left", 1)):
        lock(g, f"temple_{side}", (4.3 * sign, -7.6, -3.0), (0, 0, -4 * sign), ((1, 3), (1, 1)), 1, 19215 + (sign > 0))
    tie(g, "tie", (0, -2.6, 4.5), (0, 0, 0), (3, 1, 2), key="A2")
    lock(g, "tail", (0, -2.2, 4.6), (12, 0, 0), TAIL, 2, 19220, motion="sway")
