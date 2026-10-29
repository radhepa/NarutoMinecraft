"""Long Tied: long straight hair parted in the middle, combed smooth over the ears with no fringe,
gathered at the nape and bound at intervals with cloth ties down to the small of the back: the
sealing corps' traditional way of wearing it."""
from anime import ring_shell, tie
from kit_hyuga import gathered_tail
from kit_kurama import part_line
from paint import scalp

META = {"name": "Long Tied", "gender": "unisex",
        "description": "Long middle-parted hair, no fringe, bound at the nape and down the back with cloth ties."}

PIVOT, TILT = (0, -1.4, 4.6), 6


def build(g):
    scalp(g, 34850, side_rows=6, back_rows=8, sideburn=4, part=3)
    ring_shell(g, 34851, side_rows=6, back_rows=8, ring_row=1)
    part_line(g, 3)
    gathered_tail(g, "tail", PIVOT, TILT, [(3, 3), (3, 4), (3, 4), (2, 3)], 34852, tie_at=0, tie_key="S3")
    tie(g, "tail_tie_low", PIVOT, (TILT, 0, 0), (3, 1, 3), y=10.5, key="S3", motion="sway")
