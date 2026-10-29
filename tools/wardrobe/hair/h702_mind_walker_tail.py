"""Mind Walker Tail: the clan head's long spiky mane, swept back off the brow and bound at the back
of the crown into a thick tail that breaks into points, with long bangs parted in the middle and
framing both sides of the face to the jaw."""
from anime import bangs, lock, ring_shell, sidelocks, spike, tie
from paint import scalp

META = {"name": "Mind Walker Tail", "gender": "unisex",
        "description": "Long spiky ponytail from the back of the crown, centre-parted bangs to the jaw."}

# (x, rz, rx, segments): the tail fans into points as it falls.
TAIL = [(0, 0, 18, ((4, 4), (4, 4), (3, 4), (2, 3), (1, 2))),
        (-1.2, 16, 26, ((3, 4), (2, 4), (1, 3))),
        (1.2, -16, 26, ((3, 4), (2, 4), (1, 3))),
        (0, 6, 40, ((3, 3), (2, 3), (1, 2)))]


def build(g):
    scalp(g, 7101, side_rows=6, back_rows=8, sideburn=3, part=3)
    ring_shell(g, 7102, side_rows=5, back_rows=7, ring_row=1)
    for i, (x, z, rx, rz) in enumerate(((-2.0, -1.8, -40, 18), (2.0, -1.8, -40, -18), (0, -.6, -50, 0))):
        spike(g, f"crown_{i}", (x, -7.9, z), (rx, 0, rz), ((3, 2), (2, 2), (1, 1)), 2, 7110 + i)
    bangs(g, "part", [(-1.4, ((2, 2), (1, 1)), 34), (1.4, ((2, 2), (1, 1)), -34)], seed=7120)
    sidelocks(g, "bang", 9, seed=7130, x=4.3, z=-3.6, flare=4, width=2)
    tie(g, "tie", (0, -5.6, 4.5), (10, 0, 0), (4, 2, 3), y=-1)
    for i, (x, rz, rx, segs) in enumerate(TAIL):
        lock(g, f"tail_{i}", (x, -5.4, 5.4), (rx, 0, rz), segs, 3 if i == 0 else 2, 7140 + i * 9, ring=None,
             motion="sway")
