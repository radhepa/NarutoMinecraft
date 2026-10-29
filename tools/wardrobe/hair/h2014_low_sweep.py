"""Low Sweep: long hair slicked straight back off the brow and gathered low at the nape, the long
tail hanging down the spine, a single loose lock left at one temple."""
from anime import lock, ring_shell, tie
from kit_nara import pulled_back
from paint import scalp

META = {"name": "Low Sweep", "gender": "unisex",
        "description": "Long hair slicked back and gathered low at the nape, a long tail down the spine."}


def build(g):
    hat = ring_shell(g, 20392, side_rows=5, back_rows=8, ring_row=1)
    scalp(g, 20391, side_rows=5, back_rows=8, sideburn=2)
    for x in (1, 3, 4, 6):
        hat.top.vline(x, 0, 7, "H1" if x in (3, 6) else "H3")
    tie(g, "tie", (0, -2.6, 4.6), (6, 0, 0), size=(3, 1, 2), y=0, key="K2")
    lock(g, "tail", (0, -2.0, 4.8), (6, 0, 0), ((3, 4), (3, 3), (2, 2), (1, 1)), 2, 20395, ring=None, motion="sway")
    lock(g, "temple", (-4.3, -7.4, -3.0), (0, 0, 8), ((1, 4), (1, 2)), 1, 20400, ring=1)
