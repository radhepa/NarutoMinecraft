"""Long Tied: long dark hair brushed back from the brow, bound once at the nape and once lower
down, falling in one straight sheet to the middle of the back, a quiet elder's style."""
from anime import curtain, ring_shell, sidelocks, tie
from paint import scalp

META = {"name": "Long Tied", "gender": "unisex",
        "description": "Long hair brushed back, bound at the nape and again lower, falling to mid-back."}

PIVOT, TILT = (0, -2.6, 4.7), (8, 0, 0)


def build(g):
    scalp(g, 10361, side_rows=5, back_rows=8, sideburn=3)
    hat = ring_shell(g, 10362, side_rows=5, back_rows=8, ring_row=1)
    for x in (2, 5):
        hat.top.vline(x, 0, 7, "H1")
    curtain(g, "length", PIVOT, TILT, 3, 11, hem=((0, 3, 2),), seed=10370)
    tie(g, "nape_tie", PIVOT, TILT, size=(4, 1, 2), y=0.2, motion="sway")
    tie(g, "low_tie", PIVOT, TILT, size=(4, 1, 2), y=7.0, motion="sway")
    sidelocks(g, "frame", 6, seed=10380, x=4.35, z=-2.6, flare=4, width=1)
