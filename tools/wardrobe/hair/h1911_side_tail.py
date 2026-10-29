"""Side Tail: a cheerful ponytail tied high above the left ear and swung forward over the shoulder,
a side-parted fringe that lifts off the brow, and a short lock framing the right cheek."""
from anime import cel_box, lock, ring_shell, tie
from paint import scalp

META = {"name": "Side Tail", "gender": "unisex",
        "description": "High side ponytail above the left ear swung over the shoulder, lifted side fringe."}

FRINGE = [(-2.8, ((2, 2), (1, 1)), 30), (-1.0, ((3, 2), (1, 1)), 52), (1.2, ((3, 2), (1, 1)), 50), (3.0, ((2, 1),), 10)]
TAIL = ((3, 3), (3, 3), (2, 3), (2, 2), (1, 2))


def build(g):
    scalp(g, 19301, side_rows=5, back_rows=7, sideburn=2, part=5)
    ring_shell(g, 19302, side_rows=5, back_rows=6, ring_row=1)
    for i, (x, segs, rz) in enumerate(FRINGE):
        lock(g, f"fringe_{i}", (x, -8.55, -4.35), (-10, 0, rz), segs, 1, 19305 + i * 7, ring=0)
    lock(g, "cheek", (-4.4, -7.6, -3.0), (0, 0, 4), ((2, 5), (1, 1)), 1, 19333)
    root = g.piece("tail_root", "HEAD", (-1.5, -1.5, -1.5), (3, 3, 3), pivot=(4.6, -6.8, 1.6))
    cel_box(root, 19335, base=2)
    tie(g, "tie", (5.2, -6.8, 1.6), (0, 0, -70), (3, 1, 3), y=-.5, key="A2")
    lock(g, "tail", (5.6, -6.6, 1.6), (-8, 0, -14), TAIL, 2, 19340, motion="sway")
